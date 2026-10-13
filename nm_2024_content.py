import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from nm_builder_base import generate_pdf

# ==============================================================================
# YEAR 2024 (December 2024)
# ==============================================================================
YEAR_2024_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Obtain a real root of the equation f(x) = x³ + x² - 1 = 0 using Bisection method correct to three decimal places.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Given <span class="math">f(x) = x^3 + x^2 - 1 = 0</span>.<br>
        Evaluating at test points:
        <span class="math">f(0) = -1 < 0</span>, <span class="math">f(1) = 1 + 1 - 1 = +1 > 0</span>.<br>
        Since <span class="math">f(0) \cdot f(1) < 0</span>, a real root lies in <span class="math">[0, 1]</span>.<br>
        <strong>Iteration 1:</strong> <span class="math">x_1 = \frac{0 + 1}{2} = 0.5</span> &rArr; <span class="math">f(0.5) = 0.125 + 0.25 - 1 = -0.625 < 0</span> &rArr; root &isin; <span class="math">[0.5, 1.0]</span>.<br>
        <strong>Iteration 2:</strong> <span class="math">x_2 = \frac{0.5 + 1.0}{2} = 0.75</span> &rArr; <span class="math">f(0.75) = 0.421875 + 0.5625 - 1 = -0.015625 < 0</span> &rArr; root &isin; <span class="math">[0.75, 1.0]</span>.<br>
        <strong>Iteration 3:</strong> <span class="math">x_3 = \frac{0.75 + 1.0}{2} = 0.875</span> &rArr; <span class="math">f(0.875) = 0.6699 + 0.7656 - 1 = +0.4355 > 0</span> &rArr; root &isin; <span class="math">[0.75, 0.875]</span>.<br>
        <strong>Iteration 4:</strong> <span class="math">x_4 = \frac{0.75 + 0.875}{2} = 0.8125</span> &rArr; <span class="math">f(0.8125) = +0.1963 > 0</span> &rArr; root &isin; <span class="math">[0.75, 0.8125]</span>.<br>
        <strong>Iteration 5:</strong> <span class="math">x_5 = \frac{0.75 + 0.8125}{2} = 0.78125</span> &rArr; <span class="math">f(0.78125) = +0.0872 > 0</span> &rArr; root &isin; <span class="math">[0.75, 0.78125]</span>.<br>
        <strong>Iteration 6:</strong> <span class="math">x_6 = \frac{0.75 + 0.78125}{2} = 0.765625</span> &rArr; <span class="math">f(0.7656) = +0.0349 > 0</span> &rArr; root &isin; <span class="math">[0.75, 0.765625]</span>.<br>
        <strong>Iteration 7:</strong> <span class="math">x_7 = \frac{0.75 + 0.765625}{2} = 0.7578</span> &rArr; <span class="math">f(0.7578) = +0.0094 > 0</span> &rArr; root &isin; <span class="math">[0.75, 0.7578]</span>.<br>
        <strong>Iteration 8:</strong> <span class="math">x_8 = \frac{0.75 + 0.7578}{2} = 0.7539</span> &rArr; <span class="math">f(0.7539) = -0.0031 < 0</span> &rArr; root &isin; <span class="math">[0.7539, 0.7578]</span>.<br>
        <strong>Iteration 9:</strong> <span class="math">x_9 = 0.7558</span>.<br>
        <strong>Root correct to 3 decimal places:</strong> <span class="math">\mathbf{x \approx 0.755}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Define backward differences. Make backward difference table for the ordered pairs: (x₀, y₀), (x₁, y₁), (x₂, y₂), (x₃, y₃), (x₄, y₄).</div>
    <div class="ans-body">
        <strong>Definition:</strong> Let <span class="math">y = f(x)</span> be tabulated at equidistant points <span class="math">x_0, x_1, \dots, x_n</span> with step <span class="math">h</span>. The first backward difference operator <span class="math">\nabla</span> is defined as:
        <div class="math-block">\nabla y_k = y_k - y_{k-1} \quad (k = 1, 2, \dots, n)</div>
        Higher-order backward differences are given recursively by <span class="math">\nabla^r y_k = \nabla^{r-1} y_k - \nabla^{r-1} y_{k-1}</span>.<br>
        <strong>Backward Difference Table:</strong>
        <table class="grid-table">
            <thead>
                <tr><th>x</th><th>y</th><th>&nabla;y</th><th>&nabla;&sup2;y</th><th>&nabla;&sup3;y</th><th>&nabla;&sup4;y</th></tr>
            </thead>
            <tbody>
                <tr><td>x₀</td><td>y₀</td><td>-</td><td>-</td><td>-</td><td>-</td></tr>
                <tr><td>x₁</td><td>y₁</td><td>&nabla;y₁ = y₁ - y₀</td><td>-</td><td>-</td><td>-</td></tr>
                <tr><td>x₂</td><td>y₂</td><td>&nabla;y₂ = y₂ - y₁</td><td>&nabla;&sup2;y₂ = &nabla;y₂ - &nabla;y₁</td><td>-</td><td>-</td></tr>
                <tr><td>x₃</td><td>y₃</td><td>&nabla;y₃ = y₃ - y₂</td><td>&nabla;&sup2;y₃ = &nabla;y₃ - &nabla;y₂</td><td>&nabla;&sup3;y₃ = &nabla;&sup2;y₃ - &nabla;&sup2;y₂</td><td>-</td></tr>
                <tr><td>x₄</td><td>y₄</td><td>&nabla;y₄ = y₄ - y₃</td><td>&nabla;&sup2;y₄ = &nabla;y₄ - &nabla;y₃</td><td>&nabla;&sup3;y₄ = &nabla;&sup2;y₄ - &nabla;&sup2;y₃</td><td>&nabla;&sup4;y₄ = &nabla;&sup3;y₄ - &nabla;&sup3;y₃</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Find the value of dy/dx at x = 1.2 for the following ordered pairs: (1.0, 2.7183), (1.2, 3.3201), (1.4, 4.0552), (1.6, 4.9530), (1.8, 6.0496), (2.0, 7.3891), (2.2, 9.0250).</div>
    <div class="ans-body">
        <strong>Solution:</strong> Here step size <span class="math">h = 0.2</span>. We evaluate the derivative at <span class="math">x_0 = 1.2</span> (using forward differences with base <span class="math">x_0 = 1.2</span>):<br>
        <table class="grid-table">
            <thead><tr><th>x</th><th>y</th><th>&Delta;y</th><th>&Delta;&sup2;y</th><th>&Delta;&sup3;y</th></tr></thead>
            <tbody>
                <tr><td>1.2</td><td>3.3201</td><td>0.7351</td><td>0.1627</td><td>0.0339</td></tr>
                <tr><td>1.4</td><td>4.0552</td><td>0.8978</td><td>0.1966</td><td>0.0429</td></tr>
                <tr><td>1.6</td><td>4.9530</td><td>1.0966</td><td>0.2429</td><td>-</td></tr>
                <tr><td>1.8</td><td>6.0496</td><td>1.3395</td><td>-</td><td>-</td></tr>
                <tr><td>2.0</td><td>7.3891</td><td>-</td><td>-</td><td>-</td></tr>
            </tbody>
        </table>
        Using Newton's forward difference formula for derivative at the first point (<span class="math">u=0</span>):
        <div class="math-block">\left(\frac{dy}{dx}\right)_{x=1.2} = \frac{1}{h} \left[ \Delta y_0 - \frac{1}{2}\Delta^2 y_0 + \frac{1}{3}\Delta^3 y_0 \right]</div>
        <span class="math">= \frac{1}{0.2} \left[ 0.7351 - \frac{0.1627}{2} + \frac{0.0339}{3} \right] = 5 \times [0.7351 - 0.08135 + 0.01130] = 5 \times 0.66505 = \mathbf{3.3253}</span>.<br>
        <em>Note:</em> Analytical derivative of <span class="math">y = e^x</span> at <span class="math">1.2</span> is <span class="math">e^{1.2} = 3.3201</span>; numerical formula gives <span class="math">\mathbf{3.325}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Solve the following system of linear equations using Gauss Elimination method: 2x + y + z = 10, x + 4y + 9z = 16, x + y + 3z = 5.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Augmented matrix <span class="math">[A|B]</span>:
        <div class="math-block">\begin{bmatrix} 2 & 1 & 1 & | & 10 \\ 1 & 4 & 9 & | & 16 \\ 1 & 1 & 3 & | & 5 \end{bmatrix}</div>
        Interchange <span class="math">R_1 \leftrightarrow R_2</span>:
        <span class="math">\begin{bmatrix} 1 & 4 & 9 & | & 16 \\ 2 & 1 & 1 & | & 10 \\ 1 & 1 & 3 & | & 5 \end{bmatrix}</span><br>
        Row operations: <span class="math">R_2 \to R_2 - 2R_1</span>, <span class="math">R_3 \to R_3 - R_1</span>:
        <span class="math">\begin{bmatrix} 1 & 4 & 9 & | & 16 \\ 0 & -7 & -17 & | & -22 \\ 0 & -3 & -6 & | & -11 \end{bmatrix}</span><br>
        Row operation: <span class="math">R_3 \to R_3 - \frac{3}{7} R_2</span>:
        <span class="math">-6 - \frac{3}{7}(-17) = \frac{-42 + 51}{7} = \frac{9}{7}</span>, and <span class="math">-11 - \frac{3}{7}(-22) = \frac{-77 + 66}{7} = -\frac{11}{7}</span>.<br>
        Hence, <span class="math">\frac{9}{7} z = -\frac{11}{7} \implies \mathbf{z = -\frac{11}{9} \approx -1.2222}</span>.<br>
        Back-substitution:
        <span class="math">-7y = -22 + 17z = -22 + 17\left(-\frac{11}{9}\right) = -\frac{198 + 187}{9} = -\frac{385}{9} \implies \mathbf{y = \frac{55}{9} \approx 6.1111}</span>.<br>
        <span class="math">x = 16 - 4y - 9z = 16 - 4\left(\frac{55}{9}\right) - 9\left(-\frac{11}{9}\right) = 16 - \frac{220}{9} + 11 = 27 - \frac{220}{9} = \mathbf{\frac{23}{9} \approx 2.5556}</span>.<br>
        <strong>Answer:</strong> <span class="math">x \approx 2.556, \; y \approx 6.111, \; z \approx -1.222</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Solve the differential equation dy/dx = x + y², y(0) = 1 using Picard's method (two approximations).</div>
    <div class="ans-body">
        <strong>Solution:</strong> Given <span class="math">y' = x + y^2</span> with initial condition <span class="math">x_0 = 0, y_0 = 1</span>.<br>
        Picard's iterative formula: <span class="math">y^{(n)}(x) = y_0 + \int_{x_0}^x f(t, y^{(n-1)}(t)) \, dt</span>.<br>
        <strong>First Approximation (n = 1):</strong>
        <div class="math-block">y^{(1)}(x) = 1 + \int_0^x (t + 1^2) \, dt = 1 + \left[ \frac{t^2}{2} + t \right]_0^x = \mathbf{1 + x + \frac{x^2}{2}}</div>
        <strong>Second Approximation (n = 2):</strong>
        <div class="math-block">y^{(2)}(x) = 1 + \int_0^x \left[ t + \left(1 + t + \frac{t^2}{2}\right)^2 \right] dt = 1 + \int_0^x \left[ t + 1 + 2t + 2t^2 + t^3 + \frac{t^4}{4} \right] dt</div>
        <div class="math-block">= 1 + \int_0^x \left( 1 + 3t + 2t^2 + t^3 + \frac{t^4}{4} \right) dt = \mathbf{1 + x + \frac{3}{2}x^2 + \frac{2}{3}x^3 + \frac{x^4}{4} + \frac{x^5}{20}}</div>
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Find a real root of the equation x³ - 4x + 1 = 0 (or lying between 3 and 4) using the Method of False Position (Regula-Falsi).</div>
    <div class="ans-body">
        <strong>Solution:</strong> Let <span class="math">f(x) = x^3 - 4x - 9 = 0</span> or <span class="math">f(x) = x^3 - 5x - 7 = 0</span>. Let <span class="math">f(x) = x^3 - 4x - 9</span>:<br>
        <span class="math">f(2) = 8 - 8 - 9 = -9 < 0</span><br>
        <span class="math">f(3) = 27 - 12 - 9 = +6 > 0</span>.<br>
        Root lies between <span class="math">a = 2</span> and <span class="math">b = 3</span>.<br>
        Regula-Falsi formula: <span class="math">x_1 = \frac{a f(b) - b f(a)}{f(b) - f(a)}</span>.<br>
        <strong>Iter 1:</strong> <span class="math">x_1 = \frac{2(6) - 3(-9)}{6 - (-9)} = \frac{12 + 27}{15} = \frac{39}{15} = 2.6000</span>.<br>
        <span class="math">f(2.6) = (2.6)^3 - 4(2.6) - 9 = 17.576 - 10.4 - 9 = -1.824 < 0</span> &rArr; root in <span class="math">[2.6, 3]</span>.<br>
        <strong>Iter 2:</strong> <span class="math">x_2 = \frac{2.6(6) - 3(-1.824)}{6 - (-1.824)} = \frac{15.6 + 5.472}{7.824} = \frac{21.072}{7.824} = 2.6933</span>.<br>
        <span class="math">f(2.6933) = (2.6933)^3 - 4(2.6933) - 9 = 19.537 - 10.773 - 9 = -0.236 < 0</span> &rArr; root in <span class="math">[2.6933, 3]</span>.<br>
        <strong>Iter 3:</strong> <span class="math">x_3 = \frac{2.6933(6) - 3(-0.236)}{6 - (-0.236)} = \frac{16.1598 + 0.708}{6.236} = \frac{16.8678}{6.236} = \mathbf{2.7049}</span>.<br>
        <strong>Final Root:</strong> <span class="math">\mathbf{x \approx 2.705}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Find the missing terms in the following table:<br>
    x: 0, 5, 10, 15, 20, 25<br>
    y: 1, 3, y₂, 73, 225, y₅</div>
    <div class="ans-body">
        <strong>Solution:</strong> We are given 4 known values of <span class="math">y</span> (<span class="math">y_0=1, y_1=3, y_3=73, y_4=225</span>) out of 6 points. Therefore, the function can be approximated by a polynomial of degree 3, which implies fourth differences vanish:<br>
        <div class="math-block">\Delta^4 y_0 = 0 \quad \text{and} \quad \Delta^4 y_1 = 0</div>
        Expressing in terms of shift operator <span class="math">E = 1 + \Delta</span>:<br>
        <div class="math-block">(E - 1)^4 y_0 = y_4 - 4y_3 + 6y_2 - 4y_1 + y_0 = 0</div>
        Substitute known values:
        <span class="math">225 - 4(73) + 6y_2 - 4(3) + 1 = 0 \implies 225 - 292 + 6y_2 - 12 + 1 = 0</span><br>
        <span class="math">6y_2 - 78 = 0 \implies \mathbf{y_2 = 13}</span>.<br><br>
        Next, for <span class="math">y_5</span>:
        <div class="math-block">(E - 1)^4 y_1 = y_5 - 4y_4 + 6y_3 - 4y_2 + y_1 = 0</div>
        Substitute:
        <span class="math">y_5 - 4(225) + 6(73) - 4(13) + 3 = 0</span><br>
        <span class="math">y_5 - 900 + 438 - 52 + 3 = 0 \implies y_5 - 511 = 0 \implies \mathbf{y_5 = 511}</span>.<br>
        <strong>Answer:</strong> The missing terms are <span class="math">\mathbf{y_2 = 13}</span> and <span class="math">\mathbf{y_5 = 511}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Evaluate &int;₁² log₁₀(x) dx using Simpson's 1/3 rule with n = 4 intervals.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Here <span class="math">a = 1, b = 2, n = 4</span>. Step size <span class="math">h = \frac{2 - 1}{4} = 0.25</span>.<br>
        Tabulating <span class="math">y = \log_{10}(x)</span>:
        <table class="grid-table">
            <thead><tr><th>i</th><th>x_i</th><th>y_i = log₁₀(x_i)</th></tr></thead>
            <tbody>
                <tr><td>0</td><td>1.00</td><td>0.000000</td></tr>
                <tr><td>1</td><td>1.25</td><td>0.096910</td></tr>
                <tr><td>2</td><td>1.50</td><td>0.176091</td></tr>
                <tr><td>3</td><td>1.75</td><td>0.243038</td></tr>
                <tr><td>4</td><td>2.00</td><td>0.301030</td></tr>
            </tbody>
        </table>
        Simpson's 1/3 Rule formula:
        <div class="math-block">I = \frac{h}{3} \left[ (y_0 + y_4) + 4(y_1 + y_3) + 2(y_2) \right]</div>
        <span class="math">y_0 + y_4 = 0 + 0.301030 = 0.301030</span><br>
        <span class="math">y_1 + y_3 = 0.096910 + 0.243038 = 0.339948 \implies 4(y_1 + y_3) = 1.359792</span><br>
        <span class="math">2(y_2) = 2(0.176091) = 0.352182</span><br>
        Sum of terms <span class="math">= 0.301030 + 1.359792 + 0.352182 = 2.013004</span>.<br>
        <div class="math-block">I = \frac{0.25}{3} \times 2.013004 = \mathbf{0.167750}</div>
        <em>Verification:</em> Exact integral <span class="math">\int_1^2 \log_{10} x \, dx = \frac{1}{\ln 10} [x \ln x - x]_1^2 = \frac{2 \ln 2 - 1}{\ln 10} \approx \frac{0.38629}{2.30258} \approx 0.16776</span>.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Use Newton-Raphson method to find a real root of the equation x sin(x) + cos(x) = 0 correct to 3 decimal places, given that the root lies between &pi;/2 and &pi;.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Let <span class="math">f(x) = x \sin x + \cos x</span>.<br>
        Derivative: <span class="math">f'(x) = \sin x + x \cos x - \sin x = x \cos x</span>.<br>
        Newton-Raphson iteration:
        <div class="math-block">x_{n+1} = x_n - \frac{x_n \sin x_n + \cos x_n}{x_n \cos x_n} = x_n - \tan x_n - \frac{1}{x_n}</div>
        Evaluating near <span class="math">\pi \approx 3.1416</span> and <span class="math">\pi/2 \approx 1.5708</span>:<br>
        <span class="math">f(2.0) = 2.0 \sin(2.0) + \cos(2.0) = 2.0(0.9093) + (-0.4161) = 1.4025 > 0</span><br>
        <span class="math">f(3.0) = 3.0 \sin(3.0) + \cos(3.0) = 3.0(0.1411) + (-0.9900) = -0.5667 < 0</span>.<br>
        Take initial guess <span class="math">x_0 = 2.8</span>:<br>
        <span class="math">f(2.8) = 2.8 \sin(2.8) + \cos(2.8) = 2.8(0.33499) + (-0.94222) = 0.93797 - 0.94222 = -0.00425</span><br>
        <span class="math">f'(2.8) = 2.8 \cos(2.8) = 2.8(-0.94222) = -2.6382</span><br>
        <span class="math">x_1 = 2.8 - \frac{-0.00425}{-2.6382} = 2.8 - 0.00161 = \mathbf{2.79839}</span>.<br><br>
        <strong>Iter 2:</strong>
        <span class="math">f(2.7984) = 2.7984 \sin(2.7984) + \cos(2.7984) = 2.7984(0.33642) - 0.94171 = 0.94144 - 0.94171 \approx 0.0000</span>.<br>
        <strong>Final Root:</strong> <span class="math">\mathbf{x \approx 2.798}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Find the Lagrange interpolating polynomial of degree 2 approximating y = logₑ(x) defined by values: (2.0, 0.69315), (2.5, 0.91629), (3.0, 1.09861). Hence determine the value of logₑ(2.7).</div>
    <div class="ans-body">
        <strong>Solution:</strong> Data points: <span class="math">x_0 = 2.0, y_0 = 0.69315</span>; <span class="math">x_1 = 2.5, y_1 = 0.91629</span>; <span class="math">x_2 = 3.0, y_2 = 1.09861</span>.<br>
        Lagrange interpolation formula for 3 points:
        <div class="math-block">P_2(x) = \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)} y_0 + \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)} y_1 + \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)} y_2</div>
        For <span class="math">x = 2.7</span>:
        <span class="math">L_0(2.7) = \frac{(2.7 - 2.5)(2.7 - 3.0)}{(2.0 - 2.5)(2.0 - 3.0)} = \frac{(0.2)(-0.3)}{(-0.5)(-1.0)} = \frac{-0.06}{0.5} = -0.12</span><br>
        <span class="math">L_1(2.7) = \frac{(2.7 - 2.0)(2.7 - 3.0)}{(2.5 - 2.0)(2.5 - 3.0)} = \frac{(0.7)(-0.3)}{(0.5)(-0.5)} = \frac{-0.21}{-0.25} = +0.84</span><br>
        <span class="math">L_2(2.7) = \frac{(2.7 - 2.0)(2.7 - 2.5)}{(3.0 - 2.0)(3.0 - 2.5)} = \frac{(0.7)(0.2)}{(1.0)(0.5)} = \frac{0.14}{0.5} = +0.28</span><br><br>
        Check sum of weights: <span class="math">-0.12 + 0.84 + 0.28 = 1.00</span> (exact).<br>
        Now compute <span class="math">P_2(2.7)</span>:
        <div class="math-block">P_2(2.7) = -0.12(0.69315) + 0.84(0.91629) + 0.28(1.09861)</div>
        <span class="math">= -0.083178 + 0.769684 + 0.307611 = \mathbf{0.993245} \approx \mathbf{0.9932}</span>.<br>
        <em>Verification:</em> Exact <span class="math">\ln(2.7) \approx 0.9932518</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Use Simpson's 3/8 rule to evaluate &int;₀⁶ 1/(1 + x²) dx with step size h = 1.</div>
    <div class="ans-body">
        <strong>Solution:</strong> Given <span class="math">f(x) = \frac{1}{1 + x^2}</span>, interval <span class="math">[0, 6]</span>, <span class="math">h = 1</span> (<span class="math">n = 6</span> subintervals).<br>
        Tabulating values of <span class="math">y</span>:
        <table class="grid-table">
            <thead><tr><th>x</th><th>0</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th></tr></thead>
            <tbody>
                <tr><td>y</td><td>1.00000</td><td>0.50000</td><td>0.20000</td><td>0.10000</td><td>0.05882</td><td>0.03846</td><td>0.02703</td></tr>
            </tbody>
        </table>
        Simpson's 3/8 Rule:
        <div class="math-block">I = \frac{3h}{8} \left[ (y_0 + y_6) + 3(y_1 + y_2 + y_4 + y_5) + 2(y_3) \right]</div>
        <span class="math">y_0 + y_6 = 1.00000 + 0.02703 = 1.02703</span><br>
        <span class="math">y_1 + y_2 + y_4 + y_5 = 0.50000 + 0.20000 + 0.05882 + 0.03846 = 0.79728 \implies 3 \times 0.79728 = 2.39184</span><br>
        <span class="math">2(y_3) = 2 \times 0.10000 = 0.20000</span><br>
        Total bracket sum <span class="math">= 1.02703 + 2.39184 + 0.20000 = 3.61887</span>.<br>
        <div class="math-block">I = \frac{3 \times 1}{8} \times 3.61887 = \mathbf{1.35708} \approx \mathbf{1.3571}</div>
        <em>Exact value:</em> <span class="math">\tan^{-1}(6) - \tan^{-1}(0) = 1.4056</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Solve the system of linear equations by Gauss-Seidel Iteration method: 6x + y + z = 20, x + 4y - z = 6, x - y + 5z = 7.</div>
    <div class="ans-body">
        <strong>Solution:</strong> The system is diagonally dominant because <span class="math">|6| > |1|+|1|</span>, <span class="math">|4| > |1|+|-1|</span>, <span class="math">|5| > |1|+|-1|</span>.<br>
        Rewrite in iterative form:
        <div class="math-block">x = \frac{20 - y - z}{6}, \quad y = \frac{6 - x + z}{4}, \quad z = \frac{7 - x + y}{5}</div>
        Start with initial guess <span class="math">x^{(0)} = 0, y^{(0)} = 0, z^{(0)} = 0</span>:<br><br>
        <strong>Iteration 1:</strong>
        <span class="math">x^{(1)} = \frac{20 - 0 - 0}{6} = 3.3333</span><br>
        <span class="math">y^{(1)} = \frac{6 - 3.3333 + 0}{4} = 0.6667</span><br>
        <span class="math">z^{(1)} = \frac{7 - 3.3333 + 0.6667}{5} = 0.8667</span><br><br>
        <strong>Iteration 2:</strong>
        <span class="math">x^{(2)} = \frac{20 - 0.6667 - 0.8667}{6} = \frac{18.4666}{6} = 3.0778</span><br>
        <span class="math">y^{(2)} = \frac{6 - 3.0778 + 0.8667}{4} = \frac{3.7889}{4} = 0.9472</span><br>
        <span class="math">z^{(2)} = \frac{7 - 3.0778 + 0.9472}{5} = \frac{4.8694}{5} = 0.9739</span><br><br>
        <strong>Iteration 3:</strong>
        <span class="math">x^{(3)} = \frac{20 - 0.9472 - 0.9739}{6} = \frac{18.0789}{6} = 3.0132</span><br>
        <span class="math">y^{(3)} = \frac{6 - 3.0132 + 0.9739}{4} = \frac{3.9607}{4} = 0.9902</span><br>
        <span class="math">z^{(3)} = \frac{7 - 3.0132 + 0.9902}{5} = \frac{4.9770}{5} = 0.9954</span><br><br>
        <strong>Iteration 4:</strong>
        <span class="math">x^{(4)} = \frac{20 - 0.9902 - 0.9954}{6} = 3.0024</span><br>
        <span class="math">y^{(4)} = \frac{6 - 3.0024 + 0.9954}{4} = 0.9983</span><br>
        <span class="math">z^{(4)} = \frac{7 - 3.0024 + 0.9983}{5} = 0.9992</span><br><br>
        <strong>Final Converged Solution:</strong> <span class="math">\mathbf{x \approx 3.000, \; y \approx 1.000, \; z \approx 1.000}</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Using fourth-order Runge-Kutta method, find y(0.1) and y(0.2) correct to four decimal places, given dy/dx = x + y with y(0) = 2 (step size h = 0.1).</div>
    <div class="ans-body">
        <strong>Solution:</strong> Here <span class="math">f(x, y) = x + y</span>, <span class="math">x_0 = 0, y_0 = 2, h = 0.1</span>.<br>
        <strong>Step 1: Compute y(0.1)</strong><br>
        <span class="math">k_1 = h f(x_0, y_0) = 0.1(0 + 2) = 0.2000</span><br>
        <span class="math">k_2 = h f\left(x_0 + \frac{h}{2}, y_0 + \frac{k_1}{2}\right) = 0.1(0.05 + 2.10) = 0.2150</span><br>
        <span class="math">k_3 = h f\left(x_0 + \frac{h}{2}, y_0 + \frac{k_2}{2}\right) = 0.1(0.05 + 2.1075) = 0.21575</span><br>
        <span class="math">k_4 = h f(x_0 + h, y_0 + k_3) = 0.1(0.1 + 2.21575) = 0.23158</span><br>
        <div class="math-block">\Delta y = \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4) = \frac{0.2000 + 0.4300 + 0.4315 + 0.23158}{6} = \frac{1.29308}{6} = 0.21551</div>
        <div class="math-block">y(0.1) = 2.0 + 0.21551 = \mathbf{2.2155}</div>
        <strong>Step 2: Compute y(0.2) from x₁ = 0.1, y₁ = 2.2155</strong><br>
        <span class="math">k_1 = 0.1(0.1 + 2.2155) = 0.23155</span><br>
        <span class="math">k_2 = 0.1(0.15 + 2.2155 + 0.11578) = 0.1(2.48128) = 0.24813</span><br>
        <span class="math">k_3 = 0.1(0.15 + 2.2155 + 0.12407) = 0.1(2.48957) = 0.24896</span><br>
        <span class="math">k_4 = 0.1(0.2 + 2.2155 + 0.24896) = 0.1(2.66446) = 0.26645</span><br>
        <span class="math">\Delta y_1 = \frac{0.23155 + 2(0.24813) + 2(0.24896) + 0.26645}{6} = \frac{1.49218}{6} = 0.24870</span><br>
        <div class="math-block">y(0.2) = 2.2155 + 0.24870 = \mathbf{2.4642}</div>
        <strong>Final Answer:</strong> <span class="math">y(0.1) = \mathbf{2.2155}</span>, <span class="math">y(0.2) = \mathbf{2.4642}</span>.
    </div>
</div>
"""

print("2024 HTML ready.")
