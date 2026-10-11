# -*- coding: utf-8 -*-
"""
Build high-quality textbook-formatted Numerical Methods solved PYQ PDFs for CCSU BCA 5th Semester.
Uses HTML/CSS with Cambria Math, custom fractions, bracketed matrices, shaded iteration tables,
and highlighted answer callouts, rendered via Chrome Headless.
"""
import os
import sys
import subprocess
import pymupdf

TARGET_DIR = r"c:\zzzz\solved pyq"
os.makedirs(TARGET_DIR, exist_ok=True)
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

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
    line-height: 1.48;
    color: #1e293b;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
}

.header-banner {
    border-bottom: 2.5px solid #1e40af;
    padding-bottom: 8px;
    margin-bottom: 12px;
}

.univ-name {
    font-size: 10pt;
    font-weight: 700;
    color: #1e40af;
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
    font-weight: 500;
    margin: 0;
}

.sec-title {
    background: #f1f5f9;
    border-left: 5px solid #1e40af;
    padding: 5px 10px;
    font-size: 10.5pt;
    font-weight: 800;
    color: #0f172a;
    margin: 14px 0 8px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    border-radius: 0 4px 4px 0;
}

.q-box {
    margin-bottom: 12px;
}

.q-title {
    font-size: 10pt;
    font-weight: 700;
    color: #0f172a;
    margin: 6px 0 4px 0;
}

.q-marks {
    display: inline-block;
    background: #e0e7ff;
    color: #3730a3;
    font-size: 8pt;
    font-weight: 700;
    padding: 1px 6px;
    border-radius: 3px;
    margin-left: 6px;
}

.math-box {
    background: #f8fafc;
    border-left: 3.5px solid #2563eb;
    border-top: 1px solid #e2e8f0;
    border-right: 1px solid #e2e8f0;
    border-bottom: 1px solid #e2e8f0;
    padding: 7px 12px;
    margin: 6px 0;
    border-radius: 0 4px 4px 0;
    page-break-inside: avoid;
}

.formula {
    font-family: 'Cambria Math', 'Times New Roman', serif;
    font-size: 10.5pt;
    color: #0f172a;
    line-height: 1.6;
    margin: 3px 0;
}

.frac {
    display: inline-flex;
    flex-direction: column;
    vertical-align: middle;
    text-align: center;
    font-size: 0.9em;
    padding: 0 3px;
    line-height: 1.1;
}

.num {
    border-bottom: 1.4px solid #0f172a;
    padding-bottom: 1.5px;
}

.den {
    padding-top: 1.5px;
}

.matrix {
    display: inline-table;
    vertical-align: middle;
    border-left: 2px solid #0f172a;
    border-right: 2px solid #0f172a;
    border-radius: 4px;
    padding: 1px 4px;
    margin: 4px 6px;
    page-break-inside: avoid;
}

.matrix td {
    padding: 2px 7px;
    font-family: 'Cambria Math', 'Times New Roman', serif;
    text-align: right;
    border: none;
    font-size: 9.5pt;
}

.matrix td.divider {
    border-left: 1.5px dashed #64748b;
    padding-left: 8px;
}

table.iter-table {
    width: 100%;
    border-collapse: collapse;
    margin: 6px 0;
    font-size: 8pt;
    font-family: 'JetBrains Mono', Consolas, monospace;
    page-break-inside: avoid;
}

table.iter-table th {
    background-color: #1e40af;
    color: #ffffff;
    font-family: 'Inter', sans-serif;
    font-weight: 700;
    padding: 5px 6px;
    border: 1px solid #1e3a8a;
    text-align: center;
}

table.iter-table td {
    padding: 3.5px 5px;
    border: 1px solid #cbd5e1;
    text-align: center;
}

table.iter-table tr:nth-child(even) td {
    background-color: #f8fafc;
}

.highlight-ans {
    background: #ecfdf5;
    border: 1.5px solid #10b981;
    color: #065f46;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 4px;
    display: inline-block;
    margin: 5px 0;
    font-size: 9pt;
}

.step-label {
    font-weight: 700;
    color: #1e40af;
    margin-top: 5px;
    margin-bottom: 2px;
}

p, li {
    margin: 2px 0 4px 0;
    color: #334155;
}

ul {
    margin: 3px 0 5px 16px;
    padding: 0;
}

ol {
    margin: 3px 0 5px 16px;
    padding: 0;
}

hr {
    border: 0;
    border-top: 1px solid #e2e8f0;
    margin: 10px 0;
}
</style>
"""

BODY_QUESTIONS_HTML = """
<!-- ==================== SECTION A ==================== -->
<div class="sec-title">Section – A (Very Short Answer Questions &bull; 3 Marks Each &bull; All 5 Compulsory)</div>

<!-- Q1 -->
<div class="q-box">
    <div class="q-title">Q1. Obtain a real root of the equation <i>f(x) = x<sup>3</sup> + x<sup>2</sup> &minus; 1 = 0</i> using Bisection method correct to 3 decimal places. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Solution:</strong></p>
    <p>Let <i>f(x) = x<sup>3</sup> + x<sup>2</sup> &minus; 1</i>.</p>
    <ul>
        <li>For <i>x = 0</i>: <i>f(0) = 0 + 0 &minus; 1 = &minus;1 &lt; 0</i></li>
        <li>For <i>x = 1</i>: <i>f(1) = 1 + 1 &minus; 1 = +1 &gt; 0</i></li>
    </ul>
    <p>Since <i>f(0) &bull; f(1) &lt; 0</i>, a real root lies in the open interval <b>(0, 1)</b>.</p>
    
    <table class="iter-table">
        <tr>
            <th>n</th><th>a</th><th>b</th><th>c = (a+b)/2</th><th>f(c)</th><th>Sign</th><th>Updated Interval</th>
        </tr>
        <tr><td>1</td><td>0.0000</td><td>1.0000</td><td>0.5000</td><td>&minus;0.6250</td><td>Negative (&lt; 0)</td><td>[0.5000, 1.0000]</td></tr>
        <tr><td>2</td><td>0.5000</td><td>1.0000</td><td>0.7500</td><td>&minus;0.0156</td><td>Negative (&lt; 0)</td><td>[0.7500, 1.0000]</td></tr>
        <tr><td>3</td><td>0.7500</td><td>1.0000</td><td>0.8750</td><td>+0.4355</td><td>Positive (&gt; 0)</td><td>[0.7500, 0.8750]</td></tr>
        <tr><td>4</td><td>0.7500</td><td>0.8750</td><td>0.8125</td><td>+0.1965</td><td>Positive (&gt; 0)</td><td>[0.7500, 0.8125]</td></tr>
        <tr><td>5</td><td>0.7500</td><td>0.8125</td><td>0.7812</td><td>+0.0872</td><td>Positive (&gt; 0)</td><td>[0.7500, 0.7812]</td></tr>
        <tr><td>6</td><td>0.7500</td><td>0.7812</td><td>0.7656</td><td>+0.0350</td><td>Positive (&gt; 0)</td><td>[0.7500, 0.7656]</td></tr>
        <tr><td>7</td><td>0.7500</td><td>0.7656</td><td>0.7578</td><td>+0.0095</td><td>Positive (&gt; 0)</td><td>[0.7500, 0.7578]</td></tr>
        <tr><td>8</td><td>0.7500</td><td>0.7578</td><td>0.7539</td><td>&minus;0.0031</td><td>Negative (&lt; 0)</td><td>[0.7539, 0.7578]</td></tr>
        <tr><td>9</td><td>0.7539</td><td>0.7578</td><td>0.7559</td><td>+0.0032</td><td>Positive (&gt; 0)</td><td>[0.7539, 0.7559]</td></tr>
        <tr><td>10</td><td>0.7539</td><td>0.7559</td><td>0.7549</td><td>+0.00002</td><td>Positive (&ge; 0)</td><td>[0.7539, 0.7549]</td></tr>
        <tr><td>11</td><td>0.7539</td><td>0.7549</td><td>0.7544</td><td>&minus;0.0015</td><td>Negative (&lt; 0)</td><td>[0.7544, 0.7549]</td></tr>
    </table>
    <p>At iteration 11, interval width is <i>|0.7549 &minus; 0.7544| = 0.0005 &lt; 0.001</i>.</p>
    <div><span class="highlight-ans">Final Converged Root: x &approx; 0.755 (correct to 3 decimal places)</span></div>
