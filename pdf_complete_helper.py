import sys
import os
import subprocess
import markdown

target_dir = r"c:\zzzz\solved pyq"
os.makedirs(target_dir, exist_ok=True)
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

css_styles = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=JetBrains+Mono:wght@400;600&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&display=swap');

@page {
    size: A4;
    margin: 18mm 14mm 18mm 14mm;
    @bottom-center {
        content: counter(page);
    }
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.55;
    color: #1e293b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}

.header-banner {
    border-bottom: 2.5px solid #1e40af;
    padding-bottom: 10px;
    margin-bottom: 16px;
}

.univ-name {
    font-size: 10.5pt;
    font-weight: 700;
    color: #1e40af;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin: 0 0 3px 0;
}

.paper-title {
    font-size: 16pt;
    font-weight: 800;
    color: #0f172a;
    margin: 0 0 3px 0;
}

.meta-info {
    font-size: 9.5pt;
    color: #475569;
    font-weight: 500;
    margin: 0;
}

h2 {
    font-size: 12pt;
    font-weight: 700;
    color: #0369a1;
    border-bottom: 1.5px solid #e2e8f0;
    padding-bottom: 4px;
    margin-top: 18px;
    margin-bottom: 10px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

h3 {
    font-size: 10.5pt;
    font-weight: 700;
    color: #0f172a;
    margin-top: 14px;
    margin-bottom: 5px;
}

p, li {
    font-size: 9.5pt;
    color: #334155;
    margin-top: 3px;
    margin-bottom: 6px;
}

strong {
    color: #0f172a;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0;
    font-size: 9pt;
    page-break-inside: avoid;
}

th {
    background-color: #f1f5f9;
    color: #0f172a;
    font-weight: 700;
    text-align: left;
    padding: 6px 8px;
    border: 1px solid #cbd5e1;
}

td {
    padding: 6px 8px;
    border: 1px solid #e2e8f0;
    vertical-align: top;
}

tr:nth-child(even) td {
    background-color: #f8fafc;
}

pre {
    background-color: #0f172a;
    color: #f8fafc;
    padding: 10px 12px;
    border-radius: 6px;
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 8pt;
    line-height: 1.4;
    overflow-x: auto;
    page-break-inside: avoid;
    margin: 8px 0;
}

code {
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 8.5pt;
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 2px 4px;
    border-radius: 4px;
}

pre code {
    background-color: transparent;
    color: #f8fafc;
    padding: 0;
}

hr {
    border: 0;
    border-top: 1px solid #cbd5e1;
    margin: 14px 0;
}
</style>
"""

def create_complete_pdf(filename, title, subtitle, markdown_content):
    html_body = markdown.markdown(markdown_content, extensions=['tables', 'fenced_code', 'nl2br'])
    full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{title} — {subtitle}</title>
    {css_styles}
</head>
<body>
    <div class="header-banner">
        <p class="univ-name">Chaudhary Charan Singh University (CCSU) • BCA V Semester</p>
        <h1 class="paper-title">{title}</h1>
        <p class="meta-info"><strong>Session:</strong> {subtitle} &nbsp;|&nbsp; <strong>Complete 100% Solved Paper (All 13 Questions)</strong></p>
    </div>
    {html_body}
</body>
</html>"""
    temp_html = os.path.join(target_dir, f"temp_{filename}.html")
    pdf_out = os.path.join(target_dir, filename)
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(full_html)
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_out}",
        temp_html
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(temp_html):
        os.remove(temp_html)
    size_kb = os.path.getsize(pdf_out) / 1024
    print(f"[OK] Generated {filename} ({size_kb:.1f} KB)")
