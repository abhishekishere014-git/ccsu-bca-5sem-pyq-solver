import os
import re
import json
import generate_dedup_master_qbank as g
from enrich_java import JAVA_ENRICHMENTS
from enrich_networks import NETWORKS_ENRICHMENTS
from enrich_dbms import DBMS_ENRICHMENTS
from enrich_nm import NM_ENRICHMENTS
from enrich_all_remaining import ALL_ADDITIONAL_ENRICHMENTS

# Merge and update all enrichment dictionaries
ALL_JAVA = {**JAVA_ENRICHMENTS}
ALL_JAVA['what is a final variable'] = ALL_JAVA.pop('final variable in java', '')
ALL_JAVA['form controls and write code for an admission form'] = ALL_JAVA.pop('html form controls and admission form', '')
ALL_JAVA['constructor overloading'] = ALL_JAVA.pop('constructor and constructor overloading', '')

ALL_NETWORKS = {**NETWORKS_ENRICHMENTS}
ALL_NETWORKS['fiber distributed data interface (fddi)'] = ALL_NETWORKS.pop('fddi operation', '')
ALL_NETWORKS['compare tcp and udp'] = ALL_NETWORKS.pop('tcp vs udp at the transport layer', '')

ALL_DBMS = {**DBMS_ENRICHMENTS}
ALL_DBMS['bcnf (boyce-codd normal form)'] = ALL_DBMS.pop('boyce-codd normal form (bcnf)', '')
ALL_DBMS['grant and revoke'] = ALL_DBMS.pop('database security and authorization: grant and revoke', '')
ALL_DBMS['query optimization'] = ALL_DBMS.pop('query optimization and heuristic optimization', '')

ALL_NM = {**NM_ENRICHMENTS}

# Distribute additional enrichments into subjects
for k, v in ALL_ADDITIONAL_ENRICHMENTS.items():
    if any(term in k for term in ['table formatting', 'responsive institutional', 'define constructor in java']):
        ALL_JAVA[k] = v
    elif any(term in k for term in ['computer network', 'hdlc', 'piggybacking', 'smtp', 'bridges', 'e-mail and its core', 'bandwidth and throughput', 'four channels', 'point-to-point', 'lan, man, and wan', 'collision domain', 'repeaters', 'transport layer', 'shannon', 'bit rate vs baud rate']):
        ALL_NETWORKS[k] = v
    elif any(term in k for term in ['play(', 'dept(', 'deadlock', 'association and aggregation', 'rdbms', 'weak entity', 'natural join', 'commit and rollback', 'hashing', 'data redundancy', 'relational data model']):
        ALL_DBMS[k] = v