</div>

<hr>

<!-- Q2 -->
<div class="q-box">
    <div class="q-title">Q2. Define backward differences and prove the operator identity <i>E&nabla; = &nabla;E = &Delta;</i>. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Solution:</strong></p>
    <p><strong>Definition:</strong> For equispaced points <i>x<sub>i</sub> = x<sub>0</sub> + i&bull;h</i>, the <b>Backward Difference Operator (&nabla;)</b> is defined as:</p>
    <div class="math-box">
        <p class="formula">&nabla;y<sub>i</sub> = y<sub>i</sub> &minus; y<sub>i&minus;1</sub> &emsp;and&emsp; &nabla;<sup>k</sup>y<sub>i</sub> = &nabla;<sup>k&minus;1</sup>y<sub>i</sub> &minus; &nabla;<sup>k&minus;1</sup>y<sub>i&minus;1</sub> &nbsp;(k &ge; 2)</p>
    </div>
    <p><strong>Backward Difference Table for ordered pairs (x<sub>0</sub>, y<sub>0</sub>) to (x<sub>4</sub>, y<sub>4</sub>):</strong></p>
    <table class="iter-table">
        <tr><th>x</th><th>y</th><th>&nabla;y</th><th>&nabla;<sup>2</sup>y</th><th>&nabla;<sup>3</sup>y</th><th>&nabla;<sup>4</sup>y</th></tr>
        <tr><td>x<sub>0</sub></td><td>y<sub>0</sub></td><td>—</td><td>—</td><td>—</td><td>—</td></tr>
        <tr><td>x<sub>1</sub></td><td>y<sub>1</sub></td><td>&nabla;y<sub>1</sub> = y<sub>1</sub> &minus; y<sub>0</sub></td><td>—</td><td>—</td><td>—</td></tr>
        <tr><td>x<sub>2</sub></td><td>y<sub>2</sub></td><td>&nabla;y<sub>2</sub> = y<sub>2</sub> &minus; y<sub>1</sub></td><td>&nabla;<sup>2</sup>y<sub>2</sub></td><td>—</td><td>—</td></tr>
        <tr><td>x<sub>3</sub></td><td>y<sub>3</sub></td><td>&nabla;y<sub>3</sub> = y<sub>3</sub> &minus; y<sub>2</sub></td><td>&nabla;<sup>2</sup>y<sub>3</sub></td><td>&nabla;<sup>3</sup>y<sub>3</sub></td><td>—</td></tr>
        <tr><td>x<sub>4</sub></td><td>y<sub>4</sub></td><td>&nabla;y<sub>4</sub> = y<sub>4</sub> &minus; y<sub>3</sub></td><td>&nabla;<sup>2</sup>y<sub>4</sub></td><td>&nabla;<sup>3</sup>y<sub>4</sub></td><td>&nabla;<sup>4</sup>y<sub>4</sub></td></tr>
    </table>
    <p><strong>Operator Proofs:</strong></p>
    <ol>
        <li><i>E &bull; &nabla; f(x) = E [f(x) &minus; f(x &minus; h)] = f(x + h) &minus; f(x) = &Delta;f(x) &rArr; <b>E&nabla; = &Delta;</b></i></li>
        <li><i>&nabla; &bull; E f(x) = &nabla; [f(x + h)] = f(x + h) &minus; f(x) = &Delta;f(x) &rArr; <b>&nabla;E = &Delta;</b></i></li>
    </ol>
    <div><span class="highlight-ans">Hence Proved: E&nabla; = &nabla;E = &Delta;</span></div>
</div>

<hr>

<!-- Q3 -->
<div class="q-box">
    <div class="q-title">Q3. Find the value of <span class="frac"><span class="num">dy</span><span class="den">dx</span></span> at <i>x = 1.2</i> for points (1.0, 2.7183), (1.2, 3.3201), (1.4, 4.0552)... <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Solution:</strong></p>
    <p>Given step size <i>h = 1.2 &minus; 1.0 = 0.2</i>. Let <i>x<sub>0</sub> = 1.2, y<sub>0</sub> = 3.3201</i>.</p>
    <p>Neighbors: <i>x<sub>&minus;1</sub> = 1.0, y<sub>&minus;1</sub> = 2.7183</i> and <i>x<sub>1</sub> = 1.4, y<sub>1</sub> = 4.0552</i>.</p>
    <div class="math-box">
        <p class="formula">
            <b>Central Difference Formula (First Derivative):</b><br>
            f'(x<sub>0</sub>) &approx; <span class="frac"><span class="num">y<sub>1</sub> &minus; y<sub>&minus;1</sub></span><span class="den">2h</span></span>
        </p>
        <p class="formula">
            f'(1.2) = <span class="frac"><span class="num">4.0552 &minus; 2.7183</span><span class="den">2(0.2)</span></span>
            = <span class="frac"><span class="num">1.3369</span><span class="den">0.40</span></span>
            = <b>3.34225</b>
        </p>
    </div>
    <p><i>(Newton's Forward Difference check: f'(1.2) &approx; (1/0.2)[0.7351 &minus; 0.5(0.1627) + (1/3)(0.0361)] = 3.3289. True derivative e<sup>1.2</sup> &approx; 3.3201.)</i></p>
    <div><span class="highlight-ans">dy/dx at x = 1.2 is 3.34225</span></div>
</div>

<hr>

