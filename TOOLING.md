# 本地工具与技能配置

本文件记录为课程论文项目准备的本地工具、Codex skills 和外部技能来源，便于后续继续写作、排版、文献整理和文件转换。

## 已安装工具

| 工具 | 版本 | 安装方式 | 本机路径 | 用途 | 备注 |
| --- | --- | --- | --- | --- | --- |
| LibreOffice | 26.2.3.2 | `winget install --id TheDocumentFoundation.LibreOffice --exact` | `C:\Program Files\LibreOffice\program\soffice.com` | 渲染、转换和检查 Word 文档；支持 `.doc`、`.docx` 到 PDF/图片等工作流 | 安装器提示需要重启电脑以完成集成 |
| Pandoc | 3.9.0.2 | `winget install --id JohnMacFarlane.Pandoc --exact` | `C:\Users\Zicheng Wang\AppData\Local\Pandoc\pandoc.exe` | Markdown、DOCX、HTML、PDF 等格式转换；辅助生成写作草稿和参考文献格式材料 | 当前 shell 可通过临时 PATH 调用；新终端通常会自动读取安装后的 PATH |

验证命令：

```powershell
$env:Path = "$env:LOCALAPPDATA\Pandoc;C:\Program Files\LibreOffice\program;$env:Path"
soffice --headless --version
pandoc --version
```

Smoke test：

- LibreOffice 已成功将课程任务书 `.docx` 转换为临时 PDF：`%TEMP%\course-paper-tooling-check\文献检索与论文写作课程论文任务书(1).pdf`。
- Pandoc 已成功将 `README.md` 转换为临时 HTML：`%TEMP%\course-paper-tooling-check\README.html`。

## 已安装或可用 Codex 技能

| 技能 | 本地状态 | 用途 |
| --- | --- | --- |
| `documents` | 已可用 | 创建、编辑、渲染和检查 `.docx` 文档 |
| `pdf` | 已可用 | 读取、渲染和检查 PDF 文件 |
| `literature-review` | 已可用 | 组织文献综述检索、专家视角问题和研究脉络整理 |
| `bib-search-citation` | 已可用 | 从本地 BibTeX/BibLaTeX 文献库检索和生成引用 |
| `paper-writing-section` | 已可用 | 按论文部分撰写摘要、引言、方法、讨论等内容 |
| `paper-audit` | 已可用 | 审稿式检查论文结构、证据、引用和提交风险 |
| `openai-docs` | 已安装到 `C:\Users\Zicheng Wang\.codex\skills\openai-docs` | 查询 OpenAI/Codex 官方文档；需要重启 Codex 后在新会话中自动加载 |
| `citation-management` | 已安装到 `C:\Users\Zicheng Wang\.agents\skills\citation-management` | 搜索 PubMed/Google Scholar、抽取 DOI/PMID/arXiv 元数据、生成和校验 BibTeX |
| `academic-paper` | 已安装到 `C:\Users\Zicheng Wang\.agents\skills\academic-paper` | 辅助论文计划、提纲、章节写作、引用检查和格式转换 |
| `academic-paper-reviewer` | 已安装到 `C:\Users\Zicheng Wang\.agents\skills\academic-paper-reviewer` | 论文初稿后进行多视角审稿式检查 |
| `academic-pipeline` | 已安装到 `C:\Users\Zicheng Wang\.agents\skills\academic-pipeline` | 协调研究、写作、完整性检查、审稿和修改流程 |
| `deep-research` | 已安装到 `C:\Users\Zicheng Wang\.agents\skills\deep-research` | 补充深度研究、文献综述、事实核查和证据合成流程 |

## 外部技能筛选记录

使用 `npx skills find` 搜索了以下关键词：

- `academic writing`
- `literature review`
- `citation bibtex`
- `paper writing`
- `docx document`

处理结果：

- 未安装低安装量或来源不明确的 `academic-writing`、`paper-writing`、`docx` 类第三方技能。
- 未安装外部 `literature-review`，因为本机已有同名成熟技能，避免重复或覆盖。
- 安装 `davila7/claude-code-templates@citation-management`，因为它补充了 DOI/PMID/BibTeX 校验能力，适合后续参考文献整理。安装器安全扫描结果显示 Gen 为 Safe、Socket 为 0 alerts、Snyk 为 Med Risk；后续使用前仍应审查脚本行为。

2026-06-06 追加筛选了课程论文、毕业设计、学术论文、系统综述、论文审校和引用管理相关技能：

- 使用 `npx skills find` 搜索 `thesis dissertation academic writing`、`graduation thesis`、`medical research writing`、`systematic literature review medical`、`academic paper audit`、`docx thesis word`、`bibliography reference management academic`。
- 重点比较 `imbad0202/academic-research-skills`、`endigo/claude-skills`、`bytedance/deer-flow`、`affaan-m/everything-claude-code`、`huangwb8/ChineseResearchLaTeX` 等来源。
- 安装 `imbad0202/academic-research-skills` 中的 `academic-paper`、`academic-paper-reviewer`、`academic-pipeline`、`deep-research`。该仓库约 27.7K stars，2026-06-06 仍活跃；其中 `academic-pipeline` 在 `npx skills find` 中显示约 2.3K installs。
- 未安装 `endigo/claude-skills@academic-research-writer`，因为虽然约 1.3K installs，但源仓库星标很低，且与新安装的 `academic-paper` 重复。
- 未安装 `bytedance/deer-flow@systematic-literature-review`，因为仓库质量高但工作流偏通用长任务，本项目当前只需要课程论文检索和 Word/DOCX 写作。
- 未安装低安装量 citation/bibliography 小技能，因为本机已有 `citation-management`。
- 详细评价见 `SKILL_PLUGIN_EVALUATION.md`。

## 后续使用建议

1. 写作和排版前，优先使用 `documents` + LibreOffice 做 DOCX 渲染检查。
2. 文献检索阶段，优先使用 `literature-review` 与 `citation-management`，并把检索式、来源链接和筛选结果写入 `SOURCES.md`。
3. 参考文献成稿前，用 DOI、PMID 或 PubMed 链接生成可校验条目，避免引用信息错误。
4. 每次新增工具、技能或来源，都要同步更新 `PROJECT_PROGRESS.md` 和 `SOURCES.md`。
