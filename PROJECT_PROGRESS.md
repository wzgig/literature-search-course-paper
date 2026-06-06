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
