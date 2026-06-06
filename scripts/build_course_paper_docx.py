from __future__ import annotations

import os
import subprocess
import tempfile
from pathlib import Path

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt


ROOT = Path(__file__).resolve().parents[1]
SOURCE_MD = ROOT / "COURSE_PAPER_DRAFT.md"
OUTPUT_DOCX = ROOT / "COURSE_PAPER_DRAFT.docx"
TEMPLATE_DOC = ROOT / "文献检索与论文写作结课论文模板-(1).doc"
SOFFICE = Path(os.environ.get("SOFFICE", r"C:\Program Files\LibreOffice\program\soffice.com"))
PANDOC = os.environ.get("PANDOC", "pandoc")


TABLES = {
    "[[TABLE1]]": (
        "表 1 文献检索与筛选流程概要",
        [
            ["步骤", "核心信息"],
            ["PubMed 宽检索", "围绕 sFlt-1、PlGF、sFlt-1/PlGF ratio 与 preeclampsia 建立英文候选池，共 2305 条结果。"],
            ["系统综述检索", "增加 systematic review、meta-analysis 限定，共 47 条结果，优先筛选综合证据。"],
            ["临床应用检索", "增加 clinical utility、implementation、rule out 等关键词，共 135 条结果，筛选管理决策相关文献。"],
            ["指南定向检索", "定向纳入 NICE PLGF-based testing guidance、ISSHP 指南和临床解释综述。"],
            ["中文补充检索", "使用“子痫前期”“sFlt-1”“胎盘生长因子”“PlGF”等关键词，纳入胡吉霞等、杨岚等中文研究。"],
            ["最终筛选", "按指南、Meta 分析、多中心研究、方法学研究和中文临床研究分层，形成 18 条临时参考文献。"],
        ],
        [1.45, 5.05],
    ),
    "[[TABLE2]]": (
        "表 2 sFlt-1、PlGF 与 sFlt-1/PlGF 比值比较",
        [
            ["指标", "核心解释", "临床检验定位"],
            ["sFlt-1", "抗血管生成相关因子，升高提示抗血管生成状态增强。", "用于机制解释和联合检测，但单项结果受孕周及个体差异影响。"],
            ["PlGF", "促血管生成因子，降低提示胎盘功能和血管生成支持不足。", "部分 PLGF-based tests 已进入指南推荐，可用于疑似早产期子痫前期辅助判断。"],
            ["sFlt-1/PlGF 比值", "同时整合 sFlt-1 升高和 PlGF 降低，反映血管生成失衡。", "适合短期排除、风险分层和辅助诊断；阳性结果不能单独确诊。"],
            ["多指标联合模型", "将血管生成因子与其他标志物或临床信息结合。", "可用于复杂场景和不良结局预测，但成本、解释和路径要求更高。"],
        ],
        [1.35, 3.0, 3.0],
    ),
    "[[TABLE3]]": (
        "表 3 核心证据矩阵",
        [
            ["文献或来源", "证据重点", "本文用途"],
            ["NICE PLGF-based testing guidance[1]", "PLGF 或 sFlt-1/PlGF 检测应与标准临床评估联合使用。", "确定临床应用边界。"],
            ["Zeisler 等 PROGNOSIS 研究[2]", "比值 ≤38 对 1 周内无子痫前期 NPV 为 99.3%。", "短期排除价值核心证据。"],
            ["Zhang 等 2025 Meta 分析[3]", "sFlt-1/PlGF AUC 0.92，高于单项 sFlt-1 或 PlGF。", "总体预测性能和局限。"],
            ["Zhao 等 2017 Meta 分析[4]", "双截断策略支持低风险、高风险和灰区分层。", "截断值解释和风险分层。"],
            ["Espinoza 等 2024 研究[5]", "MoM 11.5 预测 2 周内重症特征，AUC 0.91。", "重症短期风险分层。"],
            ["胡吉霞等 2022 研究[6]", "比值预测早发型子痫前期 AUC 0.873。", "国内中文临床证据。"],
            ["杨岚等 2024 研究[12]", "PLGF、SFLT-1、GLYFN 三项联合 AUC 0.986。", "多标志物联合证据。"],
            ["Lafuente-Ganuza 等 2020 研究[13]", "sFlt-1/PlGF 联合 NT-proBNP 可改善 rule-in/rule-out。", "局限性和未来方向。"],
        ],
        [2.05, 4.0, 1.95],
    ),
}


def run(command: list[str | os.PathLike[str]], cwd: Path = ROOT) -> None:
    completed = subprocess.run([str(part) for part in command], cwd=cwd, check=False)
    if completed.returncode != 0:
        raise RuntimeError(f"command failed with exit code {completed.returncode}: {command}")


def replace_block(text: str, start: str, end: str, placeholder: str) -> str:
    start_index = text.index(start)
    end_index = text.index(end, start_index)
    return text[:start_index] + placeholder + "\n\n" + end + text[end_index + len(end) :]


