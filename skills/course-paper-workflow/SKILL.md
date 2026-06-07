---
name: course-paper-workflow
description: Use when assisting with Chinese course papers, literature retrieval and paper writing assignments, especially when the task involves reading a course task sheet/template/topic table, avoiding duplicate topics, collecting sources, drafting a literature-review paper, formatting DOCX/Word output, recording project progress, and pushing to GitHub.
---

# Course Paper Workflow

Use this skill for Chinese course-paper or literature-review projects that need traceable search, writing, Word formatting, and GitHub hygiene.

## First Actions

1. Read project rules first:
   - `AGENTS.md`
   - `PROJECT_PROGRESS.md`
   - `SOURCES.md`
2. Inspect local materials:
   - course task sheet
   - paper template
   - topic table or selected-topic list
   - existing draft, outline, search records, evidence matrix
3. Check git state with:

```powershell
git -c core.longpaths=true status --short --branch
```

Do not revert unrelated dirty files. Work with user changes and stage only files relevant to the current task.

## Non-Negotiable Tracking

After every meaningful step:

- Append `PROJECT_PROGRESS.md` with date, operator, goal, changed files, sources, validation, and git status.
- Update `SOURCES.md` for every new article, webpage, database search, local source, tool, skill, or script.
- Commit and push to `origin/main` when the work is meaningful and a remote is configured.
- If push fails, record the blocker in `PROJECT_PROGRESS.md`.

## Privacy Rules

- Do not commit original topic tables containing names, student IDs, phone numbers, emails, or other personal information.
- Use a desensitized topic summary if topic-deduplication evidence is needed in a public repo.
- Before public DOCX/PDF output, scan for keywords such as `姓名`, `学号`, `班级`, `电话`, `邮箱`, `身份证`, actual user names, and account names.
- Ignore Office temp files such as `~$*.docx`, `~$*.xlsx`, `*.tmp`, and accidental local copies unless the user explicitly asks to clean them.

## Workflow

### 1. Understand Requirements

Extract from the task sheet:

- word count and deliverable type
- whether PPT is needed
- topic rules and duplicate-topic constraints
- required structure
- reference count and style
- scoring rubric
- submission format and deadline

Record conclusions in `PROJECT_PROGRESS.md`.

### 2. Topic Selection

Read the topic table and create or update `TOPIC_DUPLICATE_CHECK.md`.

Choose topics that are:

- not duplicated by disease, indicator, method, or application scenario
- narrow enough for a course paper
- supported by guidelines, systematic reviews, meta-analyses, or high-quality studies
- connected to the student's major
- suitable for discussing methods, clinical application, limitations, and quality control

### 3. Planning

Create or update `COURSE_PAPER_TASK_PLAN.md` and include:

- task boundary
- final topic
- research questions
- scoring-standard mapping
- databases and search strings
- inclusion/exclusion criteria
- evidence-management fields
- chapter plan
- figure/table plan
- final checklist

### 4. Literature Search

Create or update:

- `LITERATURE_SEARCH_RECORD.md`
- `SOURCES.md`

Use layered searches:

1. broad search to build the candidate pool
2. systematic review/meta-analysis search
3. clinical application/implementation search
4. Chinese database or journal-site search when relevant
5. guideline and official-source search

For biomedical topics, prefer PubMed, guideline pages, journal pages, DOI, PMID, and official PDFs. Use web browsing for current or uncertain facts.

### 5. Evidence Management

Create or update:

- `EVIDENCE_MATRIX.md`
- `CORE_LITERATURE_NOTES.md`

Classify each source as `核心`, `候选`, or `待核`.

Do not turn unverified search-result snippets into firm claims. Keep DOI, PMID, sample size, design, population, platform, cutoff, result, limitation, and paper-use position when possible.

### 6. Outline and Draft

Create or update:

- `COURSE_PAPER_DETAILED_OUTLINE.md`
- `COURSE_PAPER_DRAFT.md`

Recommended structure:

1. title
2. Chinese abstract and keywords
3. English abstract and keywords
4. introduction
5. literature search strategy
6. mechanism/background
7. methods or testing principles
8. core evidence review
9. limitations, quality control, and clinical interpretation
10. search/writing reflection and academic ethics
11. conclusion
12. references

Write cautiously:

- separate rule-out, rule-in, diagnosis, prediction, and risk stratification
- avoid overstating AUC, sensitivity, or single-study findings
- discuss population, platform, cutoff, and applicability limits
- connect evidence to the student's professional field

### 7. Tables and Figures

Useful high-score artifacts:

- literature search and screening table
- core evidence matrix
- indicator/method comparison table
- clinical or application pathway figure

For DOCX, keep tables to 2-3 columns when possible. Long Markdown tables often render poorly; use Python/Word table generation for final DOCX if needed.

### 8. Word/DOCX Formatting

Preferred robust path:

1. Write content in Markdown.
2. Use Pandoc and the course template/reference DOCX.
3. Use `python-docx` for real Word tables, cover page, page breaks, headers, footers, and table widths.
4. Export with LibreOffice:

```powershell
& 'C:\Program Files\LibreOffice\program\soffice.com' --headless --norestore --convert-to pdf --outdir $env:TEMP .\COURSE_PAPER_FORMATTED.docx
```

5. Render pages with Poppler:

```powershell
pdfinfo <pdf-path>
pdftoppm -png -r 120 <pdf-path> <output-prefix>
```

6. Inspect cover,目录, abstract, first body page, tables, figures, references, and last page.

If a bundled document-rendering script fails on Windows paths or `soffice.exe`, use `soffice.com` plus Poppler manually and record the workaround.

### 9. Validation

Run:

```powershell
git -c core.longpaths=true diff --check
python -m py_compile .\scripts\build_course_paper_docx.py
git -c core.longpaths=true status --short --branch
```

For DOCX:

- verify PDF page count and A4/expected page size
- render page PNGs
- inspect critical pages visually
- extract DOCX text and scan for personal information

### 10. Git

Use:

```powershell
git -c core.longpaths=true add <changed-files>
git -c core.longpaths=true commit -m "docs: describe the step"
git -c core.longpaths=true push origin main
```

Stage only files relevant to the current step. Leave unrelated user-created dirty files alone.

## Deliverable Checklist

- `PROJECT_PROGRESS.md` updated
- `SOURCES.md` updated if any source/tool changed
- topic duplicate check done
- task plan done
- search record done
- evidence matrix done
- core notes done
- outline done
- Markdown draft done
- references 15+ and verifiable
- Word/DOCX formatted
- render QA done
- privacy scan done
- git commit and push done
