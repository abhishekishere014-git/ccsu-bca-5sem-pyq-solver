import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from dbms_builder_base import generate_dbms_pdf

# ==============================================================================
# YEAR 2021 (December 2021 / CV-3 Pattern)
# ==============================================================================
YEAR_2021_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks / CV-3 Pattern)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (7.5M)</span>Explain the Three-Level Architecture of DBMS with a neat block diagram.</div>
    <div class="ans-body">
        <strong>Three-Level ANSI/SPARC Architecture:</strong>
        <div class="diagram-box">
+---------------------+   +---------------------+   +---------------------+
|  External View 1    |   |  External View 2    |   |  External View n    |
+---------------------+   +---------------------+   +---------------------+
           \                         |                         /
            ================== External / Conceptual Mapping =============
                                     v
                        +-------------------------+
                        |    Conceptual Schema    | (Logical community view)
                        +-------------------------+
                                     |
            ================== Conceptual / Internal Mapping =============
                                     v
                        +-------------------------+
                        |     Internal Schema     | (Physical disk storage, indexes)
                        +-------------------------+
                                     |
                                     v
                        +=========================+
                        |    Physical Database    | (Blocks, sectors on disk)
                        +=========================+
        </div>
        <strong>1. External Level (View Level):</strong> User-specific customized views presenting only relevant subsets of data while hiding confidential fields.<br>
        <strong>2. Conceptual Level (Logical Level):</strong> Describes <em>what data</em> is stored in the entire database and the relationships among data without physical storage details.<br>
        <strong>3. Internal Level (Physical Level):</strong> Describes <em>how data</em> is physically stored on storage media (record formats, B+ trees, hashing).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (7.5M)</span>Define Primary Key, NOT NULL Key, and UNIQUE Key with differences.</div>
    <div class="ans-body">
        <strong>Definitions & Differences:</strong>
        <table class="grid-table">
            <thead><tr><th>Feature</th><th>PRIMARY KEY</th><th>UNIQUE KEY</th><th>NOT NULL</th></tr></thead>
            <tbody>
                <tr><td>Purpose</td><td>Uniquely identifies each record.</td><td>Ensures distinct non-duplicate values.</td><td>Prevents missing or null values.</td></tr>
                <tr><td>NULL Allowed</td><td><strong>Never</strong> allowed (strictly 0 nulls).</td><td>Allowed (usually 1 or more nulls per column).</td><td>Does not enforce uniqueness, only disallows null.</td></tr>
                <tr><td>Count per table</td><td>Only <strong>1</strong> per table.</td><td>Multiple unique constraints allowed.</td><td>Can be applied to every column.</td></tr>
                <tr><td>Index created</td><td>Automatically creates Primary Clustered Index.</td><td>Creates Secondary Unique Non-Clustered Index.</td><td>No index created by default.</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (7.5M)</span>Explain Hashing in brief with its collision handling techniques.</div>
    <div class="ans-body">
        <strong>Definition:</strong> <strong>Hashing</strong> is an efficient direct search technique where a mathematical hash function <span class="math">h(k)</span> maps a search key <span class="math">k</span> directly to the disk address/bucket number where the record resides, providing average <span class="math">O(1)</span> time complexity.<br>
        <strong>Collision:</strong> Occurs when two distinct search keys hash to the same bucket address: <span class="math">h(k_1) = h(k_2)</span>.<br>
        <strong>Collision Handling Techniques:</strong>
        <ul>
            <li><strong>Open Addressing (Linear Probing):</strong> Searches the next contiguous sequential bucket until an empty slot is located.</li>
            <li><strong>Chaining / Separate Overflow Buckets:</strong> Maintains a linked list of overflow buckets chained to the primary bucket.</li>
            <li><strong>Extendible Hashing (Dynamic Hashing):</strong> Uses a directory of pointers with local and global depths to double directories and split buckets dynamically without rehashing all records.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (7.5M)</span>What are the pitfalls of Lock-Based Protocols in concurrency control?</div>
    <div class="ans-body">
        <strong>Pitfalls:</strong>
        <ol>
            <li><strong>Deadlock:</strong> Occurs when two or more transactions are waiting indefinitely for locks held by each other (e.g., <span class="math">T_1</span> holds Lock on A and waits for B, while <span class="math">T_2</span> holds Lock on B and waits for A). Requires deadlock detection (Wait-For Graph) and victim rollback.</li>
            <li><strong>Starvation:</strong> A transaction waits indefinitely because other higher-priority transactions repeatedly acquire locks on the required data item.</li>
            <li><strong>Cascading Rollback:</strong> In non-strict 2PL, if a transaction aborts, all dependent uncommitted transactions that read its dirty data must also be rolled back in a cascade.</li>
            <li><strong>Concurrency Bottleneck:</strong> Excessive long-duration exclusive locks reduce system throughput and degrade response times.</li>
        </ol>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (7.5M)</span>Why is Concurrency Control needed in DBMS? Explain with concurrency anomalies.</div>
    <div class="ans-body">
        <strong>Need for Concurrency Control:</strong> When multiple transactions execute concurrently without coordination, interference causes severe anomalies:<br>
        <ul>
            <li><strong>Lost Update Problem:</strong> Two transactions overwrite each other's updates without reading the intermediate result.</li>
            <li><strong>Dirty Read (Uncommitted Dependency):</strong> A transaction reads modified data from an uncommitted transaction that subsequently aborts.</li>
            <li><strong>Inconsistent Analysis (Non-Repeatable Read):</strong> A transaction reads data while another transaction modifies it midway, producing skewed sums.</li>
        </ul>
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (1 &times; 15 = 15 Marks / CV-3 Pattern)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (15M)</span>Given the Relational Schema:<br>
    EMPLOYEE(<u>EmpID</u>, EmpName, Age, Gender, Salary, City, DeptID, Designation, HireDate)<br>
    DEPARTMENT(<u>DeptID</u>, DeptName, Location)<br>
    Write SQL Queries for:<br>
    1. Display the age of 'Male' employees.<br>
    2. Display the name of the highest salary employee.<br>
    3. Display the name of department of employee 'Aman'.<br>
    4. Display all employees belonging to the same address (city).<br>
    5. Which employee is the oldest manager in the company?</div>
    <div class="ans-body">
        <strong>SQL Queries:</strong>
