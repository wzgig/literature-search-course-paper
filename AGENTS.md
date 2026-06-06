# 项目工作规则

本项目是《文献检索与论文写作》课程论文资料夹。后续每次修改、检索、写作或整理文件时，必须遵守以下规则。

## 必做记录

1. 每次开始工作前，先查看 `PROJECT_PROGRESS.md` 和 `SOURCES.md`，确认已有进展、题目、来源和待办。
2. 每次修改后，必须在 `PROJECT_PROGRESS.md` 追加一条记录，至少写明：
   - 日期和操作者；
   - 本次工作目标；
   - 修改或新增的文件；
   - 使用的数据、文献、网址或本地材料；
   - 验证结果；
   - git 提交和推送状态。
3. 每次新增文献、网页、数据库检索结果或本地数据来源，必须同步更新 `SOURCES.md`，写清楚来源名称、链接或文件名、访问日期、用途和备注。
4. 每次形成有意义的修改后，必须执行 git 提交；如果已配置 GitHub 远程仓库，还要推送到 `origin/main`。
5. 如果因为隐私、网络、权限或 GitHub 认证问题无法推送，必须把阻塞原因写入 `PROJECT_PROGRESS.md`。

## 文件处理

1. 原始课程材料原则上不直接改写，包括任务书、论文模板和选题表；需要编辑时应先复制成新文件。
2. 公开发布前必须检查是否包含姓名、学号、联系方式等个人信息。包含个人信息的文件不得未经确认直接发布到公开仓库。
3. 论文写作、题目调整和文献整理应优先保留可追溯依据，避免只留下口头结论。
4. 文件名尽量使用清晰语义；新建文档优先放在项目根目录或后续明确创建的分类目录中。

## 推荐 git 流程

```powershell
git -c core.longpaths=true status --short
git -c core.longpaths=true add <changed-files>
git -c core.longpaths=true commit -m "docs: record project setup and sources"
git -c core.longpaths=true push origin main
```

提交前检查不要包含 Word/Excel 临时文件、缓存文件、误生成的备份文件或未确认公开的个人信息。
