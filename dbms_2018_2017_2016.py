import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from dbms_builder_base import generate_dbms_pdf

# ==============================================================================
# YEAR 2018 (December 2018)
# ==============================================================================
YEAR_2018_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Define Super Keys, Candidate Keys, and Primary Keys.</div>
    <div class="ans-body">
        <strong>Definitions:</strong>
        <ul>
            <li><strong>Super Key:</strong> A set of one or more attributes that uniquely identifies each tuple in a relation (may contain redundant attributes).</li>
            <li><strong>Candidate Key:</strong> A minimal super key having no extraneous/redundant attributes.</li>
            <li><strong>Primary Key:</strong> The specific candidate key chosen by the database designer as the principal tuple identifier. Cannot contain <code>NULL</code>.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Explain the term "Data Independence".</div>
    <div class="ans-body">
        <strong>Definition:</strong> <strong>Data Independence</strong> is the capacity to change the schema at one level of the database system without having to alter the schema at the next higher level. It includes Physical Data Independence (modifying internal storage without affecting conceptual schema) and Logical Data Independence (modifying conceptual schema without altering external views).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>What is Hashing? Explain.</div>
    <div class="ans-body">
        <strong>Definition:</strong> <strong>Hashing</strong> is a direct addressing technique where a mathematical algorithm (hash function) calculates the exact physical block address of a record from its search key value, enabling <span class="math">O(1)</span> constant-time retrieval.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What do you mean by Relational Database? Describe.</div>
    <div class="ans-body">
        <strong>Definition:</strong> A <strong>Relational Database</strong> is a collection of data items organized into formal tables (relations) of rows and columns based on first-order predicate logic, where relations are linked together via primary and foreign key constraints.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Briefly explain the terms Security and Authorization.</div>
    <div class="ans-body">
        <strong>Definitions:</strong>
        <ul>
            <li><strong>Database Security:</strong> Protection of the database against unauthorized access, malicious attacks, corruption, or destruction.</li>
            <li><strong>Authorization:</strong> The mechanism that defines and enforces what actions (e.g., SELECT, INSERT, UPDATE, DROP) a validated user or role is permitted to perform on specific database objects.</li>
        </ul>
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>What is a Referential Integrity Constraint? Why do we need it? Explain with a suitable example.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> Referential integrity requires that a foreign key value in a referencing table must match an existing primary key value in the referenced table, or be <code>NULL</code>.<br>
        <strong>Need:</strong> Prevents orphan records and inconsistent states.<br>
        <strong>Example:</strong>
<pre>
-- Parent Table
CREATE TABLE Department (DeptNo INT PRIMARY KEY, DName VARCHAR(30));

