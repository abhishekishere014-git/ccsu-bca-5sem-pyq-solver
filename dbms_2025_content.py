import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from dbms_builder_base import generate_dbms_pdf

# ==============================================================================
# YEAR 2025 (December 2025)
# ==============================================================================
YEAR_2025_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>What is a Database?</div>
    <div class="ans-body">
        <strong>Definition:</strong> A <strong>Database</strong> is an organized, logically coherent collection of related data modeled to represent real-world entities and enterprise operations. Key properties include:
        <ul>
            <li><strong>Self-describing nature:</strong> Stores both data and metadata (system catalog/data dictionary).</li>
            <li><strong>Program-data independence:</strong> Structure of data files is stored separately from user access programs.</li>
            <li><strong>Multi-user transaction processing:</strong> Guarantees concurrent access without collision or corruption.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>State the key advantages of DBMS over File Processing Systems.</div>
    <div class="ans-body">
        <strong>Advantages:</strong>
        <table class="grid-table">
            <thead><tr><th>Aspect</th><th>Traditional File System</th><th>Database Management System (DBMS)</th></tr></thead>
            <tbody>
                <tr><td>Data Redundancy</td><td>High redundancy across duplicate files</td><td>Controlled and minimized via normalization</td></tr>
                <tr><td>Data Inconsistency</td><td>High risk due to isolated updates</td><td>Eliminated via centralized repository</td></tr>
                <tr><td>Data Independence</td><td>None; changes in files break code</td><td>Physical and Logical Data Independence achieved</td></tr>
                <tr><td>Concurrent Access</td><td>Prone to race conditions and lost updates</td><td>ACID compliant concurrency control (2PL, timestamp)</td></tr>
                <tr><td>Security & Integrity</td><td>OS-level passwords, hard to enforce</td><td>Fine-grained role-based access & constraints</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Who is a Database Administrator (DBA)? Mention key duties.</div>
    <div class="ans-body">
        <strong>Definition:</strong> A <strong>Database Administrator (DBA)</strong> is the central authority responsible for supervising and administering the entire database environment.<br>
        <strong>Primary Functions:</strong>
        <ol>
            <li><strong>Schema Definition:</strong> Designing and altering conceptual, external, and internal schemas.</li>
            <li><strong>Storage & Access Tuning:</strong> Specifying storage structures, file organizations, and primary/secondary indexes.</li>
            <li><strong>Security & Authorization:</strong> Granting and revoking user privileges, managing roles, and enforcing access control.</li>
            <li><strong>Backup & Recovery:</strong> Scheduling periodic backups and executing disaster recovery strategies.</li>
            <li><strong>Integrity Enforcement:</strong> Defining domain, entity, and referential integrity constraints.</li>
        </ol>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Differentiate between Schema and Instance in DBMS.</div>
    <div class="ans-body">
        <strong>Comparison:</strong>
        <ul>
            <li><strong>Database Schema:</strong> The overall logical blueprint, structure, and design of the database (e.g., table names, column data types, constraints). It is specified during system design and changes very infrequently.</li>
            <li><strong>Database Instance (State):</strong> The actual data content populated within the database at a specific moment in time. It changes dynamically whenever records are inserted, updated, or deleted.</li>
        </ul>
        <em>Analogy:</em> In programming languages, a Schema corresponds to a Class/Data Type, whereas an Instance corresponds to an Object/Value of that type.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What do you mean by Data Inconsistency in File Management Systems? Explain.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> <strong>Data Inconsistency</strong> occurs when multiple copies of the exact same data across different files contain conflicting, contradictory values.<br>
        <strong>Example:</strong> In a university file system, a student's address is recorded in the <em>Library File</em> and also in the <em>Fee Accounting File</em>. If the student changes their residential address and only the Library office updates their local file while the Fee office does not, the university now holds two contradictory addresses for the same student. This occurs due to uncoordinated duplicate storage without centralized integrity control.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain ER Diagram. Describe all standard ER notations and symbols with diagrams.</div>
    <div class="ans-body">
        <strong>Definition:</strong> An <strong>Entity-Relationship (ER) Diagram</strong> is a graphical semantic modeling tool that represents the logical structure of a database in terms of entities, their attributes, and relationships.<br>
        <strong>Standard Symbols & Notations:</strong>
        <div class="diagram-box">
