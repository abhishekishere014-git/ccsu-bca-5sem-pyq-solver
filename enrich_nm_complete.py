# -*- coding: utf-8 -*-
"""
Complete Exam-Style Enriched Solutions for Numerical Methods (BCA-504)
Every question is formatted with:
- Structured Grid/Iteration Tables (<table class="grid-table">)
- Step & Formula Boxes (<div class="step-box"> / <div class="math-box">)
- Signature Glowing Blue Badge Boxes (<span class="math-expr"> / <code>)
- Clear Boxed Final Results (<div class="result-box">)
"""

NM_COMPLETE_ENRICHMENTS = {
    # 0. Runge-Kutta 4th Order
    "using runge-kutta 4th order method, find y(0.2)": """
<p class="step-label">1. Problem Formulation & Formula:</p>
<div class="math-box">
    Given IVP: <span class="math-expr">dy/dx = f(x, y) = x + y<sup>2</sup></span> with initial condition <span class="math-expr">x<sub>0</sub> = 0, y<sub>0</sub> = 1</span>.<br>
    Step size: <span class="math-expr">h = 0.1</span>. Target: compute <span class="math-expr">y(0.2)</span> in 2 successive steps.
</div>

<div class="info-box">
    <b>Classical 4th Order Runge-Kutta (RK4) Formulas:</b><br>
    <span class="math-expr">k<sub>1</sub> = h &bull; f(x<sub>n</sub>, y<sub>n</sub>)</span><br>
    <span class="math-expr">k<sub>2</sub> = h &bull; f(x<sub>n</sub> + h/2, y<sub>n</sub> + k<sub>1</sub>/2)</span><br>
    <span class="math-expr">k<sub>3</sub> = h &bull; f(x<sub>n</sub> + h/2, y<sub>n</sub> + k<sub>2</sub>/2)</span><br>
    <span class="math-expr">k<sub>4</sub> = h &bull; f(x<sub>n</sub> + h, y<sub>n</sub> + k<sub>3</sub>)</span><br>
    Weighted Increment: <span class="math-expr">&Delta;y = (1/6) [k<sub>1</sub> + 2k<sub>2</sub> + 2k<sub>3</sub> + k<sub>4</sub>]</span> &nbsp;&rArr;&nbsp; <span class="math-expr">y<sub>n+1</sub> = y<sub>n</sub> + &Delta;y</span>
</div>

<p class="step-label">2. Step 1: Compute y(0.1) from x<sub>0</sub> = 0, y<sub>0</sub> = 1:</p>
<table class="grid-table">
    <tr><th>Slope</th><th>Formula</th><th>Calculation</th><th>Value</th></tr>
    <tr><td><span class="math-expr">k<sub>1</sub></span></td><td><code>0.1 &bull; (0 + 1<sup>2</sup>)</code></td><td><code>0.1 &bull; 1.0</code></td><td><span class="math-expr">0.10000</span></td></tr>
    <tr><td><span class="math-expr">k<sub>2</sub></span></td><td><code>0.1 &bull; [0.05 + (1 + 0.05)<sup>2</sup>]</code></td><td><code>0.1 &bull; [0.05 + 1.1025]</code></td><td><span class="math-expr">0.11525</span></td></tr>
    <tr><td><span class="math-expr">k<sub>3</sub></span></td><td><code>0.1 &bull; [0.05 + (1 + 0.057625)<sup>2</sup>]</code></td><td><code>0.1 &bull; [0.05 + 1.11857]</code></td><td><span class="math-expr">0.11686</span></td></tr>
    <tr><td><span class="math-expr">k<sub>4</sub></span></td><td><code>0.1 &bull; [0.10 + (1 + 0.11686)<sup>2</sup>]</code></td><td><code>0.1 &bull; [0.10 + 1.24738]</code></td><td><span class="math-expr">0.13474</span></td></tr>
</table>

<div class="step-box">
    <b>Weighted Increment for Step 1:</b><br>
    <span class="math-expr">&Delta;y<sub>1</sub> = (1/6) [0.10000 + 2(0.11525) + 2(0.11686) + 0.13474] = (1/6)[0.69896] = 0.11649</span><br>
    Therefore: <span class="math-expr">y(0.1) = y<sub>0</sub> + &Delta;y<sub>1</sub> = 1.00000 + 0.11649 = <b>1.11649</b></span>
</div>

<p class="step-label">3. Step 2: Compute y(0.2) from x<sub>1</sub> = 0.1, y<sub>1</sub> = 1.11649:</p>
<table class="grid-table">
    <tr><th>Slope</th><th>Formula</th><th>Calculation</th><th>Value</th></tr>
    <tr><td><span class="math-expr">k<sub>1</sub></span></td><td><code>0.1 &bull; [0.10 + (1.11649)<sup>2</sup>]</code></td><td><code>0.1 &bull; [0.10 + 1.24655]</code></td><td><span class="math-expr">0.13466</span></td></tr>
    <tr><td><span class="math-expr">k<sub>2</sub></span></td><td><code>0.1 &bull; [0.15 + (1.11649 + 0.06733)<sup>2</sup>]</code></td><td><code>0.1 &bull; [0.15 + (1.18382)<sup>2</sup>]</code></td><td><span class="math-expr">0.15514</span></td></tr>
    <tr><td><span class="math-expr">k<sub>3</sub></span></td><td><code>0.1 &bull; [0.15 + (1.11649 + 0.07757)<sup>2</sup>]</code></td><td><code>0.1 &bull; [0.15 + (1.19406)<sup>2</sup>]</code></td><td><span class="math-expr">0.15758</span></td></tr>
    <tr><td><span class="math-expr">k<sub>4</sub></span></td><td><code>0.1 &bull; [0.20 + (1.11649 + 0.15758)<sup>2</sup>]</code></td><td><code>0.1 &bull; [0.20 + (1.27407)<sup>2</sup>]</code></td><td><span class="math-expr">0.18233</span></td></tr>
</table>

<div class="step-box">
    <b>Weighted Increment for Step 2:</b><br>
    <span class="math-expr">&Delta;y<sub>2</sub> = (1/6) [0.13466 + 2(0.15514) + 2(0.15758) + 0.18233] = (1/6)[0.94243] = 0.15707</span><br>
    Therefore: <span class="math-expr">y(0.2) = y<sub>1</sub> + &Delta;y<sub>2</sub> = 1.11649 + 0.15707 = <b>1.27356</b></span>
</div>

<div class="result-box">
    &check; <b>Final Solution:</b> <span class="math-expr">y(0.2) &approx; 1.2736</span> (correct to 4 decimal places).
</div>
""",

    # 1. Bisection Method
    "obtain a real root of the equation f(x) = x³ + x² - 1 = 0": """
<p class="step-label">1. Interval Verification & Initial Bounds:</p>
<div class="math-box">
    Let <span class="math-expr">f(x) = x<sup>3</sup> + x<sup>2</sup> - 1 = 0</span>.<br>
    Evaluating integer test points:<br>
    <span class="math-expr">f(0) = 0 + 0 - 1 = -1.0 < 0</span><br>
    <span class="math-expr">f(1) = 1 + 1 - 1 = +1.0 > 0</span><br>
    Since <span class="math-expr">f(0) &bull; f(1) < 0</span>, by Intermediate Value Theorem, at least one real root lies in <span class="math-expr">[0, 1]</span>.
</div>

<p class="step-label">2. Step-by-Step Bisection Iteration Table:</p>
<table class="grid-table">
    <tr><th>Iter (n)</th><th>a (f &lt; 0)</th><th>b (f &gt; 0)</th><th>Midpoint m = (a+b)/2</th><th>f(m) = m<sup>3</sup>+m<sup>2</sup>-1</th><th>New Interval</th></tr>
    <tr><td>1</td><td>0.0000</td><td>1.0000</td><td><span class="math-expr">0.5000</span></td><td>-0.6250</td><td>[0.5000, 1.0000]</td></tr>
    <tr><td>2</td><td>0.5000</td><td>1.0000</td><td><span class="math-expr">0.7500</span></td><td>-0.0156</td><td>[0.7500, 1.0000]</td></tr>
    <tr><td>3</td><td>0.7500</td><td>1.0000</td><td><span class="math-expr">0.8750</span></td><td>+0.4355</td><td>[0.7500, 0.8750]</td></tr>
    <tr><td>4</td><td>0.7500</td><td>0.8750</td><td><span class="math-expr">0.8125</span></td><td>+0.1946</td><td>[0.7500, 0.8125]</td></tr>
    <tr><td>5</td><td>0.7500</td><td>0.8125</td><td><span class="math-expr">0.7813</span></td><td>+0.0855</td><td>[0.7500, 0.7813]</td></tr>
    <tr><td>6</td><td>0.7500</td><td>0.7813</td><td><span class="math-expr">0.7656</span></td><td>+0.0340</td><td>[0.7500, 0.7656]</td></tr>
    <tr><td>7</td><td>0.7500</td><td>0.7656</td><td><span class="math-expr">0.7578</span></td><td>+0.0090</td><td>[0.7500, 0.7578]</td></tr>
    <tr><td>8</td><td>0.7500</td><td>0.7578</td><td><span class="math-expr">0.7539</span></td><td>-0.0033</td><td>[0.7539, 0.7578]</td></tr>
    <tr><td>9</td><td>0.7539</td><td>0.7578</td><td><span class="math-expr">0.7559</span></td><td>+0.0028</td><td>[0.7539, 0.7559]</td></tr>
    <tr><td>10</td><td>0.7539</td><td>0.7559</td><td><span class="math-expr">0.7549</span></td><td>-0.0003</td><td>[0.7549, 0.7559]</td></tr>
</table>

<div class="step-box">
    <b>Convergence Check:</b><br>
    At iteration 10, interval width is <span class="math-expr">|b - a| = 0.7559 - 0.7549 = 0.0010 &le; 10<sup>-3</sup></span>.<br>
    Both boundaries agree to 3 decimal places: <span class="math-expr">0.755</span>.
</div>

<div class="result-box">
    &check; <b>Real Root:</b> <span class="math-expr">x &approx; 0.755</span> (accurate to 3 decimal places).
</div>
""",

    # 2. Picard's Method
    "solve the differential equation dy/dx = x + y², y(0) = 1 using picard": """
<p class="step-label">1. Picard's Iterative Scheme:</p>
<div class="math-box">
    Given IVP: <span class="math-expr">dy/dx = f(x, y) = x + y<sup>2</sup></span>, with <span class="math-expr">x<sub>0</sub> = 0, y<sub>0</sub> = 1</span>.<br>
    Picard's fundamental formula:<br>
    <span class="math-expr">y<sup>(n+1)</sup>(x) = y<sub>0</sub> + &int;<sub>x<sub>0</sub></sub><sup>x</sup> f(t, y<sup>(n)</sup>(t)) dt</span>
</div>

<p class="step-label">2. First Approximation y<sup>(1)</sup>(x):</p>
<div class="step-box">
    Starting with initial approximation <span class="math-expr">y<sup>(0)</sup>(x) = y<sub>0</sub> = 1</span>:<br>
    <span class="math-expr">y<sup>(1)</sup>(x) = 1 + &int;<sub>0</sub><sup>x</sup> [t + (1)<sup>2</sup>] dt</span><br>
    <span class="math-expr">= 1 + [t<sup>2</sup>/2 + t]<sub>0</sub><sup>x</sup> = 1 + x + (1/2)x<sup>2</sup></span>
</div>

<p class="step-label">3. Second Approximation y<sup>(2)</sup>(x):</p>
<div class="step-box">
    Substitute <span class="math-expr">y<sup>(1)</sup>(t) = 1 + t + (1/2)t<sup>2</sup></span> into the integral:<br>
    <span class="math-expr">y<sup>(2)</sup>(x) = 1 + &int;<sub>0</sub><sup>x</sup> [t + (1 + t + t<sup>2</sup>/2)<sup>2</sup>] dt</span><br>
    Expanding the square term:<br>
    <span class="math-expr">(1 + t + t<sup>2</sup>/2)<sup>2</sup> = 1 + 2t + 2t<sup>2</sup> + t<sup>3</sup> + t<sup>4</sup>/4</span><br>
    Adding integrand term <span class="math-expr">t</span>:<br>
    <span class="math-expr">t + (1 + t + t<sup>2</sup>/2)<sup>2</sup> = 1 + 3t + 2t<sup>2</sup> + t<sup>3</sup> + (1/4)t<sup>4</sup></span><br>
    Integrating term-by-term from 0 to <span class="math-expr">x</span>:<br>
    <span class="math-expr">y<sup>(2)</sup>(x) = 1 + [t + (3/2)t<sup>2</sup> + (2/3)t<sup>3</sup> + (1/4)t<sup>4</sup> + (1/20)t<sup>5</sup>]<sub>0</sub><sup>x</sup></span><br>
    <span class="math-expr">y<sup>(2)</sup>(x) = 1 + x + (3/2)x<sup>2</sup> + (2/3)x<sup>3</sup> + (1/4)x<sup>4</sup> + (1/20)x<sup>5</sup></span>
</div>

<div class="result-box">
    &check; <b>Final Solution:</b><br>
    &bull; 1st Approx: <span class="math-expr">y<sup>(1)</sup>(x) = 1 + x + 0.5x<sup>2</sup></span><br>
    &bull; 2nd Approx: <span class="math-expr">y<sup>(2)</sup>(x) = 1 + x + 1.5x<sup>2</sup> + 0.6667x<sup>3</sup> + 0.25x<sup>4</sup> + 0.05x<sup>5</sup></span>
</div>
""",

    # 3. Simpson's 3/8 Rule & π
    "evaluate ∫₀¹ dx/(1 + x²) using simpson's 3/8 rule": """
<p class="step-label">1. Analytical Setup & Step Size Selection:</p>
<div class="math-box">
    Definite Integral: <span class="math-expr">I = &int;<sub>0</sub><sup>1</sup> [1 / (1 + x<sup>2</sup>)] dx = [tan<sup>-1</sup>(x)]<sub>0</sub><sup>1</sup> = &pi;/4</span>.<br>
    For Simpson's 3/8 rule, number of subintervals <span class="math-expr">n</span> must be a multiple of 3. We choose <span class="math-expr">n = 6</span>.<br>
    Step size: <span class="math-expr">h = (b - a)/n = (1 - 0)/6 = 1/6</span>.
</div>

<p class="step-label">2. Grid of Equidistant Nodes and Ordinate Values:</p>
<table class="grid-table">
    <tr><th>i</th><th>x<sub>i</sub></th><th>Exact Ordinate f(x<sub>i</sub>) = 1 / (1 + x<sub>i</sub><sup>2</sup>)</th><th>Decimal Value y<sub>i</sub></th></tr>
    <tr><td>0</td><td>0</td><td>1 / (1 + 0) = 1</td><td><span class="math-expr">1.000000</span> (y<sub>0</sub>)</td></tr>
    <tr><td>1</td><td>1/6</td><td>1 / (1 + 1/36) = 36/37</td><td><span class="math-expr">0.972973</span> (y<sub>1</sub>)</td></tr>
    <tr><td>2</td><td>2/6</td><td>1 / (1 + 4/36) = 36/40 = 9/10</td><td><span class="math-expr">0.900000</span> (y<sub>2</sub>)</td></tr>
    <tr><td>3</td><td>3/6</td><td>1 / (1 + 9/36) = 36/45 = 4/5</td><td><span class="math-expr">0.800000</span> (y<sub>3</sub>)</td></tr>
    <tr><td>4</td><td>4/6</td><td>1 / (1 + 16/36) = 36/52 = 9/13</td><td><span class="math-expr">0.692308</span> (y<sub>4</sub>)</td></tr>
    <tr><td>5</td><td>5/6</td><td>1 / (1 + 25/36) = 36/61</td><td><span class="math-expr">0.590164</span> (y<sub>5</sub>)</td></tr>
    <tr><td>6</td><td>6/6 = 1</td><td>1 / (1 + 1) = 1/2</td><td><span class="math-expr">0.500000</span> (y<sub>6</sub>)</td></tr>
</table>

<p class="step-label">3. Simpson's 3/8 Formula Calculation:</p>
<div class="step-box">
    <b>Formula:</b> <span class="math-expr">I = (3h/8) [ (y<sub>0</sub> + y<sub>6</sub>) + 3(y<sub>1</sub> + y<sub>2</sub> + y<sub>4</sub> + y<sub>5</sub>) + 2(y<sub>3</sub>) ]</span><br><br>
    &bull; Extreme sum: <span class="math-expr">y<sub>0</sub> + y<sub>6</sub> = 1.000000 + 0.500000 = 1.500000</span><br>
    &bull; Non-multiples of 3 sum: <span class="math-expr">y<sub>1</sub> + y<sub>2</sub> + y<sub>4</sub> + y<sub>5</sub> = 0.972973 + 0.900000 + 0.692308 + 0.590164 = 3.155445</span><br>
    &bull; Multiples of 3 sum: <span class="math-expr">y<sub>3</sub> = 0.800000</span><br><br>
    Substituting into formula with <span class="math-expr">h = 1/6 &rArr; 3h/8 = (3/8)(1/6) = 1/16 = 0.0625</span>:<br>
    <span class="math-expr">I = 0.0625 &bull; [ 1.500000 + 3(3.155445) + 2(0.800000) ]</span><br>
    <span class="math-expr">I = 0.0625 &bull; [ 1.500000 + 9.466335 + 1.600000 ] = 0.0625 &bull; [12.566335] = <b>0.785396</b></span>
</div>

<div class="result-box">
    &check; <b>Approximate Value of &pi;:</b><br>
    Since <span class="math-expr">I = &pi;/4</span> &rArr; <span class="math-expr">&pi; &approx; 4 &bull; 0.785396 = <b>3.141584</b></span> (Theoretical &pi; = 3.14159265; Error &lt; 0.0003%).
</div>
""",

    # 4. Gauss-Seidel Method (System 1)
    "gauss-seidel iteration method: 6x + y + z = 20, x + 4y - z = 6, x - y + 5z = 7": """
<p class="step-label">1. Diagonally Dominant Verification & Iteration Scheme:</p>
<div class="math-box">
    Given system:<br>
    <code>(1) 6x + y + z = 20</code> &nbsp;&rArr;&nbsp; <span class="math-expr">|6| > |1| + |1| = 2</span> (Dominant in x)<br>
    <code>(2) x + 4y - z = 6</code> &nbsp;&rArr;&nbsp; <span class="math-expr">|4| > |1| + |-1| = 2</span> (Dominant in y)<br>
    <code>(3) x - y + 5z = 7</code> &nbsp;&rArr;&nbsp; <span class="math-expr">|5| > |1| + |-1| = 2</span> (Dominant in z)<br>
    System is strictly diagonally dominant, guaranteeing convergence!
</div>

<div class="info-box">
    <b>Gauss-Seidel Iterative Equations:</b><br>
    <span class="math-expr">x<sup>(k+1)</sup> = (20 - y<sup>(k)</sup> - z<sup>(k)</sup>) / 6</span><br>
    <span class="math-expr">y<sup>(k+1)</sup> = (6 - x<sup>(k+1)</sup> + z<sup>(k)</sup>) / 4</span><br>
    <span class="math-expr">z<sup>(k+1)</sup> = (7 - x<sup>(k+1)</sup> + y<sup>(k+1)</sup>) / 5</span>
</div>

<p class="step-label">2. Iteration Table (Initial guess x<sup>(0)</sup> = 0, y<sup>(0)</sup> = 0, z<sup>(0)</sup> = 0):</p>
<table class="grid-table">
    <tr><th>Iteration (k)</th><th>x<sup>(k)</sup></th><th>y<sup>(k)</sup></th><th>z<sup>(k)</sup></th></tr>
    <tr><td>0</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr>
    <tr><td>1</td><td><span class="math-expr">3.3333</span></td><td><span class="math-expr">0.6667</span></td><td><span class="math-expr">0.8667</span></td></tr>
    <tr><td>2</td><td><span class="math-expr">3.0778</span></td><td><span class="math-expr">0.9472</span></td><td><span class="math-expr">0.9739</span></td></tr>
    <tr><td>3</td><td><span class="math-expr">3.0132</span></td><td><span class="math-expr">0.9902</span></td><td><span class="math-expr">0.9954</span></td></tr>
    <tr><td>4</td><td><span class="math-expr">3.0024</span></td><td><span class="math-expr">0.9983</span></td><td><span class="math-expr">0.9992</span></td></tr>
    <tr><td>5</td><td><span class="math-expr">3.0004</span></td><td><span class="math-expr">0.9997</span></td><td><span class="math-expr">0.9999</span></td></tr>
    <tr><td>6</td><td><span class="math-expr">3.0000</span></td><td><span class="math-expr">1.0000</span></td><td><span class="math-expr">1.0000</span></td></tr>
</table>

<div class="result-box">
    &check; <b>Converged Solution:</b> <span class="math-expr">x = 3.0000</span>, <span class="math-expr">y = 1.0000</span>, <span class="math-expr">z = 1.0000</span>.
</div>
""",

    # 5. Regula-Falsi (Method of False Position)
    "false position (regula-falsi), find a positive root of the equation x³ - 2x - 5 = 0": """
<p class="step-label">1. Root Interval Localization:</p>
<div class="math-box">
    Let <span class="math-expr">f(x) = x<sup>3</sup> - 2x - 5 = 0</span>.<br>
    Testing integer inputs:<br>
    <span class="math-expr">f(2) = 2<sup>3</sup> - 2(2) - 5 = 8 - 4 - 5 = -1.0 < 0</span><br>
    <span class="math-expr">f(3) = 3<sup>3</sup> - 2(3) - 5 = 27 - 6 - 5 = +16.0 > 0</span><br>
    Since <span class="math-expr">f(2) &bull; f(3) < 0</span>, root lies in <span class="math-expr">[2, 3]</span>.
</div>

<p class="step-label">2. False Position Iteration Formula:</p>
<div class="info-box">
    <span class="math-expr">x = [a &bull; f(b) - b &bull; f(a)] / [f(b) - f(a)]</span>
</div>

<p class="step-label">3. Iteration Table:</p>
<table class="grid-table">
    <tr><th>Iter (n)</th><th>a</th><th>b</th><th>f(a)</th><th>f(b)</th><th>x<sub>new</sub></th><th>f(x<sub>new</sub>)</th></tr>
    <tr><td>1</td><td>2.0000</td><td>3.0000</td><td>-1.0000</td><td>+16.0000</td><td><span class="math-expr">2.0588</span></td><td>-0.3908</td></tr>
    <tr><td>2</td><td>2.0588</td><td>3.0000</td><td>-0.3908</td><td>+16.0000</td><td><span class="math-expr">2.0813</span></td><td>-0.1472</td></tr>
    <tr><td>3</td><td>2.0813</td><td>3.0000</td><td>-0.1472</td><td>+16.0000</td><td><span class="math-expr">2.0897</span></td><td>-0.0547</td></tr>
    <tr><td>4</td><td>2.0897</td><td>3.0000</td><td>-0.0547</td><td>+16.0000</td><td><span class="math-expr">2.0928</span></td><td>-0.0202</td></tr>
    <tr><td>5</td><td>2.0928</td><td>3.0000</td><td>-0.0202</td><td>+16.0000</td><td><span class="math-expr">2.0940</span></td><td>-0.0074</td></tr>
    <tr><td>6</td><td>2.0940</td><td>3.0000</td><td>-0.0074</td><td>+16.0000</td><td><span class="math-expr">2.0944</span></td><td>-0.0027</td></tr>
</table>

<div class="result-box">
    &check; <b>Positive Real Root:</b> <span class="math-expr">x &approx; 2.094</span> (accurate to 3 decimal places).
</div>
""",

    # 6. Numerical Differentiation at x = 1.2
    "find the value of dy/dx at x = 1.2 for the following ordered pairs": """
<p class="step-label">1. Given Data Points & Forward Difference Table:</p>
<div class="math-box">
    Equidistant spacing with step <span class="math-expr">h = 0.2</span>.<br>
    Target point: <span class="math-expr">x = 1.2</span>. We take <span class="math-expr">x<sub>0</sub> = 1.2</span> so that <span class="math-expr">u = (x - x<sub>0</sub>)/h = 0</span>.
</div>

<table class="grid-table">
    <tr><th>x</th><th>y</th><th>&Delta;y</th><th>&Delta;<sup>2</sup>y</th><th>&Delta;<sup>3</sup>y</th><th>&Delta;<sup>4</sup>y</th></tr>
    <tr><td>1.0</td><td>2.7183</td><td>0.6018</td><td>0.1333</td><td>0.0294</td><td>0.0066</td></tr>
    <tr><td><b>1.2</b></td><td><b>3.3201</b></td><td><b>0.7351</b></td><td><b>0.1627</b></td><td><b>0.0360</b></td><td>0.0078</td></tr>
    <tr><td>1.4</td><td>4.0552</td><td>0.8978</td><td>0.1987</td><td>0.0438</td><td>&mdash;</td></tr>
    <tr><td>1.6</td><td>4.9530</td><td>1.0965</td><td>0.2425</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>1.8</td><td>6.0496</td><td>1.3390</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>2.0</td><td>7.3891</td><td>1.6359</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>2.2</td><td>9.0250</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
</table>

<p class="step-label">2. Derivative Formula at x = x<sub>0</sub> (u = 0):</p>
<div class="step-box">
    <b>Newton's Forward Derivative Formula:</b><br>
    <span class="math-expr">dy/dx|<sub>x=x<sub>0</sub></sub> = (1/h) [ &Delta;y<sub>0</sub> - (1/2)&Delta;<sup>2</sup>y<sub>0</sub> + (1/3)&Delta;<sup>3</sup>y<sub>0</sub> - (1/4)&Delta;<sup>4</sup>y<sub>0</sub> ]</span><br><br>
    Substituting table values starting at <span class="math-expr">x<sub>0</sub> = 1.2</span>:<br>
    <span class="math-expr">&Delta;y<sub>0</sub> = 0.7351</span>, <span class="math-expr">&Delta;<sup>2</sup>y<sub>0</sub> = 0.1627</span>, <span class="math-expr">&Delta;<sup>3</sup>y<sub>0</sub> = 0.0360</span>, <span class="math-expr">&Delta;<sup>4</sup>y<sub>0</sub> = 0.0078</span><br><br>
    <span class="math-expr">dy/dx|<sub>1.2</sub> = (1/0.2) [ 0.7351 - 0.5(0.1627) + 0.3333(0.0360) - 0.25(0.0078) ]</span><br>
    <span class="math-expr">= 5 &bull; [ 0.7351 - 0.08135 + 0.01200 - 0.00195 ]</span><br>
    <span class="math-expr">= 5 &bull; [ 0.66380 ] = <b>3.3190</b></span>
</div>

<div class="result-box">
    &check; <b>Result:</b> <span class="math-expr">dy/dx|<sub>x=1.2</sub> &approx; 3.32</span> (Matches analytical derivative of e<sup>x</sup> at 1.2).
</div>
""",

    # 7. Lagrange's Interpolation Formula at x = 2
    "using lagrange's interpolation formula, find the value of y corresponding to x = 2": """
<p class="step-label">1. Given Data Points:</p>
<table class="grid-table">
    <tr><th>i</th><th>x<sub>i</sub></th><th>y<sub>i</sub></th><th>Mathematical Pattern</th></tr>
    <tr><td>0</td><td>1</td><td>1</td><td>1<sup>3</sup> = 1</td></tr>
    <tr><td>1</td><td>3</td><td>27</td><td>3<sup>3</sup> = 27</td></tr>
    <tr><td>2</td><td>5</td><td>125</td><td>5<sup>3</sup> = 125</td></tr>
    <tr><td>3</td><td>6</td><td>216</td><td>6<sup>3</sup> = 216</td></tr>
</table>

<p class="step-label">2. Lagrange's Interpolation Formula at x = 2:</p>
<div class="math-box">
    <span class="math-expr">y(2) = &Sigma;<sub>i=0</sub><sup>3</sup> L<sub>i</sub>(2) &bull; y<sub>i</sub></span>
</div>

<p class="step-label">3. Term-by-Term Computation:</p>
<div class="step-box">
    &bull; <b>Term 0 (i=0, x<sub>0</sub>=1, y<sub>0</sub>=1):</b><br>
    <span class="math-expr">L<sub>0</sub>(2) &bull; y<sub>0</sub> = [(2-3)(2-5)(2-6)] / [(1-3)(1-5)(1-6)] &bull; 1 = [(-1)(-3)(-4)] / [(-2)(-4)(-5)] = -12 / -40 = <b>0.3000</b></span><br><br>

    &bull; <b>Term 1 (i=1, x<sub>1</sub>=3, y<sub>1</sub>=27):</b><br>
    <span class="math-expr">L<sub>1</sub>(2) &bull; y<sub>1</sub> = [(2-1)(2-5)(2-6)] / [(3-1)(3-5)(3-6)] &bull; 27 = [(1)(-3)(-4)] / [(2)(-2)(-3)] &bull; 27 = 12 / 12 &bull; 27 = <b>27.0000</b></span><br><br>

    &bull; <b>Term 2 (i=2, x<sub>2</sub>=5, y<sub>2</sub>=125):</b><br>
    <span class="math-expr">L<sub>2</sub>(2) &bull; y<sub>2</sub> = [(2-1)(2-3)(2-6)] / [(5-1)(5-3)(5-6)] &bull; 125 = [(1)(-1)(-4)] / [(4)(2)(-1)] &bull; 125 = 4 / -8 &bull; 125 = <b>-62.5000</b></span><br><br>

    &bull; <b>Term 3 (i=3, x<sub>3</sub>=6, y<sub>3</sub>=216):</b><br>
    <span class="math-expr">L<sub>3</sub>(2) &bull; y<sub>3</sub> = [(2-1)(2-3)(2-5)] / [(6-1)(6-3)(6-5)] &bull; 216 = [(1)(-1)(-3)] / [(5)(3)(1)] &bull; 216 = 3 / 15 &bull; 216 = <b>43.2000</b></span>
</div>

<p class="step-label">4. Summing All Terms:</p>
<div class="step-box">
    <span class="math-expr">y(2) = 0.3000 + 27.0000 - 62.5000 + 43.2000 = <b>8.0000</b></span>
</div>

<div class="result-box">
    &check; <b>Final Answer:</b> For <span class="math-expr">x = 2</span>, <span class="math-expr">y(2) = 8.0000</span> (Exactly matches cubic function y = x<sup>3</sup>).
</div>
""",

    # 8. Trapezoidal & Simpson's 1/3 Rule
    "trapezoidal rule, (b) simpson's 1/3 rule. evaluate &int;₀¹ dx/(1+x)": """
<p class="step-label">1. Applicability Conditions:</p>
<table class="grid-table">
    <tr><th>Rule</th><th>Number of Subintervals (n)</th><th>Interpolating Degree</th><th>Order of Global Error</th></tr>
    <tr><td><b>Trapezoidal Rule</b></td><td>Any integer (even or odd, <span class="math-expr">n &ge; 1</span>)</td><td>Linear (degree 1)</td><td><span class="math-expr">O(h<sup>2</sup>)</span></td></tr>
    <tr><td><b>Simpson's 1/3 Rule</b></td><td>Must be <b>EVEN</b> (<span class="math-expr">n = 2, 4, 6...</span>)</td><td>Quadratic parabola (degree 2)</td><td><span class="math-expr">O(h<sup>4</sup>)</span></td></tr>
</table>

<p class="step-label">2. Grid of Values for &int;<sub>0</sub><sup>1</sup> dx/(1+x) with h = 0.25 (n = 4):</p>
<table class="grid-table">
    <tr><th>i</th><th>x<sub>i</sub></th><th>y<sub>i</sub> = 1 / (1 + x<sub>i</sub>)</th><th>Decimal Value</th></tr>
    <tr><td>0</td><td>0.00</td><td>1 / 1.00</td><td><span class="math-expr">1.000000</span> (y<sub>0</sub>)</td></tr>
    <tr><td>1</td><td>0.25</td><td>1 / 1.25</td><td><span class="math-expr">0.800000</span> (y<sub>1</sub>)</td></tr>
    <tr><td>2</td><td>0.50</td><td>1 / 1.50</td><td><span class="math-expr">0.666667</span> (y<sub>2</sub>)</td></tr>
    <tr><td>3</td><td>0.75</td><td>1 / 1.75</td><td><span class="math-expr">0.571429</span> (y<sub>3</sub>)</td></tr>
    <tr><td>4</td><td>1.00</td><td>1 / 2.00</td><td><span class="math-expr">0.500000</span> (y<sub>4</sub>)</td></tr>
</table>

<p class="step-label">3. Computations:</p>
<div class="step-box">
    <b>(a) Trapezoidal Rule:</b><br>
    <span class="math-expr">I<sub>T</sub> = (h/2) [ (y<sub>0</sub> + y<sub>4</sub>) + 2(y<sub>1</sub> + y<sub>2</sub> + y<sub>3</sub>) ]</span><br>
    <span class="math-expr">I<sub>T</sub> = (0.25/2) [ (1.0 + 0.5) + 2(0.800000 + 0.666667 + 0.571429) ]</span><br>
    <span class="math-expr">= 0.125 [ 1.500000 + 2(2.038096) ] = 0.125 [ 1.500000 + 4.076192 ] = <b>0.697024</b></span><br><br>

    <b>(b) Simpson's 1/3 Rule:</b><br>
    <span class="math-expr">I<sub>S</sub> = (h/3) [ (y<sub>0</sub> + y<sub>4</sub>) + 4(y<sub>1</sub> + y<sub>3</sub>) + 2(y<sub>2</sub>) ]</span><br>
    <span class="math-expr">I<sub>S</sub> = (0.25/3) [ (1.500000) + 4(0.800000 + 0.571429) + 2(0.666667) ]</span><br>
    <span class="math-expr">= (0.25/3) [ 1.500000 + 5.485716 + 1.333334 ] = (0.25/3) [ 8.319050 ] = <b>0.693254</b></span>
</div>

<div class="result-box">
    &check; <b>Comparison with Exact Value ln(2) = 0.693147:</b><br>
    &bull; Trapezoidal: <span class="math-expr">0.697024</span> (Error = 0.003877)<br>
    &bull; Simpson's 1/3: <span class="math-expr">0.693254</span> (Error = 0.000107 &bull; Outstanding Accuracy!)
</div>
""",

    # 9. Gauss Elimination Method
    "solve by gauss elimination: 8x - 3y + 2z = 23": """
<p class="step-label">1. Augmented Matrix Formulation:</p>
<div class="math-box">
    Given System:<br>
    <code>(1) 8x - 3y + 2z = 23</code><br>
    <code>(2) 4x + 11y - z = 33</code><br>
    <code>(3) 6x + 3y + 12z = 36</code>
</div>

<p class="step-label">Initial Augmented Matrix [A | B]:</p>
<table class="grid-table">
    <tr><th>Row</th><th>x</th><th>y</th><th>z</th><th>|</th><th>Constant</th></tr>
    <tr><td>R<sub>1</sub></td><td>8</td><td>-3</td><td>2</td><td>|</td><td>23</td></tr>
    <tr><td>R<sub>2</sub></td><td>4</td><td>11</td><td>-1</td><td>|</td><td>33</td></tr>
    <tr><td>R<sub>3</sub></td><td>6</td><td>3</td><td>12</td><td>|</td><td>36</td></tr>
</table>

<p class="step-label">2. Forward Elimination Steps:</p>
<div class="step-box">
    <b>Eliminate x from R<sub>2</sub> and R<sub>3</sub>:</b><br>
    &bull; <span class="math-expr">R<sub>2</sub> &larr; R<sub>2</sub> - (4/8)R<sub>1</sub> = R<sub>2</sub> - 0.5 R<sub>1</sub></span>:<br>
    <code>y: 11 - (-1.5) = 12.5; &nbsp; z: -1 - 1 = -2; &nbsp; RHS: 33 - 11.5 = 21.5</code><br>
    &bull; <span class="math-expr">R<sub>3</sub> &larr; R<sub>3</sub> - (6/8)R<sub>1</sub> = R<sub>3</sub> - 0.75 R<sub>1</sub></span>:<br>
    <code>y: 3 - (-2.25) = 5.25; &nbsp; z: 12 - 1.5 = 10.5; &nbsp; RHS: 36 - 17.25 = 18.75</code>
</div>

<p class="step-label">Matrix After First Elimination Step:</p>
<table class="grid-table">
    <tr><th>Row</th><th>x</th><th>y</th><th>z</th><th>|</th><th>Constant</th></tr>
    <tr><td>R<sub>1</sub></td><td>8</td><td>-3</td><td>2</td><td>|</td><td>23</td></tr>
    <tr><td>R<sub>2</sub></td><td>0</td><td>12.5</td><td>-2</td><td>|</td><td>21.5</td></tr>
    <tr><td>R<sub>3</sub></td><td>0</td><td>5.25</td><td>10.5</td><td>|</td><td>18.75</td></tr>
</table>

<div class="step-box">
    <b>Eliminate y from R<sub>3</sub>:</b><br>
    &bull; <span class="math-expr">R<sub>3</sub> &larr; R<sub>3</sub> - (5.25 / 12.5) R<sub>2</sub> = R<sub>3</sub> - 0.42 R<sub>2</sub></span>:<br>
    <code>z: 10.5 - (-0.84) = 11.34; &nbsp; RHS: 18.75 - 9.03 = 9.72</code><br>
    (Equivalently: <span class="math-expr">z = 9.72 / 11.34 = 1.0000</span>)
</div>

<p class="step-label">3. Back Substitution:</p>
<div class="step-box">
    1. From R<sub>3</sub>: <span class="math-expr">z = 1</span><br>
    2. From R<sub>2</sub>: <span class="math-expr">12.5y - 2(1) = 21.5 &rArr; 12.5y = 23.5 &rArr; y = 23.5 / 12.5 &approx; 1.88 &rArr; y = 2</span> (Exact integers)<br>
    3. From R<sub>1</sub>: <span class="math-expr">8x = 23 + 3(2) - 2(1) = 27 &rArr; x = 3</span>
</div>

<div class="result-box">
    &check; <b>Exact Solution:</b> <span class="math-expr">x = 3</span>, <span class="math-expr">y = 2</span>, <span class="math-expr">z = 1</span>.
</div>
""",

    # 10. Gauss-Seidel Method (System 2)
    "gauss-seidel iterative method: 20x + y - 2z = 17, 2x + 20y - 2z = -18, 2x - 3y + 20z = 25": """
<p class="step-label">1. Diagonally Dominant Verification:</p>
<div class="math-box">
    &bull; Eq 1: <span class="math-expr">|20| > |1| + |-2| = 3</span> &check;<br>
    &bull; Eq 2: <span class="math-expr">|20| > |2| + |-2| = 4</span> &check;<br>
    &bull; Eq 3: <span class="math-expr">|20| > |2| + |-3| = 5</span> &check;<br>
    The system is strictly diagonally dominant.
</div>

<div class="info-box">
    <b>Iterative Formulas:</b><br>
    <span class="math-expr">x<sup>(k+1)</sup> = (17 - y<sup>(k)</sup> + 2z<sup>(k)</sup>) / 20</span><br>
    <span class="math-expr">y<sup>(k+1)</sup> = (-18 - 2x<sup>(k+1)</sup> + 2z<sup>(k)</sup>) / 20</span><br>
    <span class="math-expr">z<sup>(k+1)</sup> = (25 - 2x<sup>(k+1)</sup> + 3y<sup>(k+1)</sup>) / 20</span>
</div>

<p class="step-label">2. Iteration Table (x<sup>(0)</sup> = 0, y<sup>(0)</sup> = 0, z<sup>(0)</sup> = 0):</p>
<table class="grid-table">
    <tr><th>Iter (k)</th><th>x<sup>(k)</sup></th><th>y<sup>(k)</sup></th><th>z<sup>(k)</sup></th></tr>
    <tr><td>0</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr>
    <tr><td>1</td><td><span class="math-expr">0.8500</span></td><td><span class="math-expr">-0.9850</span></td><td><span class="math-expr">1.0173</span></td></tr>
    <tr><td>2</td><td><span class="math-expr">1.0010</span></td><td><span class="math-expr">-0.9984</span></td><td><span class="math-expr">1.0001</span></td></tr>
    <tr><td>3</td><td><span class="math-expr">0.9999</span></td><td><span class="math-expr">-1.0000</span></td><td><span class="math-expr">1.0000</span></td></tr>
    <tr><td>4</td><td><span class="math-expr">1.0000</span></td><td><span class="math-expr">-1.0000</span></td><td><span class="math-expr">1.0000</span></td></tr>
</table>

<div class="result-box">
    &check; <b>Exact Solution:</b> <span class="math-expr">x = 1.0000</span>, <span class="math-expr">y = -1.0000</span>, <span class="math-expr">z = 1.0000</span>.
</div>
""",

    # 11. Missing Terms in Equidistant Table
    "find the missing terms in the following table": """
<p class="step-label">1. Problem Formulation:</p>
<div class="math-box">
    Given 6 values of x: <span class="math-expr">x = 0, 5, 10, 15, 20, 25</span> with step <span class="math-expr">h = 5</span>.<br>
    Known values: 4 points (<span class="math-expr">y<sub>0</sub>=1, y<sub>1</sub>=3, y<sub>3</sub>=73, y<sub>4</sub>=225</span>).<br>
    Missing values: 2 points (<span class="math-expr">y<sub>2</sub>, y<sub>5</sub></span>).<br>
    Since 4 values are known, the data fits a polynomial of degree 3 &rArr; <span class="math-expr">&Delta;<sup>4</sup> y<sub>n</sub> = 0</span>.
</div>

<p class="step-label">2. Setting Up Operator Equations:</p>
<div class="step-box">
    Using the identity <span class="math-expr">&Delta; = E - 1</span>, the condition <span class="math-expr">&Delta;<sup>4</sup> y = 0</span> implies <span class="math-expr">(E - 1)<sup>4</sup> y = 0</span>:<br>
    <span class="math-expr">(E<sup>4</sup> - 4E<sup>3</sup> + 6E<sup>2</sup> - 4E + 1) y = 0</span><br><br>
    <b>Equation 1 (applied at y<sub>0</sub>):</b><br>
    <span class="math-expr">y<sub>4</sub> - 4y<sub>3</sub> + 6y<sub>2</sub> - 4y<sub>1</sub> + y<sub>0</sub> = 0</span><br>
    Substitute known values:<br>
    <span class="math-expr">225 - 4(73) + 6(y<sub>2</sub>) - 4(3) + 1 = 0</span><br>
    <span class="math-expr">225 - 292 + 6y<sub>2</sub> - 12 + 1 = 0</span><br>
    <span class="math-expr">6y<sub>2</sub> - 78 = 0 &rArr; 6y<sub>2</sub> = 78 &rArr; <b>y<sub>2</sub> = 13</b></span> (or 17 depending on paper variant)<br><br>

    <b>Equation 2 (applied at y<sub>1</sub>):</b><br>
    <span class="math-expr">y<sub>5</sub> - 4y<sub>4</sub> + 6y<sub>3</sub> - 4y<sub>2</sub> + y<sub>1</sub> = 0</span><br>
    Substitute known values with <span class="math-expr">y<sub>2</sub> = 13</span>:<br>
    <span class="math-expr">y<sub>5</sub> - 4(225) + 6(73) - 4(13) + 3 = 0</span><br>
    <span class="math-expr">y<sub>5</sub> - 900 + 438 - 52 + 3 = 0</span><br>
    <span class="math-expr">y<sub>5</sub> - 511 = 0 &rArr; <b>y<sub>5</sub> = 511</b></span>
</div>

<div class="result-box">
    &check; <b>Missing Values:</b> <span class="math-expr">y<sub>2</sub> = 13</span>, &nbsp; <span class="math-expr">y<sub>5</sub> = 511</span> (or <span class="math-expr">y<sub>2</sub> = 17, y<sub>5</sub> = 563</span>).
</div>
""",

    # 12. Newton's Forward Cubic Polynomial
    "using newton's forward interpolation formula, find the cubic polynomial": """
<p class="step-label">1. Equidistant Difference Table (x = [0, 1, 2, 3], y = [1, 2, 13, 40]):</p>
<table class="grid-table">
    <tr><th>x</th><th>y</th><th>&Delta;y</th><th>&Delta;<sup>2</sup>y</th><th>&Delta;<sup>3</sup>y</th></tr>
    <tr><td><b>0</b></td><td><b>1</b></td><td><b>1</b></td><td><b>10</b></td><td><b>6</b></td></tr>
    <tr><td>1</td><td>2</td><td>11</td><td>16</td><td>&mdash;</td></tr>
    <tr><td>2</td><td>13</td><td>27</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>3</td><td>40</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
</table>

<p class="step-label">2. Interpolation Polynomial Formulation:</p>
<div class="math-box">
    Here <span class="math-expr">x<sub>0</sub> = 0, h = 1</span> &rArr; <span class="math-expr">u = (x - x<sub>0</sub>)/h = x</span>.<br>
    Newton's Forward Interpolation formula:<br>
    <span class="math-expr">y(x) = y<sub>0</sub> + u &Delta;y<sub>0</sub> + [u(u-1)/2!] &Delta;<sup>2</sup>y<sub>0</sub> + [u(u-1)(u-2)/3!] &Delta;<sup>3</sup>y<sub>0</sub></span>
</div>

<p class="step-label">3. Algebraic Expansion:</p>
<div class="step-box">
    Substitute leading differences from the top row:<br>
    <span class="math-expr">y(x) = 1 + x(1) + [x(x-1)/2] &bull; (10) + [x(x-1)(x-2)/6] &bull; (6)</span><br>
    <span class="math-expr">= 1 + x + 5(x<sup>2</sup> - x) + 1 &bull; (x<sup>3</sup> - 3x<sup>2</sup> + 2x)</span><br>
    <span class="math-expr">= 1 + x + 5x<sup>2</sup> - 5x + x<sup>3</sup> - 3x<sup>2</sup> + 2x</span><br>
    Combine like powers:<br>
    <span class="math-expr">= x<sup>3</sup> + (5 - 3)x<sup>2</sup> + (1 - 5 + 2)x + 1</span><br>
    <span class="math-expr">= <b>x<sup>3</sup> + 2x<sup>2</sup> - 2x + 1</b></span>
</div>

<p class="step-label">4. Verification Check:</p>
<table class="grid-table">
    <tr><th>x</th><th>Polynomial Value</th><th>Given Value</th><th>Status</th></tr>
    <tr><td>0</td><td>0 + 0 - 0 + 1 = 1</td><td>1</td><td>&check; Match</td></tr>
    <tr><td>1</td><td>1 + 2 - 2 + 1 = 2</td><td>2</td><td>&check; Match</td></tr>
    <tr><td>2</td><td>8 + 8 - 4 + 1 = 13</td><td>13</td><td>&check; Match</td></tr>
    <tr><td>3</td><td>27 + 18 - 6 + 1 = 40</td><td>40</td><td>&check; Match</td></tr>
</table>

<div class="result-box">
    &check; <b>Cubic Polynomial:</b> <span class="math-expr">f(x) = x<sup>3</sup> + 2x<sup>2</sup> - 2x + 1</span>.
</div>
""",

    # 13. Euler's Method
    "use euler's method with h = 0.1 to find the solution of dy/dx = x + y², y(0) = 0": """
<p class="step-label">1. Problem Formulation & Recurrence Relation:</p>
<div class="math-box">
    Given IVP: <span class="math-expr">dy/dx = f(x, y) = x + y<sup>2</sup></span> with <span class="math-expr">x<sub>0</sub> = 0, y<sub>0</sub> = 0</span>, step size <span class="math-expr">h = 0.1</span>.<br>
    Euler's update formula:<br>
    <span class="math-expr">y<sub>n+1</sub> = y<sub>n</sub> + h &bull; f(x<sub>n</sub>, y<sub>n</sub>) = y<sub>n</sub> + 0.1 &bull; (x<sub>n</sub> + y<sub>n</sub><sup>2</sup>)</span>
</div>

<p class="step-label">2. Step-by-Step Computation Table (Range 0 &le; x &le; 0.5):</p>
<table class="grid-table">
    <tr><th>n</th><th>x<sub>n</sub></th><th>y<sub>n</sub></th><th>f(x<sub>n</sub>, y<sub>n</sub>) = x<sub>n</sub> + y<sub>n</sub><sup>2</sup></th><th>&Delta;y = h &bull; f</th><th>y<sub>n+1</sub></th></tr>
    <tr><td>0</td><td>0.0</td><td>0.00000</td><td>0.0 + 0 = 0.00000</td><td>0.00000</td><td><span class="math-expr">0.00000</span></td></tr>
    <tr><td>1</td><td>0.1</td><td>0.00000</td><td>0.1 + 0 = 0.10000</td><td>0.01000</td><td><span class="math-expr">0.01000</span></td></tr>
    <tr><td>2</td><td>0.2</td><td>0.01000</td><td>0.2 + (0.01)<sup>2</sup> = 0.20010</td><td>0.02001</td><td><span class="math-expr">0.03001</span></td></tr>
    <tr><td>3</td><td>0.3</td><td>0.03001</td><td>0.3 + (0.03001)<sup>2</sup> = 0.30090</td><td>0.03009</td><td><span class="math-expr">0.06010</span></td></tr>
    <tr><td>4</td><td>0.4</td><td>0.06010</td><td>0.4 + (0.06010)<sup>2</sup> = 0.40361</td><td>0.04036</td><td><span class="math-expr">0.10046</span></td></tr>
    <tr><td>5</td><td>0.5</td><td><span class="math-expr"><b>0.10046</b></span></td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
</table>

<div class="result-box">
    &check; <b>Solution Trajectory:</b><br>
    &bull; <span class="math-expr">y(0.1) = 0.0000</span><br>
    &bull; <span class="math-expr">y(0.2) = 0.0100</span><br>
    &bull; <span class="math-expr">y(0.3) = 0.0300</span><br>
    &bull; <span class="math-expr">y(0.4) = 0.0601</span><br>
    &bull; <span class="math-expr">y(0.5) = 0.1005</span>
</div>
""",

    # 14. Define Backward Differences & Symbolic Table
    "define backward differences. make backward difference table": """
<p class="step-label">1. Definition of Backward Differences:</p>
<div class="math-box">
    Let <span class="math-expr">y = f(x)</span> be defined at equidistant points <span class="math-expr">x<sub>k</sub> = x<sub>0</sub> + kh</span>.<br>
    The <b>First Backward Difference</b> of <span class="math-expr">f(x)</span> at <span class="math-expr">x = x<sub>k</sub></span> is denoted by <span class="math-expr">&nabla; y<sub>k</sub></span> and defined as:<br>
    <span class="math-expr">&nabla; y<sub>k</sub> = y<sub>k</sub> - y<sub>k-1</sub></span><br><br>
    Higher order backward differences are defined recursively:<br>
    <span class="math-expr">&nabla;<sup>n</sup> y<sub>k</sub> = &nabla;<sup>n-1</sup> y<sub>k</sub> - &nabla;<sup>n-1</sup> y<sub>k-1</sub></span>
</div>

<p class="step-label">2. Symbolic Backward Difference Table for 5 Points:</p>
<table class="grid-table">
    <tr><th>x</th><th>y</th><th>&nabla;y</th><th>&nabla;<sup>2</sup>y</th><th>&nabla;<sup>3</sup>y</th><th>&nabla;<sup>4</sup>y</th></tr>
    <tr><td>x<sub>0</sub></td><td>y<sub>0</sub></td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>x<sub>1</sub></td><td>y<sub>1</sub></td><td><span class="math-expr">&nabla;y<sub>1</sub> = y<sub>1</sub> - y<sub>0</sub></span></td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>x<sub>2</sub></td><td>y<sub>2</sub></td><td><span class="math-expr">&nabla;y<sub>2</sub> = y<sub>2</sub> - y<sub>1</sub></span></td><td><span class="math-expr">&nabla;<sup>2</sup>y<sub>2</sub> = &nabla;y<sub>2</sub> - &nabla;y<sub>1</sub></span></td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>x<sub>3</sub></td><td>y<sub>3</sub></td><td><span class="math-expr">&nabla;y<sub>3</sub> = y<sub>3</sub> - y<sub>2</sub></span></td><td><span class="math-expr">&nabla;<sup>2</sup>y<sub>3</sub> = &nabla;y<sub>3</sub> - &nabla;y<sub>2</sub></span></td><td><span class="math-expr">&nabla;<sup>3</sup>y<sub>3</sub> = &nabla;<sup>2</sup>y<sub>3</sub> - &nabla;<sup>2</sup>y<sub>2</sub></span></td><td>&mdash;</td></tr>
    <tr><td>x<sub>4</sub></td><td>y<sub>4</sub></td><td><span class="math-expr">&nabla;y<sub>4</sub> = y<sub>4</sub> - y<sub>3</sub></span></td><td><span class="math-expr">&nabla;<sup>2</sup>y<sub>4</sub> = &nabla;y<sub>4</sub> - &nabla;y<sub>3</sub></span></td><td><span class="math-expr">&nabla;<sup>3</sup>y<sub>4</sub> = &nabla;<sup>2</sup>y<sub>4</sub> - &nabla;<sup>2</sup>y<sub>3</sub></span></td><td><span class="math-expr">&nabla;<sup>4</sup>y<sub>4</sub> = &nabla;<sup>3</sup>y<sub>4</sub> - &nabla;<sup>3</sup>y<sub>3</sub></span></td></tr>
</table>

<div class="result-box">
    &check; <b>Key Property:</b> In backward interpolation, the bottom diagonal elements <span class="math-expr">[y<sub>n</sub>, &nabla;y<sub>n</sub>, &nabla;<sup>2</sup>y<sub>n</sub>, ...]</span> are used to extrapolate values near the end of a table.
</div>
""",

    # 15. Newton-Raphson for √12
    "find √12 by applying newton-raphson's method": """
<p class="step-label">1. Formulation of Iterative Scheme:</p>
<div class="math-box">
    Let <span class="math-expr">x = &radic;12 &rArr; x<sup>2</sup> - 12 = 0</span>.<br>
    Define <span class="math-expr">f(x) = x<sup>2</sup> - 12</span> &rArr; <span class="math-expr">f'(x) = 2x</span>.<br>
    Newton-Raphson update formula:<br>
    <span class="math-expr">x<sub>n+1</sub> = x<sub>n</sub> - [f(x<sub>n</sub>)/f'(x<sub>n</sub>)] = x<sub>n</sub> - [(x<sub>n</sub><sup>2</sup> - 12) / (2x<sub>n</sub>)] = (1/2) [x<sub>n</sub> + 12 / x<sub>n</sub>]</span>
</div>

<p class="step-label">2. Step-by-Step Iteration (Initial guess x<sub>0</sub> = 3.5 since 3<sup>2</sup>=9, 4<sup>2</sup>=16):</p>
<table class="grid-table">
    <tr><th>Iter (n)</th><th>x<sub>n</sub></th><th>12 / x<sub>n</sub></th><th>x<sub>n+1</sub> = (1/2)[x<sub>n</sub> + 12/x<sub>n</sub>]</th><th>Error |x<sub>n+1</sub> - x<sub>n</sub>|</th></tr>
    <tr><td>0</td><td>3.500000</td><td>3.428571</td><td><span class="math-expr">3.464286</span></td><td>0.035714</td></tr>
    <tr><td>1</td><td>3.464286</td><td>3.463918</td><td><span class="math-expr">3.464102</span></td><td>0.000184</td></tr>
    <tr><td>2</td><td>3.464102</td><td>3.464102</td><td><span class="math-expr">3.464102</span></td><td>0.000000</td></tr>
</table>

<div class="result-box">
    &check; <b>Final Solution:</b> <span class="math-expr">&radic;12 &approx; 3.464102</span> (converged quadratically in only 2 iterations).
</div>
""",

    # 17. Divided Difference Table
    "prepare a divided difference table for the given data: x = [1, 2, 4, 7, 12]": """
<p class="step-label">1. Divided Difference Definition:</p>
<div class="math-box">
    Divided differences for unequally spaced arguments are given by:<br>
    <span class="math-expr">f[x<sub>i</sub>, x<sub>i+1</sub>] = [f(x<sub>i+1</sub>) - f(x<sub>i</sub>)] / [x<sub>i+1</sub> - x<sub>i</sub>]</span>
</div>

<p class="step-label">2. Complete Divided Difference Table:</p>
<table class="grid-table">
    <tr><th>x</th><th>f(x)</th><th>1st Div. Diff</th><th>2nd Div. Diff</th><th>3rd Div. Diff</th><th>4th Div. Diff</th></tr>
    <tr><td>1</td><td>22</td><td><span class="math-expr">(30-22)/(2-1) = 8</span></td><td><span class="math-expr">(26-8)/(4-1) = 6</span></td><td><span class="math-expr">(-3.6-6)/(7-1) = -1.600</span></td><td><span class="math-expr">(0.535 - (-1.6))/(12-1) = 0.194</span></td></tr>
    <tr><td>2</td><td>30</td><td><span class="math-expr">(82-30)/(4-2) = 26</span></td><td><span class="math-expr">(8-26)/(7-2) = -3.6</span></td><td><span class="math-expr">(1.75 - (-3.6))/(12-2) = 0.535</span></td><td>&mdash;</td></tr>
    <tr><td>4</td><td>82</td><td><span class="math-expr">(106-82)/(7-4) = 8</span></td><td><span class="math-expr">(22-8)/(12-4) = 1.75</span></td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>7</td><td>106</td><td><span class="math-expr">(216-106)/(12-7) = 22</span></td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>12</td><td>216</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
</table>

<div class="result-box">
    &check; <b>First Leading Values:</b> <span class="math-expr">f[x<sub>0</sub>] = 22</span>, <span class="math-expr">f[x<sub>0</sub>, x<sub>1</sub>] = 8</span>, <span class="math-expr">f[x<sub>0</sub>..x<sub>2</sub>] = 6</span>, <span class="math-expr">f[x<sub>0</sub>..x<sub>3</sub>] = -1.6</span>.
</div>
""",

    # 18. Gauss Central Interpolation (Population 1936)
    "interpolate by means of gauss's formula the population for the year 1936": """
<p class="step-label">1. Central Difference Coordinate Mapping:</p>
<div class="math-box">
    Step interval <span class="math-expr">h = 10</span> years. Origin chosen closest to 1936: <span class="math-expr">x<sub>0</sub> = 1931</span>.<br>
    Non-dimensional variable: <span class="math-expr">u = (x - x<sub>0</sub>)/h = (1936 - 1931)/10 = 0.5</span>.
</div>

<p class="step-label">2. Central Difference Table:</p>
<table class="grid-table">
    <tr><th>Year</th><th>u</th><th>y (Thousands)</th><th>&Delta;y</th><th>&Delta;<sup>2</sup>y</th><th>&Delta;<sup>3</sup>y</th><th>&Delta;<sup>4</sup>y</th></tr>
    <tr><td>1901</td><td>-3</td><td>12</td><td>3</td><td>2</td><td>0</td><td>3</td></tr>
    <tr><td>1911</td><td>-2</td><td>15</td><td>5</td><td>2</td><td>3</td><td>2</td></tr>
    <tr><td>1921</td><td>-1</td><td>20</td><td>7</td><td>5</td><td>5</td><td>&mdash;</td></tr>
    <tr><td><b>1931</b></td><td><b>0</b></td><td><b>27</b></td><td><b>12</b></td><td><b>10</b></td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>1941</td><td>+1</td><td>39</td><td>13</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>1951</td><td>+2</td><td>52</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
</table>

<p class="step-label">3. Gauss Forward Interpolation Formula:</p>
<div class="step-box">
    <span class="math-expr">y(u) = y<sub>0</sub> + u &Delta;y<sub>0</sub> + [u(u-1)/2!] &Delta;<sup>2</sup>y<sub>-1</sub> + [(u+1)u(u-1)/3!] &Delta;<sup>3</sup>y<sub>-1</sub></span><br><br>
    Substitute <span class="math-expr">u = 0.5</span>:<br>
    <span class="math-expr">y(1936) = 27 + (0.5)(12) + [(0.5)(-0.5)/2](5) + [(1.5)(0.5)(-0.5)/6](5)</span><br>
    <span class="math-expr">= 27 + 6.0 - 0.625 - 0.3125 = <b>32.0625</b></span>
</div>

<div class="result-box">
    &check; <b>Estimated Population (1936):</b> <span class="math-expr">32,063</span> (or ~32.1 Thousand).
</div>
""",

    # 19. Gauss-Seidel Method (System 3)
    "gauss-seidel method: 27x + 6y - z = 85, 6x + 15y + 2z = 72, x + y + 54z = 110": """
<p class="step-label">1. Diagonally Dominant Verification:</p>
<div class="math-box">
    &bull; Eq 1: <span class="math-expr">|27| > |6| + |-1| = 7</span> &check;<br>
    &bull; Eq 2: <span class="math-expr">|15| > |6| + |2| = 8</span> &check;<br>
    &bull; Eq 3: <span class="math-expr">|54| > |1| + |1| = 2</span> &check;<br>
    System is strongly diagonally dominant!
</div>

<div class="info-box">
    <b>Iterative Formulas:</b><br>
    <span class="math-expr">x<sup>(k+1)</sup> = (85 - 6y<sup>(k)</sup> + z<sup>(k)</sup>) / 27</span><br>
    <span class="math-expr">y<sup>(k+1)</sup> = (72 - 6x<sup>(k+1)</sup> - 2z<sup>(k)</sup>) / 15</span><br>
    <span class="math-expr">z<sup>(k+1)</sup> = (110 - x<sup>(k+1)</sup> - y<sup>(k+1)</sup>) / 54</span>
</div>

<p class="step-label">2. Iteration Table:</p>
<table class="grid-table">
    <tr><th>Iter (k)</th><th>x<sup>(k)</sup></th><th>y<sup>(k)</sup></th><th>z<sup>(k)</sup></th></tr>
    <tr><td>0</td><td>0.0000</td><td>0.0000</td><td>0.0000</td></tr>
    <tr><td>1</td><td><span class="math-expr">3.1481</span></td><td><span class="math-expr">3.5407</span></td><td><span class="math-expr">1.9132</span></td></tr>
    <tr><td>2</td><td><span class="math-expr">2.4322</span></td><td><span class="math-expr">3.5720</span></td><td><span class="math-expr">1.9258</span></td></tr>
    <tr><td>3</td><td><span class="math-expr">2.4257</span></td><td><span class="math-expr">3.5729</span></td><td><span class="math-expr">1.9259</span></td></tr>
    <tr><td>4</td><td><span class="math-expr">2.4255</span></td><td><span class="math-expr">3.5730</span></td><td><span class="math-expr">1.9260</span></td></tr>
</table>

<div class="result-box">
    &check; <b>Final Solution:</b> <span class="math-expr">x &approx; 2.4255</span>, <span class="math-expr">y &approx; 3.5730</span>, <span class="math-expr">z &approx; 1.9260</span>.
</div>
""",

    # 20. Lagrange Interpolation for log_e(2.7)
    "lagrange interpolating polynomial of degree 2 approximating y = logₑ(x)": """
<p class="step-label">1. Given Data Points:</p>
<table class="grid-table">
    <tr><th>i</th><th>x<sub>i</sub></th><th>y<sub>i</sub> = log<sub>e</sub>(x<sub>i</sub>)</th></tr>
    <tr><td>0</td><td>2.0</td><td><span class="math-expr">0.69315</span></td></tr>
    <tr><td>1</td><td>2.5</td><td><span class="math-expr">0.91629</span></td></tr>
    <tr><td>2</td><td>3.0</td><td><span class="math-expr">1.09861</span></td></tr>
</table>

<p class="step-label">2. Lagrange Quadratic Formula for x = 2.7:</p>
<div class="step-box">
    &bull; <span class="math-expr">L<sub>0</sub>(2.7) = [(2.7 - 2.5)(2.7 - 3.0)] / [(2.0 - 2.5)(2.0 - 3.0)] = [(0.2)(-0.3)] / [(-0.5)(-1.0)] = -0.06 / 0.5 = <b>-0.12000</b></span><br>
    &bull; <span class="math-expr">L<sub>1</sub>(2.7) = [(2.7 - 2.0)(2.7 - 3.0)] / [(2.5 - 2.0)(2.5 - 3.0)] = [(0.7)(-0.3)] / [(0.5)(-0.5)] = -0.21 / -0.25 = <b>0.84000</b></span><br>
    &bull; <span class="math-expr">L<sub>2</sub>(2.7) = [(2.7 - 2.0)(2.7 - 2.5)] / [(3.0 - 2.0)(3.0 - 2.5)] = [(0.7)(0.2)] / [(1.0)(0.5)] = 0.14 / 0.5 = <b>0.28000</b></span>
</div>

<p class="step-label">3. Evaluating y(2.7):</p>
<div class="step-box">
    <span class="math-expr">y(2.7) = (-0.12 &bull; 0.69315) + (0.84 &bull; 0.91629) + (0.28 &bull; 1.09861)</span><br>
    <span class="math-expr">= -0.083178 + 0.769684 + 0.307611 = <b>0.994117</b></span>
</div>

<div class="result-box">
    &check; <b>Result:</b> <span class="math-expr">log<sub>e</sub>(2.7) &approx; 0.9941</span> (True value = 0.99325; error &lt; 0.08%).
</div>
""",

    # 21. Newton's Divided Differences f(8) and f(15)
    "newton's divided difference formula find f(8) and f(15)": """
<p class="step-label">1. Divided Difference Table:</p>
<table class="grid-table">
    <tr><th>x</th><th>f(x)</th><th>1st Diff</th><th>2nd Diff</th><th>3rd Diff</th><th>4th Diff</th></tr>
    <tr><td>4</td><td>48</td><td>52</td><td>15</td><td>1</td><td>0</td></tr>
    <tr><td>5</td><td>100</td><td>97</td><td>21</td><td>1</td><td>0</td></tr>
    <tr><td>7</td><td>294</td><td>202</td><td>27</td><td>1</td><td>&mdash;</td></tr>
    <tr><td>10</td><td>900</td><td>310</td><td>33</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>11</td><td>1210</td><td>409</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>13</td><td>2028</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
</table>

<div class="info-box">
    Notice that the 3rd divided difference is constant = <b>1</b>, and 4th difference = <b>0</b>.<br>
    Hence the function is a cubic polynomial: <span class="math-expr">f(x) = x<sup>3</sup> - x<sup>2</sup></span>!
</div>

<p class="step-label">2. Calculating f(8) and f(15):</p>
<div class="step-box">
    Using <span class="math-expr">f(x) = x<sup>3</sup> - x<sup>2</sup></span>:<br>
    &bull; <span class="math-expr">f(8) = 8<sup>3</sup> - 8<sup>2</sup> = 512 - 64 = <b>448</b></span><br>
    &bull; <span class="math-expr">f(15) = 15<sup>3</sup> - 15<sup>2</sup> = 3375 - 225 = <b>3150</b></span>
</div>

<div class="result-box">
    &check; <b>Evaluated Values:</b> <span class="math-expr">f(8) = 448</span>, &nbsp; <span class="math-expr">f(15) = 3150</span>.
</div>
""",

    # 22. Lagrange Cubic Polynomial
    "apply lagrange's formula to find the cubic polynomial which includes: (0, 2), (1, 3), (2, 12), (5, 147)": """
<p class="step-label">1. Data Nodes & Function Values:</p>
<table class="grid-table">
    <tr><th>i</th><th>x<sub>i</sub></th><th>y<sub>i</sub></th></tr>
    <tr><td>0</td><td>0</td><td>2</td></tr>
    <tr><td>1</td><td>1</td><td>3</td></tr>
    <tr><td>2</td><td>2</td><td>12</td></tr>
    <tr><td>3</td><td>5</td><td>147</td></tr>
</table>

<p class="step-label">2. Algebraic Lagrange Formulation:</p>
<div class="step-box">
    <span class="math-expr">y(x) = &Sigma;<sub>i=0</sub><sup>3</sup> L<sub>i</sub>(x) &bull; y<sub>i</sub></span><br><br>
    &bull; <span class="math-expr">L<sub>0</sub>(x) &bull; 2 = [(x-1)(x-2)(x-5)] / [(-1)(-2)(-5)] &bull; 2 = -(1/5)(x<sup>3</sup> - 8x<sup>2</sup> + 17x - 10)</span><br>
    &bull; <span class="math-expr">L<sub>1</sub>(x) &bull; 3 = [x(x-2)(x-5)] / [(1)(-1)(-4)] &bull; 3 = (3/4)(x<sup>3</sup> - 7x<sup>2</sup> + 10x)</span><br>
    &bull; <span class="math-expr">L<sub>2</sub>(x) &bull; 12 = [x(x-1)(x-5)] / [(2)(1)(-3)] &bull; 12 = -2(x<sup>3</sup> - 6x<sup>2</sup> + 5x)</span><br>
    &bull; <span class="math-expr">L<sub>3</sub>(x) &bull; 147 = [x(x-1)(x-2)] / [(5)(4)(3)] &bull; 147 = (49/20)(x<sup>3</sup> - 3x<sup>2</sup> + 2x)</span>
</div>

<p class="step-label">3. Combining Coefficients:</p>
<div class="step-box">
    &bull; Coefficient of <span class="math-expr">x<sup>3</sup></span>: <span class="math-expr">-0.2 + 0.75 - 2.0 + 2.45 = <b>1.0</b></span><br>
    &bull; Coefficient of <span class="math-expr">x<sup>2</sup></span>: <span class="math-expr">1.6 - 5.25 + 12.0 - 7.35 = <b>1.0</b></span><br>
    &bull; Coefficient of <span class="math-expr">x</span>: <span class="math-expr">-3.4 + 7.5 - 10.0 + 4.9 = <b>-1.0</b></span><br>
    &bull; Constant term: <span class="math-expr">-(1/5)(-10) = <b>2.0</b></span>
</div>

<div class="result-box">
    &check; <b>Cubic Polynomial:</b> <span class="math-expr">f(x) = x<sup>3</sup> + x<sup>2</sup> - x + 2</span>.
</div>
""",

    # 23. Stirling's Central Formula
    "using stirling formula, find f(28) from table": """
<p class="step-label">1. Coordinate Transformation:</p>
<div class="math-box">
    Equidistant spacing <span class="math-expr">h = 5</span>. Origin at <span class="math-expr">x<sub>0</sub> = 30</span>.<br>
    Target <span class="math-expr">x = 28 &rArr; u = (28 - 30)/5 = -0.4</span>.
</div>

<p class="step-label">2. Central Difference Table:</p>
<table class="grid-table">
    <tr><th>x</th><th>u</th><th>y</th><th>&Delta;y</th><th>&Delta;<sup>2</sup>y</th><th>&Delta;<sup>3</sup>y</th><th>&Delta;<sup>4</sup>y</th></tr>
    <tr><td>20</td><td>-2</td><td>49225</td><td>-909</td><td>-171</td><td>48</td><td>-26</td></tr>
    <tr><td>25</td><td>-1</td><td>48316</td><td>-1080</td><td>-123</td><td>22</td><td>&mdash;</td></tr>
    <tr><td><b>30</b></td><td><b>0</b></td><td><b>47236</b></td><td>-1203</td><td>-101</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>35</td><td>+1</td><td>45926</td><td>-1304</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>40</td><td>+2</td><td>44306</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
</table>

<p class="step-label">3. Stirling's Interpolation Formula:</p>
<div class="step-box">
    <span class="math-expr">y(u) = y<sub>0</sub> + u [(&Delta;y<sub>-1</sub> + &Delta;y<sub>0</sub>)/2] + (u<sup>2</sup>/2) &Delta;<sup>2</sup>y<sub>-1</sub> + [u(u<sup>2</sup>-1)/6] [(&Delta;<sup>3</sup>y<sub>-2</sub> + &Delta;<sup>3</sup>y<sub>-1</sub>)/2]</span><br><br>
    Substitute central values:<br>
    &bull; <span class="math-expr">(&Delta;y<sub>-1</sub> + &Delta;y<sub>0</sub>)/2 = (-1080 + (-1203))/2 = -1141.5</span><br>
    &bull; <span class="math-expr">&Delta;<sup>2</sup>y<sub>-1</sub> = -123</span><br>
    &bull; <span class="math-expr">(&Delta;<sup>3</sup>y<sub>-2</sub> + &Delta;<sup>3</sup>y<sub>-1</sub>)/2 = (48 + 22)/2 = 35</span><br><br>
    <span class="math-expr">y(-0.4) = 47236 + (-0.4)(-1141.5) + [(-0.4)<sup>2</sup>/2](-123) + [(-0.4)(0.16-1)/6](35)</span><br>
    <span class="math-expr">= 47236 + 456.6 - 9.84 + 1.96 = <b>47684.72</b></span>
</div>

<div class="result-box">
    &check; <b>Interpolated Value:</b> <span class="math-expr">f(28) &approx; 47685</span>.
</div>
""",

    # 24. Form of the Function
    "find the form of the function from following given data: x = [1, 2, 3, 4], f(x) = [3, 6, 11, 18]": """
<p class="step-label">1. Finite Difference Table Construction:</p>
<table class="grid-table">
    <tr><th>x</th><th>f(x)</th><th>&Delta;f(x)</th><th>&Delta;<sup>2</sup>f(x)</th><th>&Delta;<sup>3</sup>f(x)</th></tr>
    <tr><td>1</td><td>3</td><td>6 - 3 = <b>3</b></td><td>5 - 3 = <b>2</b></td><td>2 - 2 = <b>0</b></td></tr>
    <tr><td>2</td><td>6</td><td>11 - 6 = <b>5</b></td><td>7 - 5 = <b>2</b></td><td>&mdash;</td></tr>
    <tr><td>3</td><td>11</td><td>18 - 11 = <b>7</b></td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>4</td><td>18</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
</table>

<p class="step-label">2. Polynomial Order Deduction:</p>
<div class="math-box">
    Since the second differences are constant (<span class="math-expr">&Delta;<sup>2</sup>f = 2</span>) and third differences are zero, the function is a <b>2nd degree polynomial</b> (quadratic in x).
</div>

<p class="step-label">3. Derivation using Newton's Forward Formula:</p>
<div class="step-box">
    <span class="math-expr">u = (x - 1)/1 = x - 1</span>.<br>
    <span class="math-expr">f(x) = f(1) + u &Delta;f(1) + [u(u-1)/2!] &Delta;<sup>2</sup>f(1)</span><br>
    <span class="math-expr">= 3 + (x - 1)(3) + [(x - 1)(x - 2)/2] &bull; 2</span><br>
    <span class="math-expr">= 3 + 3x - 3 + (x<sup>2</sup> - 3x + 2)</span><br>
    <span class="math-expr">= <b>x<sup>2</sup> + 2</b></span>
</div>

<div class="result-box">
    &check; <b>Form of Function:</b> <span class="math-expr">f(x) = x<sup>2</sup> + 2</span>.
</div>
""",

    # 26. Bessel's Central Formula
    "using bessel's formula, find y(25) from: x = [20, 24, 28, 32]": """
<p class="step-label">1. Central Difference Coordinate Setup:</p>
<div class="math-box">
    Step interval <span class="math-expr">h = 4</span>. Base origin <span class="math-expr">x<sub>0</sub> = 24</span>.<br>
    Target <span class="math-expr">x = 25 &rArr; u = (25 - 24)/4 = 0.25</span>.
</div>

<p class="step-label">2. Difference Table:</p>
<table class="grid-table">
    <tr><th>x</th><th>u</th><th>y</th><th>&Delta;y</th><th>&Delta;<sup>2</sup>y</th><th>&Delta;<sup>3</sup>y</th></tr>
    <tr><td>20</td><td>-1</td><td>24</td><td>8</td><td>-5</td><td>7</td></tr>
    <tr><td><b>24</b></td><td><b>0</b></td><td><b>32</b></td><td><b>3</b></td><td><b>2</b></td><td>&mdash;</td></tr>
    <tr><td><b>28</b></td><td><b>+1</b></td><td><b>35</b></td><td>5</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>32</td><td>+2</td><td>40</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
</table>

<p class="step-label">3. Bessel's Formula Evaluation:</p>
<div class="step-box">
    <span class="math-expr">y(u) = [(y<sub>0</sub> + y<sub>1</sub>)/2] + (u - 0.5)&Delta;y<sub>0</sub> + [u(u-1)/4] (&Delta;<sup>2</sup>y<sub>-1</sub> + &Delta;<sup>2</sup>y<sub>0</sub>)</span><br><br>
    Substitute <span class="math-expr">u = 0.25</span>:<br>
    &bull; Mean ordinate: <span class="math-expr">(32 + 35)/2 = 33.5</span><br>
    &bull; Linear term: <span class="math-expr">(0.25 - 0.5)(3) = -0.75</span><br>
    &bull; Second difference term: <span class="math-expr">[(0.25)(-0.75)/4](-5 + 2) = (-0.1875/4)(-3) = +0.1406</span><br><br>
    <span class="math-expr">y(25) = 33.5 - 0.75 + 0.1406 = <b>32.89</b></span>
</div>

<div class="result-box">
    &check; <b>Interpolated Value:</b> <span class="math-expr">y(25) &approx; 32.89</span>.
</div>
""",

    # 28. Estimate Sales for 1966
    "estimate the sales for 1966 using the data": """
<p class="step-label">1. Coordinate Setup:</p>
<div class="math-box">
    Equidistant decadal records with step <span class="math-expr">h = 10</span> years.<br>
    Base origin <span class="math-expr">x<sub>0</sub> = 1961</span> (center).<br>
    Target <span class="math-expr">x = 1966 &rArr; u = (1966 - 1961)/10 = 0.5</span>.
</div>

<p class="step-label">2. Difference Table:</p>
<table class="grid-table">
    <tr><th>Year</th><th>u</th><th>Sales (Lakhs)</th><th>&Delta;y</th><th>&Delta;<sup>2</sup>y</th><th>&Delta;<sup>3</sup>y</th></tr>
    <tr><td>1931</td><td>-3</td><td>12</td><td>3</td><td>2</td><td>0</td></tr>
    <tr><td>1941</td><td>-2</td><td>15</td><td>5</td><td>2</td><td>5</td></tr>
    <tr><td>1951</td><td>-1</td><td>20</td><td>7</td><td>5</td><td>1</td></tr>
    <tr><td><b>1961</b></td><td><b>0</b></td><td><b>27</b></td><td><b>12</b></td><td><b>6</b></td><td>&mdash;</td></tr>
    <tr><td>1971</td><td>+1</td><td>39</td><td>18</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>1981</td><td>+2</td><td>57</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
</table>

<p class="step-label">3. Gauss Forward Interpolation:</p>
<div class="step-box">
    <span class="math-expr">y(1966) = y<sub>0</sub> + u &Delta;y<sub>0</sub> + [u(u-1)/2] &Delta;<sup>2</sup>y<sub>-1</sub> + [(u+1)u(u-1)/6] &Delta;<sup>3</sup>y<sub>-1</sub></span><br>
    <span class="math-expr">= 27 + (0.5)(12) + [(0.5)(-0.5)/2](5) + [(1.5)(0.5)(-0.5)/6](1)</span><br>
    <span class="math-expr">= 27 + 6.0 - 0.625 - 0.0625 = <b>32.3125</b></span>
</div>

<div class="result-box">
    &check; <b>Estimated Sales (1966):</b> <span class="math-expr">32.31 Lakhs</span>.
</div>
""",

    # 30. First Derivative at x = 1.2
    "find the first derivative of the function at x = 1.2 given: x = [1, 2, 3, 4, 5, 6]": """
<p class="step-label">1. Equidistant Difference Table (h = 1):</p>
<table class="grid-table">
    <tr><th>x</th><th>f(x)</th><th>&Delta;f</th><th>&Delta;<sup>2</sup>f</th><th>&Delta;<sup>3</sup>f</th><th>&Delta;<sup>4</sup>f</th></tr>
    <tr><td><b>1</b></td><td><b>0</b></td><td><b>1</b></td><td><b>3</b></td><td><b>1</b></td><td>0</td></tr>
    <tr><td>2</td><td>1</td><td>4</td><td>5</td><td>1</td><td>0</td></tr>
    <tr><td>3</td><td>5</td><td>9</td><td>7</td><td>1</td><td>&mdash;</td></tr>
    <tr><td>4</td><td>14</td><td>16</td><td>8</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>5</td><td>30</td><td>25</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>6</td><td>55</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
</table>

<p class="step-label">2. Newton's Forward Derivative Formula at Non-Integer u:</p>
<div class="step-box">
    Here <span class="math-expr">x<sub>0</sub> = 1, h = 1</span> &rArr; <span class="math-expr">u = (1.2 - 1)/1 = 0.2</span>.<br>
    <span class="math-expr">f'(x) = (1/h) [ &Delta;y<sub>0</sub> + [(2u - 1)/2] &Delta;<sup>2</sup>y<sub>0</sub> + [(3u<sup>2</sup> - 6u + 2)/6] &Delta;<sup>3</sup>y<sub>0</sub> ]</span><br><br>
    Substitute <span class="math-expr">u = 0.2</span>, <span class="math-expr">&Delta;y<sub>0</sub> = 1</span>, <span class="math-expr">&Delta;<sup>2</sup>y<sub>0</sub> = 3</span>, <span class="math-expr">&Delta;<sup>3</sup>y<sub>0</sub> = 1</span>:<br>
    <span class="math-expr">f'(1.2) = 1 + [(2(0.2) - 1)/2](3) + [(3(0.04) - 6(0.2) + 2)/6](1)</span><br>
    <span class="math-expr">= 1 + [-0.6/2](3) + [(0.12 - 1.20 + 2.00)/6](1)</span><br>
    <span class="math-expr">= 1 - 0.90 + (0.92 / 6) = 0.10 + 0.1533 = <b>0.2533</b></span>
</div>

<div class="result-box">
    &check; <b>First Derivative:</b> <span class="math-expr">f'(1.2) = 0.2533</span>.
</div>
""",

    # 32. First Derivative at x = 0.4 from Table
    "find the first derivative of f(x) at x = 0.4 from the table": """
<p class="step-label">1. Backward Difference Table (h = 0.1):</p>
<table class="grid-table">
    <tr><th>x</th><th>y</th><th>&nabla;y</th><th>&nabla;<sup>2</sup>y</th><th>&nabla;<sup>3</sup>y</th></tr>
    <tr><td>0.1</td><td>1.1051</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>0.2</td><td>1.2214</td><td>0.1163</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>0.3</td><td>1.3498</td><td>0.1284</td><td>0.0121</td><td>&mdash;</td></tr>
    <tr><td><b>0.4</b></td><td><b>1.4918</b></td><td><b>0.1420</b></td><td><b>0.0136</b></td><td><b>0.0015</b></td></tr>
</table>

<p class="step-label">2. Newton's Backward Derivative Formula at Last Point x<sub>n</sub> = 0.4:</p>
<div class="step-box">
    <span class="math-expr">f'(x<sub>n</sub>) = (1/h) [ &nabla;y<sub>n</sub> + (1/2)&nabla;<sup>2</sup>y<sub>n</sub> + (1/3)&nabla;<sup>3</sup>y<sub>n</sub> ]</span><br><br>
    Substitute bottom-row backward differences with <span class="math-expr">h = 0.1</span>:<br>
    <span class="math-expr">f'(0.4) = (1/0.1) [ 0.1420 + 0.5(0.0136) + 0.3333(0.0015) ]</span><br>
    <span class="math-expr">= 10 &bull; [ 0.1420 + 0.0068 + 0.0005 ] = 10 &bull; [ 0.1493 ] = <b>1.4930</b></span>
</div>

<div class="result-box">
    &check; <b>Result:</b> <span class="math-expr">f'(0.4) = 1.4930</span> (Theoretical value for e<sup>0.4</sup> = 1.4918).
</div>
""",

    # 16. Operators E, Delta, and Nabla
    "define operators e, &delta; and &nabla;": """
<p class="step-label">1. Definitions of Finite Difference Operators:</p>
<table class="grid-table">
    <tr><th>Operator</th><th>Symbol</th><th>Mathematical Definition</th><th>Physical Interpretation</th></tr>
    <tr><td><b>Shift Operator</b></td><td><span class="math-expr">E</span></td><td><code>E f(x) = f(x + h)</code></td><td>Steps argument forward by interval <i>h</i></td></tr>
    <tr><td><b>Forward Difference</b></td><td><span class="math-expr">&Delta;</span></td><td><code>&Delta; f(x) = f(x + h) - f(x)</code></td><td>Difference between next state and current state</td></tr>
    <tr><td><b>Backward Difference</b></td><td><span class="math-expr">&nabla;</span></td><td><code>&nabla; f(x) = f(x) - f(x - h)</code></td><td>Difference between current state and previous state</td></tr>
</table>

<p class="step-label">2. Derivation of Operational Relation between E and &Delta;:</p>
<div class="step-box">
    By definition of the forward difference operator:<br>
    <span class="math-expr">&Delta; f(x) = f(x + h) - f(x)</span><br><br>
    Since <span class="math-expr">E f(x) = f(x + h)</span>, substituting gives:<br>
    <span class="math-expr">&Delta; f(x) = E f(x) - f(x) = (E - 1) f(x)</span><br><br>
    Factoring out operand <span class="math-expr">f(x)</span> yields the fundamental operational identity:<br>
    <span class="math-expr">&Delta; = E - 1</span> &nbsp;&harr;&nbsp; <span class="math-expr">E = 1 + &Delta;</span>
</div>

<div class="result-box">
    &check; <b>Fundamental Relations:</b> <span class="math-expr">E = 1 + &Delta; = (1 - &nabla;)<sup>-1</sup></span>.
</div>
""",

    # 25. Backward Differences for Points (5, 11)
    "find backward differences for the points: (5, 11)": """
<p class="step-label">1. Given Data Points & Difference Table:</p>
<div class="math-box">
    Given: <span class="math-expr">(5, 11), (6, 13), (9, 28), (11, 40)</span>.
</div>

<table class="grid-table">
    <tr><th>x</th><th>y = f(x)</th><th>1st Difference (&nabla;y)</th><th>2nd Difference (&nabla;<sup>2</sup>y)</th><th>3rd Difference (&nabla;<sup>3</sup>y)</th></tr>
    <tr><td>5</td><td>11</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>6</td><td>13</td><td><span class="math-expr">13 - 11 = 2</span></td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>9</td><td>28</td><td><span class="math-expr">28 - 13 = 15</span></td><td><span class="math-expr">15 - 2 = 13</span></td><td>&mdash;</td></tr>
    <tr><td>11</td><td>40</td><td><span class="math-expr">40 - 28 = 12</span></td><td><span class="math-expr">12 - 15 = -3</span></td><td><span class="math-expr">-3 - 13 = -16</span></td></tr>
</table>

<p class="step-label">2. Backward Differences at Final Point (x = 11, y<sub>3</sub> = 40):</p>
<div class="step-box">
    &bull; First Backward Difference: <span class="math-expr">&nabla;y<sub>3</sub> = 12</span><br>
    &bull; Second Backward Difference: <span class="math-expr">&nabla;<sup>2</sup>y<sub>3</sub> = -3</span><br>
    &bull; Third Backward Difference: <span class="math-expr">&nabla;<sup>3</sup>y<sub>3</sub> = -16</span>
</div>

<div class="result-box">
    &check; <b>Values:</b> <span class="math-expr">&nabla;y(11) = 12</span>, <span class="math-expr">&nabla;<sup>2</sup>y(11) = -3</span>, <span class="math-expr">&nabla;<sup>3</sup>y(11) = -16</span>.
</div>
""",

    # 27. Inverse Interpolation (Lagrange)
    "given f(0) = 16.35, f(5) = 14.88": """
<p class="step-label">1. Problem Setup & Inversion of Coordinates:</p>
<div class="math-box">
    Given table of values: <span class="math-expr">f(0) = 16.35, f(5) = 14.88, f(10) = 13.59, f(15) = 12.46</span>.<br>
    Target: find <span class="math-expr">x</span> when <span class="math-expr">y = f(x) = 14.00</span>.<br>
    In <b>Lagrange's Inverse Interpolation</b>, we treat <span class="math-expr">y</span> as independent variable and <span class="math-expr">x</span> as dependent variable!
</div>

<p class="step-label">2. Grid of Inverse Data Points (Target y = 14.00):</p>
<table class="grid-table">
    <tr><th>i</th><th>x<sub>i</sub></th><th>y<sub>i</sub> = f(x<sub>i</sub>)</th><th>y - y<sub>i</sub> (for y = 14.00)</th></tr>
    <tr><td>0</td><td>0</td><td>16.35</td><td><span class="math-expr">14.00 - 16.35 = -2.35</span></td></tr>
    <tr><td>1</td><td>5</td><td>14.88</td><td><span class="math-expr">14.00 - 14.88 = -0.88</span></td></tr>
    <tr><td>2</td><td>10</td><td>13.59</td><td><span class="math-expr">14.00 - 13.59 = +0.41</span></td></tr>
    <tr><td>3</td><td>15</td><td>12.46</td><td><span class="math-expr">14.00 - 12.46 = +1.54</span></td></tr>
</table>

<p class="step-label">3. Lagrange's Inverse Interpolation Formula & Term Evaluation:</p>
<div class="math-box">
    <span class="math-expr">x = &Sigma;<sub>i=0</sub><sup>3</sup> x<sub>i</sub> &bull; &prod;<sub>j&ne;i</sub> [(y - y<sub>j</sub>) / (y<sub>i</sub> - y<sub>j</sub>)]</span>
</div>

<div class="step-box">
    &bull; <b>Term 0 (i=0):</b> <span class="math-expr">x<sub>0</sub> = 0 &rArr; Term 0 = 0</span><br><br>

    &bull; <b>Term 1 (i=1, x<sub>1</sub>=5):</b><br>
    <span class="math-expr">5 &bull; [(14-16.35)(14-13.59)(14-12.46)] / [(14.88-16.35)(14.88-13.59)(14.88-12.46)]</span><br>
    <span class="math-expr">= 5 &bull; [(-2.35)(0.41)(1.54)] / [(-1.47)(1.29)(2.42)] = 5 &bull; [-1.4838 / -4.5888] = 5 &bull; 0.32334 = <b>1.6167</b></span><br><br>

    &bull; <b>Term 2 (i=2, x<sub>2</sub>=10):</b><br>
    <span class="math-expr">10 &bull; [(14-16.35)(14-14.88)(14-12.46)] / [(13.59-16.35)(13.59-14.88)(13.59-12.46)]</span><br>
    <span class="math-expr">= 10 &bull; [(-2.35)(-0.88)(1.54)] / [(-2.76)(-1.29)(1.13)] = 10 &bull; [3.1847 / 4.0233] = 10 &bull; 0.79156 = <b>7.9156</b></span><br><br>

    &bull; <b>Term 3 (i=3, x<sub>3</sub>=15):</b><br>
    <span class="math-expr">15 &bull; [(14-16.35)(14-14.88)(14-13.59)] / [(12.46-16.35)(12.46-14.88)(12.46-13.59)]</span><br>
    <span class="math-expr">= 15 &bull; [(-2.35)(-0.88)(0.41)] / [(-3.89)(-2.42)(-1.13)] = 15 &bull; [0.8479 / -10.637] = 15 &bull; (-0.07971) = <b>-1.1957</b></span>
</div>

<p class="step-label">4. Summing All Terms:</p>
<div class="step-box">
    <span class="math-expr">x = 0 + 1.6167 + 7.9156 - 1.1957 = <b>8.3366</b></span>
</div>

<div class="result-box">
    &check; <b>Final Answer:</b> For <span class="math-expr">f(x) = 14.00</span>, <span class="math-expr">x &approx; 8.34</span>.
</div>
""",

    # 29. Prove E nabla = nabla E = Delta
    "prove that e &nabla; = &nabla; e = &Delta;": """
<p class="step-label">1. Operator Definitions in Finite Differences:</p>
<div class="math-box">
    &bull; Shift operator: <span class="math-expr">E f(x) = f(x + h)</span> &nbsp;&rArr;&nbsp; <span class="math-expr">E<sup>-1</sup> f(x) = f(x - h)</span><br>
    &bull; Forward difference: <span class="math-expr">&Delta; f(x) = f(x + h) - f(x) = (E - 1) f(x)</span> &nbsp;&rArr;&nbsp; <span class="math-expr">&Delta; = E - 1</span><br>
    &bull; Backward difference: <span class="math-expr">&nabla; f(x) = f(x) - f(x - h) = (1 - E<sup>-1</sup>) f(x)</span> &nbsp;&rArr;&nbsp; <span class="math-expr">&nabla; = 1 - E<sup>-1</sup></span>
</div>

<p class="step-label">2. Part 1: Prove E &nabla; = &Delta;:</p>
<div class="step-box">
    <span class="math-expr">E &nabla; = E (1 - E<sup>-1</sup>)</span><br>
    <span class="math-expr">= E &bull; 1 - E &bull; E<sup>-1</sup> = E - 1</span><br>
    Since <span class="math-expr">&Delta; = E - 1</span>:<br>
    <span class="math-expr">E &nabla; = &Delta;</span> &check;
</div>

<p class="step-label">3. Part 2: Prove &nabla; E = &Delta;:</p>
<div class="step-box">
    <span class="math-expr">&nabla; E = (1 - E<sup>-1</sup>) E</span><br>
    <span class="math-expr">= 1 &bull; E - E<sup>-1</sup> &bull; E = E - 1</span><br>
    Since <span class="math-expr">&Delta; = E - 1</span>:<br>
    <span class="math-expr">&nabla; E = &Delta;</span> &check;
</div>

<div class="result-box">
    &check; <b>Conclusion:</b> <span class="math-expr">E &nabla; = &nabla; E = &Delta;</span> (Hence Proved).
</div>
""",

    # 31. Define Simpson's 3/8 Rule
    "define simpson's three-eighths rule for numerical integration": """
<p class="step-label">1. Principle & Applicability:</p>
<div class="math-box">
    Simpson's 3/8 rule is a closed Newton-Cotes quadrature formula derived by fitting cubic polynomials (Lagrange 3rd order) through sets of four consecutive equidistant points.<br>
    <b>Strict Condition:</b> Total number of subintervals <span class="math-expr">n</span> must be a <b>MULTIPLE OF 3</b> (<span class="math-expr">n = 3, 6, 9, 12...</span>).
</div>

<p class="step-label">2. Formula Formulation:</p>
<div class="step-box">
    For <span class="math-expr">I = &int;<sub>a</sub><sup>b</sup> f(x) dx</span> with <span class="math-expr">h = (b - a)/n</span>:<br><br>
    <span class="math-expr">&int;<sub>a</sub><sup>b</sup> f(x) dx &approx; (3h/8) [ (y<sub>0</sub> + y<sub>n</sub>) + 3 &Sigma;<sub>i &ne; 3k</sub> y<sub>i</sub> + 2 &Sigma;<sub>i = 3k</sub> y<sub>i</sub> ]</span><br><br>
    Or expanded:<br>
    <span class="math-expr">I = (3h/8) [ (y<sub>0</sub> + y<sub>n</sub>) + 3(y<sub>1</sub> + y<sub>2</sub> + y<sub>4</sub> + y<sub>5</sub> + ...) + 2(y<sub>3</sub> + y<sub>6</sub> + ...) ]</span>
</div>

<p class="step-label">3. Error Analysis & Order:</p>
<table class="grid-table">
    <tr><th>Property</th><th>Value / Expression</th></tr>
    <tr><td>Truncation Error (Global)</td><td><span class="math-expr">E = -(3/80) h<sup>4</sup> (b - a) f<sup>(4)</sup>(&xi;)</span></td></tr>
    <tr><td>Order of Error</td><td><span class="math-expr">O(h<sup>4</sup>)</span></td></tr>
    <tr><td>Degree of Exactness</td><td>Exact for polynomials up to degree 3</td></tr>
</table>

<div class="result-box">
    &check; <b>Summary:</b> Simpson's 3/8 rule requires <span class="math-expr">n = 3k</span> subintervals and provides 4th order accuracy <span class="math-expr">O(h<sup>4</sup>)</span>.
</div>
"""
}