-- Child Table with Foreign Key
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    DeptNo INT,
    CONSTRAINT fk_emp_dept FOREIGN KEY (DeptNo) REFERENCES Department(DeptNo)
        ON DELETE CASCADE ON UPDATE CASCADE
);
</pre>
        If department 10 is deleted, <code>ON DELETE CASCADE</code> automatically removes all employees assigned to department 10, preventing dangling references.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>List four significant differences between a File-Processing System and a DBMS.</div>
    <div class="ans-body">
        <strong>Differences:</strong>
        <table class="grid-table">
            <thead><tr><th>Aspect</th><th>File-Processing System</th><th>DBMS</th></tr></thead>
            <tbody>
                <tr><td>Data Redundancy</td><td>High redundancy across duplicate files.</td><td>Controlled and normalized.</td></tr>
                <tr><td>Data Independence</td><td>None (tight coupling with code).</td><td>Logical & Physical Data Independence.</td></tr>
                <tr><td>Concurrency</td><td>Prone to race conditions and lost updates.</td><td>ACID compliant concurrency control.</td></tr>
                <tr><td>Crash Recovery</td><td>Manual restore; inconsistent state.</td><td>Automated log-based rollback and redo.</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain Third Normal Form (3NF) with example.</div>
    <div class="ans-body">
        <strong>Definition:</strong> A relation is in <strong>3NF</strong> if it is in 2NF and has no transitive functional dependencies for non-prime attributes. Formally, for every non-trivial FD <span class="math">X \to Y</span>, either <span class="math">X</span> is a super key or <span class="math">Y</span> is a prime attribute.<br>
        <strong>Example:</strong> <code>Student(<u>RollNo</u>, Name, DeptID, DeptHead)</code>.<br>
        <span class="math">RollNo \to DeptID</span> and <span class="math">DeptID \to DeptHead</span> (Transitive!).<br>
        Decompose into: <code>Student(<u>RollNo</u>, Name, DeptID)</code> and <code>Department(<u>DeptID</u>, DeptHead)</code>.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Explain the different locking techniques with examples for concurrency control.</div>
    <div class="ans-body">
        <strong>Locking Techniques:</strong>
        <ol>
            <li><strong>Shared Lock (S-Lock / Read Lock):</strong> Multiple transactions can simultaneously hold shared locks to read data without conflict.</li>
            <li><strong>Exclusive Lock (X-Lock / Write Lock):</strong> Only one transaction can hold an exclusive lock to read and write. No other transaction can hold any lock on that item.</li>
            <li><strong>Two-Phase Locking (2PL):</strong> Growing Phase (acquiring locks) followed by Shrinking Phase (releasing locks). Guarantees conflict serializability.</li>
            <li><strong>Strict 2PL:</strong> Exclusive locks held until transaction commits, eliminating cascading rollbacks.</li>
        </ol>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain Indexed Sequential, B-Tree, and B+ Tree file organizations with examples.</div>
    <div class="ans-body">
        <strong>Comparison of File Organizations:</strong>
        <ul>
            <li><strong>Indexed Sequential (ISAM):</strong> Records stored in sequential key order with a multilevel static index. Good for sequential and direct access, but degrades with many overflow records.</li>
            <li><strong>B-Tree:</strong> Self-balancing dynamic multi-way search tree. Keys and data record pointers reside in both internal nodes and leaf nodes.</li>
            <li><strong>B+ Tree:</strong> Modern standard for relational DBMS storage engines. Internal nodes store only search keys to guide navigation, while <strong>all actual data records/pointers reside in leaf nodes</strong> connected via a doubly linked list, enabling superior range scans.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain Super Class, Sub Class, Inheritance, and Generalization with examples.</div>
    <div class="ans-body">
        <strong>Enhanced ER (EER) Concepts:</strong>
        <ul>
            <li><strong>Superclass:</strong> A generic entity set that includes distinct subgroups (e.g., <code>PERSON</code>).</li>
            <li><strong>Subclass:</strong> A specialized sub-entity set that inherits all attributes and relationships from its superclass, while adding specialized attributes (e.g., <code>STUDENT</code> with GPA, <code>TEACHER</code> with Rank).</li>
            <li><strong>Attribute Inheritance:</strong> Subclass entities automatically inherit the primary key and all general attributes of their superclass.</li>
            <li><strong>Generalization:</strong> Bottom-up synthesis where lower-level entity sets are combined into a generalized superclass entity.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Write short notes on: (i) Strong and Weak Entity, (ii) Different Levels of Data Abstraction, (iii) Database Recovery Techniques.</div>
    <div class="ans-body">
        <strong>(i) Strong vs Weak Entity:</strong> A Strong entity has a primary key of its own. A Weak entity does not have a primary key and depends on the existence of an identifying strong entity set (identified by discriminator + strong entity PK).<br>
        <strong>(ii) Data Abstraction Levels:</strong> Physical level (low-level block storage), Logical level (community tables and relations), and View level (user-specific abstractions).<br>
        <strong>(iii) Database Recovery Techniques:</strong> Log-based recovery (Write-Ahead Logging), Deferred/Immediate update schemes, and Checkpoints to restore consistency following system failures.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>A hospital maintains data about entities: PATIENTS, DOCTORS, BEDS, ACCOUNTS. Construct an E-R diagram specifying keys, mapping cardinalities, and participation constraints. Show table mapping.</div>
    <div class="ans-body">
        <strong>Entities & Attributes:</strong>
        <ul>
            <li><code>PATIENTS(<u>SSNo</u>, LastName, FirstName, HomePhone, Sex, DOB, Age, Street, City, State, Zip)</code></li>
            <li><code>DOCTORS(<u>SSNo</u>, LastName, FirstName, OfficePhone, Pager, Specialty)</code></li>
            <li><code>BEDS(<u>RoomNumber</u>, <u>BedNumber</u>, Type, Status, PricePerHour)</code></li>
            <li><code>ACCOUNTS(<u>AccountNo</u>, DateIn, DateOut, TotalAmount, Status)</code></li>
        </ul>
        <strong>Relationships:</strong>
        <ul>
            <li><code>TREATS</code> (M:N between DOCTORS and PATIENTS)</li>
            <li><code>ASSIGNED_BED</code> (1:1 between PATIENTS and BEDS)</li>
            <li><code>HAS_ACCOUNT</code> (1:1 between PATIENTS and ACCOUNTS)</li>
        </ul>
        <div class="diagram-box">
  +------------+             ( M )             +------------+
  |  DOCTORS   | <---------------------------> |  PATIENTS  |
  | <u>SSNo</u>, Spec |          < TREATS >           | <u>SSNo</u>, Name |
  +------------+                               +------------+
                                                    | (1)
                                            < ASSIGNED_BED >
                                                    | (1)
                                                    v
                                               +------------+
                                               |    BEDS    |
                                               | <u>Room</u>, <u>Bed</u> |
                                               +------------+
        </div>
    </div>