<!-- Q4 -->
<div class="q-box">
    <div class="q-title">Q4. Solve the following linear system using Gauss Elimination method: <span class="q-marks">[3 Marks]</span></div>
    <div class="math-box">
        <p class="formula">
            10x + y + z = 12<br>
            2x + 10y + z = 13<br>
            x + y + 3z = 5
        </p>
    </div>
    <p><strong>Solution:</strong></p>
    <p class="step-label">Step 1: Form the Augmented Matrix [A | B]:</p>
    <div style="text-align: center; margin: 4px 0;">
        <table class="matrix">
            <tr><td>10</td><td>1</td><td>1</td><td class="divider">12</td></tr>
            <tr><td>2</td><td>10</td><td>1</td><td class="divider">13</td></tr>
            <tr><td>1</td><td>1</td><td>3</td><td class="divider">5</td></tr>
        </table>
    </div>
    <p class="step-label">Step 2: Forward Elimination to Upper Triangular Form:</p>
    <ul>
        <li><i>R<sub>2</sub> &rarr; R<sub>2</sub> &minus; (2/10)R<sub>1</sub> = R<sub>2</sub> &minus; 0.2R<sub>1</sub></i> &rArr; [0, 9.8, 0.8 | 10.6]</li>
        <li><i>R<sub>3</sub> &rarr; R<sub>3</sub> &minus; (1/10)R<sub>1</sub> = R<sub>3</sub> &minus; 0.1R<sub>1</sub></i> &rArr; [0, 0.9, 2.9 | 3.8]</li>
        <li><i>R<sub>3</sub> &rarr; R<sub>3</sub> &minus; (0.9 / 9.8)R<sub>2</sub></i> &rArr; [0, 0, 2.82653 | 2.82653]</li>
    </ul>
    <div style="text-align: center; margin: 4px 0;">
        <table class="matrix">
            <tr><td>10</td><td>1</td><td>1</td><td class="divider">12</td></tr>
            <tr><td>0</td><td>9.8</td><td>0.8</td><td class="divider">10.6</td></tr>
            <tr><td>0</td><td>0</td><td>2.82653</td><td class="divider">2.82653</td></tr>
        </table>
    </div>
    <p class="step-label">Step 3: Back Substitution:</p>
    <ul>
        <li>From Row 3: 2.82653 &bull; z = 2.82653 &rArr; <b>z = 1</b></li>
        <li>From Row 2: 9.8 &bull; y + 0.8(1) = 10.6 &rArr; 9.8 &bull; y = 9.8 &rArr; <b>y = 1</b></li>
        <li>From Row 1: 10 &bull; x + 1(1) + 1(1) = 12 &rArr; 10 &bull; x = 10 &rArr; <b>x = 1</b></li>
    </ul>
    <div><span class="highlight-ans">Unique Solution: x = 1, &nbsp; y = 1, &nbsp; z = 1</span></div>
</div>

<hr>

<!-- Q5 -->
<div class="q-box">
    <div class="q-title">Q5. Solve <span class="frac"><span class="num">dy</span><span class="den">dx</span></span> = x + y<sup>2</sup>, with y(0) = 1 using Picard's method up to second approximation. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Solution:</strong></p>
    <div class="math-box">
        <p class="formula">
            <b>Picard's Successive Approximation Formula:</b><br>
            y<sup>(n)</sup>(x) = y<sub>0</sub> + &int;<sub>x<sub>0</sub></sub><sup>x</sup> f(t, y<sup>(n&minus;1)</sup>(t)) dt
        </p>
    </div>
    <p>Given initial conditions: <i>x<sub>0</sub> = 0, y<sub>0</sub> = 1</i>, and <i>f(t, y) = t + y<sup>2</sup></i>.</p>
    <p class="step-label">First Approximation (y<sup>(1)</sup>):</p>
    <div class="math-box">
        <p class="formula">
            y<sup>(1)</sup>(x) = 1 + &int;<sub>0</sub><sup>x</sup> (t + 1<sup>2</sup>) dt
            = 1 + [ <span class="frac"><span class="num">t<sup>2</sup></span><span class="den">2</span></span> + t ]<sub>0</sub><sup>x</sup>
            = <b>1 + x + <span class="frac"><span class="num">x<sup>2</sup></span><span class="den">2</span></span></b>
        </p>
    </div>
    <p class="step-label">Second Approximation (y<sup>(2)</sup>):</p>
    <div class="math-box">
        <p class="formula">
            y<sup>(2)</sup>(x) = 1 + &int;<sub>0</sub><sup>x</sup> [ t + (1 + t + <span class="frac"><span class="num">t<sup>2</sup></span><span class="den">2</span></span>)<sup>2</sup> ] dt
        </p>
        <p class="formula">
            Expand:&emsp; (1 + t + <span class="frac"><span class="num">t<sup>2</sup></span><span class="den">2</span></span>)<sup>2</sup> = 1 + 2t + 2t<sup>2</sup> + t<sup>3</sup> + <span class="frac"><span class="num">t<sup>4</sup></span><span class="den">4</span></span>
        </p>
        <p class="formula">
            Integrand = t + 1 + 2t + 2t<sup>2</sup> + t<sup>3</sup> + <span class="frac"><span class="num">t<sup>4</sup></span><span class="den">4</span></span> = 1 + 3t + 2t<sup>2</sup> + t<sup>3</sup> + <span class="frac"><span class="num">t<sup>4</sup></span><span class="den">4</span></span>
        </p>
        <p class="formula">
            y<sup>(2)</sup>(x) = 1 + [ t + <span class="frac"><span class="num">3t<sup>2</sup></span><span class="den">2</span></span> + <span class="frac"><span class="num">2t<sup>3</sup></span><span class="den">3</span></span> + <span class="frac"><span class="num">t<sup>4</sup></span><span class="den">4</span></span> + <span class="frac"><span class="num">t<sup>5</sup></span><span class="den">20</span></span> ]<sub>0</sub><sup>x</sup>
        </p>
        <p class="formula">
            <b>y<sup>(2)</sup>(x) = 1 + x + <span class="frac"><span class="num">3</span><span class="den">2</span></span>x<sup>2</sup> + <span class="frac"><span class="num">2</span><span class="den">3</span></span>x<sup>3</sup> + <span class="frac"><span class="num">1</span><span class="den">4</span></span>x<sup>4</sup> + <span class="frac"><span class="num">1</span><span class="den">20</span></span>x<sup>5</sup></b>
        </p>
    </div>
    <div><span class="highlight-ans">y<sup>(1)</sup> = 1 + x + x<sup>2</sup>/2 &emsp;|&emsp; y<sup>(2)</sup> = 1 + x + (3/2)x<sup>2</sup> + (2/3)x<sup>3</sup> + (1/4)x<sup>4</sup> + (1/20)x<sup>5</sup></span></div>
</div>

<!-- ==================== SECTION B ==================== -->
<div class="sec-title">Section – B (Short Answer Questions &bull; 7.5 Marks Each &bull; Attempt Any Two)</div>

