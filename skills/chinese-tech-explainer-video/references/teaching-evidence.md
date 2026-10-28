# 教学方法的依据与边界

本文件固化 2026-09-29 方案中使用的研究及执行含义。以下是设计参考，不是 B 站流量、完播或学习效果保证。新增关键断言仍应查原始来源；只查看标题、摘要、文字讲义时明确所见范围，不声称完整观看了视频。

| 来源 | 可以支持的设计方向 | 不能推出的结论 | 本技能的实施 |
|---|---|---|---|
| Merrill, First Principles of Instruction (2002) | 围绕完整问题，激活已有经验、示范、应用、整合 | 此篇是理论综合，不是对所有原则的系统实证检验；不能保证留存 | 展示完整任务，再从较简单的问题逐渐增加条件 |
| Mayer & Pilegard，预训练与分段章节 | 先认识组成部分，再处理复杂连接；分成可消化步骤 | 不等于删掉机制或固定两分钟一集；可控分段与平台拆片不是同一操作 | 教清样本/输入/目标再讲训练；推理台阶处停顿 |
| Muller 等，Saying the wrong thing (2008) | 在其物理教学研究中，明确处理误解可以改善概念学习 | 不等于所有科普都要争论、错误越多越好，或可直接外推 B 站完播率 | 使用材料中有代表性的追问，明确原直觉为何失效 |
| 3Blue1Brown 官方神经网络讲义 | 可观察案例：同一数字识别对象贯穿结构说明，后续检查实际网络与最初直觉的差别 | 这是教学案例，不是形式优越性的对照实验；不能凭名气证明效果 | 用稳定的小数据/对象贯穿，并检验初始解释的边界 |
| Guo, Kim & Rubin (2014) | 四门 edX 课程约 690 万会话中的观看参与度分析 | 回顾性观察不证明某长度因果最优，观看参与度不等于学习效果，也不直接代表 B 站受众 | 时长按完整解释规划；观看与教学效果分别验收 |

一手来源：
- Merrill 作者论文：https://mdavidmerrill.wordpress.com/wp-content/uploads/2019/04/firstprinciplesbymerrill.pdf
- Mayer 与 Pilegard 章节：https://www.cambridge.org/core/books/abs/cambridge-handbook-of-multimedia-learning/principles-for-managing-essential-processing-in-multimedia-learning-segmenting-pretraining-and-modality-principles/DD24C2F48B9B1277CE59F78276110258
- Muller 等论文：https://onlinelibrary.wiley.com/doi/10.1111/j.1365-2729.2007.00248.x
- 3Blue1Brown 结构讲义：https://www.3blue1brown.com/lessons/neural-networks/
- 3Blue1Brown 检验网络讲义：https://www.3blue1brown.com/lessons/neural-network-analysis/
- Guo 等原论文：https://up.csail.mit.edu/other-pubs/las2014-pguo-engagement.pdf

## 技术史核查示范

Netflix 2012 官方说明：竞赛中的部分方法进入生产；最终大奖的整个组合，其新增收益不足以抵偿部署所需工程投入。不能将它改写为矩阵分解失败或竞赛成果完全没用。
来源：https://medium.com/netflix-techblog/netflix-recommendations-beyond-the-5-stars-part-1-55838468f429

原材料里的全体配对数、年份、固定曝光门槛、统一探索比例、法律解释、某算法“死亡”等都需分别核实。区分模型示意与普遍规律；蒸馏、双塔、特定训练节奏、多目标融合方式均是具体设计选项，不能因材料提到就当作所有系统必备。监督信号来自行为，不代表内心偏好的无噪声真值。
