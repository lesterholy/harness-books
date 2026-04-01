# Claude Code 和 Codex 的 Harness 设计哲学

副标题：殊途同归还是各表一枝

这是一套新的比较型内容，放在 `book2-comparing/` 目录下。它不打算把 Claude Code 和 Codex 写成两份产品说明书，也不打算罗列功能清单，而是试图回答一个更有工程价值的问题：

同样是把大模型接进终端、文件系统、工具调用和团队流程里，为什么两套系统最后会长出相似的器官，却保持不同的骨架？

内容边界：

- 这份内容基于源码结构、模块边界、公开文档占位文件和仓库内工程约束来写
- 这份内容不会附带 Claude Code 或 Codex 的源代码副本
- 这份内容会在必要范围内引用文件路径、模块名和少量实现细节，用于支撑架构判断
- 重点是比较 harness 设计哲学，而不是转录受版权保护的实现文本

建议阅读顺序：

1. [preface.md](preface.md)
2. [chapter-01-why-this-comparison.md](chapter-01-why-this-comparison.md)
3. [chapter-02-two-control-planes.md](chapter-02-two-control-planes.md)
4. [chapter-03-loop-thread-and-rollout.md](chapter-03-loop-thread-and-rollout.md)
5. [chapter-04-tools-sandbox-and-exec-policy.md](chapter-04-tools-sandbox-and-exec-policy.md)
6. [chapter-05-skills-hooks-and-local-governance.md](chapter-05-skills-hooks-and-local-governance.md)
7. [chapter-06-delegation-verification-and-state.md](chapter-06-delegation-verification-and-state.md)
8. [chapter-07-convergence-and-divergence.md](chapter-07-convergence-and-divergence.md)
9. [chapter-08-how-to-choose-or-build.md](chapter-08-how-to-choose-or-build.md)
10. [appendix-a-source-map.md](appendix-a-source-map.md)
11. [appendix-b-checklists.md](appendix-b-checklists.md)

当前定位：

- 约 50 页的比较型长文初稿
- 风格延续前一套内容的冷静叙述，但更强调对照、归类和判断
- 写法基于源码，但尽量超脱源码目录，不把文字写成注释合集

图稿目录：

- `book2-comparing/diagrams/diag-01-control-plane-comparison.puml`
- `book2-comparing/diagrams/diag-02-continuity-comparison.puml`
- `book2-comparing/diagrams/diag-03-tool-governance-comparison.puml`
- `book2-comparing/diagrams/diag-04-local-governance-comparison.puml`

图稿命名约定：

- 所有图统一使用 `diag-` 前缀
- `.puml` 是主编辑源文件
- `.png` 是章节里实际嵌入的导出产物

如果继续扩展，最自然的方向有三个：

- 为各章补充更细的行号级文件引用
- 补一组 `book2-comparing/diagrams/` 的比较图稿
- 把第 4 章和第 6 章再扩成更偏“团队设计准则”的版本
