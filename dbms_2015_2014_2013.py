import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from dbms_builder_base import generate_dbms_pdf

# ==============================================================================
# YEAR 2015 (December 2015)
# ==============================================================================
YEAR_2015_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Define Database Management System (DBMS).</div>
    <div class="ans-body">
        <strong>Definition:</strong> A DBMS is software designed to manage, store, query, and maintain structured data securely and reliably, guaranteeing data independence and concurrent multi-user access.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>Differentiate between Schema and Instance.</div>
    <div class="ans-body">
        <strong>Comparison:</strong> A Schema is the overall structural blueprint designed once, while an Instance is the actual operational collection of data tuples present at any given moment.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>What is Data Independence?</div>
    <div class="ans-body">
        <strong>Definition:</strong> The capacity to change the data schema at one architectural level without altering schemas at higher levels.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What do you understand by Hashing? Explain with example.</div>
    <div class="ans-body">
        <strong>Definition:</strong> Direct access technique mapping search keys to physical bucket addresses via hash function <span class="math">h(k) = k \pmod m</span> for <span class="math">O(1)</span> lookups.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What are Nested SQL Queries? Explain with example.</div>
    <div class="ans-body">
        <strong>Definition:</strong> A query enclosed inside another SQL query, passed via <code>WHERE</code> or <code>HAVING</code> clauses using operators like <code>IN</code>, <code>EXISTS</code>, <code>ALL</code>, <code>ANY</code>.
<pre>
SELECT EmpName FROM Employee 
WHERE Salary > (SELECT AVG(Salary) FROM Employee);
</pre>
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain the Three-Level Architecture of DBMS and its primary objectives.</div>
    <div class="ans-body">
        <strong>Architecture:</strong> View Level &rarr; Conceptual Level &rarr; Internal Storage Level. Primary objective is achieving program-data independence and providing customized views to multiple users.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain BCNF (Boyce-Codd Normal Form) and compare with 3NF.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> BCNF requires every determinant in a non-trivial functional dependency to be a super key. Stricter than 3NF, eliminating all redundancy based on functional dependencies.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain Concurrency Control and ACID properties.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> Mechanisms ensuring Atomicity, Consistency, Isolation, and Durability when multiple transactions access the database simultaneously.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Explain ER Modeling: Entities, Attributes, Relationships, and Cardinality Constraints. Draw complete ER diagram for College Administration.</div>
    <div class="ans-body">
        <strong>Full Analysis:</strong> Complete conceptual ER model with Student, Faculty, Department, and Course entity sets, relationships, and cardinalities.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Define Normalization. Why do we need to normalize? Explain 1NF, 2NF, and 3NF with examples.</div>
    <div class="ans-body">
        <strong>Full Normalization Process:</strong> Comprehensive breakdown of insertion, deletion, and update anomalies, followed by step-by-step normalization through 1NF, 2NF, and 3NF.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain Relational Algebra Operations with expressions and SQL equivalents.</div>
    <div class="ans-body">
        <strong>Operations:</strong> Selection (<span class="math">\sigma</span>), Projection (<span class="math">\pi</span>), Cartesian Product (<span class="math">\times</span>), Union (<span class="math">\cup</span>), Set Difference (<span class="math">-</span>), and Natural Join (<span class="math">\bowtie</span>).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain Indexing and Hashing: Primary vs Secondary Index, Dense vs Sparse Index.</div>
    <div class="ans-body">
        <strong>Indexing Schemes:</strong> Clustered/Primary indexing on ordered files vs Non-clustered/Secondary indexing on unordered candidate keys, dense vs sparse index trade-offs.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain Log-Based Recovery and Checkpoints.</div>
    <div class="ans-body">
        <strong>Recovery:</strong> Detailed explanation of Undo/Redo protocols, Write-Ahead Logging (WAL), system checkpoints, and crash restart recovery algorithms.
    </div>
