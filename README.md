# 中文科技教学视频技能包

这是一套用于中文科技教学内容的 AI agent 技能：从资料拆解、事实与机制核对，到课程设计、讲稿、分镜、配音、视频制作和验收。它包含两个互补的技能：

- **知识拆解** `chinese-tech-knowledge-decomposer`：建立可追溯的知识底稿，解释前提、机制、算例和边界。
- **教学视频** `chinese-tech-explainer-video`：把知识底稿转成观众能跟随的教学内容、可见演示与视频交付。

两者同级安装并通过联合协议交接；可以只做知识整理、只写方案，也可以在相应授权下制作视频。技能文件是工作方法，不包含视频生成服务、模型权重或成片。

## 看成品与版本演进

- 用户提供的 B 站视频入口：[AI 内容鉴伪视频](https://www.bilibili.com/video/BV1Doxu6LEuk/)。该入口暂未能通过自动工具核验分集和文件版本，具体对应以页面及后续核对为准。
- [技能演进与参考来源](docs/版本演进.md)：每个有记录的阶段、所解决的问题、参考来源与证据边界。
- [视频与技能版本对照](docs/视频版本对照.md)：三个代表性视频版本及其记录中的技能版本。

视频版本、教学工作流版本、知识工作流版本与视觉规范版本分别编号。某个视频名中的 `v3` 不代表它使用了教学技能 3.0；更新技能也不会自动修改旧视频。

## 参考与致谢

- 语音合成使用过 [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM)，历史制作记录中使用的是 VoxCPM2。它是独立的第三方项目；本包不包含模型、参考声音或其实现。每条视频的实际语音来源须以制作记录为准。安装、模型和许可请查看上游说明。
- 教学设计参考了 [OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) 的多智能体互动课堂思路，重点借鉴学习结果、可操作演示和反馈设计；本技能并非 OpenMAIC，也不要求安装它。其他参考与各阶段用途见[版本演进](docs/版本演进.md)和[研究记录](skills/chinese-tech-explainer-video/references/research.md)。

## 安装与使用

本技能包使用 Codex 的 **GPT-6.1 SOL** 制作与验证，建议尽量在 Codex 中使用。其他工具或模型的效果可能不同，使用时请自行验证。

将 `skills/` 下两个目录完整复制到支持 `SKILL.md` 的 agent 技能目录并保持同级。例如 Codex 用户技能目录通常为 `~/.codex/skills/`。重新加载技能列表或重启客户端；具体发现方式取决于客户端。不要只复制 `SKILL.md`，还需要同目录的 `references/`、`assets/` 和 `scripts/`。

```text
使用 chinese-tech-knowledge-decomposer，拆解这份资料并标明事实、假设与待验证问题。
使用两个教学视频技能，基于这份资料设计面向初学者的中文教学视频，先给我课程方案。
```

## 依赖与布局检查

文字分析和课程设计不要求安装视频工具。实际制作时自行选择渲染、音频、字体和图像工具；模型、素材、声音及外部服务需遵循各自许可和授权。图像生成不可用时可使用有权使用的素材或可控图形。

布局检查脚本需要 Python 3、Pillow 和带 weight 轴的 Noto Sans SC 可变字体。通过 `python -m pip install Pillow` 安装 Pillow；字体可从 [Noto CJK](https://github.com/notofonts/noto-cjk) 获取。指定本机字体路径：

```sh
python skills/chinese-tech-explainer-video/scripts/check_layout.py layout.json --font /path/to/NotoSansSC-VF.ttf --output layout-report.json
```

输入为渲染导出的文字布局数组，格式见[分镜模板](skills/chinese-tech-explainer-video/references/storyboard-template.md)。检查仅覆盖文字几何，不能代替遮挡、缺字、音画同步、解码和观看检查。

## 许可

本项目暂以 [MIT License](LICENSE) 提供；公开前请确认发布权属及许可选择。第三方项目、字体、模型和素材遵循各自许可，本包不会重新授权它们。视频不随技能包发布。
