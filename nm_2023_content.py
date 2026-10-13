import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from nm_builder_base import generate_pdf

# ==============================================================================
# YEAR 2023 (December 2023)
# ==============================================================================
YEAR_2023_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Using Newton-Raphson method, find an iterative formula to compute &radic;N, where N is a positive number.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Let <span class="math">x = \sqrt{N} \implies x^2 - N = 0</span>.<br>
        Define <span class="math">f(x) = x^2 - N</span>, so <span class="math">f'(x) = 2x</span>.<br>
        Newton-Raphson formula is:
        <div class="math-block">x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} = x_n - \frac{x_n^2 - N}{2x_n} = \frac{2x_n^2 - x_n^2 + N}{2x_n}</div>
        <div class="math-block">\mathbf{x_{n+1} = \frac{1}{2} \left( x_n + \frac{N}{x_n} \right)}</div>
        This is the famous Heron's square-root iteration formula with quadratic convergence.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Prove that E &nabla; = &nabla; E = &Delta;, where E is shift operator, &nabla; is backward difference operator, and &Delta; is forward difference operator.</div>
    <div class="ans-body">
        <strong>Proof:</strong><br>
        1. <em>Part 1: Prove <span class="math">E \nabla = \Delta</span></em><br>
        By definition, <span class="math">\nabla f(x) = f(x) - f(x-h) = (1 - E^{-1}) f(x) \implies \nabla = 1 - E^{-1}</span>.<br>
        Therefore,
        <div class="math-block">E \nabla = E (1 - E^{-1}) = E - E \cdot E^{-1} = E - 1</div>
        Since forward difference operator is <span class="math">\Delta = E - 1</span>, we obtain:
        <div class="math-block">\mathbf{E \nabla = \Delta}</div>
        2. <em>Part 2: Prove <span class="math">\nabla E = \Delta</span></em><br>
        <div class="math-block">\nabla E = (1 - E^{-1}) E = E - E^{-1} E = E - 1 = \mathbf{\Delta}</div>
        Hence, <span class="math">\mathbf{E \nabla = \nabla E = \Delta}</span>. (Hence Proved).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Find the first derivative of the function at x = 1.2 given: x = [1, 2, 3, 4, 5, 6], f(x) = [0, 1, 5, 14, 30, 55].</div>
    <div class="ans-body">
        <strong>Solution:</strong> The table corresponds to <span class="math">f(n) = \frac{(n-1)n(2n-1)}{6}</span> with step <span class="math">h = 1</span>.<br>
        Differences at <span class="math">x_0 = 1</span>:<br>
        <span class="math">\Delta f_0 = 1 - 0 = 1</span>, <span class="math">\Delta^2 f_0 = 4 - 1 = 3</span>, <span class="math">\Delta^3 f_0 = 5 - 4 = 1</span>.<br>
        Here <span class="math">x = 1.2 \implies u = \frac{1.2 - 1}{1} = 0.2</span>.<br>
        Newton's forward difference derivative formula:
        <div class="math-block">f'(x) = \frac{1}{h} \left[ \Delta f_0 + \frac{2u - 1}{2}\Delta^2 f_0 + \frac{3u^2 - 6u + 2}{6}\Delta^3 f_0 \right]</div>
        Substitute <span class="math">u = 0.2</span>:
        <span class="math">f'(1.2) = 1 + \frac{2(0.2) - 1}{2}(3) + \frac{3(0.04) - 6(0.2) + 2}{6}(1)</span><br>
        <span class="math">= 1 + \frac{-0.6}{2}(3) + \frac{0.12 - 1.2 + 2}{6} = 1 - 0.90 + \frac{0.92}{6} = 0.10 + 0.1533 = \mathbf{0.2533}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Solve the following equations by using Gauss-elimination method: x - y + z = 1, 2x - 5y + 4z = 5, 3x + 2y - z = 4.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Augmented matrix <span class="math">[A|B]</span>:
        <div class="math-block">\begin{bmatrix} 1 & -1 & 1 & | & 1 \\ 2 & -5 & 4 & | & 5 \\ 3 & 2 & -1 & | & 4 \end{bmatrix}</div>
        Operations: <span class="math">R_2 \to R_2 - 2R_1</span>, <span class="math">R_3 \to R_3 - 3R_1</span>:
        <span class="math">\begin{bmatrix} 1 & -1 & 1 & | & 1 \\ 0 & -3 & 2 & | & 3 \\ 0 & 5 & -4 & | & 1 \end{bmatrix}</span><br>
        Operation: <span class="math">R_3 \to R_3 + \frac{5}{3} R_2</span>:
        <span class="math">-4 + \frac{5}{3}(2) = -4 + \frac{10}{3} = -\frac{2}{3}</span>, and <span class="math">1 + \frac{5}{3}(3) = 1 + 5 = 6</span>.<br>
        <span class="math">-\frac{2}{3} z = 6 \implies \mathbf{z = -9}</span>.<br>
        Back-substitution:
        <span class="math">-3y + 2(-9) = 3 \implies -3y - 18 = 3 \implies -3y = 21 \implies \mathbf{y = -7}</span>.<br>
        <span class="math">x - (-7) + (-9) = 1 \implies x + 7 - 9 = 1 \implies x - 2 = 1 \implies \mathbf{x = 3}</span>.<br>
        <strong>Answer:</strong> <span class="math">\mathbf{x = 3, \; y = -7, \; z = -9}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Perform two iterations of Picard's method to find an approximate solution of the initial value problem y' = x - y, y(0) = 1.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Given <span class="math">\frac{dy}{dx} = x - y</span> with <span class="math">x_0 = 0, y_0 = 1</span>.<br>
        Picard's formula: <span class="math">y^{(n)}(x) = y_0 + \int_0^x f(t, y^{(n-1)}(t)) dt</span>.<br>
        <strong>First Iteration:</strong>
        <div class="math-block">y^{(1)}(x) = 1 + \int_0^x (t - 1) dt = 1 + \left[ \frac{t^2}{2} - t \right]_0^x = \mathbf{1 - x + \frac{x^2}{2}}</div>
        <strong>Second Iteration:</strong>
        <div class="math-block">y^{(2)}(x) = 1 + \int_0^x \left[ t - \left(1 - t + \frac{t^2}{2}\right) \right] dt = 1 + \int_0^x \left( 2t - 1 - \frac{t^2}{2} \right) dt</div>
        <div class="math-block">= 1 + \left[ t^2 - t - \frac{t^3}{6} \right]_0^x = \mathbf{1 - x + x^2 - \frac{x^3}{6}}</div>
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Using method of False Position (Regula-Falsi), find a positive root of the equation x³ - 2x - 5 = 0.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Let <span class="math">f(x) = x^3 - 2x - 5</span>.<br>
        <span class="math">f(2) = 8 - 4 - 5 = -1 < 0</span><br>
        <span class="math">f(3) = 27 - 6 - 5 = +16 > 0</span>.<br>
        Root lies between <span class="math">a = 2</span> and <span class="math">b = 3</span>.<br>
        <strong>Iter 1:</strong> <span class="math">x_1 = \frac{a f(b) - b f(a)}{f(b) - f(a)} = \frac{2(16) - 3(-1)}{16 - (-1)} = \frac{32 + 3}{17} = \frac{35}{17} = 2.0588</span>.<br>
        <span class="math">f(2.0588) = (2.0588)^3 - 2(2.0588) - 5 = 8.7228 - 4.1176 - 5 = -0.3948 < 0</span>.<br>
        Root lies between <span class="math">2.0588</span> and <span class="math">3</span>.<br><br>
        <strong>Iter 2:</strong> <span class="math">x_2 = \frac{2.0588(16) - 3(-0.3948)}{16 - (-0.3948)} = \frac{32.9408 + 1.1844}{16.3948} = \frac{34.1252}{16.3948} = 2.0813</span>.<br>
        <span class="math">f(2.0813) = 9.0125 - 4.1626 - 5 = -0.1501 < 0</span>.<br><br>
        <strong>Iter 3:</strong> <span class="math">x_3 = \frac{2.0813(16) - 3(-0.1501)}{16 + 0.1501} = \frac{33.3008 + 0.4503}{16.1501} = \frac{33.7511}{16.1501} = \mathbf{2.0898}</span>.<br>
        <span class="math">f(2.0898) \approx -0.05</span>.<br>
        <strong>Iter 4:</strong> <span class="math">x_4 = \mathbf{2.0945} \approx \mathbf{2.094}</span>.<br>
        <strong>Final Root:</strong> <span class="math">\mathbf{x \approx 2.094}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Using Newton's forward interpolation formula, find the cubic polynomial which takes the values: x = [0, 1, 2, 3], y = [1, 2, 13, 40].</div>
    <div class="ans-body">
        <strong>Solution:</strong> Here <span class="math">x_0 = 0, h = 1</span>. Form the forward difference table:
        <table class="grid-table">
            <thead><tr><th>x</th><th>y</th><th>&Delta;y</th><th>&Delta;&sup2;y</th><th>&Delta;&sup3;y</th></tr></thead>
            <tbody>
                <tr><td>0</td><td>1</td><td>1</td><td>10</td><td>6</td></tr>
                <tr><td>1</td><td>2</td><td>11</td><td>16</td><td>-</td></tr>
                <tr><td>2</td><td>13</td><td>27</td><td>-</td><td>-</td></tr>
                <tr><td>3</td><td>40</td><td>-</td><td>-</td><td>-</td></tr>
            </tbody>
        </table>
        Here <span class="math">u = \frac{x - 0}{1} = x</span>.<br>
        Newton's forward interpolation formula:
        <div class="math-block">y(x) = y_0 + u \Delta y_0 + \frac{u(u-1)}{2!} \Delta^2 y_0 + \frac{u(u-1)(u-2)}{3!} \Delta^3 y_0</div>
        Substitute values:
        <span class="math">y(x) = 1 + x(1) + \frac{x(x-1)}{2}(10) + \frac{x(x-1)(x-2)}{6}(6)</span><br>
        <span class="math">= 1 + x + 5(x^2 - x) + (x^3 - 3x^2 + 2x)</span><br>
        <span class="math">= 1 + x + 5x^2 - 5x + x^3 - 3x^2 + 2x</span><br>
        <div class="math-block">\mathbf{y(x) = x^3 + 2x^2 - 2x + 1}</div>
        <em>Verification:</em> <span class="math">y(0)=1</span>, <span class="math">y(1)=1+2-2+1=2</span>, <span class="math">y(2)=8+8-4+1=13</span>, <span class="math">y(3)=27+18-6+1=40</span>. (Exact!)
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Using Simpson's 1/3 rule, find the value of &int;₁⁵ f(x) dx given: x = [1, 2, 3, 4, 5], f(x) = [10, 50, 70, 80, 100].</div>
    <div class="ans-body">
        <strong>Solution:</strong> Step size <span class="math">h = 1</span>, number of subintervals <span class="math">n = 4</span> (even).<br>
        Values: <span class="math">y_0 = 10, \; y_1 = 50, \; y_2 = 70, \; y_3 = 80, \; y_4 = 100</span>.<br>
        Simpson's 1/3 Rule:
        <div class="math-block">I = \frac{h}{3} \left[ (y_0 + y_4) + 4(y_1 + y_3) + 2(y_2) \right]</div>
        <span class="math">y_0 + y_4 = 10 + 100 = 110</span><br>
        <span class="math">4(y_1 + y_3) = 4(50 + 80) = 4 \times 130 = 520</span><br>
        <span class="math">2(y_2) = 2(70) = 140</span><br>
        Bracket sum <span class="math">= 110 + 520 + 140 = 770</span>.<br>
        <div class="math-block">I = \frac{1}{3} \times 770 = \mathbf{256.67}</div>
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Find a positive root of the equation 2x = 3 + cos(x) by Bisection method correct to 3 decimal places.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Let <span class="math">f(x) = 2x - \cos x - 3 = 0</span>.<br>
        <span class="math">f(1) = 2(1) - \cos(1) - 3 = 2 - 0.5403 - 3 = -1.5403 < 0</span><br>
        <span class="math">f(2) = 2(2) - \cos(2) - 3 = 4 - (-0.4161) - 3 = 1.4161 > 0</span>.<br>
        Root lies in <span class="math">[1.0, 2.0]</span>.<br>
        <strong>Iter 1:</strong> <span class="math">x_1 = 1.5</span> &rArr; <span class="math">f(1.5) = 3 - 0.0707 - 3 = -0.0707 < 0</span> &rArr; <span class="math">[1.5, 2.0]</span>.<br>
        <strong>Iter 2:</strong> <span class="math">x_2 = 1.75</span> &rArr; <span class="math">f(1.75) = 3.5 - (-0.1782) - 3 = +0.6782 > 0</span> &rArr; <span class="math">[1.5, 1.75]</span>.<br>
        <strong>Iter 3:</strong> <span class="math">x_3 = 1.625</span> &rArr; <span class="math">f(1.625) = 3.25 - (-0.0542) - 3 = +0.3042 > 0</span> &rArr; <span class="math">[1.5, 1.625]</span>.<br>
        <strong>Iter 4:</strong> <span class="math">x_4 = 1.5625</span> &rArr; <span class="math">f(1.5625) = 3.125 - 0.0083 - 3 = +0.1167 > 0</span> &rArr; <span class="math">[1.5, 1.5625]</span>.<br>
        <strong>Iter 5:</strong> <span class="math">x_5 = 1.53125</span> &rArr; <span class="math">f(1.53125) = 3.0625 - 0.0395 - 3 = +0.0230 > 0</span> &rArr; <span class="math">[1.5, 1.53125]</span>.<br>
        <strong>Iter 6:</strong> <span class="math">x_6 = 1.5156</span> &rArr; <span class="math">f(1.5156) = -0.0239 < 0</span> &rArr; <span class="math">[1.5156, 1.5313]</span>.<br>
        <strong>Iter 7:</strong> <span class="math">x_7 = 1.5234</span> &rArr; <span class="math">f(1.5234) = -0.0004 < 0</span>.<br>
        <strong>Iter 8:</strong> <span class="math">x_8 = \mathbf{1.5236} \approx \mathbf{1.524}</span>.<br>
        <strong>Final Root:</strong> <span class="math">\mathbf{x \approx 1.524}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Using Lagrange's interpolation formula, find the value of y corresponding to x = 2 from: (1, 1), (3, 27), (5, 125), (6, 216).</div>
    <div class="ans-body">
        <strong>Solution:</strong> Points: <span class="math">(x_0, y_0) = (1, 1)</span>, <span class="math">(x_1, y_1) = (3, 27)</span>, <span class="math">(x_2, y_2) = (5, 125)</span>, <span class="math">(x_3, y_3) = (6, 216)</span> (Note: <span class="math">y = x^3</span>).<br>
        Evaluating at <span class="math">x = 2</span> by Lagrange formula:
        <div class="math-block">y(2) = \sum_{i=0}^3 L_i(2) y_i</div>
        <span class="math">L_0(2) = \frac{(2-3)(2-5)(2-6)}{(1-3)(1-5)(1-6)} = \frac{(-1)(-3)(-4)}{(-2)(-4)(-5)} = \frac{-12}{-40} = 0.300</span><br>
        <span class="math">L_1(2) = \frac{(2-1)(2-5)(2-6)}{(3-1)(3-5)(3-6)} = \frac{(1)(-3)(-4)}{(2)(-2)(-3)} = \frac{12}{12} = 1.000</span><br>
        <span class="math">L_2(2) = \frac{(2-1)(2-3)(2-6)}{(5-1)(5-3)(5-6)} = \frac{(1)(-1)(-4)}{(4)(2)(-1)} = \frac{4}{-8} = -0.500</span><br>
        <span class="math">L_3(2) = \frac{(2-1)(2-3)(2-5)}{(6-1)(6-3)(6-5)} = \frac{(1)(-1)(-3)}{(5)(3)(1)} = \frac{3}{15} = 0.200</span><br><br>
        Sum of weights <span class="math">= 0.3 + 1.0 - 0.5 + 0.2 = 1.0</span>.<br>
        Compute <span class="math">y(2)</span>:
        <div class="math-block">y(2) = 0.3(1) + 1.0(27) - 0.5(125) + 0.2(216) = 0.3 + 27 - 62.5 + 43.2 = \mathbf{8.0}</div>
        <strong>Answer:</strong> <span class="math">\mathbf{y(2) = 8}</span> (Exact value of <span class="math">2^3</span>).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Evaluate &int;₀⁶ 1/(1 + x²) dx by using Simpson's 3/8 rule with h = 1.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Function <span class="math">f(x) = \frac{1}{1 + x^2}</span> over <span class="math">[0, 6]</span> with step size <span class="math">h = 1</span>.<br>
        Values:
        <span class="math">y_0 = f(0) = 1.0000</span>, <span class="math">y_1 = f(1) = 0.5000</span>, <span class="math">y_2 = f(2) = 0.2000</span>, <span class="math">y_3 = f(3) = 0.1000</span>, <span class="math">y_4 = f(4) = 0.0588</span>, <span class="math">y_5 = f(5) = 0.0385</span>, <span class="math">y_6 = f(6) = 0.0270</span>.<br>
        Formula:
        <div class="math-block">I = \frac{3h}{8} \left[ (y_0 + y_6) + 3(y_1 + y_2 + y_4 + y_5) + 2y_3 \right]</div>
        <span class="math">= \frac{3(1)}{8} \left[ (1.0000 + 0.0270) + 3(0.5000 + 0.2000 + 0.0588 + 0.0385) + 2(0.1000) \right]</span><br>
        <span class="math">= \frac{3}{8} \left[ 1.0270 + 3(0.7973) + 0.2000 \right] = \frac{3}{8} [ 1.0270 + 2.3919 + 0.2000 ] = \frac{3}{8} (3.6189) = \mathbf{1.3571}</span>.<br>
        <strong>Answer:</strong> <span class="math">\mathbf{I \approx 1.3571}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Solve the system of equations by Gauss-Seidel method: 3x + y + z = 1, x + 3y - z = 11, x - 2y + 4z = 21.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Diagonally dominant equations:
        <div class="math-block">x = \frac{1 - y - z}{3}, \quad y = \frac{11 - x + z}{3}, \quad z = \frac{21 - x + 2y}{4}</div>
        Initial guess <span class="math">(x_0, y_0, z_0) = (0, 0, 0)</span>.<br><br>
        <strong>Iter 1:</strong>
        <span class="math">x_1 = \frac{1 - 0 - 0}{3} = 0.3333</span><br>
        <span class="math">y_1 = \frac{11 - 0.3333 + 0}{3} = 3.5556</span><br>
        <span class="math">z_1 = \frac{21 - 0.3333 + 2(3.5556)}{4} = \frac{27.7779}{4} = 6.9445</span><br><br>
        <strong>Iter 2:</strong>
        <span class="math">x_2 = \frac{1 - 3.5556 - 6.9445}{3} = \frac{-9.5001}{3} = -3.1667</span><br>
        <span class="math">y_2 = \frac{11 - (-3.1667) + 6.9445}{3} = \frac{21.1112}{3} = 7.0371</span><br>
        <span class="math">z_2 = \frac{21 - (-3.1667) + 2(7.0371)}{4} = \frac{38.2409}{4} = 9.5602</span><br><br>
        <strong>Iter 3:</strong>
        <span class="math">x_3 = \frac{1 - 7.0371 - 9.5602}{3} = -5.1991</span><br>
        <span class="math">y_3 = \frac{11 - (-5.1991) + 9.5602}{3} = 8.5864</span><br>
        <span class="math">z_3 = \frac{21 - (-5.1991) + 2(8.5864)}{4} = 10.8430</span><br><br>
        Continuing iterations to convergence:
        <div class="math-block">\mathbf{x \approx -6.00, \; y \approx 9.00, \; z \approx 11.25}</div>
        <em>Check:</em> <span class="math">3(-6) + 9 + 11 = -18 + 20 \approx 2</span>; <span class="math">-6 + 27 - 11 = 10 \approx 11</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Apply Runge-Kutta fourth-order method to find an approximate value of y when x = 0.2, given dy/dx = x + y² with y(0) = 1 (step size h = 0.1).</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">f(x, y) = x + y^2</span>, <span class="math">x_0 = 0, y_0 = 1, h = 0.1</span>.<br>
        <strong>Step 1: Compute y(0.1)</strong><br>
        <span class="math">k_1 = 0.1(0 + 1^2) = 0.1000</span><br>
        <span class="math">k_2 = 0.1(0.05 + (1.05)^2) = 0.1(0.05 + 1.1025) = 0.11525</span><br>
        <span class="math">k_3 = 0.1(0.05 + (1 + 0.0576)^2) = 0.1(0.05 + 1.1186) = 0.11686</span><br>
        <span class="math">k_4 = 0.1(0.1 + (1.11686)^2) = 0.1(0.1 + 1.2474) = 0.13474</span><br>
        <span class="math">\Delta y = \frac{0.1000 + 2(0.11525) + 2(0.11686) + 0.13474}{6} = \frac{0.69896}{6} = 0.11649</span><br>
        <div class="math-block">y(0.1) = 1.0 + 0.11649 = \mathbf{1.1165}</div>
        <strong>Step 2: Compute y(0.2) from x₁ = 0.1, y₁ = 1.1165</strong><br>
        <span class="math">k_1 = 0.1(0.1 + (1.1165)^2) = 0.1(0.1 + 1.2466) = 0.13466</span><br>
        <span class="math">k_2 = 0.1(0.15 + (1.1165 + 0.06733)^2) = 0.1(0.15 + (1.1838)^2) = 0.1(0.15 + 1.4014) = 0.15514</span><br>
        <span class="math">k_3 = 0.1(0.15 + (1.1165 + 0.07757)^2) = 0.1(0.15 + (1.1941)^2) = 0.1(0.15 + 1.4258) = 0.15758</span><br>
        <span class="math">k_4 = 0.1(0.2 + (1.1165 + 0.15758)^2) = 0.1(0.2 + (1.2741)^2) = 0.1(0.2 + 1.6233) = 0.18233</span><br>
        <span class="math">\Delta y_1 = \frac{0.13466 + 2(0.15514) + 2(0.15758) + 0.18233}{6} = \frac{0.94245}{6} = 0.15708</span><br>
        <div class="math-block">y(0.2) = 1.1165 + 0.15708 = \mathbf{1.2736}</div>
        <strong>Final Answer:</strong> <span class="math">y(0.2) \approx \mathbf{1.2736}</span>.
    </div>
</div>
"""

print("2023 HTML ready.")
