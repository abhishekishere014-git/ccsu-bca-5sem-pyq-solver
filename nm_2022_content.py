import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from nm_builder_base import generate_pdf

# ==============================================================================
# YEAR 2022
# ==============================================================================
YEAR_2022_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Obtain a real root of the equation f(x) = x³ - x - 1 = 0 using Bisection method correct to three decimal places.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">f(x) = x^3 - x - 1</span>.<br>
        <span class="math">f(1) = 1 - 1 - 1 = -1 < 0</span>, <span class="math">f(2) = 8 - 2 - 1 = +5 > 0</span>. Root lies in <span class="math">[1, 2]</span>.<br>
        Iter 1: <span class="math">x_1 = 1.5</span> &rArr; <span class="math">f(1.5) = 3.375 - 1.5 - 1 = 0.875 > 0</span> &rArr; <span class="math">[1, 1.5]</span>.<br>
        Iter 2: <span class="math">x_2 = 1.25</span> &rArr; <span class="math">f(1.25) = 1.953 - 1.25 - 1 = -0.297 < 0</span> &rArr; <span class="math">[1.25, 1.5]</span>.<br>
        Iter 3: <span class="math">x_3 = 1.375</span> &rArr; <span class="math">f(1.375) = 2.599 - 1.375 - 1 = +0.224 > 0</span> &rArr; <span class="math">[1.25, 1.375]</span>.<br>
        Iter 4: <span class="math">x_4 = 1.3125</span> &rArr; <span class="math">f(1.3125) = -0.0515 < 0</span> &rArr; <span class="math">[1.3125, 1.375]</span>.<br>
        Iter 5: <span class="math">x_5 = 1.3438</span> &rArr; <span class="math">f(1.3438) = +0.0826 > 0</span> &rArr; <span class="math">[1.3125, 1.3438]</span>.<br>
        Iter 6: <span class="math">x_6 = 1.3281</span> &rArr; <span class="math">f(1.3281) = +0.0145 > 0</span>.<br>
        Iter 7: <span class="math">x_7 = 1.3203</span> &rArr; <span class="math">x_8 \approx 1.3247</span>.<br>
        <strong>Root:</strong> <span class="math">\mathbf{x \approx 1.325}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Define forward difference. Make forward difference table for the ordered pairs: (x₀, y₀), (x₁, y₁), (x₂, y₂), (x₃, y₃), (x₄, y₄).</div>
    <div class="ans-body">
        <strong>Definition:</strong> For equally spaced points <span class="math">x_i = x_0 + i h</span>, the forward difference operator <span class="math">\Delta</span> is defined as:
        <div class="math-block">\Delta y_i = y_{i+1} - y_i</div>
        Higher-order differences: <span class="math">\Delta^n y_i = \Delta^{n-1} y_{i+1} - \Delta^{n-1} y_i</span>.<br>
        <strong>Forward Difference Table:</strong>
        <table class="grid-table">
            <thead><tr><th>x</th><th>y</th><th>&Delta;y</th><th>&Delta;&sup2;y</th><th>&Delta;&sup3;y</th><th>&Delta;&sup4;y</th></tr></thead>
            <tbody>
                <tr><td>x₀</td><td>y₀</td><td>&Delta;y₀ = y₁ - y₀</td><td>&Delta;&sup2;y₀ = &Delta;y₁ - &Delta;y₀</td><td>&Delta;&sup3;y₀ = &Delta;&sup2;y₁ - &Delta;&sup2;y₀</td><td>&Delta;&sup4;y₀ = &Delta;&sup3;y₁ - &Delta;&sup3;y₀</td></tr>
                <tr><td>x₁</td><td>y₁</td><td>&Delta;y₁ = y₂ - y₁</td><td>&Delta;&sup2;y₁ = &Delta;y₂ - &Delta;y₁</td><td>&Delta;&sup3;y₁ = &Delta;&sup2;y₂ - &Delta;&sup2;y₁</td><td>-</td></tr>
                <tr><td>x₂</td><td>y₂</td><td>&Delta;y₂ = y₃ - y₂</td><td>&Delta;&sup2;y₂ = &Delta;y₃ - &Delta;y₂</td><td>-</td><td>-</td></tr>
                <tr><td>x₃</td><td>y₃</td><td>&Delta;y₃ = y₄ - y₃</td><td>-</td><td>-</td><td>-</td></tr>
                <tr><td>x₄</td><td>y₄</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Find the value of dy/dx at x = 2.2 for: (1.0, 2.7183), (1.2, 3.3201), (1.4, 4.0552), (1.6, 4.9530), (1.8, 6.0496), (2.0, 7.3891), (2.2, 9.0250).</div>
    <div class="ans-body">
        <strong>Solution:</strong> Here <span class="math">x = 2.2</span> is at the end of the table (<span class="math">x_n = 2.2</span>, <span class="math">h = 0.2</span>).<br>
        Backward differences at <span class="math">x_n = 2.2</span>:<br>
        <span class="math">\nabla y_n = 9.0250 - 7.3891 = 1.6359</span><br>
        <span class="math">\nabla^2 y_n = 1.6359 - (7.3891 - 6.0496) = 1.6359 - 1.3395 = 0.2964</span><br>
        <span class="math">\nabla^3 y_n = 0.2964 - (1.3395 - 1.0966) = 0.2964 - 0.2429 = 0.0535</span><br>
        Newton's backward derivative formula at <span class="math">x = x_n</span>:
        <div class="math-block">f'(x_n) = \frac{1}{h} \left[ \nabla y_n + \frac{1}{2}\nabla^2 y_n + \frac{1}{3}\nabla^3 y_n \right]</div>
        <span class="math">= \frac{1}{0.2} \left[ 1.6359 + \frac{0.2964}{2} + \frac{0.0535}{3} \right] = 5 \times [1.6359 + 0.1482 + 0.0178] = 5 \times 1.8019 = \mathbf{9.0095} \approx \mathbf{9.01}</span>.<br>
        <em>Exact value (<span class="math">e^{2.2}</span>):</em> <span class="math">9.0250</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Solve using Gauss elimination: 3x + 2y + 3z = 18, 2x + y + z = 10, x + 4y + 9z = 16.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Reordering rows with row 3 as first:
        <div class="math-block">\begin{bmatrix} 1 & 4 & 9 & | & 16 \\ 2 & 1 & 1 & | & 10 \\ 3 & 2 & 3 & | & 18 \end{bmatrix}</div>
        <span class="math">R_2 \to R_2 - 2R_1</span>, <span class="math">R_3 \to R_3 - 3R_1</span>:
        <span class="math">\begin{bmatrix} 1 & 4 & 9 & | & 16 \\ 0 & -7 & -17 & | & -22 \\ 0 & -10 & -24 & | & -30 \end{bmatrix}</span><br>
        <span class="math">R_3 \to R_3 - \frac{10}{7} R_2</span>:
        <span class="math">-24 - \frac{10}{7}(-17) = \frac{-168 + 170}{7} = \frac{2}{7}</span>, and <span class="math">-30 - \frac{10}{7}(-22) = \frac{-210 + 220}{7} = \frac{10}{7}</span>.<br>
        <span class="math">\frac{2}{7} z = \frac{10}{7} \implies \mathbf{z = 5}</span>.<br>
        <span class="math">-7y - 17(5) = -22 \implies -7y - 85 = -22 \implies -7y = 63 \implies \mathbf{y = -9}</span>.<br>
        <span class="math">x = 16 - 4(-9) - 9(5) = 16 + 36 - 45 = \mathbf{7}</span>.<br>
        <strong>Answer:</strong> <span class="math">\mathbf{x = 7, \; y = -9, \; z = 5}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Solve dy/dx = x + y², y(0) = 0 using Picard's method.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">y_0 = 0, x_0 = 0</span>.<br>
        <span class="math">y^{(1)}(x) = 0 + \int_0^x (t + 0) dt = \mathbf{\frac{x^2}{2}}</span>.<br>
        <span class="math">y^{(2)}(x) = \int_0^x \left( t + \frac{t^4}{4} \right) dt = \mathbf{\frac{x^2}{2} + \frac{x^5}{20}}</span>.<br>
        <span class="math">y^{(3)}(x) = \int_0^x \left[ t + \left(\frac{t^2}{2} + \frac{t^5}{20}\right)^2 \right] dt = \mathbf{\frac{x^2}{2} + \frac{x^5}{20} + \frac{x^8}{160}}</span>.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Find a real root of f(x) = x³ - 5x + 3 = 0 using method of false position.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">f(1) = 1 - 5 + 3 = -1 < 0</span>, <span class="math">f(2) = 8 - 10 + 3 = +1 > 0</span>. Root &isin; <span class="math">[1, 2]</span>.<br>
        Iter 1: <span class="math">x_1 = \frac{1(1) - 2(-1)}{1 - (-1)} = \frac{1 + 2}{2} = 1.5</span>.<br>
        <span class="math">f(1.5) = 3.375 - 7.5 + 3 = -1.125 < 0</span> &rArr; root &isin; <span class="math">[1.5, 2]</span>.<br>
        Iter 2: <span class="math">x_2 = \frac{1.5(1) - 2(-1.125)}{1 - (-1.125)} = \frac{1.5 + 2.25}{2.125} = \frac{3.75}{2.125} = 1.7647</span>.<br>
        <span class="math">f(1.7647) = 5.4955 - 8.8235 + 3 = -0.328 < 0</span> &rArr; root &isin; <span class="math">[1.7647, 2]</span>.<br>
        Iter 3: <span class="math">x_3 = \frac{1.7647(1) - 2(-0.328)}{1 + 0.328} = \frac{2.4207}{1.328} = 1.8228</span>.<br>
        <span class="math">f(1.8228) = -0.062 < 0</span>.<br>
        Iter 4: <span class="math">x_4 = \mathbf{1.831}</span>.<br>
        <strong>Answer:</strong> <span class="math">\mathbf{x \approx 1.831}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Find the missing term in the following table: x = [1, 2, 3, 4], y = [1, 3, 9, y₃].</div>
    <div class="ans-body">
        <strong>Solution:</strong> Since 3 values are given, approximate by a 2nd degree polynomial, so <span class="math">\Delta^3 y_0 = 0</span>:<br>
        <div class="math-block">(E - 1)^3 y_0 = y_3 - 3y_2 + 3y_1 - y_0 = 0</div>
        Substitute known values:
        <span class="math">y_3 - 3(9) + 3(3) - 1 = 0 \implies y_3 - 27 + 9 - 1 = 0 \implies y_3 - 19 = 0</span>.<br>
        <div class="math-block">\mathbf{y_3 = 19}</div>
        <em>Note:</em> If sequence was <span class="math">3^{x-1}</span>, value would be 27, but by polynomial interpolation <span class="math">\mathbf{y_3 = 19}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Evaluate &int;₀^(π/2) &radic;(sin x) dx using Simpson's 1/3 rule with h = &pi;/12.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Interval <span class="math">[0, \pi/2]</span> divided into 6 equal parts with <span class="math">h = \pi/12 = 15^\circ</span>.<br>
        <table class="grid-table">
            <thead><tr><th>x</th><th>0°</th><th>15°</th><th>30°</th><th>45°</th><th>60°</th><th>75°</th><th>90°</th></tr></thead>
            <tbody>
                <tr><td>&radic;(sin x)</td><td>0.0000</td><td>0.5087</td><td>0.7071</td><td>0.8409</td><td>0.9306</td><td>0.9828</td><td>1.0000</td></tr>
            </tbody>
        </table>
        Simpson's 1/3 Rule:
        <div class="math-block">I = \frac{h}{3} [ (y_0 + y_6) + 4(y_1 + y_3 + y_5) + 2(y_2 + y_4) ]</div>
        <span class="math">y_0 + y_6 = 0 + 1 = 1.0000</span><br>
        <span class="math">4(0.5087 + 0.8409 + 0.9828) = 4(2.3324) = 9.3296</span><br>
        <span class="math">2(0.7071 + 0.9306) = 2(1.6377) = 3.2754</span><br>
        Sum <span class="math">= 1.0000 + 9.3296 + 3.2754 = 13.6050</span>.<br>
        <div class="math-block">I = \frac{\pi / 12}{3} \times 13.6050 = \frac{\pi}{36} \times 13.6050 \approx 0.087266 \times 13.6050 = \mathbf{1.1873}</div>
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Use Newton-Raphson method to find a real root of 4e⁻ˣ sin(x) - 1 = 0 correct to 3 decimal places, lying between 0 and 0.5.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">f(x) = 4e^{-x}\sin x - 1</span>.<br>
        <span class="math">f'(x) = 4e^{-x}(\cos x - \sin x)</span>.<br>
        <span class="math">f(0) = 4(1)(0) - 1 = -1 < 0</span>.<br>
        <span class="math">f(0.5) = 4e^{-0.5}\sin(0.5) - 1 = 4(0.6065)(0.4794) - 1 = 1.1630 - 1 = +0.1630 > 0</span>.<br>
        Take <span class="math">x_0 = 0.3</span>:<br>
        <span class="math">f(0.3) = 4e^{-0.3}\sin(0.3) - 1 = 4(0.7408)(0.2955) - 1 = 0.8757 - 1 = -0.1243</span>.<br>
        <span class="math">f'(0.3) = 4(0.7408)(\cos 0.3 - \sin 0.3) = 2.9633(0.9553 - 0.2955) = 2.9633(0.6598) = 1.9552</span>.<br>
        <span class="math">x_1 = 0.3 - \frac{-0.1243}{1.9552} = 0.3 + 0.0636 = 0.3636</span>.<br><br>
        <strong>Iter 2:</strong>
        <span class="math">f(0.3636) = 4e^{-0.3636}\sin(0.3636) - 1 = 4(0.6952)(0.3556) - 1 = 0.9888 - 1 = -0.0112</span>.<br>
        <span class="math">f'(0.3636) = 4(0.6952)(0.9346 - 0.3556) = 2.7808(0.5790) = 1.6101</span>.<br>
        <span class="math">x_2 = 0.3636 - \frac{-0.0112}{1.6101} = 0.3636 + 0.0070 = 0.3706</span>.<br><br>
        <strong>Iter 3:</strong>
        <span class="math">f(0.3706) = 4e^{-0.3706}\sin(0.3706) - 1 \approx 0.0000 \implies \mathbf{x = 0.371}</span>.<br>
        <strong>Final Root:</strong> <span class="math">\mathbf{x \approx 0.371}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Using Lagrange's interpolation formula, find the form of the function y(x) from: (0, -12), (1, 0), (3, 12), (4, 24).</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">(x_0, y_0) = (0, -12), (x_1, y_1) = (1, 0), (x_2, y_2) = (3, 12), (x_3, y_3) = (4, 24)</span>.<br>
        Since <span class="math">y_1 = 0</span>, the second term vanishes.<br>
        <span class="math">L_0(x) = \frac{(x-1)(x-3)(x-4)}{(0-1)(0-3)(0-4)} = \frac{(x-1)(x-3)(x-4)}{-12}</span>.<br>
        <span class="math">L_2(x) = \frac{x(x-1)(x-4)}{(3-0)(3-1)(3-4)} = \frac{x(x-1)(x-4)}{-6}</span>.<br>
        <span class="math">L_3(x) = \frac{x(x-1)(x-3)}{(4-0)(4-1)(4-3)} = \frac{x(x-1)(x-3)}{12}</span>.<br>
        Therefore:
        <span class="math">y(x) = L_0(x)(-12) + L_2(x)(12) + L_3(x)(24)</span><br>
        <span class="math">= (x-1)(x-3)(x-4) - 2x(x-1)(x-4) + 2x(x-1)(x-3)</span><br>
        <span class="math">= (x-1)[ (x-3)(x-4) - 2x(x-4) + 2x(x-3) ]</span><br>
        <span class="math">= (x-1)[ x^2 - 7x + 12 - 2x^2 + 8x + 2x^2 - 6x ] = (x-1)[ x^2 - 5x + 12 ]</span><br>
        <div class="math-block">\mathbf{y(x) = x^3 - 6x^2 + 17x - 12}</div>
        <em>Verification:</em> <span class="math">y(0) = -12</span>, <span class="math">y(1) = 0</span>, <span class="math">y(3) = 27 - 54 + 51 - 12 = 12</span>, <span class="math">y(4) = 64 - 96 + 68 - 12 = 24</span>. (Exact!)
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Use Simpson's 3/8 rule to evaluate &int;₀¹ 1/(1+x²) dx with n = 6 intervals. Hence find the approximate value of &pi;.</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">h = 1/6</span>. Values:
        <span class="math">y_0 = 1, y_1 = \frac{36}{37} \approx 0.9730, y_2 = \frac{36}{40} = 0.9000, y_3 = \frac{36}{45} = 0.8000</span>,
        <span class="math">y_4 = \frac{36}{52} \approx 0.6923, y_5 = \frac{36}{61} \approx 0.5902, y_6 = \frac{36}{72} = 0.5000</span>.<br>
        Simpson's 3/8 Rule:
        <div class="math-block">I = \frac{3h}{8} [ (y_0 + y_6) + 3(y_1 + y_2 + y_4 + y_5) + 2y_3 ]</div>
        <span class="math">y_0 + y_6 = 1.5000</span><br>
        <span class="math">3(0.9730 + 0.9000 + 0.6923 + 0.5902) = 3(3.1555) = 9.4665</span><br>
        <span class="math">2(0.8000) = 1.6000</span><br>
        <span class="math">I = \frac{3(1/6)}{8} [ 1.5000 + 9.4665 + 1.6000 ] = \frac{1}{16} [ 12.5665 ] = \mathbf{0.785406}</span>.<br>
        Since <span class="math">\int_0^1 \frac{dx}{1+x^2} = \frac{\pi}{4} \implies \pi \approx 4 \times 0.785406 = \mathbf{3.1416}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Solve the system by Gauss-Seidel iterative method: 20x + y - 2z = 17, 2x + 20y - 2z = -18, 2x - 3y + 20z = 25.</div>
    <div class="ans-body">
        <strong>Solution:</strong> The system is strictly diagonally dominant:<br>
        <div class="math-block">x = \frac{17 - y + 2z}{20}, \quad y = \frac{-18 - 2x + 2z}{20}, \quad z = \frac{25 - 2x + 3y}{20}</div>
        Start with <span class="math">(x_0, y_0, z_0) = (0, 0, 0)</span>.<br>
        <strong>Iter 1:</strong>
        <span class="math">x_1 = \frac{17}{20} = 0.8500</span><br>
        <span class="math">y_1 = \frac{-18 - 2(0.85)}{20} = \frac{-19.7}{20} = -0.9850</span><br>
        <span class="math">z_1 = \frac{25 - 2(0.85) + 3(-0.985)}{20} = \frac{25 - 1.7 - 2.955}{20} = 1.0173</span><br><br>
        <strong>Iter 2:</strong>
        <span class="math">x_2 = \frac{17 - (-0.9850) + 2(1.0173)}{20} = \frac{20.0196}{20} = 1.0010</span><br>
        <span class="math">y_2 = \frac{-18 - 2(1.0010) + 2(1.0173)}{20} = \frac{-17.9674}{20} = -0.9984</span><br>
        <span class="math">z_2 = \frac{25 - 2(1.0010) + 3(-0.9984)}{20} = \frac{20.0028}{20} = 1.0001</span><br><br>
        <strong>Iter 3:</strong>
        <span class="math">x_3 = \frac{17 - (-0.9984) + 2(1.0001)}{20} = 1.0000</span><br>
        <span class="math">y_3 = \frac{-18 - 2(1) + 2(1)}{20} = -1.0000</span><br>
        <span class="math">z_3 = \frac{25 - 2(1) + 3(-1)}{20} = 1.0000</span><br>
        <strong>Final Answer:</strong> <span class="math">\mathbf{x = 1.000, \; y = -1.000, \; z = 1.000}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Using fourth order Runge-Kutta method, find y(0.2) and y(0.4) given dy/dx = x + y with y(0) = 1 (step size h = 0.2).</div>
    <div class="ans-body">
        <strong>Solution:</strong> <span class="math">f(x, y) = x + y</span>, <span class="math">x_0 = 0, y_0 = 1, h = 0.2</span>.<br>
        <strong>Step 1: Compute y(0.2)</strong><br>
        <span class="math">k_1 = 0.2(0 + 1) = 0.2000</span><br>
        <span class="math">k_2 = 0.2(0.1 + 1.1) = 0.2400</span><br>
        <span class="math">k_3 = 0.2(0.1 + 1.12) = 0.2440</span><br>
        <span class="math">k_4 = 0.2(0.2 + 1.244) = 0.2888</span><br>
        <span class="math">\Delta y = \frac{0.2000 + 2(0.2400) + 2(0.2440) + 0.2888}{6} = \frac{1.4568}{6} = 0.2428</span><br>
        <div class="math-block">y(0.2) = 1 + 0.2428 = \mathbf{1.2428}</div>
        <strong>Step 2: Compute y(0.4) from x₁ = 0.2, y₁ = 1.2428</strong><br>
        <span class="math">k_1 = 0.2(0.2 + 1.2428) = 0.2886</span><br>
        <span class="math">k_2 = 0.2(0.3 + 1.2428 + 0.1443) = 0.3374</span><br>
        <span class="math">k_3 = 0.2(0.3 + 1.2428 + 0.1687) = 0.3423</span><br>
        <span class="math">k_4 = 0.2(0.4 + 1.2428 + 0.3423) = 0.3970</span><br>
        <span class="math">\Delta y_1 = \frac{0.2886 + 2(0.3374) + 2(0.3423) + 0.3970}{6} = \frac{2.0450}{6} = 0.3408</span><br>
        <div class="math-block">y(0.4) = 1.2428 + 0.3408 = \mathbf{1.5836}</div>
        <strong>Answer:</strong> <span class="math">y(0.2) = \mathbf{1.2428}</span>, <span class="math">y(0.4) = \mathbf{1.5836}</span>.
    </div>
</div>
"""

print("2022 HTML ready. Generating 2022...")
generate_pdf("December 2022", "numerical methods 2022 solved.pdf", YEAR_2022_HTML)