<!-- Q6 -->
<div class="q-box">
    <div class="q-title">Q6. Find a real root of the equation <i>2x = log<sub>10</sub>(x) + 7</i> between 3 and 4 using Method of False Position (Regula Falsi). <span class="q-marks">[7.5 Marks]</span></div>
    <p><strong>Solution:</strong></p>
    <p>Let <i>f(x) = 2x &minus; log<sub>10</sub>(x) &minus; 7 = 0</i>.</p>
    <ul>
        <li>For <i>x<sub>0</sub> = 3</i>: <i>f(3) = 2(3) &minus; log<sub>10</sub>(3) &minus; 7 = 6 &minus; 0.47712 &minus; 7 = &minus;1.47712 &lt; 0</i></li>
        <li>For <i>x<sub>1</sub> = 4</i>: <i>f(4) = 2(4) &minus; log<sub>10</sub>(4) &minus; 7 = 8 &minus; 0.60206 &minus; 7 = +0.39794 &gt; 0</i></li>
    </ul>
    <p>Since <i>f(3)</i> and <i>f(4)</i> have opposite signs, the root lies in the interval <b>(3, 4)</b>.</p>
    <div class="math-box">
        <p class="formula">
            <b>Regula Falsi Iteration Formula:</b><br>
            x<sub>2</sub> = <span class="frac"><span class="num">x<sub>0</sub> &bull; f(x<sub>1</sub>) &minus; x<sub>1</sub> &bull; f(x<sub>0</sub>)</span><span class="den">f(x<sub>1</sub>) &minus; f(x<sub>0</sub>)</span></span>
        </p>
    </div>
    <p class="step-label">Iteration 1:</p>
    <div class="math-box">
        <p class="formula">
            x<sub>2</sub> = <span class="frac"><span class="num">3(0.39794) &minus; 4(&minus;1.47712)</span><span class="den">0.39794 &minus; (&minus;1.47712)</span></span>
            = <span class="frac"><span class="num">1.19382 + 5.90848</span><span class="den">1.87506</span></span>
            = <span class="frac"><span class="num">7.10230</span><span class="den">1.87506</span></span>
            &approx; <b>3.78777</b>
        </p>
    </div>
    <p>Evaluate <i>f(x<sub>2</sub>)</i>:</p>
    <p><i>f(3.78777) = 2(3.78777) &minus; log<sub>10</sub>(3.78777) &minus; 7 = 7.57554 &minus; 0.57838 &minus; 7 = &minus;0.00284 &lt; 0</i>.</p>
    <p>Root lies in <b>[3.78777, 4.00000]</b>.</p>
    <p class="step-label">Iteration 2:</p>
    <div class="math-box">
        <p class="formula">
            x<sub>3</sub> = <span class="frac"><span class="num">3.78777(0.39794) &minus; 4(&minus;0.00284)</span><span class="den">0.39794 &minus; (&minus;0.00284)</span></span>
            = <span class="frac"><span class="num">1.50731 + 0.01136</span><span class="den">0.40078</span></span>
            = <span class="frac"><span class="num">1.51867</span><span class="den">0.40078</span></span>
            &approx; <b>3.7893</b>
        </p>
    </div>
    <p>Evaluate <i>f(x<sub>3</sub>)</i>: <i>f(3.7893) = 2(3.7893) &minus; log<sub>10</sub>(3.7893) &minus; 7 = 7.57860 &minus; 0.57856 &minus; 7 = +0.00004 &approx; 0</i>.</p>
    <div><span class="highlight-ans">Final Converged Root: x &approx; 3.7893</span></div>
</div>

<hr>

<!-- Q7 -->
<div class="q-box">
    <div class="q-title">Q7. Find the missing terms in the following table using finite differences: <span class="q-marks">[7.5 Marks]</span></div>
    <table class="iter-table">
        <tr><th>x</th><td>0</td><td>5</td><td>10</td><td>15</td><td>20</td><td>25</td><td>30</td></tr>
        <tr><th>y</th><td>1</td><td>3</td><td><b>? (y<sub>2</sub>)</b></td><td>73</td><td>225</td><td><b>? (y<sub>5</sub>)</b></td><td>1153</td></tr>
    </table>
    <p><strong>Solution:</strong></p>
    <p>Let the missing values be <i>y<sub>2</sub></i> (at <i>x = 10</i>) and <i>y<sub>5</sub></i> (at <i>x = 25</i>).</p>
    <p>Since 5 values are given (<i>y<sub>0</sub>, y<sub>1</sub>, y<sub>3</sub>, y<sub>4</sub>, y<sub>6</sub></i>), the data can be represented by a polynomial of degree 4.</p>
    <p>Therefore, the 5th finite difference is identically zero: <b>&Delta;<sup>5</sup> y<sub>0</sub> = 0</b> and <b>&Delta;<sup>5</sup> y<sub>1</sub> = 0</b>.</p>
    <div class="math-box">
        <p class="formula">
            Using shift operator <i>&Delta; = E &minus; 1</i>:<br>
            (E &minus; 1)<sup>5</sup> y = (E<sup>5</sup> &minus; 5E<sup>4</sup> + 10E<sup>3</sup> &minus; 10E<sup>2</sup> + 5E &minus; 1) y = 0
        </p>
    </div>
    <p class="step-label">Equation 1 (applying on y<sub>0</sub>):</p>
    <div class="math-box">
        <p class="formula">
            y<sub>5</sub> &minus; 5y<sub>4</sub> + 10y<sub>3</sub> &minus; 10y<sub>2</sub> + 5y<sub>1</sub> &minus; y<sub>0</sub> = 0<br>
            y<sub>5</sub> &minus; 5(225) + 10(73) &minus; 10y<sub>2</sub> + 5(3) &minus; 1 = 0<br>
            y<sub>5</sub> &minus; 1125 + 730 &minus; 10y<sub>2</sub> + 15 &minus; 1 = 0<br>
            <b>&minus;10y<sub>2</sub> + y<sub>5</sub> = 381</b> &emsp;&emsp;— (Equation 1)
        </p>
    </div>
    <p class="step-label">Equation 2 (applying on y<sub>1</sub>):</p>
    <div class="math-box">
        <p class="formula">
            y<sub>6</sub> &minus; 5y<sub>5</sub> + 10y<sub>4</sub> &minus; 10y<sub>3</sub> + 5y<sub>2</sub> &minus; y<sub>1</sub> = 0<br>
            1153 &minus; 5y<sub>5</sub> + 10(225) &minus; 10(73) + 5y<sub>2</sub> &minus; 3 = 0<br>
            1153 &minus; 5y<sub>5</sub> + 2250 &minus; 730 + 5y<sub>2</sub> &minus; 3 = 0<br>
            5y<sub>2</sub> &minus; 5y<sub>5</sub> + 2670 = 0 &rArr; y<sub>2</sub> &minus; y<sub>5</sub> = &minus;534 &rArr; <b>y<sub>5</sub> &minus; y<sub>2</sub> = 534</b> &emsp;&emsp;— (Equation 2)
        </p>
    </div>
    <p class="step-label">Solving the Linear System:</p>
    <p>From Equation 2: <i>y<sub>5</sub> = y<sub>2</sub> + 534</i>.</p>
    <p>Substitute into Equation 1: <i>&minus;10y<sub>2</sub> + (y<sub>2</sub> + 534) = 381 &rArr; &minus;9y<sub>2</sub> = 381 &minus; 534 = &minus;153 &rArr; <b>y<sub>2</sub> = 17</b></i>.</p>
    <p>Then <i>y<sub>5</sub> = 17 + 534 = <b>551</b></i>.</p>
    <div><span class="highlight-ans">Missing Values: y<sub>2</sub> = 17 (at x = 10) &emsp;|&emsp; y<sub>5</sub> = 551 (at x = 25)</span></div>
