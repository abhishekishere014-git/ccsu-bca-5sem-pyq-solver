import os
import re
import subprocess
import shutil

TARGET_PDF = r"c:\zzzz\solved pyq\BCA5_Question_Bank.pdf"
COPY_PDF = r"c:\zzzz\pyq_solver_scripts\pdfs\BCA5_Question_Bank.pdf"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

files_to_load = [
    # DBMS (12 Years)
    ("DBMS", "BCA-501", "Introduction to DBMS", "2025", r"c:\zzzz\pyq_solver_scripts\dbms_2025_content.py", "YEAR_2025_HTML"),
    ("DBMS", "BCA-501", "Introduction to DBMS", "2024", r"c:\zzzz\pyq_solver_scripts\dbms_2024_content.py", "YEAR_2024_HTML"),
    ("DBMS", "BCA-501", "Introduction to DBMS", "2023", r"c:\zzzz\pyq_solver_scripts\dbms_2023_content.py", "YEAR_2023_HTML"),
    ("DBMS", "BCA-501", "Introduction to DBMS", "2021", r"c:\zzzz\pyq_solver_scripts\dbms_2021_2020_2019.py", "YEAR_2021_HTML"),
    ("DBMS", "BCA-501", "Introduction to DBMS", "2020", r"c:\zzzz\pyq_solver_scripts\dbms_2021_2020_2019.py", "YEAR_2020_HTML"),
    ("DBMS", "BCA-501", "Introduction to DBMS", "2019", r"c:\zzzz\pyq_solver_scripts\dbms_2021_2020_2019.py", "YEAR_2019_HTML"),
    ("DBMS", "BCA-501", "Introduction to DBMS", "2018", r"c:\zzzz\pyq_solver_scripts\dbms_2018_2017_2016.py", "YEAR_2018_HTML"),
    ("DBMS", "BCA-501", "Introduction to DBMS", "2017", r"c:\zzzz\pyq_solver_scripts\dbms_2018_2017_2016.py", "YEAR_2017_HTML"),
    ("DBMS", "BCA-501", "Introduction to DBMS", "2016", r"c:\zzzz\pyq_solver_scripts\dbms_2018_2017_2016.py", "YEAR_2016_HTML"),
    ("DBMS", "BCA-501", "Introduction to DBMS", "2015", r"c:\zzzz\pyq_solver_scripts\dbms_2015_2014_2013.py", "YEAR_2015_HTML"),
    ("DBMS", "BCA-501", "Introduction to DBMS", "2014", r"c:\zzzz\pyq_solver_scripts\dbms_2015_2014_2013.py", "YEAR_2014_HTML"),
    ("DBMS", "BCA-501", "Introduction to DBMS", "2013", r"c:\zzzz\pyq_solver_scripts\dbms_2015_2014_2013.py", "YEAR_2013_HTML"),

    # Java (9 Years)
    ("Java", "BCA-502", "Java Programming & Dynamic Webpage Design", "2025", r"c:\zzzz\pyq_solver_scripts\java_2025_2024_2023.py", "YEAR_2025_HTML"),
    ("Java", "BCA-502", "Java Programming & Dynamic Webpage Design", "2024", r"c:\zzzz\pyq_solver_scripts\java_2025_2024_2023.py", "YEAR_2024_HTML"),
    ("Java", "BCA-502", "Java Programming & Dynamic Webpage Design", "2023", r"c:\zzzz\pyq_solver_scripts\java_2025_2024_2023.py", "YEAR_2023_HTML"),
    ("Java", "BCA-502", "Java Programming & Dynamic Webpage Design", "2021", r"c:\zzzz\pyq_solver_scripts\java_2021_2020_2019.py", "YEAR_2021_HTML"),
    ("Java", "BCA-502", "Java Programming & Dynamic Webpage Design", "2020", r"c:\zzzz\pyq_solver_scripts\java_2021_2020_2019.py", "YEAR_2020_HTML"),
    ("Java", "BCA-502", "Java Programming & Dynamic Webpage Design", "2019", r"c:\zzzz\pyq_solver_scripts\java_2021_2020_2019.py", "YEAR_2019_HTML"),
    ("Java", "BCA-502", "Java Programming & Dynamic Webpage Design", "2018", r"c:\zzzz\pyq_solver_scripts\java_2018_2017_2016.py", "YEAR_2018_HTML"),
    ("Java", "BCA-502", "Java Programming & Dynamic Webpage Design", "2017", r"c:\zzzz\pyq_solver_scripts\java_2018_2017_2016.py", "YEAR_2017_HTML"),
    ("Java", "BCA-502", "Java Programming & Dynamic Webpage Design", "2016", r"c:\zzzz\pyq_solver_scripts\java_2018_2017_2016.py", "YEAR_2016_HTML"),

    # Networks (9 Years)
    ("Networks", "BCA-503", "Computer Networks", "2025", r"c:\zzzz\pyq_solver_scripts\networks_2025_2024_2023.py", "YEAR_2025_HTML"),
    ("Networks", "BCA-503", "Computer Networks", "2024", r"c:\zzzz\pyq_solver_scripts\networks_2025_2024_2023.py", "YEAR_2024_HTML"),
    ("Networks", "BCA-503", "Computer Networks", "2023", r"c:\zzzz\pyq_solver_scripts\networks_2025_2024_2023.py", "YEAR_2023_HTML"),
    ("Networks", "BCA-503", "Computer Networks", "2021", r"c:\zzzz\pyq_solver_scripts\networks_2021_2020_2019.py", "YEAR_2021_HTML"),
    ("Networks", "BCA-503", "Computer Networks", "2020", r"c:\zzzz\pyq_solver_scripts\networks_2021_2020_2019.py", "YEAR_2020_HTML"),
    ("Networks", "BCA-503", "Computer Networks", "2019", r"c:\zzzz\pyq_solver_scripts\networks_2021_2020_2019.py", "YEAR_2019_HTML"),
    ("Networks", "BCA-503", "Computer Networks", "2018", r"c:\zzzz\pyq_solver_scripts\networks_2018_2017_2016.py", "YEAR_2018_HTML"),
    ("Networks", "BCA-503", "Computer Networks", "2017", r"c:\zzzz\pyq_solver_scripts\networks_2018_2017_2016.py", "YEAR_2017_HTML"),
    ("Networks", "BCA-503", "Computer Networks", "2016", r"c:\zzzz\pyq_solver_scripts\networks_2018_2017_2016.py", "YEAR_2016_HTML"),

    # Numerical Methods (7 Years)
    ("NM", "BCA-504", "Numerical Methods", "2024", r"c:\zzzz\pyq_solver_scripts\nm_2024_content.py", "YEAR_2024_HTML"),
    ("NM", "BCA-504", "Numerical Methods", "2023", r"c:\zzzz\pyq_solver_scripts\nm_2023_content.py", "YEAR_2023_HTML"),
    ("NM", "BCA-504", "Numerical Methods", "2022", r"c:\zzzz\pyq_solver_scripts\nm_2022_content.py", "YEAR_2022_HTML"),
    ("NM", "BCA-504", "Numerical Methods", "2021", r"c:\zzzz\pyq_solver_scripts\nm_2021_content.py", "YEAR_2021_HTML"),
    ("NM", "BCA-504", "Numerical Methods", "2020", r"c:\zzzz\pyq_solver_scripts\nm_2020_content.py", "YEAR_2020_HTML"),
    ("NM", "BCA-504", "Numerical Methods", "2019", r"c:\zzzz\pyq_solver_scripts\nm_2019_content.py", "YEAR_2019_HTML"),
    ("NM", "BCA-504", "Numerical Methods", "2018", r"c:\zzzz\pyq_solver_scripts\build_real_nm_2018.py", "YEAR_2018_HTML"),
]