def clean_latex(html_text):
    if not html_text:
        return ""
    t = html_text

    # 1. Spacing tokens
    t = re.sub(r'\\qquad', '&nbsp;&nbsp;&nbsp;&nbsp;', t)
    t = re.sub(r'\\quad', '&nbsp;&nbsp;', t)
    t = re.sub(r'\\[,;!]', ' ', t)

    # 2. Left / Right brackets
    t = re.sub(r'\\left\[', '[', t)
    t = re.sub(r'\\right\]', ']', t)
    t = re.sub(r'\\left\(', '(', t)
    t = re.sub(r'\\right\)', ')', t)
    t = re.sub(r'\\left\\\{', '{', t)
    t = re.sub(r'\\right\\\}', '}', t)
    t = re.sub(r'\\left\|', '|', t)
    t = re.sub(r'\\right\|', '|', t)
    t = re.sub(r'\\left\.', '', t)
    t = re.sub(r'\\right\.', '', t)

    # 3. Fractions: iterative resolution
    while r'\frac' in t:
        new_t = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'(\1)/(\2)', t)
        if new_t == t:
            new_t = re.sub(r'\\frac\s*([0-9a-zA-Z])\s*([0-9a-zA-Z])', r'(\1)/(\2)', t)
            if new_t == t:
                new_t = re.sub(r'\\frac', '', t)
        t = new_t

    # 4. Functions & Operators
    t = re.sub(r'\\tan\^\{-1\}', 'tan<sup>-1</sup>', t)
    t = re.sub(r'\\sin\^\{-1\}', 'sin<sup>-1</sup>', t)
    t = re.sub(r'\\cos\^\{-1\}', 'cos<sup>-1</sup>', t)
    t = re.sub(r'\\tan', 'tan', t)
    t = re.sub(r'\\sin', 'sin', t)
    t = re.sub(r'\\cos', 'cos', t)
    t = re.sub(r'\\log', 'log', t)
    t = re.sub(r'\\ln', 'ln', t)
    t = re.sub(r'\\exp', 'exp', t)

    # 5. Greek, Set, & Relational symbols
    t = re.sub(r'\\Delta', '&Delta;', t)
    t = re.sub(r'\\nabla', '&nabla;', t)
    t = re.sub(r'\\approx', '&approx;', t)
    t = re.sub(r'\\neq', '&ne;', t)
    t = re.sub(r'\\le\b', '&le;', t)
    t = re.sub(r'\\ge\b', '&ge;', t)
    t = re.sub(r'\\times', '&times;', t)
    t = re.sub(r'\\cdot', '&bull;', t)
    t = re.sub(r'\\dots', '&hellip;', t)
    t = re.sub(r'\\cdots', '&hellip;', t)
    t = re.sub(r'\\implies', '&rArr;', t)
    t = re.sub(r'\\leftrightarrow', '&harr;', t)
    t = re.sub(r'\\to\b', '&rarr;', t)
    t = re.sub(r'\\lambda', '&lambda;', t)
    t = re.sub(r'\\xi', '&xi;', t)
    t = re.sub(r'\\prod', '&prod;', t)
    t = re.sub(r'\\sum', '&Sigma;', t)
    t = re.sub(r'\\int', '&int;', t)
    t = re.sub(r'\\sqrt\{([^}]+)\}', r'&radic;(\1)', t)
    t = re.sub(r'\\sigma', '&sigma;', t)
    t = re.sub(r'\\pi', '&pi;', t)
    t = re.sub(r'\\cup', '&cup;', t)
    t = re.sub(r'\\cap', '&cap;', t)
    t = re.sub(r'\\bowtie', '&bowtie;', t)
    t = re.sub(r'\\rho', '&rho;', t)
    t = re.sub(r'\\in\b', '&isin;', t)
    t = re.sub(r'\\infty', '&infin;', t)
    t = re.sub(r'\\mathbf\{([^}]+)\}', r'<b>\1</b>', t)
    t = re.sub(r'\\text\{([^}]+)\}', r'\1', t)

    # 6. Matrix & Array clean conversion
    t = re.sub(r'\\begin\{(?:matrix|array|pmatrix|bmatrix)\}(.*?)\\end\{(?:matrix|array|pmatrix|bmatrix)\}', 
               lambda m: '<table class="grid-table">' + ''.join('<tr>' + ''.join(f'<td>{c.strip()}</td>' for c in row.split('&')) + '</tr>' for row in m.group(1).split(r'\\') if row.strip()) + '</table>', 
               t, flags=re.DOTALL)

    # 7. Subscripts & Superscripts
    t = re.sub(r'_\{([^}]+)\}', r'<sub>\1</sub>', t)
    t = re.sub(r'\^\{([^}]+)\}', r'<sup>\1</sup>', t)
    t = re.sub(r'_([0-9a-zA-Z])\b', r'<sub>\1</sub>', t)
    t = re.sub(r'\^([0-9a-zA-Z])\b', r'<sup>\1</sup>', t)

    # 8. Clean leftover math tags into math-expr (NOT code pills!)
    t = re.sub(r'<span class="math">\\text\{([^}]+)\} = ([^<]+)</span>', r'<b>\1</b> = \2', t)
    t = re.sub(r'<span class="math">(.*?)</span>', r'<span class="math-expr">\1</span>', t)
    t = re.sub(r'\$([^$]+)\$', r'<span class="math-expr">\1</span>', t)

    # 9. Ensure ASCII diagrams are strictly pre tags so spaces and newlines are preserved
    t = re.sub(r'<div class="diagram-box">(.*?)</div>', r'<pre class="diagram-box">\1</pre>', t, flags=re.DOTALL)
    return t

