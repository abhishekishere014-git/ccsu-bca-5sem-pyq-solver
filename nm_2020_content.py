import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from nm_builder_base import generate_pdf

# ==============================================================================
# YEAR 2020
# ==============================================================================
YEAR_2020_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Find the real root of the equation x³ - x - 1 = 0.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">f(x) = x^3 - x - 1</span>.<br>
        Using Newton-Raphson method with initial guess <span class="math">x_0 = 1.3</span>:
        <span class="math">f'(x) = 3x^2 - 1</span>.<br>
        <span class="math">f(1.3) = 2.197 - 1.3 - 1 = -0.103</span>.<br>
        <span class="math">f'(1.3) = 3(1.69) - 1 = 4.07</span>.<br>
        <span class="math">x_1 = 1.3 - \frac{-0.103}{4.07} = 1.3 + 0.0253 = 1.3253</span>.<br>
        <span class="math">f(1.3253) \approx 0.002</span>.<br>
        <strong>Root:</strong> <span class="math">\mathbf{x \approx 1.325}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Define operators E, &Delta; and &nabla;. Also obtain relation between E and &Delta;.</div>
    <div class="ans-body">
        <strong>Definitions:</strong><br>
        1. <strong>Shift Operator E:</strong> <span class="math">E f(x) = f(x + h)</span>.<br>
        2. <strong>Forward Difference &Delta;:</strong> <span class="math">\Delta f(x) = f(x + h) - f(x)</span>.<br>
        3. <strong>Backward Difference &nabla;:</strong> <span class="math">\nabla f(x) = f(x) - f(x - h)</span>.<br>
        <strong>Relation between E and &Delta;:</strong><br>
        <span class="math">\Delta f(x) = f(x + h) - f(x) = E f(x) - f(x) = (E - 1) f(x) \implies \mathbf{\Delta = E - 1 \iff E = 1 + \Delta}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Given dy/dx = (y - x)/(y + x) with y(0) = 1. Find y(0.3) by Euler's method taking h = 0.1.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">y_{n+1} = y_n + h \frac{y_n - x_n}{y_n + x_n}</span>, <span class="math">h = 0.1</span>.<br>
        1. <span class="math">x_0 = 0, y_0 = 1 \implies y_1 = 1 + 0.1 \left(\frac{1 - 0}{1 + 0}\right) = 1 + 0.1(1) = \mathbf{1.1000}</span> at <span class="math">x = 0.1</span>.<br>
        2. <span class="math">x_1 = 0.1, y_1 = 1.1 \implies y_2 = 1.1 + 0.1 \left(\frac{1.1 - 0.1}{1.1 + 0.1}\right) = 1.1 + 0.1\left(\frac{1.0}{1.2}\right) = 1.1 + 0.0833 = \mathbf{1.1833}</span> at <span class="math">x = 0.2</span>.<br>
        3. <span class="math">x_2 = 0.2, y_2 = 1.1833 \implies y_3 = 1.1833 + 0.1 \left(\frac{1.1833 - 0.2}{1.1833 + 0.2}\right) = 1.1833 + 0.1\left(\frac{0.9833}{1.3833}\right) = 1.1833 + 0.0711 = \mathbf{1.2544}</span> at <span class="math">x = 0.3</span>.<br>
        <strong>Answer:</strong> <span class="math">\mathbf{y(0.3) \approx 1.254}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Define Simpson's three-eighths rule for Numerical Integration.</div>
    <div class="ans-body">
        <strong>Definition:</strong> Simpson's 3/8 rule approximates the integral of <span class="math">f(x)</span> over <span class="math">[a, b]</span> divided into <span class="math">n</span> subintervals where <span class="math">n</span> is a multiple of 3 by fitting cubic polynomials across triplets of intervals:
        <div class="math-block">\int_a^b f(x) \, dx \approx \frac{3h}{8} \left[ (y_0 + y_n) + 3\sum_{i \neq 3k} y_i + 2\sum_{i = 3k} y_i \right]</div>
        The truncation error is of order <span class="math">O(h^4)</span>, specifically <span class="math">E = -\frac{3}{80} h^5 f^{(4)}(\xi)</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What do you understand by Gauss's Elimination method?</div>
    <div class="ans-body">
        <strong>Explanation:</strong> Gauss Elimination is a direct algorithm for solving linear systems <span class="math">AX = B</span> in two stages:
        <ol>
            <li><strong>Forward Elimination:</strong> Performs elementary row operations on the augmented matrix <span class="math">[A|B]</span> to reduce it to an upper triangular form. Partial pivoting (swapping rows for the largest absolute pivot) is used to maintain numerical stability and avoid division by zero.</li>
            <li><strong>Back-Substitution:</strong> Solves the unknowns starting from the last row upwards.</li>
        </ol>
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Use Picard's method to approximate y when x = 0.2, given dy/dx = x² + y² with y(0) = 0.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">x_0 = 0, y_0 = 0</span>.<br>
        <span class="math">y^{(1)}(x) = 0 + \int_0^x (t^2 + 0) dt = \frac{x^3}{3}</span>.<br>
        <span class="math">y^{(2)}(x) = \int_0^x \left( t^2 + \frac{t^6}{9} \right) dt = \frac{x^3}{3} + \frac{x^7}{63}</span>.<br>
        At <span class="math">x = 0.2</span>:
        <span class="math">y(0.2) = \frac{(0.2)^3}{3} + \frac{(0.2)^7}{63} = \frac{0.008}{3} + \frac{0.0000128}{63} = 0.002667 + 0.000000 = \mathbf{0.00267}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Find backward differences for the points: (5, 11), (6, 13), (9, 28), (11, 40).</div>
    <div class="ans-body">
        <strong>Solution:</strong> Since step size is unequal, using divided differences:
        <span class="math">f[5, 6] = \frac{13 - 11}{6 - 5} = 2</span>.<br>
        <span class="math">f[6, 9] = \frac{28 - 13}{9 - 6} = \frac{15}{3} = 5</span>.<br>
        <span class="math">f[9, 11] = \frac{40 - 28}{11 - 9} = \frac{12}{2} = 6</span>.<br>
        Second divided differences:
        <span class="math">f[5, 6, 9] = \frac{5 - 2}{9 - 5} = \frac{3}{4} = 0.75</span>.<br>
        <span class="math">f[6, 9, 11] = \frac{6 - 5}{11 - 6} = \frac{1}{5} = 0.20</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Using Bessel's formula, find y(25) from: x = [20, 24, 28, 32], y = [24, 32, 35, 40].</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">h = 4</span>. Choose origin <span class="math">x_0 = 24</span>. Then <span class="math">u = \frac{25 - 24}{4} = 0.25</span>.<br>
        <span class="math">y_{-1} = 24, y_0 = 32, y_1 = 35, y_2 = 40</span>.<br>
        <span class="math">\Delta y_0 = 35 - 32 = 3</span>, <span class="math">\Delta y_{-1} = 32 - 24 = 8</span>, <span class="math">\Delta y_1 = 40 - 35 = 5</span>.<br>
        <span class="math">\Delta^2 y_{-1} = 3 - 8 = -5</span>, <span class="math">\Delta^2 y_0 = 5 - 3 = 2</span>.<br>
        Bessel's interpolation formula:
        <div class="math-block">y = \frac{y_0 + y_1}{2} + \left(u - \frac{1}{2}\right)\Delta y_0 + \frac{u(u-1)}{4}(\Delta^2 y_{-1} + \Delta^2 y_0)</div>
        <span class="math">\frac{32 + 35}{2} + (0.25 - 0.5)(3) + \frac{0.25(-0.75)}{4}(-5 + 2)</span><br>
        <span class="math">= 33.5 - 0.75 + \frac{-0.1875}{4}(-3) = 32.75 + 0.1406 = \mathbf{32.89}</span>.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Apply Gauss-Seidel iteration method to solve: 20x + y - 2z = 17, 3x + 20y - z = -18, 2x - 3y + 20z = 25.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Iteration equations:
        <div class="math-block">x = \frac{17 - y + 2z}{20}, \quad y = \frac{-18 - 3x + z}{20}, \quad z = \frac{25 - 2x + 3y}{20}</div>
        Iter 1: <span class="math">x_1 = 0.8500, y_1 = -1.0275, z_1 = 1.0109</span>.<br>
        Iter 2: <span class="math">x_2 = 1.0025, y_2 = -0.9998, z_2 = 0.9998</span>.<br>
        Iter 3: <span class="math">x_3 = 1.0000, y_3 = -1.0000, z_3 = 1.0000</span>.<br>
        <strong>Answer:</strong> <span class="math">\mathbf{x = 1.000, \; y = -1.000, \; z = 1.000}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Use Runge-Kutta method of fourth order to find y(0.2) for dy/dx = y + x with y(0) = 1 (take h = 0.2).</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">f(x, y) = y + x</span>, <span class="math">x_0 = 0, y_0 = 1, h = 0.2</span>.<br>
        <span class="math">k_1 = 0.2(1 + 0) = 0.2000</span><br>
        <span class="math">k_2 = 0.2(1.1 + 0.1) = 0.2400</span><br>
        <span class="math">k_3 = 0.2(1.12 + 0.1) = 0.2440</span><br>
        <span class="math">k_4 = 0.2(1.244 + 0.2) = 0.2888</span><br>
        <span class="math">\Delta y = \frac{0.2000 + 2(0.2400) + 2(0.2440) + 0.2888}{6} = 0.2428</span><br>
        <div class="math-block">\mathbf{y(0.2) = 1.2428}</div>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Evaluate &int;₀⁶ 1/(1+x²) dx by using: (a) Trapezoidal rule, (b) Simpson's 3/8 rule.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">h = 1</span>, <span class="math">y = [1.0000, 0.5000, 0.2000, 0.1000, 0.0588, 0.0385, 0.0270]</span>.<br>
        <strong>(a) Trapezoidal Rule:</strong>
        <div class="math-block">I_T = \frac{h}{2} [ (y_0 + y_6) + 2(y_1 + y_2 + y_3 + y_4 + y_5) ] = 0.5 \times [ 1.0270 + 2(0.8973) ] = 0.5 \times 2.8216 = \mathbf{1.4108}</div>
        <strong>(b) Simpson's 3/8 Rule:</strong>
        <div class="math-block">I_{3/8} = \frac{3}{8} [ (y_0 + y_6) + 3(y_1 + y_2 + y_4 + y_5) + 2(y_3) ] = \frac{3}{8} [ 1.0270 + 3(0.7973) + 0.2000 ] = \mathbf{1.3571}</div>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>By using Newton-Raphson's method, find the root of x³ - 2x - 5 = 0 near x = 2 correct to 3 decimal places. Also obtain the rate of convergence of Newton-Raphson method.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">f(x) = x^3 - 2x - 5</span>, <span class="math">f'(x) = 3x^2 - 2</span>.<br>
        Starting at <span class="math">x_0 = 2</span>:<br>
        <span class="math">f(2) = -1</span>, <span class="math">f'(2) = 10 \implies x_1 = 2 - \frac{-1}{10} = 2.1000</span>.<br>
        <span class="math">f(2.1) = 9.261 - 4.2 - 5 = 0.061</span>, <span class="math">f'(2.1) = 3(4.41) - 2 = 11.23</span>.<br>
        <span class="math">x_2 = 2.1 - \frac{0.061}{11.23} = 2.1 - 0.00543 = 2.09457 \implies \mathbf{x \approx 2.095}</span>.<br><br>
        <strong>Rate of Convergence Proof:</strong><br>
        Let <span class="math">\alpha</span> be the exact root, <span class="math">x_n = \alpha + \epsilon_n</span>.<br>
        By Taylor expansion:
        <span class="math">f(x_n) = f(\alpha) + \epsilon_n f'(\alpha) + \frac{\epsilon_n^2}{2} f''(\alpha) + \dots = \epsilon_n f'(\alpha) + \frac{\epsilon_n^2}{2} f''(\alpha)</span>.<br>
        <span class="math">f'(x_n) = f'(\alpha) + \epsilon_n f''(\alpha)</span>.<br>
        Substitute into NR formula:
        <span class="math">\epsilon_{n+1} = \epsilon_n - \frac{\epsilon_n f'(\alpha) + \frac{\epsilon_n^2}{2}f''(\alpha)}{f'(\alpha) + \epsilon_n f''(\alpha)} = \epsilon_n - \epsilon_n \left(1 + \frac{\epsilon_n f''(\alpha)}{2 f'(\alpha)}\right)\left(1 - \frac{\epsilon_n f''(\alpha)}{f'(\alpha)}\right) \approx \frac{f''(\alpha)}{2 f'(\alpha)} \epsilon_n^2</span>.<br>
        Since <span class="math">\epsilon_{n+1} \propto \epsilon_n^2</span>, the convergence is <strong>quadratic (order = 2)</strong>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Apply Lagrange's formula to find the cubic polynomial which includes: (0, 2), (1, 3), (2, 12), (5, 147).</div>
    <div class="ans-body">
        <strong>Solution:</strong> Applying Lagrange interpolation across <span class="math">x = [0, 1, 2, 5]</span>, <span class="math">y = [2, 3, 12, 147]</span>:<br>
        Notice <span class="math">y = x^3 + 2</span>:<br>
        <span class="math">x=0 \implies y=2</span>;<br>
        <span class="math">x=1 \implies y=3</span>;<br>
        <span class="math">x=2 \implies y=8+2=10 \approx 12</span>.<br>
        Computing Lagrange polynomial:
        <div class="math-block">\mathbf{y(x) = x^3 + x^2 - x + 2}</div>
        <em>Verification:</em> <span class="math">y(0)=2, y(1)=3, y(2)=8+4-2+2=12, y(5)=125+25-5+2=147</span>. (Exact!)
    </div>
</div>
"""

print("Generating 2020 PDF...")
generate_pdf("December 2020", "numerical methods 2020 solved.pdf", YEAR_2020_HTML)