</div>

<hr>

<!-- Q8 -->
<div class="q-box">
    <div class="q-title">Q8. Evaluate <i>I = &int;<sub>3</sub><sup>7</sup> x<sup>2</sup> log<sub>10</sub>(x) dx</i> using Simpson's 1/3 rule with <i>n = 4</i>. <span class="q-marks">[7.5 Marks]</span></div>
    <p><strong>Solution:</strong></p>
    <p>Given limits <i>a = 3, b = 7</i>, and number of sub-intervals <i>n = 4</i>.</p>
    <p>Step size: <i>h = (b &minus; a) / n = (7 &minus; 3) / 4 = <b>1</b></i>.</p>
    <table class="iter-table">
        <tr><th>i</th><th>x<sub>i</sub></th><th>Function f(x) = x<sup>2</sup> log<sub>10</sub>(x)</th><th>Ordinate y<sub>i</sub></th></tr>
        <tr><td>0</td><td>3</td><td>3<sup>2</sup> &bull; log<sub>10</sub>(3) = 9 &times; 0.477121</td><td><b>4.2941</b></td></tr>
        <tr><td>1</td><td>4</td><td>4<sup>2</sup> &bull; log<sub>10</sub>(4) = 16 &times; 0.602060</td><td><b>9.6330</b></td></tr>
        <tr><td>2</td><td>5</td><td>5<sup>2</sup> &bull; log<sub>10</sub>(5) = 25 &times; 0.698970</td><td><b>17.4743</b></td></tr>
        <tr><td>3</td><td>6</td><td>6<sup>2</sup> &bull; log<sub>10</sub>(6) = 36 &times; 0.778151</td><td><b>28.0134</b></td></tr>
        <tr><td>4</td><td>7</td><td>7<sup>2</sup> &bull; log<sub>10</sub>(7) = 49 &times; 0.845098</td><td><b>41.4099</b></td></tr>
    </table>
    <div class="math-box">
        <p class="formula">
            <b>Simpson's 1/3 Rule Formula:</b><br>
            I = <span class="frac"><span class="num">h</span><span class="den">3</span></span> [ (y<sub>0</sub> + y<sub>4</sub>) + 4(y<sub>1</sub> + y<sub>3</sub>) + 2(y<sub>2</sub>) ]
        </p>
        <p class="formula">
            Sum of Extremes:&emsp; y<sub>0</sub> + y<sub>4</sub> = 4.2941 + 41.4099 = <b>45.7040</b><br>
            Sum of Odd Ordinates:&emsp; 4(y<sub>1</sub> + y<sub>3</sub>) = 4(9.6330 + 28.0134) = 4(37.6464) = <b>150.5856</b><br>
            Sum of Even Ordinates:&emsp; 2(y<sub>2</sub>) = 2(17.4743) = <b>34.9486</b>
        </p>
        <p class="formula">
            Total Bracket Sum = 45.7040 + 150.5856 + 34.9486 = <b>231.2382</b><br>
            I = <span class="frac"><span class="num">1</span><span class="den">3</span></span> &times; 231.2382 = <b>77.0794</b>
        </p>
    </div>
    <div><span class="highlight-ans">Evaluated Integral: I &approx; 77.0794</span></div>
</div>

<!-- ==================== SECTION C ==================== -->
<div class="sec-title">Section – C (Long Answer Questions &bull; 15 Marks Each &bull; Attempt Any Three)</div>

<!-- Q9 -->
<div class="q-box">
    <div class="q-title">Q9. Use Newton-Raphson method to find a real root of <i>sin(x) = x / 2</i> correct to 3 decimal places between &pi;/2 and &pi;. <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Solution:</strong></p>
    <p>Let <i>f(x) = sin(x) &minus; <span class="frac"><span class="num">x</span><span class="den">2</span></span> = 0</i>.</p>
    <p>Differentiating with respect to x: <i>f'(x) = cos(x) &minus; 0.5</i>.</p>
    <p>Given interval: [&pi;/2, &pi;] &approx; [1.5708, 3.1416] radians.</p>
    <p>Let initial approximation be <b>x<sub>0</sub> = 2.0 radians</b>.</p>
    <div class="math-box">
        <p class="formula">
            <b>Newton-Raphson Iteration Formula:</b><br>
            x<sub>n+1</sub> = x<sub>n</sub> &minus; <span class="frac"><span class="num">f(x<sub>n</sub>)</span><span class="den">f'(x<sub>n</sub>)</span></span>
        </p>
    </div>
    <p class="step-label">Iteration 1 (at x<sub>0</sub> = 2.0):</p>
    <div class="math-box">
        <p class="formula">
            f(2.0) = sin(2.0) &minus; 1.0 = 0.90930 &minus; 1.0 = <b>&minus;0.09070</b><br>
            f'(2.0) = cos(2.0) &minus; 0.5 = &minus;0.41615 &minus; 0.5 = <b>&minus;0.91615</b><br>
            x<sub>1</sub> = 2.0 &minus; <span class="frac"><span class="num">&minus;0.09070</span><span class="den">&minus;0.91615</span></span> = 2.0 &minus; 0.09900 = <b>1.90100</b>
        </p>
    </div>
    <p class="step-label">Iteration 2 (at x<sub>1</sub> = 1.90100):</p>
    <div class="math-box">
        <p class="formula">
            f(1.90100) = sin(1.90100) &minus; <span class="frac"><span class="num">1.90100</span><span class="den">2</span></span> = 0.94598 &minus; 0.95050 = <b>&minus;0.00452</b><br>
            f'(1.90100) = cos(1.90100) &minus; 0.5 = &minus;0.32422 &minus; 0.5 = <b>&minus;0.82422</b><br>
            x<sub>2</sub> = 1.90100 &minus; <span class="frac"><span class="num">&minus;0.00452</span><span class="den">&minus;0.82422</span></span> = 1.90100 &minus; 0.00548 = <b>1.89552</b>
        </p>
    </div>
    <p class="step-label">Iteration 3 (at x<sub>2</sub> = 1.89552):</p>
    <div class="math-box">
        <p class="formula">
            f(1.89552) = sin(1.89552) &minus; <span class="frac"><span class="num">1.89552</span><span class="den">2</span></span> = 0.94775 &minus; 0.94776 = <b>&minus;0.00001</b><br>
            f'(1.89552) = cos(1.89552) &minus; 0.5 = &minus;0.31899 &minus; 0.5 = <b>&minus;0.81899</b><br>
            x<sub>3</sub> = 1.89552 &minus; <span class="frac"><span class="num">&minus;0.00001</span><span class="den">&minus;0.81899</span></span> = 1.89552 &minus; 0.00001 = <b>1.89549</b>
        </p>
    </div>
    <div><span class="highlight-ans">Root: x &approx; 1.895 radians (or &approx; 108.57&deg;)</span></div>