<pre>
-- Query 1: Age of Male employees
SELECT EmpName, Age 
FROM EMPLOYEE 
WHERE Gender = 'Male';

-- Query 2: Name of the highest salary employee
SELECT EmpName, Salary 
FROM EMPLOYEE 
WHERE Salary = (SELECT MAX(Salary) FROM EMPLOYEE);

-- Query 3: Department name of employee 'Aman'
SELECT D.DeptName 
FROM DEPARTMENT D 
JOIN EMPLOYEE E ON D.DeptID = E.DeptID 
WHERE E.EmpName = 'Aman';

-- Query 4: Display all employees grouped by identical city
SELECT City, COUNT(EmpID) AS TotalEmps, 
       GROUP_CONCAT(EmpName) AS EmployeeNames 
FROM EMPLOYEE 
GROUP BY City 
HAVING COUNT(EmpID) > 1;

-- Query 5: Oldest manager in the company
SELECT EmpName, Age, Designation, HireDate 
FROM EMPLOYEE 
WHERE Designation = 'Manager' 
ORDER BY Age DESC 
LIMIT 1;
</pre>
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (2 &times; 22.5 = 45 Marks / CV-3 Pattern)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (22.5M)</span>Explain Two-Phase Locking (2PL) Protocol. Compare Strict 2PL and Rigorous 2PL with serializability guarantees.</div>
    <div class="ans-body">
        <strong>Two-Phase Locking (2PL):</strong> A concurrency control protocol guaranteeing conflict serializability by dividing a transaction into two distinct phases:
        <ol>
            <li><strong>Growing Phase:</strong> Transaction may obtain locks (Shared or Exclusive) but cannot release any lock.</li>
            <li><strong>Shrinking Phase:</strong> Transaction may release locks but cannot acquire any new lock.</li>
        </ol>
        <strong>Variants of 2PL:</strong>
        <ul>
            <li><strong>Basic 2PL:</strong> Guaranteed conflict serializability, but vulnerable to cascading aborts and deadlocks.</li>
            <li><strong>Strict 2PL:</strong> All Exclusive (X) locks held by a transaction must be retained until the transaction commits or aborts. <em>Guarantees strict schedules and eliminates cascading aborts!</em></li>
            <li><strong>Rigorous 2PL:</strong> Both Shared (S) and Exclusive (X) locks must be retained until transaction commit/abort. Ensures serializability in commit order.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (22.5M)</span>Define Normalization. Explain 1NF, 2NF, 3NF, and BCNF with a complete enterprise example.</div>
    <div class="ans-body">
        <strong>Comprehensive Enterprise Example:</strong><br>
        Consider unnormalized table: <code>STUDENT_COURSE_REG(StudentID, StudentName, CourseID, CourseName, Instructor, InstructorOffice)</code>.<br>
        Functional Dependencies:
        <ul>
            <li><span class="math">StudentID \to StudentName</span></li>
            <li><span class="math">CourseID \to CourseName, Instructor</span></li>
            <li><span class="math">Instructor \to InstructorOffice</span></li>
        </ul>
        Candidate Key: <span class="math">(StudentID, CourseID)</span>.<br><br>
        <strong>Step 1: Convert to 2NF (Eliminate Partial Dependencies):</strong><br>
        - <code>STUDENT(<u>StudentID</u>, StudentName)</code><br>
        - <code>COURSE(<u>CourseID</u>, CourseName, Instructor, InstructorOffice)</code><br>
        - <code>ENROLLMENT(<u>StudentID</u>, <u>CourseID</u>)</code><br><br>
        <strong>Step 2: Convert to 3NF (Eliminate Transitive Dependency in COURSE):</strong><br>
        In <code>COURSE</code>, <span class="math">Instructor \to InstructorOffice</span> is transitive.<br>
        - <code>COURSE(<u>CourseID</u>, CourseName, Instructor)</code> (FK: Instructor)<br>
        - <code>INSTRUCTOR(<u>Instructor</u>, InstructorOffice)</code><br>
        All relations are now in 3NF and BCNF with zero redundancy!
    </div>
