# 项目进展记录

本文件用于记录《文献检索与论文写作》课程论文项目的每次工作进展。后续每次修改都必须追加记录，不能只依赖 git 历史。

## 2026-06-05 初始材料阅读与选题建议

- 操作者：Codex
- 工作目标：阅读课程任务书、论文模板和选题表，理解课程论文要求，并提出适合医检专业与课程要求的论文题目。
- 涉及文件：
  - `文献检索与论文写作课程论文任务书(1).docx`
  - `文献检索与论文写作结课论文模板-(1).doc`
  - `文献检索结课论文选题表.xlsx`
- 关键结论：
  - 课程论文要求 5000 字以上，面向 23 级医学检验技术专业。
  - 题目需自主命题且避免重复，应结合临床检验诊断、实验技术应用、质量控制、疾病标志物、检验医学与临床医学交叉等方向。
  - 评分标准强调学术规范、选题创新、内容深度、文献综述和写作表达；高分文献综述建议覆盖 15 篇以上权威文献。
  - 建议题目：`血清肌酐-胱抑素C联合估算肾小球滤过率与尿白蛋白/肌酐比值在慢性肾脏病分期中的应用进展`。
- 使用来源：见 `SOURCES.md` 的本地材料和 CKD 初始文献来源。
- 验证结果：已成功读取 `.docx` 任务书、`.doc` 模板和 `.xlsx` 选题表内容。
- git 状态：当时尚未初始化 git 仓库。

## 2026-06-06 项目跟踪文件与 GitHub 推送准备

- 操作者：Codex
- 工作目标：建立项目规则、进展记录和来源记录文件，为后续写作、检索、修改和 GitHub 同步提供可追溯基础。
- 新增文件：
  - `AGENTS.md`
  - `PROJECT_PROGRESS.md`
  - `SOURCES.md`
  - `README.md`
  - `.gitignore`
  - `文献检索结课论文选题表_公开摘要.md`
- 关键结论：
  - `文献检索结课论文选题表.xlsx` 包含多名学生姓名和学号，公开仓库默认不提交原始表。
  - 为便于公开查看选题避重依据，新增只含选题名称的脱敏公开摘要。
  - GitHub CLI 已登录 `wzgig` 账号，可用于创建仓库和推送。
- 使用来源：本地文件列表、GitHub CLI 状态、`SOURCES.md` 中列出的初始来源。
- 验证结果：已确认选题表共有 51 条学生记录，其中 45 条已有选题、6 条未填写选题。
- git 状态：已创建初始提交 `676c70d`，提交信息为 `docs: initialize course paper tracking`。

## 2026-06-06 GitHub 公开仓库创建与推送

- 操作者：Codex
- 工作目标：将项目公开安全版本推送到 GitHub，便于后续查看、同步和继续写作。
- 涉及文件：
  - `.gitignore`
  - `AGENTS.md`
  - `PROJECT_PROGRESS.md`
  - `README.md`
  - `SOURCES.md`
  - `文献检索与论文写作课程论文任务书(1).docx`
  - `文献检索与论文写作结课论文模板-(1).doc`
  - `文献检索结课论文选题表_公开摘要.md`
- GitHub 仓库：
  - https://github.com/wzgig/literature-search-course-paper
- 隐私处理：
  - 原始 `文献检索结课论文选题表.xlsx` 包含姓名和学号，已通过 `.gitignore` 保持本地保存，不进入公开仓库和公开 git 历史。
  - 公开仓库使用 `文献检索结课论文选题表_公开摘要.md` 作为脱敏替代材料。
- 验证结果：
  - GitHub CLI 登录账号：`wzgig`。
  - 公开仓库创建成功。
  - 本地 `main` 已跟踪 `origin/main`。
- git 状态：本次记录添加后需要再次提交并推送。

## 2026-06-06 本地写作工具与技能安装

- 操作者：Codex
- 工作目标：安装并验证课程论文写作、文档转换、文献检索和参考文献管理所需的本地工具与技能。
- 新增或修改文件：
  - `TOOLING.md`
  - `README.md`
  - `SOURCES.md`
  - `PROJECT_PROGRESS.md`
- 安装工具：
  - LibreOffice 26.2.3.2，路径 `C:\Program Files\LibreOffice\program\soffice.com`。
  - Pandoc 3.9.0.2，路径 `C:\Users\Zicheng Wang\AppData\Local\Pandoc\pandoc.exe`。