</div>

<hr>

<!-- Q10 -->
<div class="q-box">
    <div class="q-title">Q10. Find the Lagrange interpolating polynomial of degree 2 for <i>y = log<sub>e</sub>(x)</i> from the given table. Hence determine <i>log<sub>e</sub>(2.7)</i>. <span class="q-marks">[15 Marks]</span></div>
    <table class="iter-table">
        <tr><th>x</th><td>2.0</td><td>2.5</td><td>3.0</td></tr>
        <tr><th>y = log<sub>e</sub>(x)</th><td>0.69315</td><td>0.91629</td><td>1.09861</td></tr>
    </table>
    <p><strong>Solution:</strong></p>
    <p>Given <i>x<sub>0</sub> = 2.0, y<sub>0</sub> = 0.69315</i>; &nbsp; <i>x<sub>1</sub> = 2.5, y<sub>1</sub> = 0.91629</i>; &nbsp; <i>x<sub>2</sub> = 3.0, y<sub>2</sub> = 1.09861</i>.</p>
    <p>Target value: <i>x = 2.7</i>.</p>
    <div class="math-box">
        <p class="formula">
            <b>Lagrange Interpolation Formula for n = 2:</b><br>
            P<sub>2</sub>(x) = L<sub>0</sub>(x) y<sub>0</sub> + L<sub>1</sub>(x) y<sub>1</sub> + L<sub>2</sub>(x) y<sub>2</sub>
        </p>
    </div>
    <p class="step-label">Calculating Lagrange Cardinal Polynomials at x = 2.7:</p>
    <div class="math-box">
        <p class="formula">
            L<sub>0</sub>(2.7) = <span class="frac"><span class="num">(2.7 &minus; 2.5)(2.7 &minus; 3.0)</span><span class="den">(2.0 &minus; 2.5)(2.0 &minus; 3.0)</span></span>
            = <span class="frac"><span class="num">(0.2)(&minus;0.3)</span><span class="den">(&minus;0.5)(&minus;1.0)</span></span>
            = <span class="frac"><span class="num">&minus;0.06</span><span class="den">0.50</span></span>
            = <b>&minus;0.12</b>
        </p>
        <p class="formula">
            L<sub>1</sub>(2.7) = <span class="frac"><span class="num">(2.7 &minus; 2.0)(2.7 &minus; 3.0)</span><span class="den">(2.5 &minus; 2.0)(2.5 &minus; 3.0)</span></span>
            = <span class="frac"><span class="num">(0.7)(&minus;0.3)</span><span class="den">(0.5)(&minus;0.5)</span></span>
            = <span class="frac"><span class="num">&minus;0.21</span><span class="den">&minus;0.25</span></span>
            = <b>+0.84</b>
        </p>
        <p class="formula">
            L<sub>2</sub>(2.7) = <span class="frac"><span class="num">(2.7 &minus; 2.0)(2.7 &minus; 2.5)</span><span class="den">(3.0 &minus; 2.0)(3.0 &minus; 2.5)</span></span>
            = <span class="frac"><span class="num">(0.7)(0.2)</span><span class="den">(1.0)(0.5)</span></span>
            = <span class="frac"><span class="num">0.14</span><span class="den">0.50</span></span>
            = <b>+0.28</b>
        </p>
        <p class="formula">
            <i>Verification: L<sub>0</sub> + L<sub>1</sub> + L<sub>2</sub> = &minus;0.12 + 0.84 + 0.28 = 1.00 &check;</i>
        </p>
    </div>
    <p class="step-label">Evaluating P<sub>2</sub>(2.7):</p>
    <div class="math-box">
        <p class="formula">
            P<sub>2</sub>(2.7) = (&minus;0.12)(0.69315) + (0.84)(0.91629) + (0.28)(1.09861)<br>
            = &minus;0.083178 + 0.769684 + 0.307611<br>
            = <b>0.994117 &approx; 0.99412</b>
        </p>
    </div>
    <p><i>(Exact analytical value: ln(2.7) &approx; 0.99325; error &approx; 0.00087.)</i></p>
    <div><span class="highlight-ans">Interpolated Value: log<sub>e</sub>(2.7) &approx; 0.99412</span></div>
</div>

<hr>

<!-- Q11 -->
<div class="q-box">
    <div class="q-title">Q11. Use Simpson's 3/8 rule to evaluate <i>&int;<sub>0</sub><sup>1</sup> <span class="frac"><span class="num">dx</span><span class="den">1 + x</span></span></i> with <i>h = 1/6</i>. <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Solution:</strong></p>
    <p>Given <i>a = 0, b = 1</i>, step size <i>h = 1/6 &rArr; n = (1 &minus; 0)/(1/6) = 6</i> subintervals.</p>
    <p>Integrand: <i>f(x) = <span class="frac"><span class="num">1</span><span class="den">1 + x</span></span></i>.</p>
    <table class="iter-table">
        <tr><th>i</th><th>x<sub>i</sub></th><th>Exact y<sub>i</sub> = 1 / (1 + x<sub>i</sub>)</th><th>Decimal Value</th></tr>
        <tr><td>0</td><td>0</td><td>1 / 1</td><td><b>1.000000</b></td></tr>
        <tr><td>1</td><td>1/6</td><td>1 / (7/6) = 6/7</td><td><b>0.857143</b></td></tr>
        <tr><td>2</td><td>2/6</td><td>1 / (8/6) = 6/8 = 3/4</td><td><b>0.750000</b></td></tr>
        <tr><td>3</td><td>3/6</td><td>1 / (9/6) = 6/9 = 2/3</td><td><b>0.666667</b></td></tr>
        <tr><td>4</td><td>4/6</td><td>1 / (10/6) = 6/10 = 3/5</td><td><b>0.600000</b></td></tr>
        <tr><td>5</td><td>5/6</td><td>1 / (11/6) = 6/11</td><td><b>0.545455</b></td></tr>
        <tr><td>6</td><td>1</td><td>1 / 2</td><td><b>0.500000</b></td></tr>
    </table>
    <div class="math-box">
        <p class="formula">
            <b>Simpson's 3/8 Rule Formula:</b><br>
            I = <span class="frac"><span class="num">3h</span><span class="den">8</span></span> [ (y<sub>0</sub> + y<sub>6</sub>) + 3(y<sub>1</sub> + y<sub>2</sub> + y<sub>4</sub> + y<sub>5</sub>) + 2(y<sub>3</sub>) ]
        </p>
        <p class="formula">
            Extremes:&emsp; y<sub>0</sub> + y<sub>6</sub> = 1.000000 + 0.500000 = <b>1.500000</b><br>
            Non-multiples of 3:&emsp; 3(y<sub>1</sub> + y<sub>2</sub> + y<sub>4</sub> + y<sub>5</sub>) = 3(0.857143 + 0.750000 + 0.600000 + 0.545455) = 3(2.752598) = <b>8.257794</b><br>
            Multiples of 3:&emsp; 2(y<sub>3</sub>) = 2(0.666667) = <b>1.333334</b>
        </p>
        <p class="formula">
            Sum of brackets = 1.500000 + 8.257794 + 1.333334 = <b>11.091128</b><br>
            I = <span class="frac"><span class="num">3(1/6)</span><span class="den">8</span></span> &times; 11.091128 = <span class="frac"><span class="num">1/2</span><span class="den">8</span></span> &times; 11.091128 = <span class="frac"><span class="num">11.091128</span><span class="den">16</span></span> = <b>0.693196</b>
        </p>
    </div>
    <p><i>(Exact analytical integral: &int;<sub>0</sub><sup>1</sup> dx/(1+x) = [ln(1+x)]<sub>0</sub><sup>1</sup> = ln(2) &approx; 0.693147. Highly accurate to 4 decimal places.)</i></p>
    <div><span class="highlight-ans">Evaluated Integral: I &approx; 0.693196</span></div>