</div>
"""

print("Generating DBMS 2021 PDF...")
generate_dbms_pdf("December 2021", "dbms 2021 solved.pdf", YEAR_2021_HTML)

# ==============================================================================
# YEAR 2020 (December 2020)
# ==============================================================================
YEAR_2020_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Define DML (Data Manipulation Language).</div>
    <div class="ans-body">
        <strong>Definition:</strong> <strong>Data Manipulation Language (DML)</strong> provides constructs for accessing, inserting, updating, and querying stored database records. Classified into <em>Procedural DML</em> (user specifies what data and how to retrieve it) and <em>Non-Procedural / Declarative DML</em> (SQL, where user specifies only what data is needed).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Give examples of Simple and Composite Attributes of an entity.</div>
    <div class="ans-body">
        <strong>Examples:</strong>
        <ul>
            <li><strong>Simple (Atomic) Attribute:</strong> Cannot be divided into subparts (e.g., <code>RollNo = 101</code>, <code>Age = 21</code>, <code>Salary = 50000</code>).</li>
            <li><strong>Composite Attribute:</strong> Can be divided into smaller sub-components with independent meanings (e.g., <code>Address</code> divided into <code>HouseNo</code>, <code>Street</code>, <code>City</code>, <code>Pincode</code>; or <code>Name</code> into <code>FirstName</code>, <code>LastName</code>).</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>What do you mean by Referential Integrity Constraint?</div>
    <div class="ans-body">
        <strong>Definition:</strong> <strong>Referential Integrity</strong> requires that any value of a foreign key attribute in a referencing relation must either match an existing primary key value in the referenced relation or be <code>NULL</code>. Enforces valid relationships and prevents "orphan records".
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What is a Data Dictionary (System Catalog)?</div>
    <div class="ans-body">
        <strong>Definition:</strong> A <strong>Data Dictionary</strong> is a reserved set of read-only system tables maintained by the DBMS that stores metadata (data about data), including schemas, table descriptions, column domains, integrity constraints, indexes, user privileges, and storage allocations.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Define Relational Schema.</div>
    <div class="ans-body">
        <strong>Definition:</strong> A <strong>Relational Schema</strong> denotes the design structure of a relation, symbolized as <span class="math">R(A_1, A_2, \dots, A_n)</span>, where <span class="math">R</span> is the relation name and <span class="math">A_i</span> are attribute names defined over specific domains <span class="math">dom(A_i)</span>.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain Lossless-Join Decomposition and Dependency Preservation in relational design.</div>
    <div class="ans-body">
        <strong>1. Lossless-Join Decomposition:</strong><br>
        A decomposition of relation <span class="math">R</span> into <span class="math">R_1</span> and <span class="math">R_2</span> is lossless if and only if natural join of the projections equals the original relation without generating spurious tuples:
        <div class="diagram-box">R_1 &bowtie; R_2 = R &hArr; (R_1 &cap; R_2 &rarr; R_1) OR (R_1 &cap; R_2 &rarr; R_2)</div>
        <strong>2. Dependency Preservation:</strong><br>
        A decomposition preserves dependencies if the union of functional dependencies enforceable within individual decomposed relations covers all functional dependencies of the original relation: <span class="math">(F_1 \cup F_2)^+ = F^+</span>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Compare 3NF and BCNF with an illustrative example.</div>
    <div class="ans-body">
        <strong>Key Differences:</strong>
        <ul>
            <li><strong>3NF:</strong> For every non-trivial FD <span class="math">X \to Y</span>, either <span class="math">X</span> is a super key <em>OR</em> <span class="math">Y</span> is a prime attribute (part of any candidate key). Allows dependency preservation always.</li>
            <li><strong>BCNF:</strong> For every non-trivial FD <span class="math">X \to Y</span>, <span class="math">X</span> <strong>must strictly be a super key</strong>. Eliminates all FD redundancy, but may not always preserve all functional dependencies.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Draw an ER Diagram for a University Examination System with entities, attributes, and relationships.</div>
    <div class="ans-body">
        <strong>Entities:</strong> <code>STUDENT</code> (<u>RollNo</u>, Name), <code>COURSE</code> (<u>CourseCode</u>, Title), <code>EXAM_CENTER</code> (<u>CenterID</u>, Location), <code>ADMIT_CARD</code> (<u>AdmitCardNo</u>).<br>
        <div class="diagram-box">
[STUDENT] ----- (1:1) ----- [ADMIT_CARD]
    | (M)
    |
 < ENROLLS >
    |
    v (N)
 [COURSE] ----- (N:1) ----- [EXAM_CENTER]
        </div>
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Discuss Relational Algebra fundamental operations with examples.</div>
    <div class="ans-body">
        <strong>Operations:</strong>
        <ol>
            <li><strong>Selection (&sigma;):</strong> <span class="math">\sigma_{Marks \ge 60}(Student)</span></li>
            <li><strong>Projection (&pi;):</strong> <span class="math">\pi_{RollNo, Name}(Student)</span></li>
            <li><strong>Cartesian Product (&times;):</strong> <span class="math">Student \times Course</span></li>
            <li><strong>Union (&cup;):</strong> <span class="math">SectionA \cup SectionB</span></li>
            <li><strong>Set Difference (&minus;):</strong> <span class="math">AllStudents - PassedStudents</span></li>
            <li><strong>Rename (&rho;):</strong> <span class="math">\rho_{S}(Student)</span></li>
        </ol>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain File Organization Techniques: Sequential, Indexed Sequential (ISAM), and Hashed File Organization.</div>
    <div class="ans-body">
        <strong>1. Sequential File Organization:</strong> Records stored consecutively ordered by a search key. Fast for full table scans, slow <span class="math">O(N)</span> for insertions/random lookups.<br>
        <strong>2. Indexed Sequential Access Method (ISAM):</strong> Combines sequential ordering with hierarchical index blocks (Cylinder, Track index). Enables rapid binary search.<br>
        <strong>3. Hashed File Organization:</strong> Uses hash function on search key for direct bucket addressing. Offers <span class="math">O(1)</span> lookups, but poor for range queries.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain Database Security and Authorization. Discuss GRANT and REVOKE commands in SQL.</div>
    <div class="ans-body">
        <strong>SQL Security Commands:</strong>
<pre>
-- Granting SELECT and INSERT privileges with delegation rights
GRANT SELECT, INSERT ON Employee TO user_ravi WITH GRANT OPTION;

-- Granting role-based access
CREATE ROLE clerk;
GRANT SELECT, UPDATE(Salary) ON Employee TO clerk;
GRANT clerk TO user_amit;

-- Revoking privileges
REVOKE INSERT ON Employee FROM user_ravi CASCADE;
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain Two-Phase Locking (2PL) and describe Deadlock Prevention and Detection mechanisms.</div>
    <div class="ans-body">
        <strong>Deadlock Handling:</strong>
        <ul>
            <li><strong>Deadlock Prevention:</strong> Uses transaction timestamps to avoid circular wait:
                <ul>
                    <li><em>Wait-Die (Non-preemptive):</em> Older waits for younger; younger dies immediately.</li>
                    <li><em>Wound-Wait (Preemptive):</em> Older wounds (preempts) younger; younger waits for older.</li>
                </ul>
            </li>
            <li><strong>Deadlock Detection:</strong> Builds periodic <em>Wait-For Graph (WFG)</em>; cycles in the graph indicate deadlocks, resolved by aborting the lowest-cost victim transaction.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain Views in SQL. What are the advantages of Views? When is a View updatable?</div>
    <div class="ans-body">
        <strong>Views in SQL:</strong> A <strong>View</strong> is a virtual table defined by an underlying stored SQL query.<br>
        <strong>Advantages:</strong> Data security (restricts column access), simplified queries, and logical data independence.<br>
        <strong>Updatable View Criteria:</strong>
        <ul>
            <li>Query contains only one base table in <code>FROM</code> clause.</li>
            <li>No aggregate functions (<code>SUM</code>, <code>AVG</code>, <code>COUNT</code>).</li>
            <li>No <code>GROUP BY</code>, <code>HAVING</code>, <code>DISTINCT</code>, or <code>UNION</code>.</li>
            <li>Primary key of base table must be included in the view columns.</li>
        </ul>
    </div>
</div>
"""