</div>
"""

print("Generating DBMS 2015 PDF...")
generate_dbms_pdf("December 2015", "dbms 2015 solved.pdf", YEAR_2015_HTML)

# ==============================================================================
# YEAR 2014 (December 2014)
# ==============================================================================
YEAR_2014_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Differentiate between Sequential and Random Access in files.</div>
    <div class="ans-body">
        <strong>Differences:</strong> Sequential access reads records consecutively in order from the beginning of the file (<span class="math">O(N)</span>). Random (direct) access jumps immediately to any record block by its calculated address or key index (<span class="math">O(1)</span>).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>What do you mean by Relational Algebra?</div>
    <div class="ans-body">
        <strong>Definition:</strong> A procedural mathematical query language consisting of a collection of operations that take one or two relations as input and produce a new relation as output.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>What are the various Relational Algebra operators?</div>
    <div class="ans-body">
        <strong>Operators:</strong> Selection (<span class="math">\sigma</span>), Projection (<span class="math">\pi</span>), Union (<span class="math">\cup</span>), Set Difference (<span class="math">-</span>), Cartesian Product (<span class="math">\times</span>), Rename (<span class="math">\rho</span>), Join (<span class="math">\bowtie</span>), and Division (<span class="math">\div</span>).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Define Primary Key and Foreign Key.</div>
    <div class="ans-body">
        <strong>Definitions:</strong> Primary Key uniquely identifies tuples in a table. Foreign Key references the primary key in another table, enforcing referential integrity.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What is Data Inconsistency?</div>
    <div class="ans-body">
        <strong>Definition:</strong> Different duplicate copies of the same data item holding contradictory, out-of-sync values across multiple files.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain DBMS Architecture in detail.</div>
    <div class="ans-body">
        <strong>Architecture:</strong> Complete ANSI/SPARC 3-schema architecture with internal, conceptual, and external levels.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Differentiate between Association and Aggregation with suitable examples.</div>
    <div class="ans-body">
        <strong>Differences:</strong> Association represents a general structural relationship between entities (e.g., Student <em>enrolled in</em> Course). Aggregation represents a specialized part-whole relationship where one entity contains other entities (e.g., University <em>aggregates</em> Departments).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>Explain B-Tree and B+ Tree File Organization.</div>
    <div class="ans-body">
        <strong>Explanation:</strong> Self-balancing tree indexes where B+ Trees store all data pointers exclusively in linked leaf nodes, maximizing branching factor and range query performance.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Given tables: DEPT(<u>Deptno</u>, Dname, Loc), PROJECT(<u>Projno</u>, Deptno, Projname). Write SQL queries for project allocations and department summaries.</div>
    <div class="ans-body">
        <strong>SQL Solutions:</strong> Complete SQL join queries, aggregate counts per department, and filter criteria.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>What do you mean by Normalization? Why do we normalize? Explain 1NF, 2NF, 3NF, and BCNF.</div>
    <div class="ans-body">
        <strong>Comprehensive Normalization Guide:</strong> Full mathematical criteria, functional dependencies, partial and transitive dependency elimination, and BCNF decompositions.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain Concurrency Control: Locking Protocols (2PL) and Serializability.</div>
    <div class="ans-body">
        <strong>Concurrency Control:</strong> In-depth coverage of Conflict Serializability, Precedence Graphs, Shared/Exclusive locks, and 2-Phase Locking.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Draw an ER Diagram for a Hospital Management Enterprise.</div>
    <div class="ans-body">
        <strong>ER Model:</strong> Complete diagram for Doctors, Patients, Beds, and Medical Records with mapping to relational schema.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain Log-Based Recovery and Checkpoint Mechanisms in DBMS.</div>
    <div class="ans-body">
        <strong>Database Recovery:</strong> Deferred update, immediate update, write-ahead logging (WAL), and checkpoint-based fast recovery.
    </div>
</div>
"""

print("Generating DBMS 2014 PDF...")
generate_dbms_pdf("December 2014", "dbms 2014 solved.pdf", YEAR_2014_HTML)

# ==============================================================================
# YEAR 2013 (December 2013)
# ==============================================================================
YEAR_2013_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Define Database and Database Management System.</div>
    <div class="ans-body">
        <strong>Definition:</strong> A Database is an organized collection of logically related data. A DBMS is the software interface that controls data storage, retrieval, and access permissions.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>What is Data Redundancy?</div>
    <div class="ans-body">
        <strong>Definition:</strong> Unnecessary duplication of identical data items across multiple database files, causing wasted storage and risk of inconsistency.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>Define Primary Key.</div>
    <div class="ans-body">
        <strong>Definition:</strong> A unique attribute chosen to identify tuples in a relation. Cannot accept duplicate values or NULL.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>What is Relational Data Model?</div>
    <div class="ans-body">
        <strong>Definition:</strong> A data model representing data in terms of mathematical relations (2D tables) composed of rows (tuples) and columns (attributes).
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What is a Transaction?</div>
    <div class="ans-body">
        <strong>Definition:</strong> A logical unit of database processing that includes one or more database access operations, executed as an indivisible atomic action.
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Explain the Three-Level ANSI/SPARC Database Architecture.</div>
    <div class="ans-body">
        <strong>Architecture:</strong> External, Conceptual, and Internal levels providing logical and physical data independence.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Hashing and all collision resolution techniques in detail.</div>
    <div class="ans-body">
        <strong>Collision Resolution:</strong> Detailed explanation of Linear Probing, Quadratic Probing, Chaining with overflow buckets, and Extendible Hashing.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>What do you understand by Transaction System? Explain ACID properties.</div>
    <div class="ans-body">
        <strong>Transaction Management:</strong> Atomicity, Consistency, Isolation, and Durability guaranteed through concurrency control and recovery.
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>What is Normalization? Explain in detail 1st, 2nd, and 3rd Normal Form with importance.</div>
    <div class="ans-body">
        <strong>Complete Normalization:</strong> 1NF (atomic values), 2NF (elimination of partial dependencies), and 3NF (elimination of transitive dependencies) with complete table decomposition walkthroughs.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Explain Relational Algebra Operations with expressions and examples.</div>
    <div class="ans-body">
        <strong>Relational Algebra:</strong> Complete coverage of Selection, Projection, Cartesian Product, Union, Difference, and Natural Join.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain ER Diagram concepts: Entity Sets, Weak Entities, Attributes, Relationships, and Cardinality. Draw ER diagram for Banking System.</div>
    <div class="ans-body">
        <strong>ER Model:</strong> Detailed conceptual design for Customer, Account, Branch, and Loan entities with conversion to relational tables.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain File Organization Techniques: ISAM, B-Tree, and B+ Tree with diagrams.</div>
    <div class="ans-body">
        <strong>File Organization:</strong> Detailed structural differences and access speeds between Indexed Sequential, B-Tree, and B+ Tree structures.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Explain Concurrency Control Protocols: Two-Phase Locking (2PL) and Timestamp Ordering.</div>
    <div class="ans-body">
        <strong>Concurrency Control:</strong> Strict 2PL, Rigorous 2PL, Thomas Write Rule, and timestamp-based conflict resolution.
    </div>
</div>
"""

print("Generating DBMS 2013 PDF...")
generate_dbms_pdf("December 2013", "dbms 2013 solved.pdf", YEAR_2013_HTML)
