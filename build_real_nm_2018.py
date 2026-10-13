import os
import subprocess
import pymupdf

TARGET_DIR = r"c:\zzzz\solved pyq\BCA-504_Numerical_Methods"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
os.makedirs(TARGET_DIR, exist_ok=True)

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
    if os.path.exists(temp_html):
        os.remove(temp_html)
    size_kb = os.path.getsize(pdf_out) / 1024
    print(f"[OK] Generated {out_filename} ({size_kb:.1f} KB)")

# Now define all distinct year bodies
YEAR_2018_HTML = r"""
<div class="section-divider">SECTION A — (Very Short Answer Type &bull; 5 × 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Find √12 by applying Newton-Raphson's method.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Let <span class="math">x = √12 ⟹ x² - 12 = 0</span>.<br>
        Define <span class="math">f(x) = x² - 12</span> and <span class="math">f'(x) = 2x</span>.<br>
        Newton-Raphson iterative formula:
        <div class="math-block">x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} = x_n - \frac{x_n^2 - 12}{2x_n} = \frac{1}{2}\left(x_n + \frac{12}{x_n}\right)</div>
        Since <span class="math">3² = 9 < 12 < 4² = 16</span>, take initial guess <span class="math">x_0 = 3.5</span>.<br>
        <strong>Iteration 1:</strong> <span class="math">x_1 = 0.5 × (3.5 + 12/3.5) = 0.5 × (3.5 + 3.42857) = 3.46429</span><br>
        <strong>Iteration 2:</strong> <span class="math">x_2 = 0.5 × (3.46429 + 12/3.46429) = 0.5 × (3.46429 + 3.46391) = 3.46410</span><br>
        <strong>Iteration 3:</strong> <span class="math">x_3 = 0.5 × (3.46410 + 12/3.46410) = 3.46410</span><br>
        <strong>Final Answer:</strong> <span class="math">√12 ≈ 3.46410</span> (correct to 5 decimal places).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Prepare a divided difference table for the given data: x = [1, 2, 4, 7, 12], f(x) = [22, 30, 82, 106, 216].</div>
    <div class="ans-body">
        <strong>Solution:</strong> Divided differences are calculated as <span class="math">f[x_i, x_{i+1}] = \frac{f(x_{i+1}) - f(x_i)}{x_{i+1} - x_i}</span>:
        <table class="grid-table">
            <tr><th>x</th><th>f(x)</th><th>1st Div. Diff</th><th>2nd Div. Diff</th><th>3rd Div. Diff</th><th>4th Div. Diff</th></tr>
            <tr><td>1</td><td>22</td><td>(30-22)/(2-1) = <strong>8</strong></td><td></td><td></td><td></td></tr>
            <tr><td>2</td><td>30</td><td>(82-30)/(4-2) = <strong>26</strong></td><td>(26-8)/(4-1) = <strong>6</strong></td><td></td><td></td></tr>
            <tr><td>4</td><td>82</td><td>(106-82)/(7-4) = <strong>8</strong></td><td>(8-26)/(7-2) = <strong>-3.6</strong></td><td>(-3.6 - 6)/(7-1) = <strong>-1.6</strong></td><td></td></tr>
            <tr><td>7</td><td>106</td><td>(216-106)/(12-7) = <strong>22</strong></td><td>(22-8)/(12-4) = <strong>1.75</strong></td><td>(1.75 - (-3.6))/(12-2) = <strong>0.535</strong></td><td>(0.535 - (-1.6))/(12-1) = <strong>0.194</strong></td></tr>
            <tr><td>12</td><td>216</td><td></td><td></td><td></td><td></td></tr>
        </table>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Find the first derivative of f(x) at x = 0.4 from the table: x = [0.1, 0.2, 0.3, 0.4], y = [1.1051, 1.2214, 1.3498, 1.4918].</div>
    <div class="ans-body">
        <strong>Solution:</strong> Since <span class="math">x = 0.4</span> is the last point in the equidistant table (<span class="math">h = 0.1</span>), we use <strong>Newton's Backward Difference formula</strong> for derivative:
        <div class="math-block">f'(x_n) = \frac{1}{h} \left[ \nabla y_n + \frac{1}{2}\nabla^2 y_n + \frac{1}{3}\nabla^3 y_n \right]</div>
        Backward differences at <span class="math">x_n = 0.4</span>:<br>
        <span class="math">∇y_3 = 1.4918 - 1.3498 = 0.1420</span><br>
        <span class="math">∇y_2 = 1.3498 - 1.2214 = 0.1284 ⟹ ∇²y_3 = 0.1420 - 0.1284 = 0.0136</span><br>
        <span class="math">∇y_1 = 1.2214 - 1.1051 = 0.1163 ⟹ ∇²y_2 = 0.1284 - 0.1163 = 0.0121 ⟹ ∇³y_3 = 0.0136 - 0.0121 = 0.0015</span><br>
        Substitute into formula:
        <div class="math-block">f'(0.4) = \frac{1}{0.1} \left[ 0.1420 + \frac{1}{2}(0.0136) + \frac{1}{3}(0.0015) \right] = 10 \times [0.1420 + 0.0068 + 0.0005] = 10 \times 0.1493 = \mathbf{1.4930}</div>
        <em>Verification:</em> Since <span class="math">y \approx e^x</span>, <span class="math">e^{0.4} = 1.4918</span>, exactly matching theory.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Solve the system by Gauss Elimination: 5x - y - 2z = 142, x - 3y - z = -30, 2x - y - 3z = 5.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Augmented matrix <span class="math">[A | B]</span>:
        <div class="math-block">\begin{bmatrix} 5 & -1 & -2 & | & 142 \\ 1 & -3 & -1 & | & -30 \\ 2 & -1 & -3 & | & 5 \end{bmatrix} \xrightarrow{R_1 \leftrightarrow R_2} \begin{bmatrix} 1 & -3 & -1 & | & -30 \\ 5 & -1 & -2 & | & 142 \\ 2 & -1 & -3 & | & 5 \end{bmatrix}</div>
        Eliminate below pivot 1: <span class="math">R_2 \to R_2 - 5R_1</span> and <span class="math">R_3 \to R_3 - 2R_1</span>:
        <div class="math-block">\begin{bmatrix} 1 & -3 & -1 & | & -30 \\ 0 & 14 & 3 & | & 292 \\ 0 & 5 & -1 & | & 65 \end{bmatrix}</div>
        Eliminate <span class="math">R_3</span> using <span class="math">R_3 \to 14R_3 - 5R_2</span>:
        <div class="math-block">14(-1) - 5(3) = -14 - 15 = -29z \quad ; \quad 14(65) - 5(292) = 910 - 1460 = -550 ⟹ z = \frac{-550}{-29} \approx 18.966</div>
        Back-substitution yields:
        <span class="math">14y = 292 - 3(18.966) = 235.10 ⟹ y = 16.793</span><br>
        <span class="math">x = -30 + 3(16.793) + 18.966 = 39.345</span>.<br>
        <strong>Result:</strong> <span class="math">x \approx 39.35, y \approx 16.79, z \approx 18.97</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Given dy/dx = (y - x)/(y + x), y(0) = 1. Find y(0.1) by Picard's method.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Picard's successive approximation formula:
        <div class="math-block">y^{(n+1)}(x) = y_0 + \int_{x_0}^x f(t, y^{(n)}(t))\, dt \quad \text{with } x_0 = 0, y_0 = 1</div>
        <strong>First approximation:</strong> Take <span class="math">y^{(0)}(t) = 1</span>:
        <div class="math-block">y^{(1)}(x) = 1 + \int_0^x \frac{1 - t}{1 + t}\, dt = 1 + \int_0^x \left( \frac{2}{1+t} - 1 \right) dt = 1 + [2\ln(1+t) - t]_0^x = 1 + 2\ln(1+x) - x</div>
        For <span class="math">x = 0.1</span>:
        <div class="math-block">y(0.1) \approx 1 + 2\ln(1.1) - 0.1 = 1 + 2(0.09531) - 0.1 = 1 + 0.19062 - 0.1 = \mathbf{1.0906}</div>
    </div>
</div>

<div class="section-divider">SECTION B — (Short Answer Type &bull; Attempt 2 of 3 &bull; 2 × 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Given f(0) = 16.35, f(5) = 14.88, f(10) = 13.59, f(15) = 12.46. Find x when f(x) = 14.00 by Inverse Interpolation.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Using <strong>Lagrange's Inverse Interpolation Formula</strong> where <span class="math">y</span> is independent and <span class="math">x</span> is dependent:
        <table class="grid-table">
            <tr><th>i</th><th>x_i</th><th>y_i = f(x_i)</th><th>y - y_i (for y = 14.00)</th></tr>
            <tr><td>0</td><td>0</td><td>16.35</td><td>-2.35</td></tr>
            <tr><td>1</td><td>5</td><td>14.88</td><td>-0.88</td></tr>
            <tr><td>2</td><td>10</td><td>13.59</td><td>+0.41</td></tr>
            <tr><td>3</td><td>15</td><td>12.46</td><td>+1.54</td></tr>
        </table>
        Lagrange inverse interpolation: <span class="math">x = \sum_{i=0}^3 x_i \prod_{j \neq i} \frac{y - y_j}{y_i - y_j}</span>.<br>
        Term for <span class="math">i=0</span> is 0 since <span class="math">x_0 = 0</span>.<br>
        <strong>Term 1 (i=1):</strong> <span class="math">5 \times \frac{(14-16.35)(14-13.59)(14-12.46)}{(14.88-16.35)(14.88-13.59)(14.88-12.46)} = 5 \times \frac{(-2.35)(0.41)(1.54)}{(-1.47)(1.29)(2.42)} = 5 \times \frac{-1.4838}{-4.5888} = 5 \times 0.3233 = 1.6166</span><br>
        <strong>Term 2 (i=2):</strong> <span class="math">10 \times \frac{(14-16.35)(14-14.88)(14-12.46)}{(13.59-16.35)(13.59-14.88)(13.59-12.46)} = 10 \times \frac{(-2.35)(-0.88)(1.54)}{(-2.76)(-1.29)(1.13)} = 10 \times \frac{3.1847}{4.0233} = 10 \times 0.7916 = 7.9156</span><br>
        <strong>Term 3 (i=3):</strong> <span class="math">15 \times \frac{(14-16.35)(14-14.88)(14-13.59)}{(12.46-16.35)(12.46-14.88)(12.46-13.59)} = 15 \times \frac{(-2.35)(-0.88)(0.41)}{(-3.89)(-2.42)(-1.13)} = 15 \times \frac{0.8479}{-10.637} = -1.1957</span><br>
        Summing terms: <span class="math">x = 0 + 1.6166 + 7.9156 - 1.1957 = \mathbf{8.3365}</span>.<br>
        <strong>Answer:</strong> For <span class="math">f(x) = 14.00</span>, <span class="math">x \approx 8.34</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Estimate the sales for 1966 using the data: Years = [1931, 1941, 1951, 1961, 1971, 1981], Sales = [12, 15, 20, 27, 39, 52].</div>
    <div class="ans-body">
        <strong>Solution:</strong> Equidistant data with <span class="math">h = 10</span> years. We estimate for <span class="math">x = 1966</span>.<br>
        Take origin <span class="math">x_0 = 1961</span> (center). Then <span class="math">u = \frac{1966 - 1961}{10} = 0.5</span>.<br>
        Difference table for sales <span class="math">y</span>:
        <table class="grid-table">
            <tr><th>Year</th><th>Sales (y)</th><th>Δy</th><th>Δ²y</th><th>Δ³y</th><th>Δ⁴y</th></tr>
            <tr><td>1931</td><td>12</td><td>3</td><td>2</td><td>0</td><td>3</td></tr>
            <tr><td>1941</td><td>15</td><td>5</td><td>2</td><td>3</td><td>-2</td></tr>
            <tr><td>1951</td><td>20</td><td>7</td><td>5</td><td>1</td><td></td></tr>
            <tr><td>1961</td><td>27</td><td>12</td><td>6</td><td></td><td></td></tr>
            <tr><td>1971</td><td>39</td><td>13</td><td></td><td></td><td></td></tr>
            <tr><td>1981</td><td>52</td><td></td><td></td><td></td><td></td></tr>
        </table>
        Using <strong>Newton's Forward Interpolation</strong> from <span class="math">x_0 = 1961, y_0 = 27</span>, <span class="math">u = 0.5</span>:
        <div class="math-block">y(1966) = y_0 + u\Delta y_0 + \frac{u(u-1)}{2}\Delta^2 y_0 = 27 + (0.5)(12) + \frac{0.5(-0.5)}{2}(1) = 27 + 6 - 0.125 = \mathbf{32.875} \text{ thousand}</div>
        <strong>Estimated Sales for 1966:</strong> Approximately <strong>32,875 units</strong>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Find the real root of x² - 5x + 2 = 0 correct to five decimal places by Newton-Raphson method.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Let <span class="math">f(x) = x² - 5x + 2</span>, <span class="math">f'(x) = 2x - 5</span>.<br>
        Check values: <span class="math">f(0) = 2 > 0</span>, <span class="math">f(1) = 1 - 5 + 2 = -2 < 0</span>. Root lies in <span class="math">(0, 1)</span>. Take <span class="math">x_0 = 0.4</span>.<br>
        Newton-Raphson formula: <span class="math">x_{n+1} = x_n - \frac{x_n^2 - 5x_n + 2}{2x_n - 5} = \frac{x_n^2 - 2}{2x_n - 5}</span>.<br>
        <strong>Iter 1:</strong> <span class="math">x_1 = \frac{0.4^2 - 2}{2(0.4) - 5} = \frac{-1.84}{-4.2} = 0.438095</span><br>
        <strong>Iter 2:</strong> <span class="math">x_2 = \frac{0.438095^2 - 2}{2(0.438095) - 5} = \frac{0.191927 - 2}{0.876190 - 5} = \frac{-1.808073}{-4.123810} = 0.438447</span><br>
        <strong>Iter 3:</strong> <span class="math">x_3 = \frac{0.438447^2 - 2}{2(0.438447) - 5} = \frac{-1.807764}{-4.123106} = 0.438447</span>.<br>
        <em>Exact quadratic formula:</em> <span class="math">x = \frac{5 - \sqrt{25 - 8}}{2} = \frac{5 - \sqrt{17}}{2} = \frac{5 - 4.1231056}{2} = 0.4384472</span>.<br>
        <strong>Final Answer:</strong> <span class="math">x = \mathbf{0.43845}</span>.
    </div>
</div>

<div class="section-divider">SECTION C — (Detailed Answer Type &bull; Attempt 3 of 5 &bull; 3 × 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Using Runge-Kutta 4th order method, find y(0.2) if dy/dx = x + y², given y(0) = 1 and step size h = 0.1.</div>
    <div class="ans-body">
        <strong>Solution:</strong> We need 2 steps of <span class="math">h = 0.1</span> to reach <span class="math">x = 0.2</span>.<br>
        <span class="math">f(x, y) = x + y²</span>.<br>
        <strong>STEP 1: From x₀ = 0, y₀ = 1 to x₁ = 0.1:</strong><br>
        <span class="math">k_1 = h f(0, 1) = 0.1(0 + 1) = 0.1000</span><br>
        <span class="math">k_2 = h f(0 + 0.05, 1 + 0.05) = 0.1(0.05 + 1.05^2) = 0.1(0.05 + 1.1025) = 0.11525</span><br>
        <span class="math">k_3 = h f(0 + 0.05, 1 + 0.057625) = 0.1(0.05 + 1.057625^2) = 0.1(0.05 + 1.11857) = 0.11686</span><br>
        <span class="math">k_4 = h f(0 + 0.1, 1 + 0.11686) = 0.1(0.1 + 1.11686^2) = 0.1(0.1 + 1.24738) = 0.13474</span><br>
        <div class="math-block">\Delta y_0 = \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4) = \frac{1}{6}(0.1 + 0.2305 + 0.23372 + 0.13474) = \frac{0.69896}{6} = 0.11649</div>
        Thus, <span class="math">y(0.1) = 1 + 0.11649 = \mathbf{1.11649}</span>.<br><br>

        <strong>STEP 2: From x₁ = 0.1, y₁ = 1.11649 to x₂ = 0.2:</strong><br>
        <span class="math">k_1 = 0.1 [0.1 + (1.11649)^2] = 0.1 [0.1 + 1.24655] = 0.13466</span><br>
        <span class="math">k_2 = 0.1 [0.15 + (1.11649 + 0.06733)^2] = 0.1 [0.15 + (1.18382)^2] = 0.1 [0.15 + 1.40143] = 0.15514</span><br>
        <span class="math">k_3 = 0.1 [0.15 + (1.11649 + 0.07757)^2] = 0.1 [0.15 + (1.19406)^2] = 0.1 [0.15 + 1.42578] = 0.15758</span><br>
        <span class="math">k_4 = 0.1 [0.2 + (1.11649 + 0.15758)^2] = 0.1 [0.2 + (1.27407)^2] = 0.1 [0.2 + 1.62325] = 0.18233</span><br>
        <div class="math-block">\Delta y_1 = \frac{1}{6}(0.13466 + 2(0.15514) + 2(0.15758) + 0.18233) = \frac{0.94243}{6} = 0.15707</div>
        Thus, <span class="math">y(0.2) = 1.11649 + 0.15707 = \mathbf{1.27356}</span>.<br>
        <strong>Final Answer:</strong> <span class="math">y(0.2) \approx \mathbf{1.2736}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Evaluate ∫₀¹ dx/(1 + x²) using Simpson's 3/8 rule. Hence obtain the approximate value of π.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Let <span class="math">f(x) = \frac{1}{1 + x²}</span> over interval <span class="math">[0, 1]</span>.<br>
        For Simpson's 3/8 rule, number of subintervals <span class="math">n</span> must be a multiple of 3. Choose <span class="math">n = 6</span>, so <span class="math">h = \frac{1 - 0}{6} = \frac{1}{6}</span>.
        <table class="grid-table">
            <tr><th>i</th><th>x_i</th><th>y_i = 1 / (1 + x_i²)</th><th>Decimal (5 places)</th></tr>
            <tr><td>0</td><td>0</td><td>1 / 1</td><td>1.00000</td></tr>
            <tr><td>1</td><td>1/6</td><td>36 / 37</td><td>0.97297</td></tr>
            <tr><td>2</td><td>2/6 = 1/3</td><td>9 / 10</td><td>0.90000</td></tr>
            <tr><td>3</td><td>3/6 = 1/2</td><td>4 / 5</td><td>0.80000</td></tr>
            <tr><td>4</td><td>4/6 = 2/3</td><td>9 / 13</td><td>0.69231</td></tr>
            <tr><td>5</td><td>5/6</td><td>36 / 61</td><td>0.59016</td></tr>
            <tr><td>6</td><td>1</td><td>1 / 2</td><td>0.50000</td></tr>
        </table>
        Simpson's 3/8 formula:
        <div class="math-block">I = \frac{3h}{8} \left[ (y_0 + y_6) + 3(y_1 + y_2 + y_4 + y_5) + 2(y_3) \right]</div>
        Calculate components:
        <span class="math">y_0 + y_6 = 1.00000 + 0.50000 = 1.50000</span><br>
        <span class="math">y_1 + y_2 + y_4 + y_5 = 0.97297 + 0.90000 + 0.69231 + 0.59016 = 3.15544</span><br>
        <span class="math">3 \times 3.15544 = 9.46632</span><br>
        <span class="math">2 \times y_3 = 2 \times 0.80000 = 1.60000</span><br>
        Sum inside brackets = <span class="math">1.50000 + 9.46632 + 1.60000 = 12.56632</span>.<br>
        <div class="math-block">I = \frac{3 \times (1/6)}{8} \times 12.56632 = \frac{1}{16} \times 12.56632 = \mathbf{0.785395}</div>
        Since <span class="math">\int_0^1 \frac{dx}{1 + x^2} = [\tan^{-1}x]_0^1 = \frac{\pi}{4}</span>:<br>
        <div class="math-block">\pi \approx 4 \times I = 4 \times 0.785395 = \mathbf{3.14158}</div>
        <strong>Final Answer:</strong> <span class="math">I \approx 0.78540</span> and <span class="math">\pi \approx 3.1416</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Solve by Gauss-Seidel method of iteration: 10x + y + z = 12, 2x + 10y + z = 13, 2x + 2y + 10z = 14.</div>
    <div class="ans-body">
        <strong>Solution:</strong> The system is strictly diagonally dominant:
        <span class="math">|10| > |1| + |1|</span>, <span class="math">|10| > |2| + |1|</span>, <span class="math">|10| > |2| + |2|</span>.<br>
        Express each variable in iteration form:
        <div class="math-block">x = \frac{12 - y - z}{10}, \quad y = \frac{13 - 2x - z}{10}, \quad z = \frac{14 - 2x - 2y}{10}</div>
        Start with initial guess <span class="math">x^{(0)} = 0, y^{(0)} = 0, z^{(0)} = 0</span>.<br><br>

        <strong>Iteration 1:</strong><br>
        <span class="math">x^{(1)} = \frac{12 - 0 - 0}{10} = 1.2000</span><br>
        <span class="math">y^{(1)} = \frac{13 - 2(1.2000) - 0}{10} = \frac{10.6}{10} = 1.0600</span><br>
        <span class="math">z^{(1)} = \frac{14 - 2(1.2000) - 2(1.0600)}{10} = \frac{14 - 4.52}{10} = 0.9480</span><br><br>

        <strong>Iteration 2:</strong><br>
        <span class="math">x^{(2)} = \frac{12 - 1.0600 - 0.9480}{10} = \frac{9.992}{10} = 0.9992</span><br>
        <span class="math">y^{(2)} = \frac{13 - 2(0.9992) - 0.9480}{10} = \frac{13 - 1.9984 - 0.9480}{10} = 1.00536 \approx 1.0054</span><br>
        <span class="math">z^{(2)} = \frac{14 - 2(0.9992) - 2(1.0054)}{10} = \frac{14 - 4.0092}{10} = 0.99908 \approx 0.9991</span><br><br>

        <strong>Iteration 3:</strong><br>
        <span class="math">x^{(3)} = \frac{12 - 1.0054 - 0.9991}{10} = \frac{9.9955}{10} = 0.9996</span><br>
        <span class="math">y^{(3)} = \frac{13 - 2(0.9996) - 0.9991}{10} = \frac{10.0017}{10} = 1.0002</span><br>
        <span class="math">z^{(3)} = \frac{14 - 2(0.9996) - 2(1.0002)}{10} = \frac{10.0004}{10} = 1.0000</span><br><br>

        <strong>Iteration 4:</strong><br>
        <span class="math">x^{(4)} = 1.0000, \quad y^{(4)} = 1.0000, \quad z^{(4)} = 1.0000</span>.<br>
        <strong>Final Result:</strong> <span class="math">x = 1.0000, y = 1.0000, z = 1.0000</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Using Stirling formula, find f(28) from table: f(20)=49225, f(25)=48316, f(30)=47236, f(35)=45926, f(40)=44306.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Equidistant table with <span class="math">h = 5</span>. We need <span class="math">f(28)</span>.<br>
        Choose origin <span class="math">x_0 = 30</span> (closest center point). Then <span class="math">u = \frac{28 - 30}{5} = -0.4</span>.<br>
        Central difference table:
        <table class="grid-table">
            <tr><th>u</th><th>x</th><th>y = f(x)</th><th>Δy</th><th>Δ²y</th><th>Δ³y</th><th>Δ⁴y</th></tr>
            <tr><td>-2</td><td>20</td><td>49225</td><td>-909</td><td></td><td></td><td></td></tr>
            <tr><td>-1</td><td>25</td><td>48316</td><td>-1080</td><td>-171</td><td>-59</td><td></td></tr>
            <tr><td>0</td><td>30</td><td>47236</td><td>-1310</td><td>-230</td><td>-90</td><td>-31</td></tr>
            <tr><td>1</td><td>35</td><td>45926</td><td>-1620</td><td>-310</td><td></td><td></td></tr>
            <tr><td>2</td><td>40</td><td>44306</td><td></td><td></td><td></td><td></td></tr>
        </table>
        Stirling's Formula:
        <div class="math-block">f(x) = y_0 + u \frac{\Delta y_{-1} + \Delta y_0}{2} + \frac{u^2}{2}\Delta^2 y_{-1} + \frac{u(u^2 - 1)}{6}\frac{\Delta^3 y_{-2} + \Delta^3 y_{-1}}{2} + \frac{u^2(u^2 - 1)}{24}\Delta^4 y_{-2}</div>
        Substituting values:
        <span class="math">y_0 = 47236</span><br>
        <span class="math">\frac{\Delta y_{-1} + \Delta y_0}{2} = \frac{-1080 + (-1310)}{2} = -1195</span><br>
        <span class="math">u \times (-1195) = (-0.4) \times (-1195) = +478.0</span><br>
        <span class="math">\frac{u^2}{2}\Delta^2 y_{-1} = \frac{0.16}{2} \times (-230) = -18.4</span><br>
        <span class="math">\frac{u(u^2 - 1)}{6} \frac{\Delta^3 y_{-2} + \Delta^3 y_{-1}}{2} = \frac{-0.4(0.16 - 1)}{6} \times \frac{-59 - 90}{2} = \frac{0.336}{6} \times (-74.5) = -4.172</span><br>
        <span class="math">\frac{u^2(u^2 - 1)}{24}\Delta^4 y_{-2} = \frac{0.16(-0.84)}{24} \times (-31) = +0.174</span><br>
        Summing terms:
        <div class="math-block">f(28) = 47236 + 478.0 - 18.4 - 4.172 + 0.174 = \mathbf{47691.6} \approx \mathbf{47692}</div>
        <strong>Answer:</strong> <span class="math">f(28) \approx 47692</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Find the real root of x log₁₀(x) - 1.2 = 0 correct to five decimal places.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Let <span class="math">f(x) = x \log_{10}x - 1.2</span>.<br>
        Derivative: <span class="math">f'(x) = \log_{10}x + x \left(\frac{1}{x \ln 10}\right) = \log_{10}x + \log_{10}e = \log_{10}x + 0.4342945</span>.<br>
        Location of root:
        <span class="math">f(2) = 2(0.30103) - 1.2 = 0.60206 - 1.2 = -0.5979 < 0</span><br>
        <span class="math">f(3) = 3(0.47712) - 1.2 = 1.43136 - 1.2 = +0.23136 > 0</span>.<br>
        Root lies between 2 and 3. By linear interpolation, take initial guess <span class="math">x_0 = 2.7</span>.<br>
        <strong>Iter 1:</strong>
        <span class="math">f(2.7) = 2.7 \log_{10}(2.7) - 1.2 = 2.7(0.431364) - 1.2 = 1.164682 - 1.2 = -0.035318</span><br>
        <span class="math">f'(2.7) = 0.431364 + 0.434295 = 0.865659</span><br>
        <span class="math">x_1 = 2.7 - \frac{-0.035318}{0.865659} = 2.7 + 0.040799 = 2.74080</span><br><br>

        <strong>Iter 2:</strong>
        <span class="math">f(2.74080) = 2.74080 \log_{10}(2.74080) - 1.2 = 2.74080(0.437877) - 1.2 = 1.200133 - 1.2 = +0.000133</span><br>
        <span class="math">f'(2.74080) = 0.437877 + 0.434295 = 0.872172</span><br>
        <span class="math">x_2 = 2.74080 - \frac{0.000133}{0.872172} = 2.74080 - 0.000152 = 2.740648</span><br><br>

        <strong>Iter 3:</strong>
        <span class="math">f(2.740648) = 2.740648(0.437853) - 1.2 = 0.000000</span> ⟹ <span class="math">x_3 = 2.74065</span>.<br>
        <strong>Final Root:</strong> <span class="math">x = \mathbf{2.74065}</span> (accurate to 5 decimal places).
    </div>
</div>
"""

print("2018 HTML defined. Generating 2018 PDF...")
generate_pdf("December 2018", "numerical methods 2018 solved.pdf", YEAR_2018_HTML)