print("Generating DBMS 2020 PDF...")
generate_dbms_pdf("December 2020", "dbms 2020 solved.pdf", YEAR_2020_HTML)

# ==============================================================================
# YEAR 2019 (November 2019)
# ==============================================================================
YEAR_2019_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Name the three levels of Data Abstraction.</div>
    <div class="ans-body">
        <strong>Three Levels:</strong>
        <ol>
            <li><strong>Physical Level (Lowest):</strong> Describes how data is stored on disk blocks.</li>
            <li><strong>Logical / Conceptual Level (Middle):</strong> Describes what data is stored and relationships among data.</li>
            <li><strong>View / External Level (Highest):</strong> Describes customized views for specific user groups.</li>
        </ol>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Differentiate between Entity Integrity and Referential Integrity.</div>
    <div class="ans-body">
        <strong>Differences:</strong>
        <ul>
            <li><strong>Entity Integrity:</strong> States that no primary key attribute value can be <code>NULL</code>, ensuring every tuple can be uniquely identified.</li>
            <li><strong>Referential Integrity:</strong> States that a foreign key value must either match an existing primary key value in the parent relation or be <code>NULL</code>.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Differentiate between Candidate Key and Primary Key.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> A relation may possess multiple candidate keys (minimal super keys). The database designer selects one candidate key as the <strong>Primary Key</strong>, while all remaining candidate keys are designated as <strong>Alternate Keys</strong>.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>List any four disadvantages of File Processing Systems.</div>
    <div class="ans-body">
        <strong>Disadvantages:</strong> Data redundancy and inconsistency, lack of data independence, concurrent access anomalies, and poor security enforcement.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Distinguish between Functional Dependency and Multivalued Dependency.</div>
    <div class="ans-body">
        <strong>Comparison:</strong>
        <ul>
            <li><strong>Functional Dependency (X &rarr; Y):</strong> For any two tuples with identical <span class="math">X</span> values, their <span class="math">Y</span> values must be identical (single-valued dependency). Basis of 2NF, 3NF, BCNF.</li>
            <li><strong>Multivalued Dependency (X &twoheadrightarrow; Y):</strong> The presence of <span class="math">(x, y_1, z_1)</span> and <span class="math">(x, y_2, z_2)</span> implies the presence of <span class="math">(x, y_1, z_2)</span> and <span class="math">(x, y_2, z_1)</span>, representing independent multi-valued facts. Basis of 4NF.</li>
        </ul>
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain Second Normal Form (2NF) and Third Normal Form (3NF) with examples.</div>
    <div class="ans-body">
        <strong>2NF:</strong> In 1NF and no partial dependencies (every non-prime attribute depends on the whole candidate key).<br>
        <strong>3NF:</strong> In 2NF and no transitive dependencies (for every non-trivial FD <span class="math">X \to Y</span>, <span class="math">X</span> is a super key or <span class="math">Y</span> is prime).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Compare B-Tree and B+ Tree Index Structures.</div>
    <div class="ans-body">
        <strong>Comparison:</strong>
        <table class="grid-table">
            <thead><tr><th>Feature</th><th>B-Tree</th><th>B+ Tree</th></tr></thead>
            <tbody>
                <tr><td>Data Storage</td><td>Keys and data records/pointers stored in both internal and leaf nodes.</td><td>Data pointers stored <strong>only in leaf nodes</strong>; internal nodes store only routing keys.</td></tr>
                <tr><td>Leaf Node Linking</td><td>Leaf nodes are not linked.</td><td>Leaf nodes are connected via a <strong>doubly linked list</strong>.</td></tr>
                <tr><td>Range Queries</td><td>Slow (requires in-order tree traversal).</td><td>Extremely fast (scan linked list across leaf nodes).</td></tr>
                <tr><td>Node Capacity</td><td>Fewer keys per node due to data pointers.</td><td>High fan-out, fewer levels, reduced disk I/O.</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain Conflict Serializability and Testing for Serializability using Precedence Graph.</div>
    <div class="ans-body">
        <strong>Precedence Graph Method:</strong>
        <ol>
            <li>Create a node for every committed transaction <span class="math">T_i</span>.</li>
            <li>Draw a directed edge <span class="math">T_i \to T_j</span> if <span class="math">T_i</span> performs a conflicting operation before <span class="math">T_j</span> on the same data item (Write-Read, Read-Write, or Write-Write).</li>
            <li>If the graph contains <strong>NO cycle</strong>, the schedule is conflict serializable. Topological sort gives the equivalent serial schedule.</li>
        </ol>
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Explain the Three-Tier Client/Server Architecture of DBMS with Data Independence.</div>
    <div class="ans-body">
        <strong>Three-Tier Architecture:</strong>
        <ul>
            <li><strong>Presentation Tier (User Interface):</strong> Web browser or desktop client GUI (React, HTML).</li>
            <li><strong>Application Tier (Business Logic):</strong> Web/Application server executing business validation and query processing (Java, Node.js, Python).</li>
            <li><strong>Database Tier (Data Storage):</strong> Enterprise RDBMS managing database engine, query processing, transactions, and tables.</li>
        </ul>
        Provides enhanced security, scalability, and clean modular separation.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Draw an ER Diagram for a Library Management System with full entities and relational schema.</div>
    <div class="ans-body">
        <strong>Entities:</strong> <code>BOOK</code>, <code>MEMBER</code>, <code>PUBLISHER</code>, <code>BORROWS</code>.<br>
        <div class="diagram-box">
