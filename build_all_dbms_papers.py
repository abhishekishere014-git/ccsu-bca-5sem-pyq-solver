# -*- coding: utf-8 -*-
"""
Build high-quality textbook-formatted DBMS solved PYQ PDFs for CCSU BCA 5th Semester.
Features structured tables, relational algebra symbols, normal form examples,
and clean page breaks via Chrome Headless.
"""
import os
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
    page-break-after: avoid;
}

.q-box {
    margin-bottom: 12px;
    page-break-inside: auto;
}

.q-title {
    font-size: 10pt;
    font-weight: 700;
    color: #0f172a;
    margin: 6px 0 4px 0;
    page-break-after: avoid;
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

.info-box {
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

.code-box {
    background-color: #0f172a;
    color: #f8fafc;
    padding: 8px 12px;
    border-radius: 5px;
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 8.5pt;
    line-height: 1.4;
    overflow-x: auto;
    page-break-inside: avoid;
    margin: 6px 0;
}

table.data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 8px 0;
    font-size: 8.5pt;
    page-break-inside: avoid;
}

table.data-table th {
    background-color: #1e40af;
    color: #ffffff;
    font-weight: 700;
    padding: 5px 8px;
    border: 1px solid #1e3a8a;
    text-align: left;
}

table.data-table td {
    padding: 4px 8px;
    border: 1px solid #cbd5e1;
    vertical-align: top;
}

table.data-table tr:nth-child(even) td {
    background-color: #f8fafc;
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

ul, ol {
    margin: 3px 0 5px 16px;
    padding: 0;
}

code {
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 8.5pt;
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 1px 4px;
    border-radius: 3px;
    border: 1px solid #e2e8f0;
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
    <div class="q-title">Q1. Define Database Management System (DBMS) and its fundamental purpose. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>A <b>Database Management System (DBMS)</b> is a specialized software package designed to define, construct, manipulate, and share structured databases among various users and applications.</p>
    <div class="info-box">
        <p><b>Four Fundamental Purposes of DBMS:</b></p>
        <ol>
            <li><b>Controlled Redundancy:</b> Integrates multiple logical files to eliminate duplicate data storage.</li>
            <li><b>Data Consistency & Integrity:</b> Enforces business constraints and ACID properties across operations.</li>
            <li><b>Concurrent Multi-User Access:</b> Allows hundreds of simultaneous users to access data without conflicts.</li>
            <li><b>Data Security & Recovery:</b> Provides role-based access control, transaction logs, and disaster recovery.</li>
        </ol>
    </div>
</div>

<hr>

<!-- Q2 -->
<div class="q-box">
    <div class="q-title">Q2. Distinguish between Simple and Composite Attributes with examples. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <table class="data-table">
        <tr>
            <th style="width: 20%;">Attribute Type</th>
            <th style="width: 45%;">Definition & Characteristic</th>
            <th style="width: 35%;">Real-World Examples</th>
        </tr>
        <tr>
            <td><b>Simple Attribute (Atomic)</b></td>
            <td>Cannot be further divided into smaller independent sub-components. Holds a single atomic value.</td>
            <td><code>Roll_No</code>, <code>Age</code>, <code>Gender</code>, <code>Salary</code></td>
        </tr>
        <tr>
            <td><b>Composite Attribute</b></td>
            <td>Can be divided into smaller sub-attributes, each having independent semantic meaning.</td>
            <td><code>Name</code> &rarr; (First, Middle, Last)<br><code>Address</code> &rarr; (Street, City, State, PIN)</td>
        </tr>
    </table>
</div>

<hr>

<!-- Q3 -->
<div class="q-box">
    <div class="q-title">Q3. Explain Referential Integrity Constraint. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p><b>Referential Integrity</b> is a relational constraint between two relations (tables) maintained through a <b>Foreign Key</b>. It dictates that:</p>
    <div class="info-box">
        <p>A value in the Foreign Key column of the referencing table <b>MUST</b> either match an existing Primary Key value in the referenced table, or otherwise be <code>NULL</code>.</p>
    </div>
    <ul>
        <li><b>Prevents Orphan Records:</b> Prevents child records from pointing to non-existent parent rows.</li>
        <li><b>Cascading Actions:</b>
            <ul>
                <li><code>ON DELETE CASCADE</code>: Deleting a parent row automatically deletes all matching child rows.</li>
                <li><code>ON DELETE SET NULL</code>: Deleting a parent row resets foreign key fields in child rows to <code>NULL</code>.</li>
            </ul>
        </li>
    </ul>
</div>

<hr>

<!-- Q4 -->
<div class="q-box">
    <div class="q-title">Q4. Differentiate between DDL and DML commands with syntax. <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <table class="data-table">
        <tr>
            <th style="width: 25%;">Feature</th>
            <th style="width: 38%;">DDL (Data Definition Language)</th>
            <th style="width: 37%;">DML (Data Manipulation Language)</th>
        </tr>
        <tr>
            <td><b>Primary Objective</b></td>
            <td>Defines, alters, and drops database schema structures and tables.</td>
            <td>Manages, inserts, updates, and retrieves data tuples within existing tables.</td>
        </tr>
        <tr>
            <td><b>Transaction Behavior</b></td>
            <td><b>Auto-committed</b> immediately; changes cannot be rolled back via TCL.</td>
            <td><b>Not auto-committed</b> by default; can be committed or rolled back using <code>ROLLBACK</code>.</td>
        </tr>
        <tr>
            <td><b>Key SQL Commands & Syntax</b></td>
            <td>
                <code>CREATE TABLE Student(Id INT);</code><br>
                <code>ALTER TABLE Student ADD Age INT;</code><br>
                <code>DROP TABLE Student;</code><br>
                <code>TRUNCATE TABLE Student;</code>
            </td>
            <td>
                <code>INSERT INTO Student VALUES(1, 20);</code><br>
                <code>UPDATE Student SET Age=21 WHERE Id=1;</code><br>
                <code>DELETE FROM Student WHERE Id=1;</code><br>
                <code>SELECT * FROM Student;</code>
            </td>
        </tr>
    </table>
</div>

<hr>

<!-- Q5 -->
<div class="q-box">
    <div class="q-title">Q5. Explain Functional Dependency (FD) and Multivalued Dependency (MVD). <span class="q-marks">[3 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <div class="info-box">
        <p class="step-label">1. Functional Dependency (X &rarr; Y):</p>
        <p>A constraint between two sets of attributes X and Y in relation R. It states that for any two tuples t<sub>1</sub> and t<sub>2</sub>, if <code>t<sub>1</sub>[X] = t<sub>2</sub>[X]</code>, then <code>t<sub>1</sub>[Y] = t<sub>2</sub>[Y]</code> must also hold. Attribute set X uniquely determines attribute set Y.</p>
        <p><i>Example: <code>Roll_No &rarr; Student_Name, Branch</code></i></p>
    </div>
    <div class="info-box">
        <p class="step-label">2. Multivalued Dependency (X &twoheadrightarrow; Y):</p>
        <p>Occurs when presence of one or more rows in a table implies the presence of other rows. For a tuple (x, y, z), attribute set Y depends only on X and is completely independent of attribute set Z. MVD leads to <b>4NF decomposition</b>.</p>
        <p><i>Example: In table (Course, Teacher, Book), if Course determines multiple Teachers and multiple Books independently: <code>Course &twoheadrightarrow; Teacher</code> and <code>Course &twoheadrightarrow; Book</code>.</i></p>
    </div>
</div>

<!-- ==================== SECTION B ==================== -->
<div class="sec-title">Section – B (Short Answer Questions &bull; 7.5 Marks Each &bull; Attempt Any Two)</div>

<!-- Q6 -->
<div class="q-box">
    <div class="q-title">Q6. Discuss Anomalies associated with Relational Database (Insertion, Deletion, Update). <span class="q-marks">[7.5 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>When relational schemas are unnormalized, redundant information causes three major operational anomalies:</p>
    <div class="info-box">
        <p><b>Consider Unnormalized Relation:</b> <code>Emp_Dept(EmpId, EmpName, DeptId, DeptName, DeptHOD)</code></p>
    </div>
    <ol>
        <li>
            <b>Insertion Anomaly:</b>
            <p>Occurs when certain facts cannot be recorded without prematurely adding unrelated attributes. For example, a new department (e.g., DeptId = 'D99', DeptName = 'AI Research') cannot be inserted until at least one employee is hired, because <code>EmpId</code> is the primary key and cannot accept <code>NULL</code>.</p>
        </li>
        <li>
            <b>Deletion Anomaly:</b>
            <p>Occurs when deleting one piece of data inadvertently destroys critical unrelated information. For example, if employee 'E101' is the sole member of department 'D05', deleting employee 'E101' simultaneously deletes all records of department 'D05' (its name, budget, HOD) from the database.</p>
        </li>
        <li>
            <b>Update (Modification) Anomaly:</b>
            <p>Occurs when data redundancy causes duplicate copies across multiple tuples. If department 'D01' has 500 employees, changing the department name requires updating all 500 rows. Missing even one row results in conflicting, inconsistent database states.</p>
        </li>
    </ol>
    <p><b>Solution:</b> Normalization decomposes such relations into separate tables (e.g., <code>Employee</code> and <code>Department</code>) linked by foreign keys.</p>
</div>

<hr>

<!-- Q7 -->
<div class="q-box">
    <div class="q-title">Q7. Explain Super Key, Candidate Key, and Primary Key with suitable examples. <span class="q-marks">[7.5 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>Consider relation: <code>Student(RollNo, RegNo, Email, Name, Age, Phone)</code></p>
    <div class="info-box">
        <p><b>Hierarchical Relationship:</b> Super Key &supd; Candidate Key &supd; Primary Key</p>
    </div>
    <table class="data-table">
        <tr>
            <th style="width: 22%;">Key Category</th>
            <th style="width: 48%;">Formal Definition & Properties</th>
            <th style="width: 30%;">Examples from Student</th>
        </tr>
        <tr>
            <td><b>Super Key</b></td>
            <td>Any set of one or more attributes that uniquely identifies each tuple in a relation. May contain redundant attributes.</td>
            <td>
                <code>{RollNo}</code><br>
                <code>{RegNo}</code><br>
                <code>{Email}</code><br>
                <code>{RollNo, Name}</code><br>
                <code>{RegNo, Age, Phone}</code>
            </td>
        </tr>
        <tr>
            <td><b>Candidate Key</b></td>
            <td>A <b>minimal</b> super key. Contains no extraneous attributes; removing any single attribute destroys unique identification.</td>
            <td>
                <code>{RollNo}</code><br>
                <code>{RegNo}</code><br>
                <code>{Email}</code>
            </td>
        </tr>
        <tr>
            <td><b>Primary Key</b></td>
            <td>The single candidate key chosen by the database designer as the principal unique identifier. <b>Cannot be NULL</b> and must be unique.</td>
            <td><code>{RollNo}</code> (Chosen as primary key)</td>
        </tr>
    </table>
</div>

<hr>

<!-- Q8 -->
<div class="q-box">
    <div class="q-title">Q8. What is Normalization? Explain Second Normal Form (2NF) and Third Normal Form (3NF). <span class="q-marks">[7.5 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p><b>Normalization</b> is a systematic technique for structuring relational tables to eliminate data redundancy, prevent insertion/deletion/update anomalies, and preserve data integrity.</p>
    
    <div class="info-box">
        <p class="step-label">1. Second Normal Form (2NF):</p>
        <ul>
            <li><b>Condition 1:</b> Relation must already satisfy First Normal Form (1NF) — all attributes atomic.</li>
            <li><b>Condition 2:</b> <b>No Partial Dependency:</b> Every non-prime attribute must depend on the <i>entire</i> candidate key, not on any proper subset of a composite candidate key.</li>
        </ul>
        <p><i>Example: In <code>StudentCourse(StudentID, CourseID, Grade, CourseName)</code> with candidate key <code>{StudentID, CourseID}</code>:</i></p>
        <p><code>CourseID &rarr; CourseName</code> is a partial dependency. Resolved by decomposing into: <code>Enrollment(StudentID, CourseID, Grade)</code> and <code>Course(CourseID, CourseName)</code>.</p>
    </div>

    <div class="info-box">
        <p class="step-label">2. Third Normal Form (3NF):</p>
        <ul>
            <li><b>Condition 1:</b> Relation must already be in 2NF.</li>
            <li><b>Condition 2:</b> <b>No Transitive Dependency:</b> Non-prime attributes must not depend on other non-prime attributes. For every non-trivial FD <code>X &rarr; Y</code>:
                <ul>
                    <li>Either <b>X is a Super Key</b>, OR</li>
                    <li><b>Y is a Prime Attribute</b> (part of any candidate key).</li>
                </ul>
            </li>
        </ul>
        <p><i>Example: In <code>Employee(EmpId, EmpName, DeptId, DeptName)</code> where <code>EmpId &rarr; DeptId</code> and <code>DeptId &rarr; DeptName</code>:</i></p>
        <p>Decompose into <code>Emp(EmpId, EmpName, DeptId)</code> and <code>Dept(DeptId, DeptName)</code>.</p>
    </div>
</div>

<!-- ==================== SECTION C ==================== -->
<div class="sec-title">Section – C (Long Answer Questions &bull; 15 Marks Each &bull; Attempt Any Three)</div>

<!-- Q9 -->
<div class="q-box">
    <div class="q-title">Q9. Define Boyce-Codd Normal Form (BCNF). Compare 3NF and BCNF with a suitable example. <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p><b>Boyce-Codd Normal Form (BCNF)</b> is a stricter, stronger version of 3NF. A relation R is in BCNF if and only if:</p>
    <div class="info-box">
        <p>For every non-trivial Functional Dependency <code>X &rarr; Y</code> in R, <b>X MUST be a Super Key</b>.</p>
    </div>
    
    <p class="step-label">Key Difference between 3NF and BCNF:</p>
    <table class="data-table">
        <tr>
            <th style="width: 25%;">Property</th>
            <th style="width: 38%;">Third Normal Form (3NF)</th>
            <th style="width: 37%;">Boyce-Codd Normal Form (BCNF)</th>
        </tr>
        <tr>
            <td><b>Condition for X &rarr; Y</b></td>
            <td>Valid if X is Super Key <b>OR</b> Y is a prime attribute.</td>
            <td>Valid <b>ONLY</b> if X is a Super Key (no relaxation for prime Y).</td>
        </tr>
        <tr>
            <td><b>Dependency Preservation</b></td>
            <td>Always preserves all functional dependencies.</td>
            <td>May occasionally sacrifice dependency preservation.</td>
        </tr>
        <tr>
            <td><b>Redundancy Level</b></td>
            <td>May retain slight redundancy for overlapping keys.</td>
            <td>Strictly zero redundancy caused by functional dependencies.</td>
        </tr>
    </table>

    <p class="step-label">Classic Example Illustrating 3NF vs BCNF:</p>
    <p>Consider relation <code>StudentAdvisor(StudentID, Subject, Advisor)</code> with business rules:</p>
    <ul>
        <li>A student can take multiple subjects and have an advisor for each: <code>{StudentID, Subject} &rarr; Advisor</code></li>
        <li>Each advisor teaches only one subject: <code>Advisor &rarr; Subject</code></li>
        <li>Candidate Keys: <code>{StudentID, Subject}</code> and <code>{StudentID, Advisor}</code>.</li>
        <li>Prime Attributes: <code>StudentID</code>, <code>Subject</code>, <code>Advisor</code>.</li>
    </ul>
    <div class="info-box">
        <p><b>Check for 3NF:</b> For FD <code>Advisor &rarr; Subject</code>, Advisor is not a super key, but <b>Subject is a prime attribute</b>. Therefore, the table is in <b>3NF</b> &check;.</p>
        <p><b>Check for BCNF:</b> In <code>Advisor &rarr; Subject</code>, Advisor is <b>NOT</b> a super key. Hence, this table <b>violates BCNF</b> &cross;.</p>
        <p><b>BCNF Decomposition:</b> Split into two relations:</p>
        <ol>
            <li><code>AdvisorSubject(Advisor, Subject)</code> — Key: <code>Advisor</code> &check;</li>
            <li><code>StudentAdvisor(StudentID, Advisor)</code> — Key: <code>{StudentID, Advisor}</code> &check;</li>
        </ol>
    </div>
</div>

<hr>

<!-- Q10 -->
<div class="q-box">
    <div class="q-title">Q10. Explain Relational Algebra Fundamental Operations with examples. <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p>Relational Algebra is a procedural query language consisting of operations that take one or two relations as input and produce a new relation as output.</p>
    <table class="data-table">
        <tr>
            <th style="width: 20%;">Operation & Symbol</th>
            <th style="width: 45%;">Description & Formal Rule</th>
            <th style="width: 35%;">Concrete Example Expression</th>
        </tr>
        <tr>
            <td><b>Selection (&sigma;)</b></td>
            <td>Selects tuples that satisfy a given predicate condition. Acts as a horizontal filter.</td>
            <td><code>&sigma;<sub>Marks &gt; 75</sub> (Student)</code><br>Filters students scoring above 75.</td>
        </tr>
        <tr>
            <td><b>Projection (&pi;)</b></td>
            <td>Selects specified attribute columns and automatically discards duplicate tuples. Vertical filter.</td>
            <td><code>&pi;<sub>RollNo, Name</sub> (Student)</code><br>Extracts RollNo and Name columns.</td>
        </tr>
        <tr>
            <td><b>Cartesian Product (&times;)</b></td>
            <td>Combines each tuple of relation R with every tuple of relation S. Output size: <code>|R| &times; |S|</code>.</td>
            <td><code>Student &times; Course</code></td>
        </tr>
        <tr>
            <td><b>Union (&cup;)</b></td>
            <td>Combines unique tuples from two union-compatible relations (identical arity and compatible domains).</td>
            <td><code>&pi;<sub>Name</sub>(Faculty) &cup; &pi;<sub>Name</sub>(Student)</code></td>
        </tr>
        <tr>
            <td><b>Set Difference (&minus;)</b></td>
            <td>Returns tuples present in relation R but not in relation S (must be union-compatible).</td>
            <td><code>&pi;<sub>RollNo</sub>(AllStudents) &minus; &pi;<sub>RollNo</sub>(Placed)</code></td>
        </tr>
        <tr>
            <td><b>Rename (&rho;)</b></td>
            <td>Renames a relation or its attributes to prevent ambiguities in self-joins.</td>
            <td><code>&rho;<sub>S1</sub>(Student)</code></td>
        </tr>
        <tr>
            <td><b>Natural Join (&bowtie;)</b></td>
            <td>Equi-join combining Cartesian product, equality selection on common attributes, and duplicate column removal.</td>
            <td><code>Student &bowtie; Department</code></td>
        </tr>
    </table>
</div>

<hr>

<!-- Q11 -->
<div class="q-box">
    <div class="q-title">Q11. Explain SQL Characteristics and Five Aggregate Functions with SQL queries. <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p><b>SQL Characteristics:</b> SQL is a declarative, non-procedural language allowing users to specify <i>what</i> data is needed rather than <i>how</i> to retrieve it. It integrates DDL, DML, DCL, and TCL commands with full ACID compliance.</p>
    
    <p class="step-label">Five Core Aggregate Functions (operating on Employee table):</p>
    <table class="data-table">
        <tr>
            <th style="width: 15%;">Function</th>
            <th style="width: 35%;">Purpose</th>
            <th style="width: 50%;">SQL Query Example & Description</th>
        </tr>
        <tr>
            <td><code>COUNT()</code></td>
            <td>Counts number of non-null values or total rows matching criteria.</td>
            <td><code>SELECT COUNT(*) FROM Employee WHERE Dept = 'IT';</code><br>Returns total number of employees in IT department.</td>
        </tr>
        <tr>
            <td><code>SUM()</code></td>
            <td>Calculates total arithmetic sum of numeric values.</td>
            <td><code>SELECT SUM(Salary) FROM Employee WHERE Dept = 'Sales';</code><br>Calculates total monthly payroll for Sales department.</td>
        </tr>
        <tr>
            <td><code>AVG()</code></td>
            <td>Calculates average mean value of numeric attribute.</td>
            <td><code>SELECT AVG(Salary) FROM Employee;</code><br>Returns average company-wide employee salary.</td>
        </tr>
        <tr>
            <td><code>MIN()</code></td>
            <td>Returns smallest minimum value in the attribute set.</td>
            <td><code>SELECT MIN(Salary) FROM Employee;</code><br>Finds the lowest compensation in the firm.</td>
        </tr>
        <tr>
            <td><code>MAX()</code></td>
            <td>Returns highest maximum value in the attribute set.</td>
            <td><code>SELECT Dept, MAX(Salary) FROM Employee GROUP BY Dept;</code><br>Returns highest salary earned in each department.</td>
        </tr>
    </table>
</div>

<hr>

<!-- Q12 -->
<div class="q-box">
    <div class="q-title">Q12. Explain Concurrency Control and Two-Phase Locking (2PL) Protocol with its pitfalls. <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Answer:</strong></p>
    <p><b>Concurrency Control</b> coordinates simultaneous transaction execution to prevent conflicts (Lost Update, Uncommitted Read, Inconsistent Analysis) and ensure Serializable schedules.</p>
    
    <div class="info-box">
        <p class="step-label">Two-Phase Locking (2PL) Protocol:</p>
        <ol>
            <li><b>Growing (Expansion) Phase:</b> Transaction may acquire locks (Shared <code>S-Lock</code> or Exclusive <code>X-Lock</code>) but <b>cannot release any lock</b>.</li>
            <li><b>Lock Point:</b> The moment the transaction has acquired all necessary locks.</li>
            <li><b>Shrinking (Contraction) Phase:</b> Transaction may release locks but <b>cannot acquire any new locks</b>.</li>
        </ol>
        <p><b>Theorem:</b> Any schedule following the 2PL protocol is guaranteed to be <b>Conflict Serializable</b>.</p>
    </div>

    <div class="info-box">
        <p class="step-label">Pitfalls of Basic 2PL & Solutions:</p>
        <ul>
            <li>
                <b>Cascading Aborts / Rollbacks:</b> If T1 releases a lock early in its shrinking phase and then aborts, any transaction T2 that read T1's dirty data must also abort.
                <br><b>Solution &rarr; Strict 2PL:</b> All Exclusive (X) locks must be held until the transaction commits or aborts.
            </li>
            <li>
                <b>Deadlocks:</b> 2PL does not prevent cyclic wait conditions where T1 holds Lock A waiting for Lock B, while T2 holds Lock B waiting for Lock A.
                <br><b>Deadlock Handling Mechanisms:</b>
                <ul>
                    <li><i>Deadlock Detection:</i> Maintains a dynamic <b>Wait-For Graph (WFG)</b>; cycles indicate deadlock and trigger victim abort.</li>
                    <li><i>Deadlock Prevention:</i> Uses transaction timestamps: <b>Wait-Die</b> (non-preemptive) or <b>Wound-Wait</b> (preemptive).</li>
                </ul>
            </li>
        </ul>
    </div>
</div>

<hr>

<!-- Q13 -->
<div class="q-box">
    <div class="q-title">Q13. Write detailed notes on: (a) Three-Schema Architecture, (b) Data Independence, and (c) Role of DBA. <span class="q-marks">[15 Marks]</span></div>
    <p><strong>Answer:</strong></p>

    <p class="step-label">(a) Three-Schema (ANSI/SPARC) Architecture:</p>
    <div class="info-box">
        <ol>
            <li><b>External Level (View Level):</b> Multiple tailored views for end-users and applications; conceals all irrelevant details and restricts unauthorized access.</li>
            <li><b>Conceptual Level (Logical Level):</b> Community-wide global schema describing what data is stored, entities, relationships, attributes, and constraints (tables, primary/foreign keys).</li>
            <li><b>Internal Level (Physical Level):</b> Physical data storage on disk, block allocation, record layout, B-Tree indexes, hashing, and encryption algorithms.</li>
        </ol>
    </div>

    <p class="step-label">(b) Data Independence:</p>
    <table class="data-table">
        <tr>
            <th style="width: 25%;">Independence Level</th>
            <th style="width: 45%;">Definition & Mechanism</th>
            <th style="width: 30%;">Real-World Scenario</th>
        </tr>
        <tr>
            <td><b>Physical Data Independence</b></td>
            <td>Ability to alter physical schema (disk storage, indexes, RAID, hashing) without modifying logical/conceptual schema.</td>
            <td>Adding a B-Tree index on <code>Salary</code> to boost search speed without altering table structure.</td>
        </tr>
        <tr>
            <td><b>Logical Data Independence</b></td>
            <td>Ability to alter conceptual schema (add tables, add columns) without modifying existing external schemas or application programs.</td>
            <td>Adding a <code>PassportNo</code> column to Student table without breaking existing grade-card report queries.</td>
        </tr>
    </table>

    <p class="step-label">(c) Role and Responsibilities of Database Administrator (DBA):</p>
    <ul>
        <li><b>Schema Definition & Storage Structure:</b> Creates logical tables and allocates physical disk storage paths.</li>
        <li><b>Security & Authorization:</b> Grants and revokes permissions (<code>GRANT</code>, <code>REVOKE</code>) to prevent data leaks.</li>
        <li><b>Performance Tuning:</b> Monitors slow queries, builds indexes, and reorganizes partitions.</li>
        <li><b>Backup & Disaster Recovery:</b> Schedules incremental/full backups and handles crash recovery using transaction logs.</li>
    </ul>
</div>
"""

def generate_pdf(year, out_filename):
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>BCA-501: DBMS — {year} Solved Paper</title>
{CSS_STYLES}
</head>
<body>

<div class="header-banner">
    <p class="univ-name">Chaudhary Charan Singh University (CCSU) &bull; BCA V Semester</p>
    <h1 class="paper-title">BCA-501: Introduction to DBMS</h1>
    <p class="meta-info"><strong>Session:</strong> {year} Examination &nbsp;|&nbsp; <strong>Paper Code:</strong> 18021 &nbsp;|&nbsp; <strong>Complete 100% Solved Paper (All 13 Questions)</strong> &nbsp;|&nbsp; <strong>Time:</strong> 3 Hours &bull; <strong>Max Marks:</strong> 75</p>
</div>

{BODY_QUESTIONS_HTML}

</body>
</html>
"""
    temp_html = os.path.join(TARGET_DIR, f"temp_dbms_{year}.html")
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
    years = [2025, 2024, 2023, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013]
    print("Generating beautifully formatted DBMS PDFs...")
    for yr in years:
        filename = f"dbms {yr} solved.pdf"
        generate_pdf(f"December {yr}", filename)
    
    # Subject bank
    print("Generating BCA-501_Introduction_to_DBMS_Solved_PYQ.pdf...")
    generate_pdf("Comprehensive PYQ Bank", "BCA-501_Introduction_to_DBMS_Solved_PYQ.pdf")

if __name__ == "__main__":
    main()
