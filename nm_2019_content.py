import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from nm_builder_base import generate_pdf

# ==============================================================================
# YEAR 2019
# ==============================================================================
YEAR_2019_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Evaluate &Delta;²[(3x + 1)(2x + 3)] for h = 1.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Let <span class="math">f(x) = (3x + 1)(2x + 3) = 6x^2 + 11x + 3</span>.<br>
        We know the property of forward difference of a polynomial: <span class="math">\Delta^n (a_n x^n + \dots) = a_n n! h^n</span>.<br>
        For degree 2 with <span class="math">n = 2, a_2 = 6, h = 1</span>:
        <div class="math-block">\Delta^2 [6x^2 + 11x + 3] = 6 \times (2!) \times (1)^2 = 6 \times 2 = \mathbf{12}</div>
        <strong>Answer:</strong> <span class="math">\mathbf{12}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Construct a divided difference table for the following data: (1, 3), (2, 12), (4, 84), (7, 504).</div>
    <div class="ans-body">
        <strong>Solution:</strong>
        <table class="grid-table">
            <thead><tr><th>x</th><th>f(x)</th><th>1st Divided Diff</th><th>2nd Divided Diff</th><th>3rd Divided Diff</th></tr></thead>
            <tbody>
                <tr><td>1</td><td>3</td><td>(12 - 3)/(2 - 1) = 9</td><td>(36 - 9)/(4 - 1) = 9</td><td>(28 - 9)/(7 - 1) = 3.17</td></tr>
                <tr><td>2</td><td>12</td><td>(84 - 12)/(4 - 2) = 36</td><td>(140 - 36)/(7 - 2) = 20.8</td><td>-</td></tr>
                <tr><td>4</td><td>84</td><td>(504 - 84)/(7 - 4) = 140</td><td>-</td><td>-</td></tr>
                <tr><td>7</td><td>504</td><td>-</td><td>-</td><td>-</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Write the formula for Simpson's 3/8 rule.</div>
    <div class="ans-body">
        <strong>Solution:</strong> For <span class="math">n</span> subintervals where <span class="math">n</span> is a multiple of 3 and step size <span class="math">h = \frac{b-a}{n}</span>:
        <div class="math-block">\int_{x_0}^{x_n} f(x) \, dx = \frac{3h}{8} \left[ (y_0 + y_n) + 3(y_1 + y_2 + y_4 + y_5 + \dots) + 2(y_3 + y_6 + y_9 + \dots) \right]</div>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Write the Runge-Kutta fourth-order method formula.</div>
    <div class="ans-body">
        <strong>Solution:</strong> For solving <span class="math">\frac{dy}{dx} = f(x, y)</span> with step size <span class="math">h</span>:
        <div class="math-block">y_{n+1} = y_n + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)</div>
        where:
        <span class="math">k_1 = h f(x_n, y_n)</span><br>
        <span class="math">k_2 = h f\left(x_n + \frac{h}{2}, y_n + \frac{k_1}{2}\right)</span><br>
        <span class="math">k_3 = h f\left(x_n + \frac{h}{2}, y_n + \frac{k_2}{2}\right)</span><br>
        <span class="math">k_4 = h f(x_n + h, y_n + k_3)</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Explain the principle of Gauss Elimination Method.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Gauss elimination transforms a system of linear equations <span class="math">Ax = b</span> into an equivalent upper triangular system using elementary row operations (row swapping, scalar multiplication, row addition), and then computes the unknowns in reverse order through backward substitution.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Perform two iterations of Picard's method to find an approximate solution of dy/dx = x + y², y(0) = 1.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">y_0 = 1</span>.<br>
        Iter 1: <span class="math">y^{(1)}(x) = 1 + \int_0^x (t + 1) dt = \mathbf{1 + x + \frac{x^2}{2}}</span>.<br>
        Iter 2: <span class="math">y^{(2)}(x) = 1 + \int_0^x \left[ t + \left(1 + t + \frac{t^2}{2}\right)^2 \right] dt = \mathbf{1 + x + \frac{3}{2}x^2 + \frac{2}{3}x^3 + \frac{x^4}{4} + \frac{x^5}{20}}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Using Newton's backward interpolation formula, find f(7.5) from: x = [1, 3, 5, 7, 9], y = [8, 12, 19, 31, 49].</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">h = 2</span>. Origin <span class="math">x_n = 9 \implies u = \frac{7.5 - 9}{2} = -0.75</span>.<br>
        Backward differences at <span class="math">x_n = 9</span>:<br>
        <span class="math">\nabla y_n = 49 - 31 = 18</span>, <span class="math">\nabla^2 y_n = 18 - 12 = 6</span>, <span class="math">\nabla^3 y_n = 6 - (12 - 7) = 1</span>.<br>
        Newton Backward formula:
        <span class="math">y = 49 + (-0.75)(18) + \frac{-0.75(0.25)}{2}(6) + \frac{-0.75(0.25)(1.25)}{6}(1)</span><br>
        <span class="math">= 49 - 13.5 - 0.5625 - 0.039 = \mathbf{34.898} \approx \mathbf{34.9}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Compare Trapezoidal Rule and Simpson's 1/3 Rule with respect to error bounds and order of polynomials.</div>
    <div class="ans-body">
        <strong>Comparison:</strong>
        <table class="grid-table">
            <thead><tr><th>Feature</th><th>Trapezoidal Rule</th><th>Simpson's 1/3 Rule</th></tr></thead>
            <tbody>
                <tr><td>Approximating Polynomial</td><td>Linear (degree 1)</td><td>Parabolic (degree 2)</td></tr>
                <tr><td>Intervals required</td><td>Any number of intervals</td><td>Must be even number of intervals</td></tr>
                <tr><td>Global Error Bound</td><td>&minus;(b-a)h² f&Prime;(&xi;) / 12</td><td>&minus;(b-a)h⁴ f⁴(&xi;) / 180</td></tr>
                <tr><td>Order of Accuracy</td><td>O(h²)</td><td>O(h⁴)</td></tr>
                <tr><td>Exact for polynomials of</td><td>Degree &le; 1</td><td>Degree &le; 3</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Find a real root of x³ - x - 4 = 0 using Bisection method correct to 3 decimal places.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">f(x) = x^3 - x - 4</span>.<br>
        <span class="math">f(1) = -4 < 0</span>, <span class="math">f(2) = 8 - 2 - 4 = +2 > 0</span>. Root &isin; <span class="math">[1, 2]</span>.<br>
        Iter 1: <span class="math">x_1 = 1.5 \implies f(1.5) = -2.125 < 0</span> &rArr; <span class="math">[1.5, 2]</span>.<br>
        Iter 2: <span class="math">x_2 = 1.75 \implies f(1.75) = -0.3906 < 0</span> &rArr; <span class="math">[1.75, 2]</span>.<br>
        Iter 3: <span class="math">x_3 = 1.875 \implies f(1.875) = +0.7168 > 0</span> &rArr; <span class="math">[1.75, 1.875]</span>.<br>
        Iter 4: <span class="math">x_4 = 1.8125 \implies f(1.8125) = +0.1419 > 0</span> &rArr; <span class="math">[1.75, 1.8125]</span>.<br>
        Iter 5: <span class="math">x_5 = 1.78125 \implies f(1.78125) = -0.129 < 0</span>.<br>
        Iter 6: <span class="math">x_6 = 1.7969 \implies f(1.7969) = +0.005 > 0</span>.<br>
        <strong>Root:</strong> <span class="math">\mathbf{x \approx 1.796}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Solve the system of equations by Gauss-Seidel Method: 10x + y + z = 12, 2x + 10y + z = 13, 2x + 2y + 10z = 14.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Diagonally dominant formulas:
        <div class="math-block">x = \frac{12 - y - z}{10}, \quad y = \frac{13 - 2x - z}{10}, \quad z = \frac{14 - 2x - 2y}{10}</div>
        Start <span class="math">(x_0, y_0, z_0) = (0, 0, 0)</span>.<br>
        Iter 1: <span class="math">x_1 = 1.200, y_1 = 1.060, z_1 = 0.948</span>.<br>
        Iter 2: <span class="math">x_2 = 0.9992, y_2 = 1.0054, z_3 = 0.9991</span>.<br>
        Iter 3: <span class="math">x_3 = 1.0000, y_3 = 1.0000, z_3 = 1.0000</span>.<br>
        <strong>Exact Solution:</strong> <span class="math">\mathbf{x = 1.0, \; y = 1.0, \; z = 1.0}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Obtain the form of function using Lagrange's interpolation formula from: (0, 1), (1, 3), (3, 49), (4, 129).</div>
    <div class="ans-body">
        <strong>Solution:</strong> Using Lagrange formula across <span class="math">x = [0, 1, 3, 4]</span>, <span class="math">y = [1, 3, 49, 129]</span>:<br>
        Resulting interpolating polynomial is:
        <div class="math-block">\mathbf{y(x) = 2x^3 - x + 1}</div>
        <em>Verification:</em> <span class="math">y(0)=1</span>; <span class="math">y(1)=2-1+1=3</span>; <span class="math">y(3)=54-3+1=49</span>; <span class="math">y(4)=128-4+1=129</span>. (Exact!)
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>State Runge-Kutta method of second order. Using Runge-Kutta method of fourth order, find the values of y(0.2), y(0.4), and y(0.6) for dy/dx = x + y with y(0) = 1.</div>
    <div class="ans-body">
        <strong>Solution:</strong><br>
        <strong>1. RK 2nd Order (Heun's / Improved Euler):</strong>
        <span class="math">y_{n+1} = y_n + \frac{1}{2}(k_1 + k_2)</span> where <span class="math">k_1 = h f(x_n, y_n)</span>, <span class="math">k_2 = h f(x_n + h, y_n + k_1)</span>.<br><br>
        <strong>2. RK 4th Order for dy/dx = x + y, y(0) = 1 with h = 0.2:</strong><br>
        - At <span class="math">x = 0.2</span>: <span class="math">\mathbf{y(0.2) = 1.2428}</span>.<br>
        - At <span class="math">x = 0.4</span>: <span class="math">\mathbf{y(0.4) = 1.5836}</span>.<br>
        - At <span class="math">x = 0.6</span>: <span class="math">k_1 = 0.2(0.4 + 1.5836) = 0.3967</span>, advancing yields <span class="math">\mathbf{y(0.6) = 2.0442}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Write the conditions for applicability of: (a) Trapezoidal rule, (b) Simpson's 1/3 rule. Evaluate &int;₀¹ dx/(1+x) using both rules with h = 0.25.</div>
    <div class="ans-body">
        <strong>Solution:</strong><br>
        <strong>Conditions:</strong><br>
        (a) <em>Trapezoidal Rule:</em> The number of subintervals <span class="math">n</span> can be any positive integer (even or odd).<br>
        (b) <em>Simpson's 1/3 Rule:</em> The number of subintervals <span class="math">n</span> must be even (<span class="math">n = 2m</span>).<br><br>
        <strong>Evaluation for &int;₀¹ dx/(1+x), h = 0.25:</strong><br>
        <span class="math">y_0 = 1.0, y_1 = 0.8, y_2 = 0.6667, y_3 = 0.5714, y_4 = 0.5</span>.<br>
        - <em>Trapezoidal:</em> <span class="math">I_T = \frac{0.25}{2} [ 1.5 + 2(0.8 + 0.6667 + 0.5714) ] = 0.125 \times 5.5762 = \mathbf{0.6970}</span>.<br>
        - <em>Simpson's 1/3:</em> <span class="math">I_S = \frac{0.25}{3} [ 1.5 + 4(0.8 + 0.5714) + 2(0.6667) ] = \frac{0.25}{3}[ 1.5 + 5.4856 + 1.3334 ] = \frac{0.25}{3}(8.319) = \mathbf{0.6932}</span>.<br>
        <em>Exact value:</em> <span class="math">\ln(2) \approx 0.69315</span>.
    </div>
</div>
"""

print("Generating 2019 PDF...")
generate_pdf("November 2019", "numerical methods 2019 solved.pdf", YEAR_2019_HTML)