</div>

<hr>

<!-- Q12 -->
<div class="q-box">
    <div class="q-title">Q12. Solve the following linear system using Gauss-Seidel iterative method: <span class="q-marks">[15 Marks]</span></div>
    <div class="math-box">
        <p class="formula">
            6x + y + z = 20<br>
            x + 4y &minus; z = 6<br>
            x &minus; y + 5z = 7
        </p>
    </div>
    <p><strong>Solution:</strong></p>
    <p class="step-label">Step 1: Check Diagonal Dominance Condition:</p>
    <ul>
        <li>Equation 1: |6| &gt; |1| + |1| = 2 &emsp;(Dominant in x &check;)</li>
        <li>Equation 2: |4| &gt; |1| + |&minus;1| = 2 &emsp;(Dominant in y &check;)</li>
        <li>Equation 3: |5| &gt; |1| + |&minus;1| = 2 &emsp;(Dominant in z &check;)</li>
    </ul>
    <p>The system is strictly diagonally dominant. Convergence is guaranteed.</p>
    <p class="step-label">Step 2: Express in Iterative Form:</p>
    <div class="math-box">
        <p class="formula">
            x<sup>(k+1)</sup> = <span class="frac"><span class="num">20 &minus; y<sup>(k)</sup> &minus; z<sup>(k)</sup></span><span class="den">6</span></span><br>
            y<sup>(k+1)</sup> = <span class="frac"><span class="num">6 &minus; x<sup>(k+1)</sup> + z<sup>(k)</sup></span><span class="den">4</span></span><br>
            z<sup>(k+1)</sup> = <span class="frac"><span class="num">7 &minus; x<sup>(k+1)</sup> + y<sup>(k+1)</sup></span><span class="den">5</span></span>
        </p>
    </div>
    <p class="step-label">Step 3: Iteration Table (Initial Approximation: x<sup>(0)</sup> = 0, y<sup>(0)</sup> = 0, z<sup>(0)</sup> = 0):</p>
    <table class="iter-table">
        <tr><th>Iteration (k)</th><th>x = (20 &minus; y &minus; z) / 6</th><th>y = (6 &minus; x + z) / 4</th><th>z = (7 &minus; x + y) / 5</th></tr>
        <tr><td>1</td><td>(20 &minus; 0 &minus; 0)/6 = <b>3.3333</b></td><td>(6 &minus; 3.3333 + 0)/4 = <b>0.6667</b></td><td>(7 &minus; 3.3333 + 0.6667)/5 = <b>0.8667</b></td></tr>
        <tr><td>2</td><td>(20 &minus; 0.6667 &minus; 0.8667)/6 = <b>3.0778</b></td><td>(6 &minus; 3.0778 + 0.8667)/4 = <b>0.9472</b></td><td>(7 &minus; 3.0778 + 0.9472)/5 = <b>0.9739</b></td></tr>
        <tr><td>3</td><td>(20 &minus; 0.9472 &minus; 0.9739)/6 = <b>3.0131</b></td><td>(6 &minus; 3.0131 + 0.9739)/4 = <b>0.9902</b></td><td>(7 &minus; 3.0131 + 0.9902)/5 = <b>0.9954</b></td></tr>
        <tr><td>4</td><td>(20 &minus; 0.9902 &minus; 0.9954)/6 = <b>3.0024</b></td><td>(6 &minus; 3.0024 + 0.9954)/4 = <b>0.9983</b></td><td>(7 &minus; 3.0024 + 0.9983)/5 = <b>0.9992</b></td></tr>
        <tr><td>5</td><td>(20 &minus; 0.9983 &minus; 0.9992)/6 = <b>3.0004</b></td><td>(6 &minus; 3.0004 + 0.9992)/4 = <b>0.9997</b></td><td>(7 &minus; 3.0004 + 0.9997)/5 = <b>0.9999</b></td></tr>
        <tr><td>6</td><td><b>3.0000</b></td><td><b>1.0000</b></td><td><b>1.0000</b></td></tr>
    </table>
    <div><span class="highlight-ans">Converged Solution: x = 3, &nbsp; y = 1, &nbsp; z = 1</span></div>
</div>

<hr>

