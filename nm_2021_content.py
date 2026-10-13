import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from nm_builder_base import generate_pdf

# ==============================================================================
# YEAR 2021
# ==============================================================================
YEAR_2021_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks / CV-3 Pattern)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (7.5M)</span>Find a root of the equation f(x) = x³ - 4x - 9 = 0 using Bisection method in four iterations.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">f(x) = x^3 - 4x - 9</span>.<br>
        <span class="math">f(2) = 8 - 8 - 9 = -9 < 0</span>, <span class="math">f(3) = 27 - 12 - 9 = +6 > 0</span>. Root &isin; <span class="math">[2, 3]</span>.<br>
        <strong>Iter 1:</strong> <span class="math">x_1 = \frac{2 + 3}{2} = 2.5</span> &rArr; <span class="math">f(2.5) = 15.625 - 10 - 9 = -3.375 < 0</span> &rArr; <span class="math">[2.5, 3]</span>.<br>
        <strong>Iter 2:</strong> <span class="math">x_2 = \frac{2.5 + 3}{2} = 2.75</span> &rArr; <span class="math">f(2.75) = 20.7969 - 11 - 9 = +0.7969 > 0</span> &rArr; <span class="math">[2.5, 2.75]</span>.<br>
        <strong>Iter 3:</strong> <span class="math">x_3 = \frac{2.5 + 2.75}{2} = 2.625</span> &rArr; <span class="math">f(2.625) = 18.0879 - 10.5 - 9 = -1.4121 < 0</span> &rArr; <span class="math">[2.625, 2.75]</span>.<br>
        <strong>Iter 4:</strong> <span class="math">x_4 = \frac{2.625 + 2.75}{2} = \mathbf{2.6875}</span>.<br>
        <strong>Answer after 4 iterations:</strong> <span class="math">\mathbf{x \approx 2.6875} \approx \mathbf{2.688}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (7.5M)</span>Find the form of the function from following given data: x = [1, 2, 3, 4], f(x) = [3, 6, 11, 18].</div>
    <div class="ans-body">
        <strong>Solution:</strong> Step <span class="math">h = 1, x_0 = 1</span>. Form difference table:
        <table class="grid-table">
            <thead><tr><th>x</th><th>f(x)</th><th>&Delta;f</th><th>&Delta;&sup2;f</th><th>&Delta;&sup3;f</th></tr></thead>
            <tbody>
                <tr><td>1</td><td>3</td><td>3</td><td>2</td><td>0</td></tr>
                <tr><td>2</td><td>6</td><td>5</td><td>2</td><td>-</td></tr>
                <tr><td>3</td><td>11</td><td>7</td><td>-</td><td>-</td></tr>
                <tr><td>4</td><td>18</td><td>-</td><td>-</td><td>-</td></tr>
            </tbody>
        </table>
        Here <span class="math">\Delta^2 f = 2</span> is constant, and <span class="math">\Delta^3 f = 0</span>. Let <span class="math">u = x - 1</span>:<br>
        <span class="math">f(x) = f_0 + u \Delta f_0 + \frac{u(u-1)}{2} \Delta^2 f_0 = 3 + (x-1)(3) + \frac{(x-1)(x-2)}{2}(2)</span><br>
        <span class="math">= 3 + 3x - 3 + (x^2 - 3x + 2) = \mathbf{x^2 + 2}</span>.<br>
        <strong>Answer:</strong> The function is <span class="math">\mathbf{f(x) = x^2 + 2}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (7.5M)</span>Evaluate &int;₀¹ 1/(1+x²) dx by Trapezoidal Rule with n = 4.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">h = \frac{1 - 0}{4} = 0.25</span>.<br>
        <span class="math">y_0 = 1.0000, y_1 = \frac{1}{1 + 0.0625} = 0.9412, y_2 = \frac{1}{1 + 0.25} = 0.8000, y_3 = \frac{1}{1 + 0.5625} = 0.6400, y_4 = 0.5000</span>.<br>
        Trapezoidal Rule:
        <div class="math-block">I = \frac{h}{2} [ (y_0 + y_4) + 2(y_1 + y_2 + y_3) ] = \frac{0.25}{2} [ 1.5000 + 2(2.3812) ] = 0.125 \times 6.2624 = \mathbf{0.7828}</div>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (7.5M)</span>Use Euler's Method with h = 0.1 to find the solution of dy/dx = x + y², y(0) = 0 in range 0 &le; x &le; 0.5.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">y_{n+1} = y_n + h f(x_n, y_n) = y_n + 0.1(x_n + y_n^2)</span>.<br>
        1. <span class="math">x_0 = 0.0, y_0 = 0 \implies y_1 = 0 + 0.1(0) = \mathbf{0.0000}</span> at <span class="math">x=0.1</span>.<br>
        2. <span class="math">x_1 = 0.1, y_1 = 0 \implies y_2 = 0 + 0.1(0.1 + 0) = \mathbf{0.0100}</span> at <span class="math">x=0.2</span>.<br>
        3. <span class="math">x_2 = 0.2, y_2 = 0.01 \implies y_3 = 0.01 + 0.1(0.2 + 0.0001) = \mathbf{0.0300}</span> at <span class="math">x=0.3</span>.<br>
        4. <span class="math">x_3 = 0.3, y_3 = 0.03 \implies y_4 = 0.03 + 0.1(0.3 + 0.0009) = \mathbf{0.0601}</span> at <span class="math">x=0.4</span>.<br>
        5. <span class="math">x_4 = 0.4, y_4 = 0.0601 \implies y_5 = 0.0601 + 0.1(0.4 + 0.0036) = \mathbf{0.1005}</span> at <span class="math">x=0.5</span>.<br>
        <strong>Answer:</strong> <span class="math">y(0.1)=0, y(0.2)=0.01, y(0.3)=0.03, y(0.4)=0.0601, y(0.5)=0.1005</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (7.5M)</span>Solve by Gauss elimination: 8x - 3y + 2z = 23, 4x + 11y - z = 33, 6x + 3y + 12z = 36.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Augmented matrix:
        <span class="math">\begin{bmatrix} 8 & -3 & 2 & | & 23 \\ 4 & 11 & -1 & | & 33 \\ 6 & 3 & 12 & | & 36 \end{bmatrix}</span><br>
        Divide row 3 by 3: <span class="math">\begin{bmatrix} 2 & 1 & 4 & | & 12 \end{bmatrix}</span>. Interchange <span class="math">R_1 \leftrightarrow R_3</span>:<br>
        <span class="math">\begin{bmatrix} 2 & 1 & 4 & | & 12 \\ 4 & 11 & -1 & | & 33 \\ 8 & -3 & 2 & | & 23 \end{bmatrix}</span><br>
        <span class="math">R_2 \to R_2 - 2R_1</span>: <span class="math">[0, 9, -9 | 9] \implies y - z = 1</span>.<br>
        <span class="math">R_3 \to R_3 - 4R_1</span>: <span class="math">[0, -7, -14 | -25]</span>.<br>
        Substitute <span class="math">y = 1 + z</span> into row 3:
        <span class="math">-7(1 + z) - 14z = -25 \implies -7 - 21z = -25 \implies -21z = -18 \implies \mathbf{z = \frac{6}{7} \approx 0.857}</span>.<br>
        <span class="math">\mathbf{y = 1 + \frac{6}{7} = \frac{13}{7} \approx 1.857}</span>.<br>
        <span class="math">2x + y + 4z = 12 \implies 2x = 12 - \frac{13}{7} - \frac{24}{7} = 12 - \frac{37}{7} = \frac{47}{7} \implies \mathbf{x = \frac{47}{14} \approx 3.357}</span>.<br>
        <strong>Answer:</strong> <span class="math">x \approx 3.357, \; y \approx 1.857, \; z \approx 0.857</span>.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (1 &times; 15 = 15 Marks / CV-3 Pattern)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (15M)</span>By means of Newton's divided difference formula find f(8) and f(15) from: x = [4, 5, 7, 10, 11, 13], f(x) = [48, 100, 294, 900, 1210, 2028].</div>
    <div class="ans-body">
        <strong>Solution:</strong> Construct divided difference table:
        <table class="grid-table">
            <thead><tr><th>x</th><th>f(x)</th><th>1st DD</th><th>2nd DD</th><th>3rd DD</th><th>4th DD</th></tr></thead>
            <tbody>
                <tr><td>4</td><td>48</td><td>52</td><td>15</td><td>1</td><td>0</td></tr>
                <tr><td>5</td><td>100</td><td>97</td><td>21</td><td>1</td><td>-</td></tr>
                <tr><td>7</td><td>294</td><td>202</td><td>27</td><td>-</td><td>-</td></tr>
                <tr><td>10</td><td>900</td><td>310</td><td>-</td><td>-</td><td>-</td></tr>
                <tr><td>11</td><td>1210</td><td>409</td><td>-</td><td>-</td><td>-</td></tr>
                <tr><td>13</td><td>2028</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
            </tbody>
        </table>
        Newton's Divided Difference formula:
        <div class="math-block">f(x) = 48 + 52(x - 4) + 15(x - 4)(x - 5) + 1(x - 4)(x - 5)(x - 7)</div>
        For <span class="math">x = 8</span>:
        <span class="math">f(8) = 48 + 52(4) + 15(4)(3) + 1(4)(3)(1) = 48 + 208 + 180 + 12 = \mathbf{448}</span>.<br>
        For <span class="math">x = 15</span>:
        <span class="math">f(15) = 48 + 52(11) + 15(11)(10) + 1(11)(10)(8) = 48 + 572 + 1650 + 880 = \mathbf{3150}</span>.<br>
        <strong>Answer:</strong> <span class="math">\mathbf{f(8) = 448}</span>, <span class="math">\mathbf{f(15) = 3150}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (15M)</span>Find dy/dx at x = 1.0 from: (1.0, 2.7183), (1.2, 3.3201), (1.4, 4.0552), (1.6, 4.9530), (1.8, 6.0496), (2.0, 7.3891).</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">h = 0.2</span>. At <span class="math">x_0 = 1.0</span>:
        <span class="math">\Delta y_0 = 3.3201 - 2.7183 = 0.6018</span><br>
        <span class="math">\Delta^2 y_0 = 0.7351 - 0.6018 = 0.1333</span><br>
        <span class="math">\Delta^3 y_0 = 0.8978 - 0.7351 - 0.1333 = 0.0294</span><br>
        <span class="math">f'(1.0) = \frac{1}{0.2} \left[ 0.6018 - \frac{0.1333}{2} + \frac{0.0294}{3} \right] = 5 \times [0.6018 - 0.06665 + 0.0098] = 5 \times 0.54495 = \mathbf{2.7248} \approx \mathbf{2.72}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (15M)</span>Using Picard's method of successive approximation obtain a solution up to fourth approximation of dy/dx = x + y with y(0) = 1.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">y_0 = 1, x_0 = 0</span>.<br>
        <span class="math">y^{(1)}(x) = 1 + \int_0^x (t + 1) dt = \mathbf{1 + x + \frac{x^2}{2}}</span>.<br>
        <span class="math">y^{(2)}(x) = 1 + \int_0^x \left( t + 1 + t + \frac{t^2}{2} \right) dt = \mathbf{1 + x + x^2 + \frac{x^3}{6}}</span>.<br>
        <span class="math">y^{(3)}(x) = 1 + \int_0^x \left( 1 + 2t + t^2 + \frac{t^3}{6} \right) dt = \mathbf{1 + x + x^2 + \frac{x^3}{3} + \frac{x^4}{24}}</span>.<br>
        <span class="math">y^{(4)}(x) = 1 + \int_0^x \left( 1 + 2t + t^2 + \frac{t^3}{3} + \frac{t^4}{24} \right) dt = \mathbf{1 + x + x^2 + \frac{x^3}{3} + \frac{x^4}{12} + \frac{x^5}{120}}</span>.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (2 &times; 22.5 = 45 Marks / CV-3 Pattern)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (22.5M)</span>Find a real root of the equation x³ - x² - 2 = 0 by False Position Method.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">f(x) = x^3 - x^2 - 2</span>.<br>
        <span class="math">f(1) = 1 - 1 - 2 = -2 < 0</span>, <span class="math">f(2) = 8 - 4 - 2 = +2 > 0</span>. Root &isin; <span class="math">[1, 2]</span>.<br>
        <strong>Iter 1:</strong> <span class="math">x_1 = \frac{1(2) - 2(-2)}{2 - (-2)} = \frac{2 + 4}{4} = 1.5000</span>.<br>
        <span class="math">f(1.5) = 3.375 - 2.25 - 2 = -0.875 < 0</span> &rArr; <span class="math">[1.5, 2]</span>.<br>
        <strong>Iter 2:</strong> <span class="math">x_2 = \frac{1.5(2) - 2(-0.875)}{2 - (-0.875)} = \frac{3 + 1.75}{2.875} = \frac{4.75}{2.875} = 1.6522</span>.<br>
        <span class="math">f(1.6522) = 4.5101 - 2.7297 - 2 = -0.2196 < 0</span> &rArr; <span class="math">[1.6522, 2]</span>.<br>
        <strong>Iter 3:</strong> <span class="math">x_3 = \frac{1.6522(2) - 2(-0.2196)}{2 + 0.2196} = \frac{3.3044 + 0.4392}{2.2196} = \mathbf{1.6869}</span>.<br>
        <span class="math">f(1.6869) \approx -0.046</span>.<br>
        <strong>Iter 4:</strong> <span class="math">x_4 = \mathbf{1.695}</span>.<br>
        <strong>Final Root:</strong> <span class="math">\mathbf{x \approx 1.695}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (22.5M)</span>Interpolate by means of Gauss's formula the population for the year 1936, given: [1901: 12k, 1911: 15k, 1921: 20k, 1931: 27k, 1941: 39k, 1951: 52k].</div>
    <div class="ans-body">
        <strong>Solution:</strong> Origin at <span class="math">x_0 = 1931, h = 10 \implies u = \frac{1936 - 1931}{10} = 0.5</span>.<br>
        Central difference table around 1931 (<span class="math">y_0 = 27</span>):<br>
        <span class="math">\Delta y_0 = 39 - 27 = 12</span>, <span class="math">\Delta y_{-1} = 27 - 20 = 7</span>, <span class="math">\Delta^2 y_{-1} = 12 - 7 = 5</span>.<br>
        Gauss Forward Interpolation formula:
        <div class="math-block">y = y_0 + u \Delta y_0 + \frac{u(u-1)}{2} \Delta^2 y_{-1} + \frac{(u+1)u(u-1)}{6} \Delta^3 y_{-1}</div>
        <span class="math">y(1936) = 27 + 0.5(12) + \frac{0.5(-0.5)}{2}(5) = 27 + 6 - 0.625 = \mathbf{32.375} \text{ thousand}</span>.<br>
        <strong>Population in 1936:</strong> <span class="math">\mathbf{\approx 32,375}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (22.5M)</span>Find the value of &int;₀¹ 1/(1+x²) dx by using Simpson's 1/3 and 3/8 rule with h = 1/6.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Step <span class="math">h = 1/6</span>. Values: <span class="math">y = [1.000, 0.9730, 0.9000, 0.8000, 0.6923, 0.5902, 0.5000]</span>.<br>
        <strong>1. Simpson's 1/3 Rule:</strong>
        <div class="math-block">I_{1/3} = \frac{1/6}{3} [ (1 + 0.5) + 4(0.9730 + 0.8000 + 0.5902) + 2(0.9000 + 0.6923) ] = \frac{1}{18} [ 1.5 + 9.4528 + 3.1846 ] = \mathbf{0.7854}</div>
        <strong>2. Simpson's 3/8 Rule:</strong>
        <div class="math-block">I_{3/8} = \frac{3(1/6)}{8} [ 1.5 + 3(0.9730 + 0.9000 + 0.6923 + 0.5902) + 2(0.8000) ] = \frac{1}{16} [ 1.5 + 9.4665 + 1.6 ] = \mathbf{0.7854}</div>
        Both formulas yield <span class="math">\mathbf{0.7854}</span>, which gives <span class="math">\pi \approx 4 \times 0.7854 = \mathbf{3.1416}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (22.5M)</span>Using Runge-Kutta method of fourth order, solve dy/dx = x + y² with y(0) = 1 at x = 0.2 and 0.4.</div>
    <div class="ans-body">
        <strong>Solution:</strong> With <span class="math">h = 0.2</span>:<br>
        <span class="math">k_1 = 0.2(0 + 1) = 0.2000</span><br>
        <span class="math">k_2 = 0.2(0.1 + 1.21) = 0.2620</span><br>
        <span class="math">k_3 = 0.2(0.1 + 1.279) = 0.2758</span><br>
        <span class="math">k_4 = 0.2(0.2 + 1.628) = 0.3656</span><br>
        <span class="math">\Delta y = \frac{0.2000 + 2(0.2620) + 2(0.2758) + 0.3656}{6} = \frac{1.6412}{6} = 0.2735</span><br>
        <div class="math-block">y(0.2) = 1 + 0.2735 = \mathbf{1.2735}</div>
        Advancing to <span class="math">x = 0.4</span> gives <span class="math">y(0.4) \approx \mathbf{1.7142}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (22.5M)</span>Find the solution of the system by Gauss-Seidel Method: 27x + 6y - z = 85, 6x + 15y + 2z = 72, x + y + 54z = 110.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Diagonally dominant formulas:
        <div class="math-block">x = \frac{85 - 6y + z}{27}, \quad y = \frac{72 - 6x - 2z}{15}, \quad z = \frac{110 - x - y}{54}</div>
        Start <span class="math">(x_0, y_0, z_0) = (0, 0, 0)</span>.<br>
        Iter 1: <span class="math">x_1 = 3.1481, y_1 = 3.5407, z_1 = 1.9132</span>.<br>
        Iter 2: <span class="math">x_2 = 2.4322, y_2 = 3.5720, z_2 = 1.9258</span>.<br>
        Iter 3: <span class="math">x_3 = 2.4257, y_3 = 3.5730, z_3 = 1.9260</span>.<br>
        Converged solution: <span class="math">\mathbf{x \approx 2.426, \; y \approx 3.573, \; z \approx 1.926}</span>.
    </div>
</div>
"""

print("Generating 2021 PDF...")
generate_pdf("December 2021", "numerical methods 2021 solved.pdf", YEAR_2021_HTML)
