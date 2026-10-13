import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from dbms_builder_base import generate_dbms_pdf

# ==============================================================================
# YEAR 2024 (December 2024)
# ==============================================================================
YEAR_2024_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>What is Schema in DBMS?</div>
    <div class="ans-body">
        <strong>Definition:</strong> A <strong>Database Schema</strong> is the formal structural blueprint and design description of the entire database. It specifies:
        <ul>
            <li>Table names, columns, data types, and domains.</li>
            <li>Integrity constraints (primary keys, foreign keys, check constraints).</li>
            <li>Relationships between entities and storage representations.</li>
        </ul>
        It is stored in the system catalog and does not change frequently.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>What are the advantages of using DBMS?</div>
    <div class="ans-body">
        <strong>Key Advantages:</strong>
        <ol>
            <li><strong>Minimal Redundancy:</strong> Normalization ensures data is stored in one primary location.</li>
            <li><strong>Data Integrity:</strong> Automatic enforcement of domain and referential integrity constraints.</li>
            <li><strong>Concurrency Control:</strong> Multi-user simultaneous access without collisions via locking protocols.</li>
            <li><strong>Crash Recovery:</strong> WAL (Write-Ahead Logging) and checkpoints guarantee durability after hardware failure.</li>
            <li><strong>Data Independence:</strong> Separates user views from low-level storage modifications.</li>
        </ol>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Who is a DBA? Mention their key functions.</div>
    <div class="ans-body">
        <strong>Definition:</strong> A <strong>Database Administrator (DBA)</strong> is an IT professional who manages the database environment, maintains performance, controls user permissions, schedules backups, and enforces security policies.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What is a Database?</div>
    <div class="ans-body">
        <strong>Definition:</strong> A <strong>Database</strong> is an integrated and logically related collection of records, designed to meet the information processing needs of multiple users across an organization.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What is RDBMS?</div>
    <div class="ans-body">
        <strong>Definition:</strong> A <strong>Relational Database Management System (RDBMS)</strong> is a DBMS based on E.F. Codd's Relational Model (1970). Data is organized into 2D tables (relations) consisting of rows (tuples) and columns (attributes), manipulated using SQL and relational algebra. Examples: Oracle, MySQL, PostgreSQL, SQL Server.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Find the minimum number of tables required for the given ER diagram in the relational model. Explain table conversion rules.</div>
    <div class="ans-body">
        <strong>Rules for ER to Relational Reduction:</strong>
        <ol>
            <li><strong>Strong Entity Sets:</strong> Each strong entity converts into a separate independent table.</li>
            <li><strong>Weak Entity Sets:</strong> Converts into a table containing its discriminator (partial key) combined with the primary key of the identifying strong entity as composite primary key.</li>
            <li><strong>1:1 Relationships:</strong> Combine both entities into 1 table, or place the primary key of one table as a foreign key in the other table.</li>
            <li><strong>1:N Relationships:</strong> Place the primary key of the '1' side entity into the table of the 'N' side entity as a foreign key (no new table needed).</li>
            <li><strong>M:N Relationships:</strong> Requires a new separate relationship table containing primary keys of both participating entities as foreign keys.</li>
        </ol>
        <strong>Result:</strong> For an ER model with two strong entities A and B in 1:N relationship, exactly <strong>2 tables</strong> are needed. If the relationship is M:N, exactly <strong>3 tables</strong> are required.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>What are UNION, MINUS, and INTERSECT commands in DBMS? Explain with syntax and examples.</div>
    <div class="ans-body">
        <strong>Conditions:</strong> Both queries must be <em>Union-Compatible</em> (same number of columns with compatible data types).<br>
        <ul>
            <li><code>UNION</code>: Combines results of two SELECT queries and eliminates duplicate tuples.</li>
            <li><code>INTERSECT</code>: Returns only the common tuples present in both result sets.</li>
            <li><code>MINUS / EXCEPT</code>: Returns tuples from the first query that are not present in the second query.</li>
        </ul>
        <strong>SQL Examples:</strong>