def build_data_js():
    smap = g.load_and_cluster()
    
    enrich_map = {
        "DBMS": ALL_DBMS,
        "Java": ALL_JAVA,
        "Networks": ALL_NETWORKS,
        "NM": ALL_NM
    }

    sub_key_map = {
        "DBMS": "dbms",
        "Java": "java",
        "Networks": "networks",
        "NM": "numerical"
    }

    sub_meta = {
        "dbms": {
            "code": "BCA-501",
            "paperCode": "18021",
            "title": "Introduction to DBMS",
            "desc": "Complete Deduplicated Question Bank covering Relational Algebra, SQL Queries, Normalization (1NF-BCNF), 2PL, Recovery & ER Modeling.",
            "icon": "fa-database",
            "color": "blue",
            "pdfBank": "pdfs/BCA501_DBMS.pdf",
            "years": [
                {"year": "2025", "pdf": "pdfs/dbms_2025.pdf"},
                {"year": "2024", "pdf": "pdfs/dbms_2024.pdf"},
                {"year": "2023", "pdf": "pdfs/dbms_2023.pdf"},
                {"year": "2021", "pdf": "pdfs/dbms_2021.pdf"},
                {"year": "2020", "pdf": "pdfs/dbms_2020.pdf"},
                {"year": "2019", "pdf": "pdfs/dbms_2019.pdf"},
                {"year": "2018", "pdf": "pdfs/dbms_2018.pdf"},
                {"year": "2017", "pdf": "pdfs/dbms_2017.pdf"},
                {"year": "2016", "pdf": "pdfs/dbms_2016.pdf"},
                {"year": "2015", "pdf": "pdfs/dbms_2015.pdf"},
                {"year": "2014", "pdf": "pdfs/dbms_2014.pdf"},
                {"year": "2013", "pdf": "pdfs/dbms_2013.pdf"}
            ]
        },
        "java": {
            "code": "BCA-502",
            "paperCode": "18022",
            "title": "Java Programming & Web Design",
            "desc": "Complete Deduplicated Question Bank covering JVM Internals, OOPs, Multithreading, Exception Handling, JDBC, Servlets, JSP & Sockets.",
            "icon": "fa-code",
            "color": "amber",
            "pdfBank": "pdfs/BCA502_Java.pdf",
            "years": [
                {"year": "2025", "pdf": "pdfs/java_2025.pdf"},
                {"year": "2024", "pdf": "pdfs/java_2024.pdf"},
                {"year": "2023", "pdf": "pdfs/java_2023.pdf"},
                {"year": "2021", "pdf": "pdfs/java_2021.pdf"},
                {"year": "2020", "pdf": "pdfs/java_2020.pdf"},
                {"year": "2019", "pdf": "pdfs/java_2019.pdf"},
                {"year": "2018", "pdf": "pdfs/java_2018.pdf"},
                {"year": "2017", "pdf": "pdfs/java_2017.pdf"},
                {"year": "2016", "pdf": "pdfs/java_2016.pdf"}
            ]
        },
        "networks": {
            "code": "BCA-503",
            "paperCode": "18023",
            "title": "Computer Networks",
            "desc": "Complete Deduplicated Question Bank covering OSI 7 Layers, TCP/IP, Sliding Window Protocols, CRC Error Control, Dijkstra, & Switching.",
            "icon": "fa-network-wired",
            "color": "emerald",
            "pdfBank": "pdfs/BCA503_Networks.pdf",
            "years": [
                {"year": "2025", "pdf": "pdfs/networks_2025.pdf"},
                {"year": "2024", "pdf": "pdfs/networks_2024.pdf"},
                {"year": "2023", "pdf": "pdfs/networks_2023.pdf"},
                {"year": "2021", "pdf": "pdfs/networks_2021.pdf"},
                {"year": "2020", "pdf": "pdfs/networks_2020.pdf"},
                {"year": "2019", "pdf": "pdfs/networks_2019.pdf"},
                {"year": "2018", "pdf": "pdfs/networks_2018.pdf"},
                {"year": "2017", "pdf": "pdfs/networks_2017.pdf"},
                {"year": "2016", "pdf": "pdfs/networks_2016.pdf"}
            ]
        },
        "numerical": {
            "code": "BCA-504",
            "paperCode": "18024",
            "title": "Numerical Methods",
            "desc": "Complete Deduplicated Question Bank covering Bisection, Newton-Raphson, Gauss Elimination, Interpolation (Newton/Lagrange) & RK4.",
            "icon": "fa-calculator",
            "color": "purple",
            "pdfBank": "pdfs/BCA504_Numerical.pdf",
            "years": [
                {"year": "2024", "pdf": "pdfs/nm_2024.pdf"},
                {"year": "2023", "pdf": "pdfs/nm_2023.pdf"},
                {"year": "2022", "pdf": "pdfs/nm_2022.pdf"},
                {"year": "2021", "pdf": "pdfs/nm_2021.pdf"},
                {"year": "2020", "pdf": "pdfs/nm_2020.pdf"},
                {"year": "2019", "pdf": "pdfs/nm_2019.pdf"},
                {"year": "2018", "pdf": "pdfs/nm_2018.pdf"}
            ]
        }
    }

    output_data = {}

    for raw_sub, sdata in smap.items():
        k = sub_key_map[raw_sub]
        enrich_dict = enrich_map[raw_sub]
        clusters = sdata["clusters"]

        # Apply enrichment
        for c in clusters:
            t_low = c["canonical_title"].lower()
            for ek, ev in enrich_dict.items():
                if ek.lower() in t_low and len(ev) > len(c["best_answer"]):
                    c["best_answer"] = ev
                    break
            # Clean LaTeX in title and answer
            c["canonical_title"] = clean_latex(c["canonical_title"])
            c["best_answer"] = clean_latex(c["best_answer"])

        # Split into Section C (>= 15M), Section B (7.5M), Section A (3M)
        sec_c = [c for c in clusters if c["max_marks"] >= 15]
        sec_b = [c for c in clusters if 5 <= c["max_marks"] < 15]
        sec_a = [c for c in clusters if c["max_marks"] < 5]

        # Sort each section by repetition count descending
        sec_c.sort(key=lambda x: (x["count"], x["max_marks"]), reverse=True)
        sec_b.sort(key=lambda x: (x["count"], x["max_marks"]), reverse=True)
        sec_a.sort(key=lambda x: (x["count"], x["max_marks"]), reverse=True)

        html_parts = []

        def render_section(q_list, sec_code, sec_name, marks_desc):
            if not q_list:
                return
            html_parts.append(f'<div class="sec-title" data-sec="{sec_code}">{sec_name} ({marks_desc} &bull; {len(q_list)} Questions)</div>\n')
            for idx, c in enumerate(q_list, start=1):
                years_badge = f"CCSU: {', '.join(c['year_list'])}"
                if c['count'] > 1:
                    years_badge += f" &bull; Repeated {c['count']}&times;"
                
                # Format question box
                html_parts.append(f'''<div class="q-box" data-section="{sec_code}">
    <div class="q-title">
        <span class="badge">{years_badge}</span>
        Q{idx}. {c['canonical_title']}
        <span class="q-marks">[{c['marks_display']}]</span>
    </div>
    <div class="ans-body">
        {c['best_answer']}
    </div>
</div>
''')

        # Render Section C first (High value 15M questions)
        render_section(sec_c, "sec-c", "Section – C", "Detailed / Long Answer Questions &bull; 15 Marks")
        # Render Section B (7.5M questions)
        render_section(sec_b, "sec-b", "Section – B", "Short Answer Questions &bull; 7.5 Marks")
        # Render Section A (3M questions)
        render_section(sec_a, "sec-a", "Section – A", "Very Short Answer Questions &bull; 3 Marks")

        full_html = "\n".join(html_parts)
        
        meta = sub_meta[k]
        meta["contentHtml"] = full_html
        meta["counts"] = {
            "total": len(clusters),
            "sec_c": len(sec_c),
            "sec_b": len(sec_b),
            "sec_a": len(sec_a)
        }
        output_data[k] = meta

    # Write data.js
    js_content = f"const SUBJECTS_DATA = {json.dumps(output_data, ensure_ascii=False)};\n"
    with open(r"c:\zzzz\pyq_solver_scripts\data.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    
    print(f"data.js generated successfully! File size: {len(js_content)} bytes")
    for k, v in output_data.items():
        cnt = v["counts"]
        print(f"  {k.upper()}: Total {cnt['total']} (Sec C: {cnt['sec_c']}, Sec B: {cnt['sec_b']}, Sec A: {cnt['sec_a']})")

if __name__ == "__main__":
    build_data_js()
