# 文献检索与论文写作课程论文

本仓库用于保存《文献检索与论文写作》课程论文相关材料、选题依据、文献来源和写作进展。

GitHub 仓库地址：https://github.com/wzgig/literature-search-course-paper

## 项目主题与当前交付

本项目已形成两条课程论文工作线：

1. 《文献检索与论文写作》课程论文：
   `可溶性fms样酪氨酸激酶-1/胎盘生长因子比值在子痫前期早期预测中的临床检验应用进展`
2. 《基因检测与解读》课程论文：
   `MSH3基因的检测与分析`

当前最新交付为 MSH3 基因检测课程论文，已根据第 81 号基因 `MSH3` 完成检索记录、证据矩阵、精读笔记、Markdown 初稿和模板化 Word 正式稿。

## 当前文件

| 文件 | 说明 |
| --- | --- |
| `文献检索与论文写作课程论文任务书(1).docx` | 课程论文任务书 |
| `文献检索与论文写作结课论文模板-(1).doc` | 课程论文模板 |
| `文献检索结课论文选题表_公开摘要.md` | 已登记选题的脱敏公开摘要 |
| `AGENTS.md` | 项目工作规则 |
| `PROJECT_PROGRESS.md` | 项目进展记录 |
| `SOURCES.md` | 数据、网页和文献来源记录 |
| `TOOLING.md` | 本地工具与技能配置记录 |
| `SKILL_PLUGIN_EVALUATION.md` | 课程论文/毕业设计相关技能和插件筛选评价 |
| `COURSE_PAPER_REUSABLE_WORKFLOW.md` | 可复用课程论文工作流程说明文档 |
| `skills/course-paper-workflow/SKILL.md` | 可复制到 Codex skills 目录复用的课程论文工作流 skill |
| `COURSE_PAPER_TASK_PLAN.md` | 高分导向的课程论文任务规划 |
| `COURSE_PAPER_DETAILED_OUTLINE.md` | 课程论文详细大纲、证据分配和图表计划 |
| `COURSE_PAPER_DRAFT.md` | 课程论文 Markdown 初稿 |
| `COURSE_PAPER_FORMATTED.docx` | 按课程论文 Word 规范排版后的正式版草稿 |
| `TOPIC_DUPLICATE_CHECK.md` | 当前题目与选题表的查重记录 |
| `LITERATURE_SEARCH_RECORD.md` | 文献检索式、检索结果和筛选过程记录 |
| `EVIDENCE_MATRIX.md` | 核心文献证据矩阵 |
| `CORE_LITERATURE_NOTES.md` | 核心文献精读笔记和可写入论文的证据链 |
| `基因检测与解读_MSH3结课论文/` | 《基因检测与解读》MSH3 结课论文资料文件夹 |
| `基因检测与解读_MSH3结课论文/README.md` | MSH3 文件夹索引 |
| `基因检测与解读_MSH3结课论文/基因检测与解读-结课论文任务书-25医检专升本.docx` | 《基因检测与解读》课程论文任务书 |
| `基因检测与解读_MSH3结课论文/MSH3_COURSE_PAPER_TASK_PLAN.md` | MSH3 基因检测课程论文任务规划 |
| `基因检测与解读_MSH3结课论文/MSH3_LITERATURE_SEARCH_RECORD.md` | MSH3 文献检索式、结果数量和筛选记录 |
| `基因检测与解读_MSH3结课论文/MSH3_EVIDENCE_MATRIX.md` | MSH3 核心证据矩阵 |
| `基因检测与解读_MSH3结课论文/MSH3_CORE_LITERATURE_NOTES.md` | MSH3 核心文献精读笔记 |
| `基因检测与解读_MSH3结课论文/MSH3_COURSE_PAPER_DRAFT.md` | MSH3 课程论文 Markdown 初稿 |
| `基因检测与解读_MSH3结课论文/MSH3_COURSE_PAPER_FORMATTED.docx` | MSH3 课程论文按模板排版后的正式 Word 草稿 |
| `基因检测与解读_MSH3结课论文/scripts/build_msh3_course_paper_docx.py` | 生成 MSH3 正式 Word 版的脚本 |

## 工作规则

每次修改、检索、写作或整理文件后，都要更新 `PROJECT_PROGRESS.md`；每次新增资料来源，都要更新 `SOURCES.md`。形成有意义的修改后，应提交 git 并推送到 GitHub。

## 本地工具

当前已配置 LibreOffice、Pandoc、`openai-docs`、`citation-management`、`academic-paper`、`academic-paper-reviewer`、`academic-pipeline` 和 `deep-research` 等工具/技能。具体版本、路径、用途和注意事项见 `TOOLING.md` 与 `SKILL_PLUGIN_EVALUATION.md`。

本项目流程已整理为 `COURSE_PAPER_REUSABLE_WORKFLOW.md`，并生成本地 skill `course-paper-workflow`。该 skill 的项目内副本位于 `skills/course-paper-workflow/SKILL.md`，同时已复制到 `C:\Users\Zicheng Wang\.codex\skills\course-paper-workflow\SKILL.md`，便于后续课程论文项目复用。

## 隐私提示

本地原始文件 `文献检索结课论文选题表.xlsx` 包含姓名和学号，公开 GitHub 仓库默认不提交该文件。公开仓库仅保留脱敏摘要，便于确认选题是否重复。