def extract_features(text):
    t = text.lower()
    t = re.sub(r'<[^>]+>', '', t)
    t = re.sub(r'[^a-z0-9\s]', ' ', t)
    words = t.split()
    stop = {'what', 'is', 'a', 'an', 'the', 'of', 'in', 'and', 'or', 'to', 'for', 'with', 'explain', 'describe', 'define', 'state', 'discuss', 'write', 'short', 'notes', 'on', 'suitable', 'example', 'examples', 'neat', 'diagram', 'diagrams', 'between', 'differentiate', 'distinguish', 'compare', 'briefly', 'detail', 'types', 'various', 'its', 'their', 'how', 'do', 'you', 'does', 'why', 'can', 'be', 'by', 'as', 'at', 'from', 'using', 'calculate', 'find', 'solve', 'evaluate', 'compute', 'mention', 'give'}
    return set(w for w in words if w not in stop and len(w) > 2)

KEY_ANCHORS = [
    'normalization', 'relational algebra', 'acid', 'concurrency', '2pl', 'locking',
    'b+ tree', 'b-tree', 'indexing', 'three-schema', 'three level', 'schema',
    'database administrator', 'dba', 'file processing', 'primary key', 'candidate key',
    'foreign key', 'ddl', 'dml', 'er diagram', 'entity relationship',
    'applet', 'servlet', 'jsp', 'jdbc', 'multithreading', 'thread', 'exception',
    'inheritance', 'interface', 'abstract class', 'jvm', 'bytecode', 'garbage collection',
    'super keyword', 'this keyword', 'osi', 'tcp/ip', 'tcp', 'udp', 'sliding window',
    'routing', 'distance vector', 'dijkstra', 'link state', 'congestion', 'leaky bucket',
    'token bucket', 'switching', 'circuit switching', 'packet switching', 'topology',
    'transmission media', 'twisted pair', 'coaxial', 'optical fiber', 'crc', 'cyclic redundancy',
    'bisection', 'newton raphson', 'regula falsi', 'false position', 'gauss elimination',
    'gauss seidel', 'jacobi', 'lagrange', 'newton forward', 'newton backward', 'divided difference',
    'trapezoidal', 'simpson', 'euler', 'runge kutta', 'rk4', 'picard', 'finite difference'
]