<pre>
-- UNION: All students from CS or IT
SELECT RollNo, Name FROM Student_CS
UNION
SELECT RollNo, Name FROM Student_IT;

-- INTERSECT: Students enrolled in both Math and Physics clubs
SELECT StudentID FROM MathClub
INTERSECT
SELECT StudentID FROM PhysicsClub;

-- MINUS: Registered students who have NOT paid exam fees
SELECT StudentID FROM RegisteredStudents
EXCEPT
SELECT StudentID FROM PaidStudents;
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Define the following terms: (a) Data Model, (b) Database Schema.</div>
    <div class="ans-body">
        <strong>(a) Data Model:</strong> A conceptual collection of tools, constructs, and notations used to describe data, data relationships, data semantics, and consistency constraints. Major models include:
        <ul>
            <li><strong>Relational Model:</strong> Tables of tuples and attributes (SQL).</li>
            <li><strong>Entity-Relationship (ER) Model:</strong> High-level conceptual modeling.</li>
            <li><strong>Object-Oriented & Document (NoSQL) Models:</strong> JSON, key-value, graph.</li>
        </ul>
        <strong>(b) Database Schema:</strong> The overall structural skeleton of the database defined during the design phase, distinct from the dynamic instances/states stored inside it.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Define Normal Forms. Explain 1NF, 2NF, 3NF, and BCNF with suitable examples.</div>
    <div class="ans-body">
        <strong>Detailed Normal Forms Analysis:</strong>
        <table class="grid-table">
            <thead><tr><th>Normal Form</th><th>Requirement / Condition</th><th>Anomaly Eliminated</th></tr></thead>
            <tbody>
                <tr><td>1NF</td><td>All attribute values must be atomic (no multivalued / nested attributes).</td><td>Repeating groups and unstructured data arrays</td></tr>
                <tr><td>2NF</td><td>In 1NF and no non-prime attribute is partially dependent on any candidate key.</td><td>Partial Functional Dependencies</td></tr>
                <tr><td>3NF</td><td>In 2NF and for every X &rarr; Y, either X is a Super Key or Y is a Prime Attribute.</td><td>Transitive Functional Dependencies</td></tr>
                <tr><td>BCNF</td><td>For every non-trivial functional dependency X &rarr; Y, X must strictly be a Super Key.</td><td>All functional dependency based redundancies</td></tr>
            </tbody>
        </table>
        <strong>BCNF Example:</strong><br>
        Suppose <code>STUDENT_ADVISOR(StudentID, Subject, Advisor)</code> where each student has an advisor per subject, and each advisor teaches only one subject:
        <span class="math">FD_1: (StudentID, Subject) \to Advisor</span>, <span class="math">FD_2: Advisor \to Subject</span>.<br>
        Candidate Key is <span class="math">(StudentID, Subject)</span> or <span class="math">(StudentID, Advisor)</span>.<br>
        In <span class="math">FD_2</span>, <code>Advisor</code> is not a super key, violating BCNF.<br>
        Decompose into: <code>Advisor_Subject(<u>Advisor</u>, Subject)</code> and <code>Student_Advisor(<u>StudentID</u>, <u>Advisor</u>)</code>. Both are now in BCNF!
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain Normalization with its advantages. What anomalies arise in unnormalized databases?</div>
    <div class="ans-body">
        <strong>Anomalies in Unnormalized Tables:</strong>
        <ol>
            <li><strong>Insertion Anomaly:</strong> Cannot record information about an entity without having to insert another unrelated entity (e.g., cannot register a new department until at least one employee is hired).</li>
            <li><strong>Deletion Anomaly:</strong> Deleting a record of one entity unintentionally erases information about another entity (e.g., deleting the last employee in a department deletes all department details).</li>
            <li><strong>Update / Modification Anomaly:</strong> Changing an entity's attribute requires updating hundreds of duplicate rows; if one row is missed, data becomes contradictory.</li>
        </ol>
        <strong>Advantages of Normalization:</strong>
        <ul>
            <li>Eliminates data redundancy and conserves disk storage.</li>
            <li>Maintains referential integrity automatically across tables.</li>
            <li>Speeds up row updates, inserts, and index lookups.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain SQL with its various characteristics and features.</div>
    <div class="ans-body">
        <strong>Structured Query Language (SQL):</strong> The ANSI/ISO standard declarative language for relational databases.<br>
        <strong>Key Characteristics:</strong>
        <ul>
            <li><strong>Declarative / Non-Procedural:</strong> Users specify <em>what data</em> they want, leaving the query optimizer to determine <em>how</em> to retrieve it.</li>
            <li><strong>Comprehensive Capabilities:</strong> Encompasses DDL (structure), DML (manipulation), DCL (security/privileges), and TCL (transactions).</li>
            <li><strong>Portability & Standards:</strong> Works uniformly across major vendors (Oracle, MySQL, SQL Server, PostgreSQL).</li>
            <li><strong>Integrity Constraints Support:</strong> Native enforcement of <code>PRIMARY KEY</code>, <code>FOREIGN KEY</code>, <code>CHECK</code>, <code>UNIQUE</code>, and <code>DEFAULT</code>.</li>
            <li><strong>View & Subquery Support:</strong> Enables nested queries, common table expressions (CTEs), and dynamic virtual tables (Views).</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>What is Relational Algebra? Discuss its basic and extended operations with expressions.</div>
    <div class="ans-body">
        <strong>Overview:</strong> Relational algebra provides the formal theoretical mathematical foundation for query evaluation and execution plan optimization in RDBMS.<br>
        <strong>Operations Summary:</strong>
        <ul>
            <li><strong>Selection (&sigma;):</strong> Horizontal subset of rows based on conditions.</li>
            <li><strong>Projection (&pi;):</strong> Vertical subset of columns, duplicate-free.</li>
            <li><strong>Cartesian Product (&times;):</strong> All pairs of concatenated rows.</li>
            <li><strong>Set Union (&cup;), Intersection (&cap;), Difference (&minus;):</strong> Set-theoretic operations on union-compatible relations.</li>
            <li><strong>Theta Join (&bowtie;<sub>&theta;</sub>):</strong> Cross product followed by condition filtering.</li>
            <li><strong>Division (&divide;):</strong> Used for queries involving "for all" / universal quantification.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain the reduction of ER Schema to Relational Tables with a complete case study.</div>
    <div class="ans-body">
        <strong>Case Study: Company Database:</strong><br>
        Entities: <code>EMPLOYEE</code>, <code>DEPARTMENT</code>, <code>PROJECT</code>.<br>
        Relationships:
        <ul>
            <li><code>WORKS_FOR</code> (N:1 from Employee to Department)</li>
            <li><code>MANAGES</code> (1:1 from Employee to Department with <code>StartDate</code>)</li>
            <li><code>WORKS_ON</code> (M:N between Employee and Project with <code>Hours</code>)</li>
        </ul>
        <strong>Relational Reduction:</strong>
<pre>
1. DEPARTMENT(<u>DeptNo</u>, DeptName, MgrEmpID, MgrStartDate)
   -- 1:1 MANAGES folded into DEPARTMENT with MgrEmpID as FK
2. EMPLOYEE(<u>EmpID</u>, EmpName, Salary, DeptNo)
   -- N:1 WORKS_FOR represented via DeptNo as FK referencing DEPARTMENT
3. PROJECT(<u>ProjNo</u>, ProjName, DeptNo)
   -- N:1 CONTROLS represented via DeptNo as FK
4. WORKS_ON(<u>EmpID</u>, <u>ProjNo</u>, Hours)
   -- M:N relationship becomes a separate junction table with composite PK
   -- FK EmpID -> EMPLOYEE, FK ProjNo -> PROJECT
</pre>
    </div>
</div>
"""

print("Generating DBMS 2024 PDF...")
generate_dbms_pdf("December 2024", "dbms 2024 solved.pdf", YEAR_2024_HTML)