[ Rectangle ]           -> Entity Set (e.g., STUDENT, COURSE)
[[ Double Rectangle ]]  -> Weak Entity Set (e.g., DEPENDENT, INSTALLMENT)
( Ellipse / Oval )      -> Attribute (e.g., Age, Name)
( Underlined Text )     -> Primary Key Attribute (e.g., <u>RollNo</u>)
(( Double Ellipse ))    -> Multivalued Attribute (e.g., PhoneNumbers, Skills)
( Dashed Ellipse )      -> Derived Attribute (e.g., Age calculated from DOB)
{ Diamond }             -> Relationship Set (e.g., ENROLLED_IN)
{{ Double Diamond }}    -> Identifying Relationship for Weak Entity Set
======== Double Line    -> Total Participation (Every entity must participate)
-------- Single Line    -> Partial Participation
        </div>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Primary Key, Foreign Key, and Candidate Key with suitable SQL examples.</div>
    <div class="ans-body">
        <strong>1. Candidate Key:</strong> A minimal super key &mdash; an attribute or minimal set of attributes that uniquely identifies each tuple in a relation without any redundant attributes.<br>
        <strong>2. Primary Key:</strong> The specific candidate key chosen by the database designer to uniquely identify tuples in a table. It cannot accept duplicate values and cannot contain <code>NULL</code>.<br>
        <strong>3. Foreign Key:</strong> An attribute in a child table whose values must match the primary key of a referenced parent table (or be <code>NULL</code>), enforcing referential integrity.<br>
        <strong>SQL Implementation Example:</strong>
<pre>
-- Parent Table: DEPARTMENT
CREATE TABLE Department (
    DeptID INT PRIMARY KEY,              -- Primary Key
    DeptName VARCHAR(50) NOT NULL UNIQUE -- Candidate Key
);

-- Child Table: EMPLOYEE
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,               -- Primary Key
    EmpName VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE,           -- Candidate Key
    DeptID INT,                          -- Foreign Key
    CONSTRAINT fk_dept FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
        ON DELETE CASCADE ON UPDATE CASCADE
);
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Differentiate between DDL and DML commands with syntax and examples.</div>
    <div class="ans-body">
        <strong>Comparison:</strong>
        <table class="grid-table">
            <thead><tr><th>Feature</th><th>Data Definition Language (DDL)</th><th>Data Manipulation Language (DML)</th></tr></thead>
            <tbody>
                <tr><td>Purpose</td><td>Defines and modifies the schema structure of the database.</td><td>Manages, accesses, and manipulates the data within the tables.</td></tr>
                <tr><td>Commit Nature</td><td>Auto-committed permanently (cannot be rolled back in most RDBMS).</td><td>Transactional (can be committed or rolled back using TCL).</td></tr>
                <tr><td>Commands</td><td><code>CREATE</code>, <code>ALTER</code>, <code>DROP</code>, <code>TRUNCATE</code>, <code>RENAME</code></td><td><code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>, <code>SELECT</code></td></tr>
            </tbody>
        </table>
        <strong>SQL Examples:</strong>
<pre>
-- DDL Commands:
CREATE TABLE Student (RollNo INT PRIMARY KEY, Name VARCHAR(50));
ALTER TABLE Student ADD COLUMN City VARCHAR(30);