def build_conversion_markdown(build_dir: Path) -> Path:
    text = SOURCE_MD.read_text(encoding="utf-8")
    text = replace_block(text, "表 1 文献检索与筛选流程概要", "## 2 子痫前期与血管生成失衡机制", "[[TABLE1]]")
    text = replace_block(
        text,
        "表 2 sFlt-1、PlGF 与 sFlt-1/PlGF 比值比较",
        "## 4 sFlt-1/PlGF 比值在早期预测和辅助诊断中的证据",
        "[[TABLE2]]",
    )
    text = replace_block(text, "表 3 核心证据矩阵", "图 1 sFlt-1/PlGF 比值辅助临床决策路径（文字版）", "[[TABLE3]]")
    temp_md = build_dir / "COURSE_PAPER_DRAFT_FOR_DOCX.md"
    temp_md.write_text(text, encoding="utf-8")
    return temp_md


def convert_reference_doc(build_dir: Path) -> Path:
    run([SOFFICE, "--headless", "--convert-to", "docx", "--outdir", build_dir, TEMPLATE_DOC])
    reference = build_dir / "文献检索与论文写作结课论文模板-(1).docx"
    if not reference.exists():
        raise FileNotFoundError(reference)
    return reference


def set_cell_shading(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_borders(cell, color: str = "BFBFBF", size: str = "4") -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    borders = tc_pr.find(qn("w:tcBorders"))
    if borders is None:
        borders = OxmlElement("w:tcBorders")
        tc_pr.append(borders)
    for edge in ("top", "left", "bottom", "right"):
        tag = f"w:{edge}"
        element = borders.find(qn(tag))
        if element is None:
            element = OxmlElement(tag)
            borders.append(element)
        element.set(qn("w:val"), "single")
        element.set(qn("w:sz"), size)
        element.set(qn("w:color"), color)


def set_cell_margins(cell, top: int = 90, start: int = 110, bottom: int = 90, end: int = 110) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    margins = tc_pr.find(qn("w:tcMar"))
    if margins is None:
        margins = OxmlElement("w:tcMar")
        tc_pr.append(margins)
    for name, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = margins.find(qn(f"w:{name}"))
        if node is None:
            node = OxmlElement(f"w:{name}")
            margins.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def format_table(table, widths: list[float]) -> None:
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    try:
        table.style = "Table Grid"
    except KeyError:
        pass
    for row in table.rows:
        for index, width in enumerate(widths):
            if index < len(row.cells):
                row.cells[index].width = Inches(width)
    for row_index, row in enumerate(table.rows):
        for cell in row.cells:
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            set_cell_borders(cell)
            set_cell_margins(cell)
            if row_index == 0:
                set_cell_shading(cell, "EDEDED")
            for paragraph in cell.paragraphs:
                paragraph.paragraph_format.space_before = Pt(0)
                paragraph.paragraph_format.space_after = Pt(3)
                paragraph.paragraph_format.line_spacing = 1.1
                for run in paragraph.runs:
                    run.font.size = Pt(9)
                    if row_index == 0:
                        run.bold = True
                    run.font.name = "Times New Roman"
                    run._element.rPr.rFonts.set(qn("w:eastAsia"), "宋体")


def insert_table_after(paragraph, caption: str, data: list[list[str]], widths: list[float], doc: Document) -> None:
    paragraph.text = caption
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    paragraph.paragraph_format.space_before = Pt(6)
    paragraph.paragraph_format.space_after = Pt(6)
    for run in paragraph.runs:
        run.font.size = Pt(10.5)
        run.font.name = "Times New Roman"
        run._element.rPr.rFonts.set(qn("w:eastAsia"), "宋体")

    table = doc.add_table(rows=len(data), cols=len(data[0]))
    table._tbl.getparent().remove(table._tbl)
    paragraph._p.addnext(table._tbl)
    for row_index, row in enumerate(data):
        for column_index, value in enumerate(row):
            table.cell(row_index, column_index).text = value
    format_table(table, widths)


def insert_custom_tables(docx_path: Path) -> None:
    doc = Document(docx_path)
    found = 0
    for paragraph in list(doc.paragraphs):
        key = paragraph.text.strip()
        if key in TABLES:
            found += 1
            caption, data, widths = TABLES[key]
            insert_table_after(paragraph, caption, data, widths, doc)
    if found != len(TABLES):
        raise RuntimeError(f"expected {len(TABLES)} table placeholders, found {found}")
    doc.save(docx_path)


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="course-paper-docx-build-") as temp_dir:
        build_dir = Path(temp_dir)
        reference_docx = convert_reference_doc(build_dir)
        conversion_md = build_conversion_markdown(build_dir)
        run([PANDOC, conversion_md, "--reference-doc", reference_docx, "-o", OUTPUT_DOCX])
        insert_custom_tables(OUTPUT_DOCX)
    print(f"wrote {OUTPUT_DOCX}")


if __name__ == "__main__":
    main()
