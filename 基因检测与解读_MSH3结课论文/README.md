# 基因检测与解读 MSH3 结课论文

本文件夹集中保存《基因检测与解读》课程论文任务书中第 81 号基因 `MSH3` 对应的写作材料、检索记录和正式 Word 成稿。

## 论文题目

`MSH3基因的检测与分析`

## 文件索引

| 文件 | 用途 |
| --- | --- |
| `基因检测与解读-结课论文任务书-25医检专升本.docx` | 原始课程任务书，用于确认选题、字数、评分标准和基因编号 |
| `MSH3_COURSE_PAPER_TASK_PLAN.md` | 任务规划、评分映射、章节安排和图表计划 |
| `MSH3_LITERATURE_SEARCH_RECORD.md` | PubMed/NCBI/法规来源检索式、结果数量和核心 PMID 记录 |
| `MSH3_EVIDENCE_MATRIX.md` | 核心证据矩阵，记录每条来源在论文中的用途 |
| `MSH3_CORE_LITERATURE_NOTES.md` | 核心文献精读笔记和可写入论文的证据链 |
| `MSH3_COURSE_PAPER_DRAFT.md` | 课程论文 Markdown 初稿 |
| `MSH3_COURSE_PAPER_FORMATTED.docx` | 按课程论文模板排版后的正式 Word 草稿 |
| `scripts/build_msh3_course_paper_docx.py` | 从 Markdown 初稿生成正式 Word 草稿的脚本 |

## 重新生成 Word

在项目根目录运行：

```powershell
python .\基因检测与解读_MSH3结课论文\scripts\build_msh3_course_paper_docx.py
```

脚本会读取本文件夹内的 `MSH3_COURSE_PAPER_DRAFT.md`，并使用项目根目录下的 `文献检索与论文写作结课论文模板-(1).doc` 作为模板来源，输出本文件夹内的 `MSH3_COURSE_PAPER_FORMATTED.docx`。

## 提交前检查

- Word 成稿只保留“姓名”“学号”空白占位，不写入真实个人信息；
- 查重报告附页为占位说明，正式提交前需要替换为学校认可平台的查重报告；
- 如继续修改论文，应同步更新根目录 `PROJECT_PROGRESS.md` 和 `SOURCES.md`。