def load_and_cluster():
    subject_map = {}
    
    for sub, code, title, yr, path, varname in files_to_load:
        if sub not in subject_map:
            subject_map[sub] = {
                "sub": sub,
                "code": code,
                "title": title,
                "clusters": []
            }
        
        with open(path, "r", encoding="utf-8") as f:
            file_code = f.read()
        pattern = rf'{varname}\s*=\s*r?["\']{{3}}(.*?)["\']{{3}}'
        m = re.search(pattern, file_code, re.DOTALL)
        if not m:
            continue
        html = m.group(1)
        
        parts = re.split(r'<div class="q-box">', html)[1:]
        for p in parts:
            tm = re.search(r'<div class="q-title">(.*?)</div>', p, re.DOTALL)
            am = re.search(r'<div class="ans-body">(.*?)(?:</div>\s*</div>|\Z)', p, re.DOTALL)
            if not tm:
                continue
            raw_title = tm.group(1).strip()
            marks_match = re.search(r'\(([0-9.]+M)\)', raw_title)
            marks = marks_match.group(1) if marks_match else "3M"
            
            clean_text = re.sub(r'<span class="badge">.*?</span>', '', raw_title)
            clean_text = re.sub(r'^Q\d+\s*[\.:\-]?\s*', '', clean_text.strip()).strip()
            ans_html = am.group(1).strip() if am else ""
            
            feat = extract_features(clean_text)
            
            # Find matching cluster
            matched_c = None
            best_sim = 0.0
            
            for c in subject_map[sub]["clusters"]:
                c_feat = c["features"]
                inter = feat.intersection(c_feat)
                if not inter:
                    continue
                overlap = len(inter) / min(len(feat), len(c_feat)) if min(len(feat), len(c_feat)) > 0 else 0
                union = feat.union(c_feat)
                jaccard = len(inter) / len(union) if len(union) > 0 else 0
                sim = 0.6 * overlap + 0.4 * jaccard
                
                t_low = clean_text.lower()
                c_low = c["canonical_title"].lower()
                for ka in KEY_ANCHORS:
                    if ka in t_low and ka in c_low and overlap >= 0.38:
                        sim = max(sim, 0.78)
                        break
                        
                if sim > 0.52 and sim > best_sim:
                    best_sim = sim
                    matched_c = c
                    
            if matched_c:
                matched_c["years"].add(yr)
                matched_c["marks"].add(marks)
                matched_c["features"].update(feat)
                if len(ans_html) > len(matched_c["best_answer"]):
                    matched_c["best_answer"] = ans_html
                    matched_c["canonical_title"] = clean_text
            else:
                subject_map[sub]["clusters"].append({
                    "canonical_title": clean_text,
                    "marks": {marks},
                    "years": {yr},
                    "features": feat,
                    "best_answer": ans_html
                })

    # Finalize clusters and apply exam-style enrichments
    try:
        from build_full_web_dedup_data import ALL_DBMS, ALL_JAVA, ALL_NETWORKS, ALL_NM, clean_latex
        enrich_map = {"DBMS": ALL_DBMS, "Java": ALL_JAVA, "Networks": ALL_NETWORKS, "NM": ALL_NM}
    except Exception as e:
        enrich_map = {}
        clean_latex = lambda x: x

    for sub, sdata in subject_map.items():
        enrich_dict = enrich_map.get(sub, {})
        for c in sdata["clusters"]:
            c["year_list"] = sorted(list(c["years"]), key=lambda y: int(re.sub(r'\D', '', y)) if re.sub(r'\D', '', y) else 0, reverse=True)
            c["count"] = len(c["year_list"])
            # normalize marks: highest mark representation
            marks_nums = [float(re.sub(r'[^\d.]', '', m)) for m in c["marks"] if re.sub(r'[^\d.]', '', m)]
            c["max_marks"] = max(marks_nums) if marks_nums else 3.0
            c["marks_display"] = " / ".join(sorted(list(c["marks"])))

            # Apply enrichment if available
            t_low = c["canonical_title"].lower()
            for ek, ev in enrich_dict.items():
                if ek.lower() in t_low and len(ev) > len(c["best_answer"]):
                    c["best_answer"] = ev
                    break

            # Clean LaTeX
            c["canonical_title"] = clean_latex(c["canonical_title"])
            c["best_answer"] = clean_latex(c["best_answer"])
            
        # Sort subject clusters:
        sdata["clusters"].sort(key=lambda x: (x["count"], x["max_marks"]), reverse=True)
        
    return subject_map