</div>
"""

print("Generating DBMS 2018 PDF...")
generate_dbms_pdf("December 2018", "dbms 2018 solved.pdf", YEAR_2018_HTML)

# ==============================================================================
# YEAR 2017 (December 2017)
# ==============================================================================
YEAR_2017_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Define Metadata and Data Dictionary.</div>
    <div class="ans-body">
        <strong>Definition:</strong> <strong>Metadata</strong> is "data about data" describing database structures, constraints, and data types. A <strong>Data Dictionary</strong> is the repository that permanently stores this metadata.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Define Tuple, Relation, Attribute, and Domain.</div>
    <div class="ans-body">
        <strong>Definitions:</strong>
        <ul>
            <li><strong>Relation:</strong> A two-dimensional table of records.</li>
            <li><strong>Tuple:</strong> A single row in a relation representing an individual entity instance.</li>
            <li><strong>Attribute:</strong> A named column describing a specific property.</li>
            <li><strong>Domain:</strong> The set of allowable atomic values for an attribute.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>What are Cardinality and Participation Constraints in ER Modeling?</div>
    <div class="ans-body">
        <strong>Definitions:</strong>
        <ul>
            <li><strong>Cardinality Ratio:</strong> Specifies the maximum number of relationship instances that an entity can participate in (1:1, 1:N, M:N).</li>
            <li><strong>Participation Constraint:</strong> Specifies whether existence of an entity depends on its being related to another entity: <em>Total</em> (double line) or <em>Partial</em> (single line).</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Differentiate between DDL and DML.</div>
    <div class="ans-body">
        <strong>DDL:</strong> Defines database schemas and tables (<code>CREATE</code>, <code>ALTER</code>, <code>DROP</code>).<br>
        <strong>DML:</strong> Manipulates and retrieves data instances (<code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>, <code>SELECT</code>).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What is a View in SQL?</div>
    <div class="ans-body">
        <strong>Definition:</strong> A <strong>View</strong> is a virtual table whose contents are defined by an underlying SQL query, providing security and abstraction without replicating stored data.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain 1NF and 2NF with examples.</div>
    <div class="ans-body">
        <strong>1NF:</strong> Eliminates repeating groups and non-atomic values.<br>
        <strong>2NF:</strong> In 1NF and contains no partial functional dependencies (all non-key attributes depend fully on the primary key).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>What is Query Optimization? Explain heuristic optimization.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> Query optimization is the process of choosing the most efficient execution plan for evaluating a query. Heuristic optimization applies algebraic rewrite rules:
        <ul>
            <li>Perform <code>Selection (&sigma;)</code> as early as possible (reduces intermediate relation sizes).</li>
            <li>Perform <code>Projection (&pi;)</code> early to eliminate unneeded attributes.</li>
            <li>Execute the most restrictive selections before performing Joins.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain Log-Based Recovery with WAL (Write-Ahead Logging) and Checkpoints.</div>
    <div class="ans-body">
        <strong>Log-Based Recovery:</strong> Records all database modifications in an append-only log file before writing changes to disk (Write-Ahead Logging). During crash recovery, log records are used to UNDO incomplete transactions and REDO committed ones. Checkpoints reduce recovery overhead by flushing dirty buffers periodically.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Explain the Three-Level ANSI/SPARC Database Architecture with detailed diagram.</div>
    <div class="ans-body">
        <strong>Architecture:</strong> External Schema (Views) &rarr; Conceptual Schema (Logical tables) &rarr; Internal Schema (Physical disk blocks and access paths). Ensures physical and logical data independence.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Given tables VENDOR(<u>VCode</u>, Name, Address, Phone) and PRODUCT(<u>PCode</u>, PName, Price, VCode). Write SQL queries for:<br>
    (i) Display all vendors from 'Delhi'.<br>
    (ii) Display products with price greater than 500.<br>
    (iii) Display vendor name who supplies product 'Laptop'.<br>
    (iv) Count total products supplied by each vendor.</div>
    <div class="ans-body">
        <strong>SQL Solutions:</strong>
<pre>
-- (i) Vendors from Delhi
SELECT * FROM VENDOR WHERE Address LIKE '%Delhi%';

-- (ii) Products with price > 500
SELECT PCode, PName, Price FROM PRODUCT WHERE Price > 500;

-- (iii) Vendor supplying 'Laptop'
SELECT V.Name 
FROM VENDOR V 
JOIN PRODUCT P ON V.VCode = P.VCode 
WHERE P.PName = 'Laptop';

-- (iv) Count total products per vendor
SELECT V.VCode, V.Name, COUNT(P.PCode) AS TotalProducts 
FROM VENDOR V 
LEFT JOIN PRODUCT P ON V.VCode = P.VCode 
GROUP BY V.VCode, V.Name;
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain Relational Algebra vs Relational Calculus.</div>
    <div class="ans-body">
        <strong>Comparison:</strong> Relational Algebra is procedural (specifies operations step-by-step), while Relational Calculus (Tuple & Domain) is non-procedural/declarative (expresses what is required via mathematical predicate logic). Codd's Theorem proves they are equivalent in expressive power.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain BCNF (Boyce-Codd Normal Form) and compare with 3NF.</div>
    <div class="ans-body">
        <strong>BCNF:</strong> Stricter form of 3NF where every determinant in a non-trivial functional dependency must be a super key. Eliminates anomalies that 3NF allows when there are overlapping composite candidate keys.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Given tables: PLAY(<u>PlayCode</u>, PlayName, DirNum), DIRECTOR(<u>DirNum</u>, DirName, DirDOB). Write SQL queries to find director names and plays directed.</div>
    <div class="ans-body">
        <strong>SQL Solutions:</strong>
<pre>
-- Director of play 'Hamlet'
SELECT D.DirName 
FROM DIRECTOR D 
JOIN PLAY P ON D.DirNum = P.DirNum 
WHERE P.PlayName = 'Hamlet';

-- All plays directed by each director
SELECT D.DirName, P.PlayName 
FROM DIRECTOR D 
JOIN PLAY P ON D.DirNum = P.DirNum 
ORDER BY D.DirName;
</pre>
    </div>
</div>
"""