-- DML Commands:
INSERT INTO Student (RollNo, Name, City) VALUES (101, 'Aman', 'Meerut');
UPDATE Student SET City = 'Delhi' WHERE RollNo = 101;
</pre>
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Explain the ACID properties of a transaction with practical examples. Why are they essential?</div>
    <div class="ans-body">
        <strong>Definition:</strong> A <strong>Transaction</strong> is a logical unit of database processing that includes one or more database access operations. To preserve database consistency and reliability, every DBMS must guarantee the four <strong>ACID Properties</strong>:<br><br>
        <strong>1. Atomicity ("All or Nothing"):</strong>
        <ul>
            <li>Either all operations of the transaction are committed successfully, or none take effect. If failure occurs mid-transaction, all changes are rolled back.</li>
            <li><em>Example:</em> Bank transfer of \$500 from Account A to Account B. If \$500 is debited from A and power fails before crediting B, the recovery subsystem rolls back A's debit.</li>
        </ul>
        <strong>2. Consistency (Preservation of Invariants):</strong>
        <ul>
            <li>Execution of a transaction in isolation preserves database integrity constraints (e.g., total balance of A + B must remain unchanged before and after the transfer).</li>
        </ul>
        <strong>3. Isolation (Independence of Concurrent Executions):</strong>
        <ul>
            <li>Even if multiple transactions execute concurrently, the intermediate uncommitted state of one transaction is hidden from others, producing a serializable execution schedule. Enforced via locking (2PL) and timestamp ordering.</li>
        </ul>
        <strong>4. Durability (Survivability of Committed Data):</strong>
        <ul>
            <li>Once a transaction commits, its updates persist permanently in secondary storage and will survive subsequent power failures, crashes, or OS reboots via Write-Ahead Logging (WAL) and checkpointing.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>What is Normalization? Explain 1NF, 2NF, 3NF, and BCNF with suitable relational examples and anomaly reduction.</div>
    <div class="ans-body">
        <strong>Definition:</strong> <strong>Normalization</strong> is a formal process of decomposing relations with anomalies into structured relations to eliminate insertion, deletion, and update anomalies while avoiding redundant data storage.<br><br>
        <strong>1. First Normal Form (1NF):</strong>
        <ul>
            <li>A relation is in 1NF if and only if all attribute values are atomic (no multivalued, composite, or nested attributes).</li>
            <li><em>Violation:</em> <code>Employee(EmpID, Skills)</code> where <code>Skills = "Java, Python, C++"</code>.</li>
            <li><em>Decomposition:</em> Split into atomic rows: <code>(101, 'Java')</code>, <code>(101, 'Python')</code>, <code>(101, 'C++')</code>.</li>
        </ul>
        <strong>2. Second Normal Form (2NF):</strong>
        <ul>
            <li>Relation must be in 1NF and have <strong>no partial dependency</strong> (no non-prime attribute should depend on a proper subset of any candidate key).</li>
            <li><em>Example:</em> <code>Enrollment(<u>StudentID</u>, <u>CourseID</u>, CourseFee, Grade)</code>. Here <code>CourseFee</code> depends only on <code>CourseID</code> (partial).</li>
            <li><em>Decomposition:</em> <code>StudentCourses(<u>StudentID</u>, <u>CourseID</u>, Grade)</code> and <code>CourseDetails(<u>CourseID</u>, CourseFee)</code>.</li>
        </ul>
        <strong>3. Third Normal Form (3NF):</strong>
        <ul>
            <li>Relation must be in 2NF and have <strong>no transitive dependency</strong> (for every non-trivial FD <span class="math">X \to Y</span>, either <span class="math">X</span> is a super key or <span class="math">Y</span> is a prime attribute).</li>
            <li><em>Example:</em> <code>Employee(<u>EmpID</u>, EmpName, DeptNo, DeptHead)</code>. Here <code>EmpID &rarr; DeptNo</code> and <code>DeptNo &rarr; DeptHead</code>, creating transitive dependency.</li>
            <li><em>Decomposition:</em> <code>Emp(<u>EmpID</u>, EmpName, DeptNo)</code> and <code>Dept(<u>DeptNo</u>, DeptHead)</code>.</li>
        </ul>
        <strong>4. Boyce-Codd Normal Form (BCNF):</strong>
        <ul>
            <li>A stricter version of 3NF where for every non-trivial FD <span class="math">X \to Y</span>, determinant <span class="math">X</span> <strong>must strictly be a Super Key</strong>.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain SQL Aggregate Functions (COUNT, SUM, AVG, MIN, MAX) with GROUP BY and HAVING clauses. Provide full query demonstrations.</div>
    <div class="ans-body">
        <strong>Aggregate Functions:</strong> Functions that perform calculations on a set of column values and return a single scalar summary value.<br>
        <ul>
            <li><code>COUNT(column)</code>: Returns total count of non-null values. <code>COUNT(*)</code> counts all rows.</li>
            <li><code>SUM(column)</code>: Calculates total numeric sum of values.</li>
            <li><code>AVG(column)</code>: Calculates arithmetic mean of non-null values.</li>
            <li><code>MIN(column)</code> / <code>MAX(column)</code>: Returns the minimum / maximum value.</li>
        </ul>
        <strong>Role of GROUP BY and HAVING:</strong>
        <ul>
            <li><code>GROUP BY</code> divides records into distinct groups based on identical column values.</li>
            <li><code>HAVING</code> filters grouped rows after aggregation (whereas <code>WHERE</code> filters individual tuples prior to grouping).</li>
        </ul>
        <strong>Comprehensive SQL Example:</strong>
<pre>
-- Schema: Employee (EmpID, EmpName, Salary, DeptID, City)
-- Query: Find DeptID, total employees, average salary, and max salary 
-- for departments having more than 3 employees and average salary > 45000:

SELECT 
    DeptID,
    COUNT(EmpID) AS TotalEmployees,
    AVG(Salary) AS AverageSalary,
    MAX(Salary) AS HighestSalary,
    MIN(Salary) AS LowestSalary