- 安装技能：
  - `openai-docs`，安装到 `C:\Users\Zicheng Wang\.codex\skills\openai-docs`。
  - `citation-management`，安装到 `C:\Users\Zicheng Wang\.agents\skills\citation-management`。
- 外部技能筛选：
  - 使用 `npx skills find` 搜索 `academic writing`、`literature review`、`citation bibtex`、`paper writing`、`docx document`。
  - 未安装低安装量、来源不明确或与本机已有技能重复的外部技能。
  - 选择安装 `citation-management`，用于 DOI/PMID/BibTeX 元数据管理和引用校验。
- 验证结果：
  - `soffice --headless --version` 可输出 LibreOffice 版本。
  - `pandoc --version` 可输出 Pandoc 版本。
  - LibreOffice 已成功将课程任务书 `.docx` 转换为临时 PDF，输出目录 `%TEMP%\course-paper-tooling-check`。
  - Pandoc 已成功将 `README.md` 转换为临时 HTML，输出目录 `%TEMP%\course-paper-tooling-check`。
  - LibreOffice 安装器提示需要重启电脑以完成集成。
  - `openai-docs` 按官方 skill installer 成功安装；新会话或重启 Codex 后生效。
  - `citation-management` 已复制到本地 skills 目录；安装器同时提示 PromptScript 不支持全局安装，但 Codex 本地技能副本存在。
- git 状态：本次记录添加后需要提交并推送。

## 2026-06-06 高分导向课程论文任务规划

- 操作者：Codex
- 工作目标：根据课程论文任务书和评分标准，制定满足高分要求的可执行任务规划。
- 新增或修改文件：
  - `COURSE_PAPER_TASK_PLAN.md`
  - `README.md`
  - `PROJECT_PROGRESS.md`
- 规划内容：
  - 明确拟定题目、研究问题和高分理由。
  - 将评分标准拆解为学术规范性、选题与创新性、内容深度、文献综述、写作表达 5 个评分维度的行动方案。
  - 设计中英文数据库检索策略、关键词、示例检索式、纳入排除标准和文献管理方案。
  - 规划 6500-7500 字论文结构、章节字数、核心图表、PPT 汇报页结构和 7 天执行时间表。
  - 设置最终提交前检查清单，覆盖字数、文献数量、引用、图表、格式、伦理、PPT 和 GitHub 记录。
- 使用来源：
  - `文献检索与论文写作课程论文任务书(1).docx`
  - `文献检索与论文写作结课论文模板-(1).doc`
  - `文献检索结课论文选题表_公开摘要.md`
  - `SOURCES.md`
  - `TOOLING.md`
- 验证结果：已重新读取任务书内容和评分表，规划逐项覆盖任务书要求和 100 分评分标准。
- git 状态：本次记录添加后需要提交并推送。

## 2026-06-06 修订任务边界与非重复选题

- 操作者：Codex
- 工作目标：根据用户最新要求，将任务规划调整为只撰写课程论文，不制作 PPT，并重新确认题目不与当前选题表重复。
- 新增或修改文件：
  - `COURSE_PAPER_TASK_PLAN.md`
  - `TOPIC_DUPLICATE_CHECK.md`
  - `README.md`
  - `SOURCES.md`
  - `PROJECT_PROGRESS.md`
- 关键调整：
  - 删除当前规划中的 PPT 制作任务和 PPT 提交检查项。
  - 不再采用旧题目“血清肌酐-胱抑素C联合估算肾小球滤过率与尿白蛋白/肌酐比值在慢性肾脏病分期中的应用进展”，因为其与选题表中“肾功能指标在慢性肾病分期中的应用探讨”等方向过近。
  - 当前推荐最终题目调整为“可溶性fms样酪氨酸激酶-1/胎盘生长因子比值在子痫前期早期预测中的临床检验应用进展”。
  - 已核对本地原始选题表中 45 个已登记题目，未发现“子痫前期”“sFlt-1”“PlGF”“胎盘生长因子”等重复方向。
  - `SOURCES.md` 已新增当前最终选题的初始权威来源，包括 NICE 指导、NEJM PROGNOSIS 研究、ISSHP 指南和综述文献。
- 验证结果：当前题目与选题表不重复；任务规划已只保留课程论文写作相关工作。
- git 状态：本次记录添加后需要提交并推送。

## 2026-06-06 课程论文与毕业设计相关技能/插件筛选安装

