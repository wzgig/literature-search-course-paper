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

## 2026-06-06 核心文献精读与中文证据补充

- 操作者：Codex
- 工作目标：继续下一步论文工作，为首批核心文献补 DOI、研究设计、样本量、孕周、截断值、关键结果和可写入论文的证据链，同时补充中文临床研究线索。
- 新增或修改文件：
  - `CORE_LITERATURE_NOTES.md`
  - `LITERATURE_SEARCH_RECORD.md`
  - `EVIDENCE_MATRIX.md`
  - `README.md`
  - `SOURCES.md`
  - `PROJECT_PROGRESS.md`
- 英文文献核验：
  - 使用 NCBI E-utilities `efetch` 分批核验 PMID 26735990、39947348、38825028、28314983、29214752、31734648、34979346 等核心文献。
  - 记录 PROGNOSIS 研究的 24+0 至 36+6 周疑似子痫前期单胎孕妇、开发队列 500 例、验证队列 550 例、截断值 38、1 周内排除 NPV 99.3%、4 周内阳性预测 PPV 36.7%。
  - 记录 2025 Meta 分析中 sFlt-1/PlGF 比值合并敏感度 0.83、特异度 0.88、AUC 0.92，优于单项 sFlt-1 或 PlGF。
  - 记录 2017 双截断值 Meta 分析、2024 MoM 截断值 11.5 预测 2 周内重症特征研究、Ann Lab Med 和 Clin Chem Lab Med 等医检相关文献。
- 中文证据补充：
  - 核验胡吉霞等 2022《临床与病理杂志》中文临床研究，记录 DOI、50 例 EOPE、60 例对照、sFlt-1/PlGF 比值预测 EOPE AUC 0.873、预测不良结局 AUC 0.936。
  - 核验杨岚等 2024《重庆医科大学学报》研究，记录 188 例孕妇、孕 16-18 周免疫荧光法检测 PLGF/SFLT-1/GLYFN，三项联合 AUC 0.986。
  - 记录刘鹏等 2026《中国妇产科临床杂志》与 SinoMed 条目作为待全文核实中文线索。
- 验证结果：
  - `CORE_LITERATURE_NOTES.md` 已形成引言背景、机制基础、检测与报告、预测与排除价值、国内应用、局限与展望 6 条证据链。
  - `EVIDENCE_MATRIX.md` 已扩展至英文核心研究、医学检验相关研究和中文临床研究分层。
- git 状态：本次记录添加后需要提交并推送。

## 2026-06-06 详细大纲与课程论文初稿启动

- 操作者：Codex
- 工作目标：根据任务规划、证据矩阵和核心文献精读笔记，进入论文写作阶段，形成详细章节大纲并启动课程论文初稿。
- 新增或修改文件：
  - `COURSE_PAPER_DETAILED_OUTLINE.md`
  - `COURSE_PAPER_DRAFT.md`
  - `README.md`
  - `PROJECT_PROGRESS.md`
- 写作内容：
  - `COURSE_PAPER_DETAILED_OUTLINE.md` 明确全文章节、建议字数、段落级写作提纲、图表计划和写作风险控制。
  - `COURSE_PAPER_DRAFT.md` 已完成题目、英文题名、中文摘要、关键词、英文摘要、英文关键词、引言和第 1 章“文献检索策略与筛选过程”初稿。
  - 初稿引用采用临时顺序编码，后续需按课程模板和最终参考文献表统一校对。
- 使用证据：
  - NICE PLGF-based testing guidance。
  - Zeisler et al. 2016 PROGNOSIS study。
  - Zhang et al. 2025 systematic review and meta-analysis。
  - Zhao et al. 2017 dual-cutoff meta-analysis。
  - Espinoza et al. 2024 MoM risk prediction study。
  - 胡吉霞等 2022 中文临床研究。
- 验证结果：
  - 初稿内容与当前题目、任务边界和“不制作 PPT”要求一致。
  - 引言和检索策略中的关键数据均可在 `CORE_LITERATURE_NOTES.md`、`EVIDENCE_MATRIX.md` 或 `LITERATURE_SEARCH_RECORD.md` 中追溯。
- git 状态：本次记录添加后需要提交并推送。

## 2026-06-06 课程论文第 2-3 章初稿

- 操作者：Codex
- 工作目标：继续课程论文正文写作，完成机制基础和检测方法学两部分，使论文从检索策略进入医学检验专业分析。
- 新增或修改文件：
  - `COURSE_PAPER_DRAFT.md`
  - `SOURCES.md`
  - `PROJECT_PROGRESS.md`
- 写作内容：
  - 将 `COURSE_PAPER_DRAFT.md` 版本更新为 v0.2。
  - 新增第 2 章“子痫前期与血管生成失衡机制”，包括子痫前期临床特点、检验需求、sFlt-1 与 PlGF 的血管生成平衡意义、比值优于单项指标的理论基础、机制证据向临床检验应用转化。
  - 新增第 3 章“sFlt-1/PlGF 比值的检测原理与方法学特点”，包括样本类型、检测平台、结果表达、截断值解释、单项指标与比值/联合检测、报告和质控要点。
  - 临时参考文献新增 Burwick 2024、Stepan 2023、Verlohren 2022、Bremner 2022、Caillon 2018。
- 来源同步：
  - `SOURCES.md` 新增 PubMed PMID 38350106 和 PMID 28851242 来源记录。
- 验证结果：
  - 新增章节围绕“辅助诊断、短期排除、风险分层”，避免把 sFlt-1/PlGF 比值写成独立确诊指标。
  - 第 3 章已突出样本、平台、孕周、截断值、质控和报告解释，符合医学检验技术专业方向。
- git 状态：本次记录添加后需要提交并推送。

## 2026-06-06 课程论文第 4 章证据主体初稿

- 操作者：Codex
- 工作目标：继续课程论文主体写作，完成第 4 章“sFlt-1/PlGF 比值在早期预测和辅助诊断中的证据”初稿。
- 新增或修改文件：
  - `COURSE_PAPER_DRAFT.md`
  - `PROJECT_PROGRESS.md`
- 写作内容：
  - 将 `COURSE_PAPER_DRAFT.md` 版本更新为 v0.3。
  - 新增第 4 章，按证据类型和应用场景展开：短期排除、阳性预测与辅助诊断、系统综述与 Meta 分析、重症风险分层、中文临床研究、证据综合和临床检验定位。
  - 重点使用 PROGNOSIS 研究、Zhang 2025 Meta 分析、Zhao 2017 双截断 Meta、Espinoza 2024 MoM 风险分层研究、胡吉霞 2022 和杨岚 2024 中文临床研究。
  - 临时参考文献新增杨岚等 2024 中文研究。
- 验证结果：
  - 第 4 章明确区分 rule-out、rule-in/辅助诊断和风险分层，避免把阳性预测结果夸大为确诊依据。
  - 中文研究已作为国内应用证据纳入，但同时说明样本量和外推限制。
- git 状态：本次记录添加后需要提交并推送。