FROM Employee
WHERE City IN ('Delhi', 'Noida', 'Gurugram')
GROUP BY DeptID
HAVING COUNT(EmpID) > 3 AND AVG(Salary) > 45000
ORDER BY AverageSalary DESC;
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>What is Relational Algebra? Discuss its fundamental operations (Select, Project, Union, Set Difference, Cartesian Product, Rename) and derived Join operation.</div>
    <div class="ans-body">
        <strong>Definition:</strong> <strong>Relational Algebra</strong> is a formal procedural query language that takes one or two relations as input and produces a new relation as output without modifying the underlying stored tables.<br><br>
        <strong>Fundamental Operators:</strong>
        <ol>
            <li><strong>Select (&sigma;):</strong> Unary operator that filters rows satisfying a predicate condition <span class="math">P</span>.
                <div class="diagram-box">&sigma;_{Salary > 50000 AND Dept = 'IT'} (Employee)</div>
            </li>
            <li><strong>Project (&pi;):</strong> Unary operator that selects specified columns and eliminates duplicate tuples.
                <div class="diagram-box">&pi;_{EmpName, Salary} (Employee)</div>
            </li>
            <li><strong>Union (&cup;):</strong> Binary operator combining tuples from two union-compatible relations.
                <div class="diagram-box">Student_CS &cup; Student_IT</div>
            </li>
            <li><strong>Set Difference (&minus;):</strong> Returns tuples present in relation R but not in S (union compatible).
                <div class="diagram-box">All_Students &minus; Placed_Students</div>
            </li>
            <li><strong>Cartesian Product (&times;):</strong> Cross product pairing every tuple of R with every tuple of S.
                <div class="diagram-box">Employee &times; Department</div>
            </li>
            <li><strong>Rename (&rho;):</strong> Renames relation or attributes: <span class="math">\rho_{S(A_1, A_2)} (R)</span>.</li>
        </ol>
        <strong>Derived Operation &mdash; Natural Join (&bowtie;):</strong>
        Combines tuples of two relations matching on identical common attribute names:
        <div class="diagram-box">Employee &bowtie; Department = &pi;_{...} (&sigma;_{Employee.DeptID = Department.DeptID} (Employee &times; Department))</div>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Draw an ER Diagram for a Hospital Management System specifying entities, attributes, primary keys, relationships, and cardinalities. Show conversion to Relational Schema.</div>
    <div class="ans-body">
        <strong>1. Entity Sets & Attributes:</strong>
        <ul>
            <li><strong>DOCTOR</strong>: <u>DocID</u>, Name, Specialty, Phone</li>
            <li><strong>PATIENT</strong>: <u>PatID</u>, Name, Age, Gender, Address</li>
            <li><strong>ROOM / BED</strong>: <u>RoomNo</u>, <u>BedNo</u>, RoomType, DailyCharge</li>
            <li><strong>BILL / ACCOUNT</strong>: <u>BillID</u>, BillDate, TotalAmount, PaymentStatus</li>
        </ul>
        <strong>2. Relationships & Cardinalities:</strong>
        <ul>
            <li><code>TREATS</code>: Many-to-Many between DOCTOR and PATIENT with attribute <code>DateOfTreatment</code>.</li>
            <li><code>ASSIGNED_TO</code>: Many-to-One between PATIENT and BED (A patient is assigned to one bed; a bed holds one patient at a time).</li>
            <li><code>GENERATES</code>: One-to-One between PATIENT and BILL.</li>
        </ul>
        <strong>3. ASCII ER Diagram Representation:</strong>
        <div class="diagram-box">
  +------------+             ( M )             +------------+
  |   DOCTOR   | <---------------------------> |  PATIENT   |
  | <u>DocID</u>      |          < TREATS >           | <u>PatID</u>      |
  | Name, Spec |        [Date, Notes]          | Name, Age  |
  +------------+                               +------------+
                                                    | (1)
                                             < ASSIGNED >
                                                    | (1)
                                                    v
                                               +------------+
                                               |  ROOM_BED  |
                                               | <u>RoomNo</u>     |
                                               | <u>BedNo</u>, Type|
                                               +------------+
        </div>
        <strong>4. Relational Schema Reduction:</strong>
<pre>
1. Doctor(<u>DocID</u>, Name, Specialty, Phone)
2. Patient(<u>PatID</u>, Name, Age, Gender, Address, RoomNo, BedNo)
   FOREIGN KEY (RoomNo, BedNo) REFERENCES Room_Bed(RoomNo, BedNo)
3. Room_Bed(<u>RoomNo</u>, <u>BedNo</u>, RoomType, DailyCharge)
4. Treats(<u>DocID</u>, <u>PatID</u>, <u>TreatmentDate</u>, Prescription)
   FOREIGN KEY (DocID) REFERENCES Doctor(DocID),
   FOREIGN KEY (PatID) REFERENCES Patient(PatID)
5. Bill(<u>BillID</u>, PatID, BillDate, TotalAmount, Status)
   FOREIGN KEY (PatID) REFERENCES Patient(PatID)
</pre>
    </div>
</div>
"""

print("Generating DBMS 2025 PDF...")
generate_dbms_pdf("December 2025", "dbms 2025 solved.pdf", YEAR_2025_HTML)
