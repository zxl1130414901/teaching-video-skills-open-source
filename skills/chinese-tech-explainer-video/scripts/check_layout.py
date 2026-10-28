"""Check exported visible-glyph text positions; does not inspect rendered video."""
import argparse
import json
from pathlib import Path
from PIL import ImageFont


def check(items, tokens, font_path=None):
    errors = []
    canvas = tokens['canvas']
    for i, item in enumerate(items):
        prefix = f"{i}: {item.get('shot', '')}"
        try:
            role = item['role']
            spec = tokens['type'][role]
            font = ImageFont.truetype(font_path, spec['size'])
            # A variable font with a weight axis is required.
            try:
                axes = font.get_variation_axes()
            except OSError:
                axes = []
            if axes:
                values = [a['default'] for a in axes]
                for j, axis in enumerate(axes):
                    if axis['name'].lower() == b'weight':
                        values[j] = spec['weight']
                font.set_variation_by_axes(values)
            else:
                raise ValueError('Expected variable font with explicit weight axis')
            lines = item['text'].split('\n')
            if not item['text'] or len(lines) > spec['max_lines']:
                raise ValueError('Empty text or too many lines')
            bx0, by0, bx1, by1 = item['bounds']
            if not (0 <= bx0 < bx1 <= canvas['width'] and 0 <= by0 < by1 <= canvas['height']):
                raise ValueError('Invalid container bounds')
            for n, line in enumerate(lines):
                box = font.getbbox(line, anchor='lt')
                width = max(font.getlength(line), box[2] - box[0])
                height = box[3] - box[1]
                x, y = item['x'], item['y'] + n * spec['line']
                if not (bx0 <= x and by0 <= y and x + width <= bx1 and y + height <= by1):
                    raise ValueError(f'Text outside container: {line}')
                if role == 'subtitle':
                    if y < canvas['subtitle_top'] or y + height > canvas['subtitle_bottom'] or x < 216 or x + width > 1704:
                        raise ValueError('Outside subtitle safe area')
                elif y + height > canvas['content_bottom']:
                    raise ValueError('Main text enters subtitle reserve')
        except (KeyError, ValueError, OSError, TypeError) as exc:
            errors.append(f'{prefix}: {exc}')
    if not items:
        errors.append('No text items exported')
    return {'items_checked': len(items), 'passed': not errors, 'errors': errors,
            'scope': 'Exported text geometry only; not rendered-frame or video validation'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('layout', type=Path)
    parser.add_argument('--tokens', type=Path, default=Path(__file__).resolve().parents[1] / 'assets/design_tokens.json')
    parser.add_argument('--font', required=True, help='Path to a variable Noto Sans SC font file')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = check(json.loads(args.layout.read_text('utf-8-sig')),
                   json.loads(args.tokens.read_text('utf-8-sig')), args.font)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(0 if result['passed'] else 1)
