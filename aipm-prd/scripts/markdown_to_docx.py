#!/usr/bin/env python3
"""Convert simple Markdown into a minimal Word .docx file.

This intentionally avoids third-party dependencies so the skill can produce a
Word document in restricted environments.
"""

from __future__ import annotations

import html
import re
import sys
import zipfile
from pathlib import Path


CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>
"""

ROOT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>
"""

STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:rPr><w:rFonts w:ascii="Aptos" w:eastAsia="Microsoft YaHei"/><w:sz w:val="22"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading1">
    <w:name w:val="heading 1"/><w:basedOn w:val="Normal"/>
    <w:pPr><w:spacing w:before="360" w:after="160"/></w:pPr>
    <w:rPr><w:b/><w:rFonts w:ascii="Aptos Display" w:eastAsia="Microsoft YaHei"/><w:sz w:val="36"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="heading 2"/><w:basedOn w:val="Normal"/>
    <w:pPr><w:spacing w:before="280" w:after="120"/></w:pPr>
    <w:rPr><w:b/><w:rFonts w:ascii="Aptos Display" w:eastAsia="Microsoft YaHei"/><w:sz w:val="30"/></w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading3">
    <w:name w:val="heading 3"/><w:basedOn w:val="Normal"/>
    <w:pPr><w:spacing w:before="220" w:after="100"/></w:pPr>
    <w:rPr><w:b/><w:rFonts w:ascii="Aptos" w:eastAsia="Microsoft YaHei"/><w:sz w:val="26"/></w:rPr>
  </w:style>
</w:styles>
"""


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def run(text: str, bold: bool = False, italic: bool = False, mono: bool = False) -> str:
    props = []
    if bold:
        props.append("<w:b/>")
    if italic:
        props.append("<w:i/>")
    if mono:
        props.append('<w:rFonts w:ascii="Cascadia Mono" w:eastAsia="Microsoft YaHei"/>')
    rpr = f"<w:rPr>{''.join(props)}</w:rPr>" if props else ""
    preserve = ' xml:space="preserve"' if text[:1].isspace() or text[-1:].isspace() else ""
    return f"<w:r>{rpr}<w:t{preserve}>{esc(text)}</w:t></w:r>"


def inline_runs(text: str) -> str:
    parts = re.split(r"(`[^`]+`|\*\*[^*]+\*\*|\*[^*]+\*)", text)
    out = []
    for part in parts:
        if not part:
            continue
        if part.startswith("`") and part.endswith("`"):
            out.append(run(part[1:-1], mono=True))
        elif part.startswith("**") and part.endswith("**"):
            out.append(run(part[2:-2], bold=True))
        elif part.startswith("*") and part.endswith("*"):
            out.append(run(part[1:-1], italic=True))
        else:
            out.append(run(part))
    return "".join(out)


def para(text: str = "", style: str | None = None, indent: int = 0) -> str:
    ppr = []
    if style:
        ppr.append(f'<w:pStyle w:val="{style}"/>')
    if indent:
        ppr.append(f'<w:ind w:left="{indent}"/>')
    props = f"<w:pPr>{''.join(ppr)}</w:pPr>" if ppr else ""
    return f"<w:p>{props}{inline_runs(text)}</w:p>"


def code_para(text: str) -> str:
    return f'<w:p><w:pPr><w:shd w:fill="F3F4F6"/></w:pPr>{run(text, mono=True)}</w:p>'


def table(rows: list[list[str]]) -> str:
    cell_width = max(1, int(9000 / max(len(row) for row in rows)))
    trs = []
    for row in rows:
        cells = []
        for cell in row:
            cells.append(
                "<w:tc>"
                f"<w:tcPr><w:tcW w:w=\"{cell_width}\" w:type=\"dxa\"/></w:tcPr>"
                f"{para(cell.strip())}"
                "</w:tc>"
            )
        trs.append(f"<w:tr>{''.join(cells)}</w:tr>")
    borders = (
        "<w:tblPr><w:tblBorders>"
        '<w:top w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/>'
        '<w:left w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/>'
        '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/>'
        '<w:right w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/>'
        '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/>'
        '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="D1D5DB"/>'
        "</w:tblBorders></w:tblPr>"
    )
    return f"<w:tbl>{borders}{''.join(trs)}</w:tbl>"


def is_separator(row: str) -> bool:
    cells = [cell.strip() for cell in row.strip().strip("|").split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell or "") for cell in cells)


def parse_table(lines: list[str], start: int) -> tuple[str | None, int]:
    if start + 1 >= len(lines) or "|" not in lines[start] or not is_separator(lines[start + 1]):
        return None, start
    rows = []
    i = start
    while i < len(lines) and "|" in lines[i]:
        if not is_separator(lines[i]):
            rows.append([cell.strip() for cell in lines[i].strip().strip("|").split("|")])
        i += 1
    return table(rows), i


def markdown_to_body(markdown: str) -> str:
    lines = markdown.splitlines()
    chunks = []
    i = 0
    in_code = False
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            in_code = not in_code
            i += 1
            continue
        if in_code:
            chunks.append(code_para(line))
            i += 1
            continue
        table_xml, next_i = parse_table(lines, i)
        if table_xml:
            chunks.append(table_xml)
            i = next_i
            continue
        stripped = line.strip()
        if not stripped:
            chunks.append(para(""))
        elif stripped.startswith("### "):
            chunks.append(para(stripped[4:], "Heading3"))
        elif stripped.startswith("## "):
            chunks.append(para(stripped[3:], "Heading2"))
        elif stripped.startswith("# "):
            chunks.append(para(stripped[2:], "Heading1"))
        elif re.match(r"^[-*]\s+", stripped):
            chunks.append(para("• " + re.sub(r"^[-*]\s+", "", stripped), indent=360))
        elif re.match(r"^\d+\.\s+", stripped):
            chunks.append(para(stripped, indent=360))
        else:
            chunks.append(para(stripped))
        i += 1
    return "".join(chunks)


def document_xml(body: str) -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {body}
    <w:sectPr>
      <w:pgSz w:w="11906" w:h="16838"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="708" w:footer="708" w:gutter="0"/>
    </w:sectPr>
  </w:body>
</w:document>
"""


def convert(input_path: Path, output_path: Path) -> None:
    markdown = input_path.read_text(encoding="utf-8")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", CONTENT_TYPES)
        docx.writestr("_rels/.rels", ROOT_RELS)
        docx.writestr("word/_rels/document.xml.rels", DOC_RELS)
        docx.writestr("word/styles.xml", STYLES)
        docx.writestr("word/document.xml", document_xml(markdown_to_body(markdown)))


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: markdown_to_docx.py input.md output.docx", file=sys.stderr)
        return 2
    convert(Path(sys.argv[1]), Path(sys.argv[2]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
