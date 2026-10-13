import os
import subprocess

TARGET_DIR = r"c:\zzzz\solved pyq\BCA-504_Numerical_Methods"
PDF_COPY_DIR = r"c:\zzzz\pyq_solver_scripts\pdfs"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

os.makedirs(TARGET_DIR, exist_ok=True)
os.makedirs(PDF_COPY_DIR, exist_ok=True)

CSS_STYLES = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

@page {
    size: A4;
    margin: 14mm 12mm 14mm 12mm;
    @bottom-center {
        content: counter(page);
    }
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    font-size: 9.5pt;
    line-height: 1.5;
    color: #1e293b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}

.header-banner {
    border-bottom: 2.5px solid #047857;
    padding-bottom: 8px;
    margin-bottom: 12px;
}

.univ-name {
    font-size: 10pt;
    font-weight: 700;
    color: #047857;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    margin: 0 0 2px 0;
}

.paper-title {
    font-size: 15pt;
    font-weight: 800;
    color: #0f172a;
    margin: 0 0 2px 0;
}

.meta-info {
    font-size: 9pt;
    color: #475569;
    margin: 0;
}

.section-divider {
    background: #ecfdf5;
    border-left: 4.5px solid #059669;
    padding: 6px 12px;
    margin: 14px 0 10px 0;
    font-weight: 700;
    font-size: 10.5pt;
    color: #065f46;
}

.q-box {
    margin-bottom: 14px;
    padding-bottom: 10px;
    border-bottom: 1px dashed #cbd5e1;
    page-break-inside: avoid;
}

.q-title {
    font-weight: 700;
    color: #0f172a;
    font-size: 9.8pt;
    margin-bottom: 4px;
}

.q-title span.badge {
    background: #d1fae5;
    color: #065f46;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 8pt;
    font-weight: 700;
    margin-right: 6px;
}

.ans-body {
    color: #334155;
    font-size: 9.3pt;
    line-height: 1.52;
}

.math {
    font-family: 'Cambria Math', 'Times New Roman', serif;
    font-size: 10.2pt;
}

.math-block {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 3.5px solid #10b981;
    padding: 7px 12px;
    margin: 6px 0;
    border-radius: 4px;
    font-family: 'Cambria Math', 'Times New Roman', serif;
    font-size: 10pt;
    overflow-x: auto;
}

table.grid-table {
    border-collapse: collapse;
    width: 100%;
    margin: 7px 0;
    font-size: 8.8pt;
}

table.grid-table th, table.grid-table td {
    border: 1px solid #cbd5e1;
    padding: 5px 8px;
    text-align: center;
}

table.grid-table th {
    background-color: #f1f5f9;
    font-weight: 700;
    color: #1e293b;
}

table.grid-table tr:nth-child(even) {
    background-color: #f8fafc;
}

.highlight-box {
    background-color: #fefce8;
    border-left: 3px solid #eab308;
    padding: 5px 10px;
    margin: 5px 0;
    font-size: 9pt;
}
</style>
"""

def generate_pdf(year_str, out_filename, body_html):
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>BCA-504: Numerical Methods — {year_str} Solved Paper</title>
{CSS_STYLES}
</head>
<body>

<div class="header-banner">
    <p class="univ-name">Chaudhary Charan Singh University (CCSU) &bull; BCA V Semester</p>
    <h1 class="paper-title">BCA-504: Numerical Methods</h1>
    <p class="meta-info"><strong>Session:</strong> {year_str} Examination &nbsp;|&nbsp; <strong>Paper Code:</strong> 18024 &nbsp;|&nbsp; <strong>Actual University Solved Paper (All 13 Questions)</strong> &nbsp;|&nbsp; <strong>Time:</strong> 3 Hours &bull; <strong>Max Marks:</strong> 75</p>
</div>

{body_html}

</body>
</html>
"""
    temp_html = os.path.join(TARGET_DIR, f"temp_{out_filename}.html")
    pdf_out = os.path.join(TARGET_DIR, out_filename)
    pdf_copy = os.path.join(PDF_COPY_DIR, out_filename)
    
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(full_html)
    
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_out}",
        temp_html
    ]
    subprocess.run(cmd, check=True)
    
    # Copy to web pdfs dir
    if os.path.exists(pdf_out):
        import shutil
        shutil.copy2(pdf_out, pdf_copy)
        print(f"[OK] Generated {out_filename} ({os.path.getsize(pdf_out) / 1024:.1f} KB)")
        if os.path.exists(temp_html):
            os.remove(temp_html)

print("NM Builder helper ready.")