[MEMBER] ----- (M:N via BORROWS with IssueDate, ReturnDate) ----- [BOOK]
                                                                    | (N:1)
                                                              [PUBLISHER]
        </div>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Discuss SQL Characteristics and explain five Aggregate Functions with complete query examples.</div>
    <div class="ans-body">
        <strong>SQL Queries for Aggregate Functions:</strong>
<pre>
-- 1. COUNT: Total employees in IT
SELECT COUNT(*) FROM Employee WHERE Dept = 'IT';

-- 2. SUM: Total payroll for Sales
SELECT SUM(Salary) FROM Employee WHERE Dept = 'Sales';

-- 3. AVG: Average salary in company
SELECT AVG(Salary) FROM Employee;

-- 4. MIN and MAX: Salary bounds
SELECT MIN(Salary) AS MinSalary, MAX(Salary) AS MaxSalary FROM Employee;
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Discuss Selection, Projection, and Join operators of Relational Algebra with detailed expressions.</div>
    <div class="ans-body">
        <strong>Detailed Operators:</strong>
        <ul>
            <li><span class="math">\sigma_{City='Noida'}(Customer)</span> selects rows where City is Noida.</li>
            <li><span class="math">\pi_{Name, Email}(Customer)</span> projects distinct Name and Email attributes.</li>
            <li><span class="math">Customer \bowtie_{Customer.ID = Order.CustID} Order</span> performs equijoin between Customer and Order relations.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain Database Recovery Techniques: Log-Based Recovery, Immediate Update, Deferred Update, and Checkpoints.</div>
    <div class="ans-body">
        <strong>Log-Based Recovery:</strong>
        <ul>
            <li><strong>Deferred Update (NO-UNDO / REDO):</strong> Updates are recorded only in the log until commit. During recovery, only committed transactions are REDONE; uncommitted transactions require NO UNDO.</li>
            <li><strong>Immediate Update (UNDO / REDO):</strong> Updates can be written to disk before commit. Active uncommitted transactions at crash must be UNDONE; committed ones are REDONE.</li>
            <li><strong>Checkpoints:</strong> Periodically flushes dirty log buffers to disk. Recovery scans backward only to the most recent checkpoint, dramatically shortening crash recovery time.</li>
        </ul>
    </div>
</div>
"""

print("Generating DBMS 2019 PDF...")
generate_dbms_pdf("November 2019", "dbms 2019 solved.pdf", YEAR_2019_HTML)