def generate_pdf():
    subject_map = load_and_cluster()
    
    # Calculate global stats
    total_raw = sum(len(f) for f in files_to_load) # 37
    total_unique = sum(len(sdata["clusters"]) for sdata in subject_map.values())
    
    # Collect all golden questions across all subjects (repeated >= 3 times)
    golden_questions = []
    for sub, sdata in subject_map.items():
        for c in sdata["clusters"]:
            if c["count"] >= 3:
                golden_questions.append({
                    "sub_code": sdata["code"],
                    "sub_name": sub,
                    "count": c["count"],
                    "years": c["year_list"],
                    "marks": c["marks_display"],
                    "title": c["canonical_title"]
                })
    golden_questions.sort(key=lambda x: (x["count"], x["sub_code"]), reverse=True)
    
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Playfair+Display:wght@700;800&display=swap');

    @page {
        size: A4;
        margin: 14mm 12mm 14mm 12mm;
        @bottom-right {
            content: "Page " counter(page);
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 8pt;
            color: #64748b;
        }
        @bottom-left {
            content: "CCSU BCA V Sem • Master Deduplicated Question Bank (2013-2025)";
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-size: 8pt;
            color: #64748b;
        }
    }

    body {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-size: 9.2pt;
        line-height: 1.5;
        color: #1e293b;
        background-color: #ffffff;
        margin: 0;
        padding: 0;
    }

    .cover-page {
        page-break-after: always;
        text-align: center;
        padding-top: 35px;
        padding-bottom: 25px;
    }

    .univ-tag {
        font-size: 11pt;
        font-weight: 800;
        letter-spacing: 1.5px;
        color: #1e40af;
        text-transform: uppercase;
        margin-bottom: 8px;
    }

    .main-title {
        font-family: 'Playfair Display', Georgia, serif;
        font-size: 25pt;
        font-weight: 800;
        color: #0f172a;
        line-height: 1.2;
        margin: 0 0 10px 0;
    }

    .subtitle {
        font-size: 11.5pt;
        color: #475569;
        font-weight: 600;
        margin-bottom: 25px;
    }

    .badge-bar {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-bottom: 25px;
    }

    .pill-stat {
        background-color: #eff6ff;
        border: 1px solid #bfdbfe;
        color: #1d4ed8;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 8.5pt;
    }

    .summary-card {
        background: #f8fafc;
        border: 1.5px solid #e2e8f0;
        border-radius: 10px;
        padding: 18px 24px;
        margin: 20px auto 30px auto;
        text-align: left;
        max-width: 600px;
    }

    .summary-card h3 {
        margin-top: 0;
        font-size: 11pt;
        color: #0f172a;
        border-bottom: 1px solid #cbd5e1;
        padding-bottom: 6px;
    }

    .summary-card ul {
        margin: 8px 0;
        padding-left: 20px;
    }

    .summary-card li {
        margin-bottom: 6px;
        font-size: 9pt;
        color: #334155;
    }

    .page-break {
        page-break-after: always;
    }

    .section-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
        color: #ffffff;
        padding: 12px 18px;
        border-radius: 8px;
        margin-top: 15px;
        margin-bottom: 16px;
        page-break-after: avoid;
    }

    .section-header h2 {
        margin: 0;
        font-size: 13pt;
        font-weight: 800;
        letter-spacing: 0.5px;
    }

    .section-header p {
        margin: 4px 0 0 0;
        font-size: 8.5pt;
        color: #93c5fd;
    }

    .golden-table {
        width: 100%;
        border-collapse: collapse;
        font-size: 8.5pt;
        margin: 12px 0 20px 0;
    }

    .golden-table th {
        background: #0f172a;
        color: #ffffff;
        padding: 7px 9px;
        text-align: left;
        font-weight: 700;
        border: 1px solid #334155;
    }

    .golden-table td {
        padding: 6px 9px;
        border: 1px solid #cbd5e1;
        vertical-align: top;
    }

    .golden-table tr:nth-child(even) td {
        background: #f8fafc;
    }

    .master-q-box {
        background: #ffffff;
        border: 1.2px solid #cbd5e1;
        border-left: 4.5px solid #2563eb;
        border-radius: 6px;
        padding: 10px 14px;
        margin-bottom: 14px;
        page-break-inside: avoid;
    }

    .master-q-box.high-freq {
        border-left-color: #dc2626;
        background: #fffafa;
    }

    .stamp-row {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 6px;
        margin-bottom: 6px;
        padding-bottom: 6px;
        border-bottom: 1px dashed #e2e8f0;
    }

    .badge-sub {
        background: #e2e8f0;
        color: #334155;
        font-size: 7.5pt;
        font-weight: 700;
        padding: 2px 7px;
        border-radius: 4px;
        text-transform: uppercase;
    }

    .badge-marks {
        background: #f1f5f9;
        color: #0f172a;
        font-size: 7.5pt;
        font-weight: 800;
        padding: 2px 7px;
        border-radius: 4px;
        border: 1px solid #cbd5e1;
    }

    .badge-freq {
        font-size: 7.5pt;
        font-weight: 800;
        padding: 2px 7px;
        border-radius: 4px;
    }

    .badge-freq.fire {
        background: #fee2e2;
        color: #b91c1c;
        border: 1px solid #fca5a5;
    }

    .badge-freq.star {
        background: #fef3c7;
        color: #b45309;
        border: 1px solid #fcd34d;
    }

    .badge-freq.normal {
        background: #ecfdf5;
        color: #047857;
        border: 1px solid #a7f3d0;
    }

    .badge-years {
        background: #1e40af;
        color: #ffffff;
        font-size: 7.5pt;
        font-weight: 700;
        padding: 2px 8px;
        border-radius: 4px;
        letter-spacing: 0.3px;
    }

    .q-text {
        font-size: 9.8pt;
        font-weight: 700;
        color: #0f172a;
        margin: 5px 0 8px 0;
        line-height: 1.45;
    }

    .ans-container {
        font-size: 8.8pt;
        color: #334155;
        line-height: 1.5;
        margin-top: 6px;
    }

    .ans-container strong {
        color: #0f172a;
    }

    .ans-container table, .grid-table {
        width: 100%;
        border-collapse: collapse;
        margin: 7px 0;
        font-size: 8.2pt;
    }

    .ans-container th, .grid-table th {
        background: #f1f5f9;
        color: #0f172a;
        font-weight: 700;
        padding: 4px 6px;
        border: 1px solid #cbd5e1;
    }

    .ans-container td, .grid-table td {
        padding: 4px 6px;
        border: 1px solid #e2e8f0;
        vertical-align: top;
    }

    .ans-container pre, .code-box, .diagram-box {
        background-color: #0f172a;
        color: #f8fafc;
        padding: 7px 10px;
        border-radius: 5px;
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 7.8pt;
        line-height: 1.35;
        margin: 6px 0;
        overflow-x: auto;
        white-space: pre-wrap;
    }

    .ans-container code {
        font-family: 'JetBrains Mono', Consolas, monospace;
        font-size: 8pt;
        background-color: #f1f5f9;
        color: #0f172a;
        padding: 1px 3px;
        border-radius: 3px;
    }

    .info-box, .step-box {
        background: #f0f9ff;
        border-left: 3px solid #0284c7;
        padding: 6px 10px;
        margin: 6px 0;
        border-radius: 0 4px 4px 0;
        font-size: 8.5pt;
    }

    .ans-container ul, .ans-container ol {
        margin: 4px 0 6px 0;
        padding-left: 18px;
    }

    .ans-container li {
        margin-bottom: 3px;
    }

    .cat-divider {
        font-size: 10.5pt;
        font-weight: 800;
        color: #1e3a8a;
        border-bottom: 2px solid #bfdbfe;
        padding-bottom: 3px;
        margin: 18px 0 10px 0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        page-break-after: avoid;
    }
    </style>
    """
    
    html_out = [f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>CCSU BCA V Semester Master Deduplicated Question Bank</title>
    {css}
</head>
<body>
"""]

    # Cover Page
    html_out.append(f"""
    <div class="cover-page">
        <div class="univ-tag">CHAUDHARY CHARAN SINGH UNIVERSITY (CCSU), MEERUT</div>
        <h1 class="main-title">BCA 5th SEMESTER<br>MASTER DEDUPLICATED QUESTION BANK</h1>
        <div class="subtitle">Complete University Past Year Exam Questions (2013 &ndash; 2025) &bull; Deduplicated &bull; Year Stamped</div>
        
        <div class="badge-bar">
            <span class="pill-stat">📚 4 Core Subjects</span>
            <span class="pill-stat">📑 37 Past Exam Papers Analyzed</span>
            <span class="pill-stat">✨ {total_unique} Unique Master Questions</span>
            <span class="pill-stat">🎯 100% Fully Solved</span>
        </div>

        <div class="summary-card">
            <h3>📖 About This Master Publication</h3>
            <ul>
                <li><strong>Zero Clutter / Deduplicated:</strong> Identical questions repeated over 12 years are consolidated into single high-yield master entries.</li>
                <li><strong>Exam Year Stamps:</strong> Every single question shows the exact university exam sessions in which it appeared (e.g. <code>CCSU 2025, 2024, 2021, 2018</code>).</li>
                <li><strong>Probability Badges:</strong> Most frequent questions are highlighted with <code>🔥 Highly Repeated (3x to 10x)</code> tags for guaranteed scoring.</li>
                <li><strong>Comprehensive Model Answers:</strong> Complete, verified, step-by-step answers including relational schemas, Java code, network layer diagrams, and numerical calculations.</li>
                <li><strong>Covers All 4 Subjects:</strong> BCA-501 (DBMS), BCA-502 (Java), BCA-503 (Networks), and BCA-504 (Numerical Methods).</li>
            </ul>
        </div>
        
        <div style="font-size: 8.5pt; color: #64748b; margin-top: 30px;">
            Published for CCSU BCA 5th Semester Students &bull; Examination Preparation &bull; 2026 Edition
        </div>
    </div>
    """)
    
    # Golden 40 Table
    html_out.append(f"""
    <div class="page-break"></div>
    <div class="section-header">
        <h2>🔥 MASTER HIGH-YIELD "GOLDEN QUESTIONS" MATRIX</h2>
        <p>Top {len(golden_questions)} Most Repeated Questions Across All 4 Subjects &bull; Must-Study for 90%+ Exam Guarantee</p>
    </div>
    
    <table class="golden-table">
        <thead>
            <tr>
                <th style="width: 10%;">Subject</th>
                <th style="width: 12%;">Frequency</th>
                <th style="width: 28%;">Exam Years Appeared</th>
                <th style="width: 10%;">Marks</th>
                <th style="width: 40%;">Core Exam Question Statement</th>
            </tr>
        </thead>
        <tbody>
    """)
    
    for g in golden_questions:
        freq_badge = f"🔥 {g['count']} Times" if g['count'] >= 5 else f"★ {g['count']} Times"
        yrs_str = ", ".join(g['years'])
        clean_title = re.sub(r'<[^>]+>', '', g['title'])
        html_out.append(f"""
            <tr>
                <td><strong>{g['sub_code']}</strong><br><small>{g['sub_name']}</small></td>
                <td><strong style="color: #b91c1c;">{freq_badge}</strong></td>
                <td><span style="font-size: 7.8pt; font-weight: 600; color: #1e40af;">{yrs_str}</span></td>
                <td><strong>{g['marks']}</strong></td>
                <td>{clean_title}</td>
            </tr>
        """)
    html_out.append("""
        </tbody>
    </table>
    """)
    
    # Now output each subject
    for sub, sdata in subject_map.items():
        html_out.append(f"""
        <div class="page-break"></div>
        <div class="section-header">
            <h2>SUBJECT: {sdata['code']} &bull; {sdata['title'].upper()}</h2>
            <p>Total Deduplicated Unique Questions: {len(sdata['clusters'])} &bull; All Sessions Fully Consolidated</p>
        </div>
        """)
        
        # Categorize clusters into Long, Medium, Short
        long_qs = [c for c in sdata["clusters"] if c["max_marks"] >= 10.0]
        med_qs = [c for c in sdata["clusters"] if 4.0 <= c["max_marks"] < 10.0]
        short_qs = [c for c in sdata["clusters"] if c["max_marks"] < 4.0]
        
        categories = [
            ("Section C &bull; Long Answer Questions (15 Marks / Detailed Solutions)", long_qs),
            ("Section B &bull; Medium Answer Questions (7.5 Marks / Core Concepts)", med_qs),
            ("Section A &bull; Short Answer Questions (3 Marks / High-Yield Definitions)", short_qs),
        ]
        
        for cat_name, q_group in categories:
            if not q_group:
                continue
            html_out.append(f'<div class="cat-divider">{cat_name} ({len(q_group)} Unique Questions)</div>')
            
            for q in q_group:
                is_high = q["count"] >= 4
                is_star = 2 <= q["count"] < 4
                
                if is_high:
                    freq_class = "fire"
                    freq_text = f"🔥 Highly Repeated ({q['count']}x)"
                    box_class = "master-q-box high-freq"
                elif is_star:
                    freq_class = "star"
                    freq_text = f"★ Repeated ({q['count']}x)"
                    box_class = "master-q-box"
                else:
                    freq_class = "normal"
                    freq_text = "CCSU Exam Question"
                    box_class = "master-q-box"
                    
                years_text = ", ".join(q["year_list"])
                
                # Sanitize title
                clean_title = q["canonical_title"]
                
                html_out.append(f"""
                <div class="{box_class}">
                    <div class="stamp-row">
                        <span class="badge-sub">{sdata['code']}</span>
                        <span class="badge-marks">Marks: {q['marks_display']}</span>
                        <span class="badge-freq {freq_class}">{freq_text}</span>
                        <span class="badge-years">CCSU Exam Years: {years_text}</span>
                    </div>
                    <div class="q-text">{clean_title}</div>
                    <div class="ans-container">
                        {q['best_answer']}
                    </div>
                </div>
                """)

    html_out.append("""
    </body>
    </html>
    """)
    
    full_html_str = "\n".join(html_out)
    
    temp_html = r"c:\zzzz\temp_dedup_master.html"
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(full_html_str)
        
    print(f"[1/3] Generated HTML (Size: {len(full_html_str) / 1024:.1f} KB)")
    
    print("[2/3] Invoking Chrome Headless to generate Master PDF...")
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={TARGET_PDF}",
        temp_html
    ]
    subprocess.run(cmd, check=True)
    
    if os.path.exists(temp_html):
        os.remove(temp_html)
        
    shutil.copy2(TARGET_PDF, COPY_PDF)
    
    size_mb = os.path.getsize(TARGET_PDF) / (1024 * 1024)
    print(f"[3/3] Master Deduplicated PDF successfully created: {TARGET_PDF} ({size_mb:.2f} MB)")
    print(f"Copied to: {COPY_PDF}")

if __name__ == "__main__":
    generate_pdf()