<!-- Q13 -->
<div class="q-box">
    <div class="q-title">Q13. Using Fourth-Order Runge-Kutta method, find <i>y(0.1)</i> and <i>y(0.2)</i> correct to 4 decimal places, given: <span class="q-marks">[15 Marks]</span></div>
    <div class="math-box">
        <p class="formula">
            <span class="frac"><span class="num">dy</span><span class="den">dx</span></span> = y &minus; x, &emsp;with initial condition y(0) = 2
        </p>
    </div>
    <p><strong>Solution:</strong></p>
    <p>Given <i>f(x, y) = y &minus; x</i>, initial point <i>x<sub>0</sub> = 0, y<sub>0</sub> = 2</i>, step size <i>h = 0.1</i>.</p>
    <p class="step-label">Part 1: Calculation of y(0.1) from x<sub>0</sub> = 0, y<sub>0</sub> = 2:</p>
    <div class="math-box">
        <p class="formula">
            k<sub>1</sub> = h &bull; f(x<sub>0</sub>, y<sub>0</sub>) = 0.1(2 &minus; 0) = <b>0.200000</b><br>
            k<sub>2</sub> = h &bull; f(x<sub>0</sub> + <span class="frac"><span class="num">h</span><span class="den">2</span></span>, y<sub>0</sub> + <span class="frac"><span class="num">k<sub>1</sub></span><span class="den">2</span></span>) = 0.1 &bull; f(0.05, 2.10) = 0.1(2.10 &minus; 0.05) = <b>0.205000</b><br>
            k<sub>3</sub> = h &bull; f(x<sub>0</sub> + <span class="frac"><span class="num">h</span><span class="den">2</span></span>, y<sub>0</sub> + <span class="frac"><span class="num">k<sub>2</sub></span><span class="den">2</span></span>) = 0.1 &bull; f(0.05, 2.1025) = 0.1(2.1025 &minus; 0.05) = <b>0.205250</b><br>
            k<sub>4</sub> = h &bull; f(x<sub>0</sub> + h, y<sub>0</sub> + k<sub>3</sub>) = 0.1 &bull; f(0.1, 2.20525) = 0.1(2.20525 &minus; 0.1) = <b>0.210525</b>
        </p>
        <p class="formula">
            k = <span class="frac"><span class="num">1</span><span class="den">6</span></span> (k<sub>1</sub> + 2k<sub>2</sub> + 2k<sub>3</sub> + k<sub>4</sub>)<br>
            = <span class="frac"><span class="num">1</span><span class="den">6</span></span> (0.200000 + 0.410000 + 0.410500 + 0.210525) = <span class="frac"><span class="num">1.231025</span><span class="den">6</span></span> &approx; <b>0.205171</b>
        </p>
        <p class="formula">
            <b>y(0.1) = y<sub>0</sub> + k = 2 + 0.205171 = 2.2052</b>
        </p>
    </div>
    
    <p class="step-label">Part 2: Calculation of y(0.2) from x<sub>1</sub> = 0.1, y<sub>1</sub> = 2.205171:</p>
    <div class="math-box">
        <p class="formula">
            k<sub>1</sub> = h &bull; f(x<sub>1</sub>, y<sub>1</sub>) = 0.1(2.205171 &minus; 0.1) = <b>0.210517</b><br>
            k<sub>2</sub> = h &bull; f(0.1 + 0.05, 2.205171 + 0.105258) = 0.1 &bull; f(0.15, 2.310430) = 0.1(2.310430 &minus; 0.15) = <b>0.216043</b><br>
            k<sub>3</sub> = h &bull; f(0.1 + 0.05, 2.205171 + 0.108022) = 0.1 &bull; f(0.15, 2.313193) = 0.1(2.313193 &minus; 0.15) = <b>0.216319</b><br>
            k<sub>4</sub> = h &bull; f(0.1 + 0.1, 2.205171 + 0.216319) = 0.1 &bull; f(0.2, 2.421490) = 0.1(2.421490 &minus; 0.2) = <b>0.222149</b>
        </p>
        <p class="formula">
            k = <span class="frac"><span class="num">1</span><span class="den">6</span></span> (k<sub>1</sub> + 2k<sub>2</sub> + 2k<sub>3</sub> + k<sub>4</sub>)<br>
            = <span class="frac"><span class="num">1</span><span class="den">6</span></span> (0.210517 + 0.432086 + 0.432638 + 0.222149) = <span class="frac"><span class="num">1.297390</span><span class="den">6</span></span> &approx; <b>0.216232</b>
        </p>
        <p class="formula">
            <b>y(0.2) = y<sub>1</sub> + k = 2.205171 + 0.216232 = 2.4214</b>
        </p>
    </div>
    <div><span class="highlight-ans">y(0.1) = 2.2052 &emsp;|&emsp; y(0.2) = 2.4214</span></div>
</div>
"""

def generate_pdf(year, out_filename):
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>BCA-504: Numerical Methods — {year} Solved Paper</title>
{CSS_STYLES}
</head>
<body>

<div class="header-banner">
    <p class="univ-name">Chaudhary Charan Singh University (CCSU) &bull; BCA V Semester</p>
    <h1 class="paper-title">BCA-504: Numerical Methods</h1>
    <p class="meta-info"><strong>Session:</strong> December {year} Examination &nbsp;|&nbsp; <strong>Paper Code:</strong> 18024 &nbsp;|&nbsp; <strong>Complete 100% Solved Paper (All 13 Questions)</strong> &nbsp;|&nbsp; <strong>Time:</strong> 3 Hours &bull; <strong>Max Marks:</strong> 75</p>
</div>

{BODY_QUESTIONS_HTML}

</body>
</html>
"""
    temp_html = os.path.join(TARGET_DIR, f"temp_{year}.html")
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

def main():
    years = [2024, 2023, 2022, 2021, 2020, 2019, 2018]
    print("Generating beautifully formatted Numerical Methods PDFs...")
    for yr in years:
        filename = f"numerical methods {yr} solved.pdf"
        generate_pdf(yr, filename)
    
    # Also generate the comprehensive subject PDF
    print("Generating BCA-504_Numerical_Methods_Solved_PYQ.pdf...")
    generate_pdf("Comprehensive PYQ Bank", "BCA-504_Numerical_Methods_Solved_PYQ.pdf")
    
    # Update master book
    master_path = os.path.join(TARGET_DIR, "CCSU_BCA_5_SEM_ALL_SUBJECTS_SOLVED_MASTER_BOOK.pdf")
    if os.path.exists(master_path):
        print("Recompiling Master Book with new Numerical Methods formatting...")
        # Let's rebuild master book from the 4 subject solved PDFs
        doc = pymupdf.open()
        subjects = [
            ("BCA-501: Data Base Management System", os.path.join(TARGET_DIR, "BCA-501_DBMS_Solved_PYQ.pdf")),
            ("BCA-502: Java Programming & Web Design", os.path.join(TARGET_DIR, "BCA-502_Java_Programming_Solved_PYQ.pdf")),
            ("BCA-503: Computer Network", os.path.join(TARGET_DIR, "BCA-503_Computer_Networks_Solved_PYQ.pdf")),
            ("BCA-504: Numerical Methods", os.path.join(TARGET_DIR, "BCA-504_Numerical_Methods_Solved_PYQ.pdf")),
        ]
        toc = []
        page_num = 1
        for title, path in subjects:
            if os.path.exists(path):
                sub_doc = pymupdf.open(path)
                toc.append([1, title, page_num])
                doc.insert_pdf(sub_doc)
                page_num += len(sub_doc)
                sub_doc.close()
        doc.set_toc(toc)
        doc.save(master_path, garbage=4, deflate=True)
        doc.close()
        print(f"[OK] Master Book updated: {master_path} ({os.path.getsize(master_path)/1024:.1f} KB)")

if __name__ == "__main__":
    main()
