# 大学生课程论文与毕业设计相关技能/插件筛选评价

记录日期：2026-06-06

本文件记录面向《文献检索与论文写作》课程论文的外部 skills、插件和本机已有能力筛选结果。筛选原则是：优先服务课程论文写作、文献检索、引用校验、证据矩阵、论文审稿式自查和 Word/PDF 排版；不安装低可信、低安装量、重复度高或与本项目任务无关的技能。

## 1. 筛选标准

| 标准 | 判断方式 |
| --- | --- |
| 任务匹配度 | 是否直接支持课程论文、毕业论文、文献综述、医学文献检索、引用管理、论文审校 |
| 来源质量 | GitHub 星标、更新日期、仓库规模、是否有明确维护者和说明 |
| 安装量 | skills.sh 或 `npx skills find` 显示的安装量，优先考虑 1K+ 或来源特别可靠者 |
| 重复度 | 本机已存在 `literature-review`、`citation-management`、`paper-writing-section`、`paper-audit`、`documents` 等能力，重复技能默认不安装 |
| 安全提示 | 安装器安全扫描、是否有脚本行为、是否需要后续审查 |
| 本项目适配 | 当前只写课程论文，不制作 PPT；优先 Word/DOCX、Markdown、PubMed、医学综述工作流 |

## 2. 已检索关键词

使用 `npx skills find`、GitHub 元数据和网页来源交叉筛选：

- `thesis dissertation academic writing`
- `graduation thesis`
- `medical research writing`
- `systematic literature review medical`
- `academic paper audit`
- `docx thesis word`
- `bibliography reference management academic`

## 3. 安装的优质技能

| 技能 | 来源 | 安装量/质量依据 | 本地路径 | 本项目用途 | 评价 |
| --- | --- | --- | --- | --- | --- |
| `academic-paper` | `imbad0202/academic-research-skills` | 同源仓库约 27.7K stars，2026-06-06 仍活跃；技能支持论文计划、提纲、综述、引用检查、格式转换 | `C:\Users\Zicheng Wang\.agents\skills\academic-paper` | 辅助课程论文结构、摘要、章节写作、引用检查和 Markdown/DOCX 工作流 | 适合安装，但实际写作必须以本项目检索记录和证据矩阵为准 |
| `academic-paper-reviewer` | `imbad0202/academic-research-skills` | 同源仓库质量高；支持多视角论文评审 | `C:\Users\Zicheng Wang\.agents\skills\academic-paper-reviewer` | 论文初稿后做审稿式检查，发现逻辑、证据、结构和格式风险 | 适合最终质检阶段使用 |
| `academic-pipeline` | `imbad0202/academic-research-skills` | `npx skills find` 显示约 2.3K installs；协调研究、写作、审查、修改流程 | `C:\Users\Zicheng Wang\.agents\skills\academic-pipeline` | 作为端到端流程提醒，避免漏掉检索、完整性检查和二次审校 | 适合安装，但不应机械执行其中所有环节 |
| `deep-research` | `imbad0202/academic-research-skills` | 与 `academic-pipeline` 配套；支持文献综述、事实核查、系统综述模式 | `C:\Users\Zicheng Wang\.agents\skills\deep-research` | 补充深度研究流程，特别是证据合成和来源核查 | 与本机已有 `literature-review` 有重叠，保留为 pipeline 依赖 |

安装命令：

```powershell
npx --yes skills add imbad0202/academic-research-skills --skill academic-paper --skill academic-paper-reviewer --skill academic-pipeline --skill deep-research -g -y
```

验证结果：

- `Test-Path` 确认四个技能的 `SKILL.md` 均存在。
- `npx --yes skills list -g --json` 可列出四个技能。
- 安装器显示 Codex 本地副本已复制；PromptScript 全局安装阶段提示不支持全局安装，不影响 Codex 本地技能副本存在。
- 安装器安全扫描：Gen 为 Safe，Socket 为 0 alerts；Snyk 对 `academic-paper`、`academic-pipeline`、`deep-research` 标为 Med Risk，对 `academic-paper-reviewer` 标为 Low Risk。后续若调用技能内脚本，应先审查具体脚本。

## 4. 未安装或暂缓的候选

| 候选 | 来源/结果 | 未安装原因 |
| --- | --- | --- |
| `endigo/claude-skills@academic-research-writer` | `npx skills find` 显示约 1.3K installs；GitHub 仓库仅约 7 stars | 安装量尚可，但仓库质量信号弱，且与已安装 `academic-paper` 重复 |
| `affaan-m/everything-claude-code@literature-review` | `npx skills find` 显示约 1.2K installs | 本机已有 `literature-review`，避免重复和覆盖 |
| `bytedance/deer-flow@systematic-literature-review` | `npx skills find` 显示约 822 installs；仓库约 70K stars | 仓库质量高，但更偏通用长任务/智能体框架；本项目只需课程论文检索与写作，暂不引入 |
| `huangwb8/chineseresearchlatex@systematic-literature-review` | `npx skills find` 显示约 789 installs | 主要面向中文科研 LaTeX 工作流；本项目以课程论文模板和 Word/DOCX 为主 |
| 多个 citation/bibliography 小技能 | 安装量多在 100-150 左右 | 本机已有 `citation-management`，且更贴合 PMID/DOI/BibTeX 校验 |
| `docx` 或 thesis 模板类低安装量技能 | 多数安装量低于 100 | 本机已有 `documents` 插件和 LibreOffice/Pandoc，暂不增加重复依赖 |

## 5. 插件适配结论

当前可用插件中，与本项目最相关的是：

| 插件 | 状态 | 用途 | 结论 |
| --- | --- | --- | --- |
| Documents | 已可用 | 创建、编辑、渲染和检查 Word/DOCX 文件 | 后续论文成稿阶段优先使用 |
| Browser/Chrome | 已可用 | 访问网页来源、核查指南、数据库页面 | 检索阶段按需使用 |
| Presentations | 已可用 | 制作 PPT/PPTX | 当前用户已明确不制作 PPT，暂不使用 |
| Spreadsheets | 已可用 | 处理表格、证据矩阵或选题表 | 原始选题表含隐私信息，公开仓库不提交；证据矩阵优先用 Markdown |

## 6. 后续使用规则

1. 写作阶段以 `COURSE_PAPER_TASK_PLAN.md`、`LITERATURE_SEARCH_RECORD.md` 和 `EVIDENCE_MATRIX.md` 为主线。
2. 新安装技能只作为辅助流程，不允许替代真实文献检索、引用校验和来源记录。
3. 每次新增技能、插件、来源或论文材料，都必须同步更新 `SOURCES.md` 与 `PROJECT_PROGRESS.md`。
4. 新技能在后续新会话或重启 Codex 后会更稳定地自动加载。

