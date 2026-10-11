## Section - A (Very Short Answer Questions — 3 Marks Each, All 5 Mandatory)

### Q1. Obtain a real root of f(x) = x^3 + x^2 - 1 = 0 using Bisection method correct to 3 decimal places.
**Solution:**
- f(0) = -1 < 0, f(1) = 1 > 0. Real root lies in (0, 1).
- Midpoint iterations:
  - c1 = 0.5 -> f(0.5) = -0.625 < 0
  - c2 = 0.75 -> f(0.75) = -0.0156 < 0
  - c3 = 0.875 -> f(0.875) = +0.4355 > 0
  - Iterations continued until |b - a| < 0.001.
- **Result:** **x = 0.755**

---

### Q2. Define backward differences and prove that E * grad = grad * E = delta.
**Solution:**
- grad y_i = y_i - y_{i-1}, grad^k y_i = grad^{k-1} y_i - grad^{k-1} y_{i-1}.
- Proof: E * grad f(x) = E [f(x) - f(x-h)] = f(x+h) - f(x) = delta f(x).
- grad * E f(x) = grad f(x+h) = f(x+h) - f(x) = delta f(x).
- Therefore, **E * grad = grad * E = delta**. (Proved).

---

### Q3. Find dy/dx at x = 1.2 for points (1.0, 2.7183), (1.2, 3.3201), (1.4, 4.0552)...
**Solution:**
- Step size h = 0.2. Points represent y = e^x.
- Central difference formula:
f'(1.2) = (y1 - y_{-1}) / (2h) = (4.0552 - 2.7183) / (2 * 0.2) = 1.3369 / 0.4 = **3.34225**

---

### Q4. Solve the following linear system using Gauss Elimination method:
10x + y + z = 12
2x + 10y + z = 13
x + y + 3z = 5

**Solution:**
- Forward elimination produces upper-triangular matrix with diagonal elements 10, 9.8, 2.82653.
- Back substitution gives:
**x = 1, y = 1, z = 1**

---

### Q5. Solve dy/dx = x + y^2, y(0) = 1 using Picard's method up to second approximation.
**Solution:**
- y^(1) = 1 + integral_0^x (t + 1) dt = **1 + x + x^2 / 2**
- y^(2) = 1 + integral_0^x [t + (1 + t + t^2/2)^2] dt = **1 + x + (3/2)x^2 + (2/3)x^3 + (1/4)x^4 + (1/20)x^5**

---

## Section - B (Short Answer Questions — 7.5 Marks Each, Attempt Any Two)

### Q6. Find a real root of 2x = log10(x) + 7 between 3 and 4 using Method of False Position.
**Solution:**
- f(x) = 2x - log10(x) - 7 = 0.
- f(3) = -1.47712 < 0, f(4) = +0.39794 > 0.
- Formula: x2 = [x0*f(x1) - x1*f(x0)] / [f(x1) - f(x0)] = [3(0.39794) - 4(-1.47712)] / [0.39794 - (-1.47712)] = 3.78777.
- Second iteration gives: **x = 3.7893**.

---

### Q7. Find missing terms in table:
x: [0, 5, 10, 15, 20, 25, 30], y: [1, 3, -, 73, 225, -, 1153].
**Solution:**
- 5 values given -> delta^5 y = 0 -> (E - 1)^5 y = 0.
- System of equations:
  - -10*y2 + y5 = 381
  - y5 - y2 = 534
- Solving gives: **y2 = 17 (at x=10)**, **y5 = 551 (at x=25)**.

---

### Q8. Evaluate I = integral_3^7 x^2 * log10(x) dx using Simpson's 1/3 rule with n = 4.
**Solution:**
- h = (7 - 3) / 4 = 1.
- y0 = 4.2941, y1 = 9.6330, y2 = 17.4743, y3 = 28.0134, y4 = 41.4099.
- I = (1/3) * [(y0 + y4) + 4*(y1 + y3) + 2*y2] = **77.0794**.

---

## Section - C (Long Answer Questions — 15 Marks Each, Attempt Any Three)

### Q9. Newton-Raphson method for sin(x) = x/2 to 3 decimal places between pi/2 and pi.
**Solution:**
- f(x) = sin(x) - x/2, f'(x) = cos(x) - 0.5. Initial guess x0 = 2.0.
- x1 = 2.0 - (-0.09070 / -0.91615) = 1.90100.
- x2 = 1.89552, x3 = 1.89549.
- **Result:** **x = 1.895 radians**.

---

### Q10. Lagrange interpolating polynomial degree 2 for y = ln(x) for x in [2.0, 2.5, 3.0]. Find ln(2.7).
**Solution:**
- Given: (2.0, 0.69315), (2.5, 0.91629), (3.0, 1.09861).
- L0 = -0.12, L1 = 0.84, L2 = 0.28.
- P2(2.7) = (-0.12)(0.69315) + (0.84)(0.91629) + (0.28)(1.09861) = **0.99412**.

---

### Q11. Use Simpson's 3/8 rule to evaluate integral_0^1 [1 / (1 + x)] dx with h = 1/6.
**Solution:**
- Points: y0 = 1, y1 = 6/7, y2 = 6/8, y3 = 6/9, y4 = 6/10, y5 = 6/11, y6 = 1/2.
- I = [3*(1/6)/8] * [y0 + y6 + 3*(y1 + y2 + y4 + y5) + 2*y3] = (1/16) * [11.091128] = **0.693196**.

---

### Q12. Solve system by Gauss-Seidel iterative method:
6x + y + z = 20
x + 4y - z = 6
x - y + 5z = 7

**Solution:**
- Diagonally dominant: |6|>2, |4|>2, |5|>2.
- Iterations converge to:
**x = 3, y = 1, z = 1**

---

### Q13. Apply Runge-Kutta 4th Order method for dy/dx = y - x, y(0) = 2 to find y(0.1) and y(0.2).
**Solution:**
- Step 1 (h=0.1): k1 = 0.20, k2 = 0.205, k3 = 0.20525, k4 = 0.210525 -> **y(0.1) = 2.2052**.
- Step 2 (h=0.1): k1 = 0.210517, k2 = 0.216043, k3 = 0.216319, k4 = 0.222149 -> **y(0.2) = 2.4214**.