print("Generating DBMS 2017 PDF...")
generate_dbms_pdf("December 2017", "dbms 2017 solved.pdf", YEAR_2017_HTML)

# ==============================================================================
# YEAR 2016 (December 2016)
# ==============================================================================
YEAR_2016_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Differentiate between Database System and File System.</div>
    <div class="ans-body">
        <strong>Differences:</strong> DBMS offers centralized control, eliminated data inconsistency, program-data independence, and built-in transaction recovery, which file systems lack.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Explain Foreign Key with ON DELETE CASCADE.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> A foreign key links a child record to a parent record. With <code>ON DELETE CASCADE</code>, deleting a parent row automatically cascades and deletes all corresponding child rows, maintaining referential integrity.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>What is a Weak Entity Set? How is it identified?</div>
    <div class="ans-body">
        <strong>Definition:</strong> An entity set lacking sufficient attributes to form a primary key. Identified using a <em>discriminator (partial key)</em> combined with the primary key of its identifying strong entity set.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Differentiate between Natural Join and Theta Join.</div>
    <div class="ans-body">
        <strong>Differences:</strong> Theta Join (<span class="math">R \bowtie_\theta S</span>) combines rows based on any arbitrary condition. Natural Join (<span class="math">R \bowtie S</span>) automatically equates attributes having identical names and eliminates duplicate columns.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>Explain COMMIT and ROLLBACK commands in SQL.</div>
    <div class="ans-body">
        <strong>TCL Commands:</strong>
        <ul>
            <li><code>COMMIT</code>: Permanently saves all transaction modifications to disk.</li>
            <li><code>ROLLBACK</code>: Reverts all uncommitted changes back to the start of the transaction or savepoint.</li>
        </ul>
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain BCNF (Boyce-Codd Normal Form) with example.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> A relation is in BCNF if for every non-trivial functional dependency <span class="math">X \to Y</span>, <span class="math">X</span> is a Super Key. Eliminates anomalies arising from overlapping candidate keys.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Compare Dense Index and Sparse Index in database indexing.</div>
    <div class="ans-body">
        <strong>Comparison:</strong>
        <ul>
            <li><strong>Dense Index:</strong> Contains an index record for <em>every single search-key value</em> in the data file. Faster search, larger index size.</li>
            <li><strong>Sparse Index:</strong> Contains index records for only some search-key values (typically one per disk block). Consumes less space, but requires scanning within blocks.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain Deadlock Detection and Prevention methods in DBMS.</div>
    <div class="ans-body">
        <strong>Methods:</strong> Deadlock prevention uses timestamp ordering (Wait-Die and Wound-Wait schemes). Deadlock detection periodically constructs a Wait-For Graph (WFG) and aborts a cycle-causing transaction.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Draw a detailed ER Diagram for a Banking Enterprise.</div>
    <div class="ans-body">
        <strong>Entities:</strong> <code>CUSTOMER</code>, <code>ACCOUNT</code>, <code>BRANCH</code>, <code>LOAN</code>.<br>
        <strong>Relationships:</strong> Customer deposits in Account, Customer borrows Loan, Branch maintains Accounts and Loans.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain Relational Algebra operators: Selection, Projection, Cartesian Product, Join, and Division.</div>
    <div class="ans-body">
        <strong>Relational Algebra:</strong> Complete explanation of fundamental algebraic query operators with mathematical notations and practical examples.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain Nested Subqueries and Correlated Subqueries in SQL with examples.</div>
    <div class="ans-body">
        <strong>Subqueries:</strong>
        <ul>
            <li><strong>Nested Subquery:</strong> Inner query executes once, and its result is used by outer query (e.g., <code>WHERE Salary > (SELECT AVG(Salary) FROM Emp)</code>).</li>
            <li><strong>Correlated Subquery:</strong> Inner query references columns of the outer query and re-executes for each row evaluated by outer query.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain ACID Properties and Serializability in transaction management.</div>
    <div class="ans-body">
        <strong>ACID & Serializability:</strong> In-depth coverage of Atomicity, Consistency, Isolation, Durability, conflict serializability, and conflict equivalence of schedules.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain ISAM and B+ Tree File Organizations with comparative analysis.</div>
    <div class="ans-body">
        <strong>File Organization:</strong> Detailed architectural comparison between static ISAM hierarchy and dynamic self-balancing B+ Trees.
    </div>
</div>
"""

print("Generating DBMS 2016 PDF...")
generate_dbms_pdf("December 2016", "dbms 2016 solved.pdf", YEAR_2016_HTML)
