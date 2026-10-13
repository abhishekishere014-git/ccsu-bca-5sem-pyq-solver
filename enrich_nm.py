# Enriched Exam-Style Answers for Numerical Methods (BCA-504)

NM_ENRICHMENTS = {
    "define operators e, &delta; and &nabla;": """
<p><strong>Answer:</strong></p>
<p>In the Calculus of Finite Differences, the fundamental operators are defined as follows:</p>
<div class=\"info-box\">
    <ol>
        <li><b>Shift Operator (E):</b> Increases the argument by step interval <i>h</i>:
            <br><code>E f(x) = f(x + h)</code>
        </li>
        <li><b>Forward Difference Operator (&Delta;):</b> Computes the difference between next value and current value:
            <br><code>&Delta; f(x) = f(x + h) - f(x)</code>
        </li>
        <li><b>Backward Difference Operator (&nabla;):</b> Computes difference between current value and previous value:
            <br><code>&nabla; f(x) = f(x) - f(x - h)</code>
        </li>
    </ol>
</div>
<p class=\"step-label\">Derivation of Relation between E and &Delta;:</p>
<div class=\"info-box\">
    <p>By definition of Forward Difference: <code>&Delta; f(x) = f(x + h) - f(x)</code></p>
    <p>Since <code>E f(x) = f(x + h)</code>, we can substitute:</p>
    <p><code>&Delta; f(x) = E f(x) - f(x) = (E - 1) f(x)</code></p>
    <p>Factoring out the operand <code>f(x)</code>, we obtain the fundamental operational identity:</p>
    <p><b>&Delta; = E - 1</b> &nbsp; or &nbsp; <b>E = 1 + &Delta; = &Delta; + 1</b> &check;</p>
</div>
""",

    "find backward differences for the points: (5, 11)": """
<p><strong>Answer:</strong></p>
<p><b>Given Data Points:</b> (5, 11), (6, 13), (9, 28), (11, 40).</p>
<div class=\"info-box\">
    <p><i>Note:</i> The argument values <i>x</i> = 5, 6, 9, 11 are unequally spaced (intervals h = 1, 3, 2). For unequally spaced arguments, Divided Differences or standard finite differences can be computed.</p>
</div>
<p class=\"step-label\">Difference Table Construction:</p>
<table class=\"data-table\">
    <tr><th>x</th><th>y = f(x)</th><th>First Difference (&Delta;y)</th><th>Second Difference (&Delta;<sup>2</sup>y)</th><th>Third Difference (&Delta;<sup>3</sup>y)</th></tr>
    <tr><td>5</td><td>11</td><td>&mdash;</td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>6</td><td>13</td><td>13 - 11 = <b>2</b></td><td>&mdash;</td><td>&mdash;</td></tr>
    <tr><td>9</td><td>28</td><td>28 - 13 = <b>15</b></td><td>15 - 2 = <b>13</b></td><td>&mdash;</td></tr>
    <tr><td>11</td><td>40</td><td>40 - 28 = <b>12</b></td><td>12 - 15 = <b>-3</b></td><td>-3 - 13 = <b>-16</b></td></tr>
</table>
<div class=\"info-box\">
    <p><b>Backward Differences at the final point (x = 11, y<sub>3</sub> = 40):</b></p>
    <ul>
        <li>First backward difference: <b>&nabla;y<sub>3</sub> = 12</b></li>
        <li>Second backward difference: <b>&nabla;<sup>2</sup>y<sub>3</sub> = -3</b></li>
        <li>Third backward difference: <b>&nabla;<sup>3</sup>y<sub>3</sub> = -16</b></li>
    </ul>
</div>
"""
}