- 操作者：Codex
- 工作目标：根据用户要求，全网搜索并评价适合大学生课程结课论文、毕业设计、文献综述、学术写作、引用管理和论文审校的 skills/插件，安装高质量且适配本项目的技能。
- 新增或修改文件：
  - `SKILL_PLUGIN_EVALUATION.md`
  - `TOOLING.md`
  - `README.md`
  - `SOURCES.md`
  - `PROJECT_PROGRESS.md`
- 检索与评价：
  - 使用 `npx skills find` 搜索 `thesis dissertation academic writing`、`graduation thesis`、`medical research writing`、`systematic literature review medical`、`academic paper audit`、`docx thesis word`、`bibliography reference management academic`。
  - 使用 GitHub CLI 核查候选仓库质量，例如 `Imbad0202/academic-research-skills` 约 27.7K stars、`bytedance/deer-flow` 约 70K stars、`endigo/claude-skills` 约 7 stars。
  - 对比后，安装 `imbad0202/academic-research-skills` 的 `academic-paper`、`academic-paper-reviewer`、`academic-pipeline`、`deep-research`。
  - 暂缓安装 `endigo/academic-research-writer`、`bytedance/deer-flow@systematic-literature-review`、外部 `literature-review`、低安装量 citation/bibliography 小技能和 thesis/docx 模板类技能，原因见 `SKILL_PLUGIN_EVALUATION.md`。
- 安装路径：
  - `C:\Users\Zicheng Wang\.agents\skills\academic-paper`
  - `C:\Users\Zicheng Wang\.agents\skills\academic-paper-reviewer`
  - `C:\Users\Zicheng Wang\.agents\skills\academic-pipeline`
  - `C:\Users\Zicheng Wang\.agents\skills\deep-research`
- 验证结果：
  - `Test-Path` 确认四个技能的 `SKILL.md` 均存在。
  - `npx --yes skills list -g --json` 可列出四个技能。
  - 安装器显示 Codex 本地副本已复制；PromptScript 全局安装阶段提示不支持全局安装，不影响 Codex 本地技能副本存在。
  - 安装器安全扫描显示 Gen Safe、Socket 0 alerts；部分技能 Snyk Med Risk，后续调用脚本前需审查具体脚本行为。
- git 状态：本次记录添加后需要提交并推送。

## 2026-06-06 论文英文文献初检与证据矩阵建立

- 操作者：Codex
- 工作目标：按 `COURSE_PAPER_TASK_PLAN.md` 开始第一步论文工作，建立正式文献检索记录和核心证据矩阵。
- 新增或修改文件：
  - `LITERATURE_SEARCH_RECORD.md`
  - `EVIDENCE_MATRIX.md`
  - `README.md`
  - `SOURCES.md`
  - `PROJECT_PROGRESS.md`
- 检索记录：
  - PubMed 宽检索：`("sFlt-1/PlGF ratio" OR "sFlt-1:PlGF ratio" OR "soluble fms-like tyrosine kinase-1" OR "placental growth factor") AND (preeclampsia OR pre-eclampsia)`，结果 2305 条，记录首批 40 个 PMID。
  - PubMed 系统综述/Meta 检索：`("sFlt-1/PlGF" OR "PlGF") AND (preeclampsia OR pre-eclampsia) AND (systematic review OR meta-analysis)`，结果 47 条，记录首批 20 个 PMID。
  - PubMed 临床应用/实施检索：`("sFlt-1/PlGF ratio") AND (preeclampsia OR pre-eclampsia) AND (clinical utility OR implementation OR decision-making OR rule out)`，结果 135 条，记录首批 20 个 PMID。
- 初步核心证据：
  - 已将 NICE PLGF-based testing guidance、ISSHP 2021 guideline、NEJM PROGNOSIS study、2025 sFlt-1/PlGF 预测性能系统综述与 Meta 分析、2023 临床应用综述、2022 临床解释与实施综述等列入 `EVIDENCE_MATRIX.md`。
  - 证据矩阵按指南、英文核心研究与综述、中文线索分层，标注 `核心`、`候选`、`待核`。
- 验证结果：
  - 已通过 NCBI E-utilities 返回检索数量、PMID 列表和 ESummary 题名/期刊/作者信息。
  - 当前仍需继续补充中文数据库检索和核心文献 DOI、样本量、孕周范围、检测平台、截断值、主要结论。
- git 状态：本次记录添加后需要提交并推送。
