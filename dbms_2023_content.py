import sys
import os
sys.path.append(r"c:\zzzz\pyq_solver_scripts")
from dbms_builder_base import generate_dbms_pdf

# ==============================================================================
# YEAR 2023 (December 2023)
# ==============================================================================
YEAR_2023_HTML = r"""
<div class="section-divider">SECTION A &mdash; VERY SHORT ANSWER QUESTIONS (5 &times; 3 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q1 (3M)</span>Define Database Management System (DBMS).</div>
    <div class="ans-body">
        <strong>Definition:</strong> A <strong>Database Management System (DBMS)</strong> is a computerized system software suite that enables users to define, create, maintain, query, and control access to a shared database. It serves as an intelligent interface between end-user applications and physical data storage.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q2 (3M)</span>List any five applications of DBMS.</div>
    <div class="ans-body">
        <strong>Applications:</strong>
        <ol>
            <li><strong>Banking:</strong> Customer accounts, loans, ATM transactions, fund transfers.</li>
            <li><strong>Airlines & Railways:</strong> Real-time reservation systems, flight schedules, ticketing.</li>
            <li><strong>Universities & Colleges:</strong> Student admissions, course registrations, grades, fee accounts.</li>
            <li><strong>E-Commerce & Retail:</strong> Online product catalogs, shopping carts, billing, inventory control.</li>
            <li><strong>Telecommunications:</strong> Call records, monthly billing, subscriber information, network routing.</li>
        </ol>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q3 (3M)</span>What are the disadvantages of a File Processing System?</div>
    <div class="ans-body">
        <strong>Disadvantages:</strong>
        <ul>
            <li><strong>Data Redundancy & Inconsistency:</strong> Same data stored in multiple files leading to conflicting copies.</li>
            <li><strong>Difficulty in Accessing Data:</strong> Requires writing a new custom program for every ad-hoc query.</li>
            <li><strong>Data Isolation:</strong> Data scattered across disparate file formats cannot be easily joined.</li>
            <li><strong>Integrity Problems:</strong> Hard to enforce consistency constraints across independent files.</li>
            <li><strong>Atomicity Failures:</strong> Incomplete updates during crashes leave data in corrupt states.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q4 (3M)</span>Define Data Model.</div>
    <div class="ans-body">
        <strong>Definition:</strong> A <strong>Data Model</strong> is an abstract framework providing a collection of conceptual concepts for describing data, relationships, semantics, and constraints in a database. Major categories: Conceptual/High-level (ER Model), Representational/Logical (Relational Model), and Physical/Low-level models.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q5 (3M)</span>What are Attributes? Give examples.</div>
    <div class="ans-body">
        <strong>Definition:</strong> An <strong>Attribute</strong> is a descriptive property or characteristic that describes an entity in an entity set.<br>
        <strong>Examples for Entity STUDENT:</strong>
        <ul>
            <li><em>Simple Attribute:</em> <code>RollNo</code>, <code>Age</code></li>
            <li><em>Composite Attribute:</em> <code>FullName</code> (composed of <code>FirstName</code>, <code>LastName</code>)</li>
            <li><em>Multivalued Attribute:</em> <code>PhoneNumbers</code>, <code>Hobbies</code></li>
            <li><em>Derived Attribute:</em> <code>Age</code> (computed from <code>DateOfBirth</code> and current date)</li>
        </ul>
    </div>
</div>

<div class="section-divider">SECTION B &mdash; SHORT ANSWER QUESTIONS (2 &times; 7.5 = 15 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q6 (7.5M)</span>Compare Generalization and Specialization with examples.</div>
    <div class="ans-body">
        <strong>Comparison:</strong>
        <table class="grid-table">
            <thead><tr><th>Criteria</th><th>Generalization</th><th>Specialization</th></tr></thead>
            <tbody>
                <tr><td>Approach</td><td><strong>Bottom-up</strong> design process</td><td><strong>Top-down</strong> design process</td></tr>
                <tr><td>Mechanism</td><td>Combines common features of multiple lower-level entities into a single higher-level entity.</td><td>Splits a higher-level entity into specialized sub-entities based on distinct features.</td></tr>
                <tr><td>Goal</td><td>Minimizes redundancy by factoring out common attributes.</td><td>Identifies distinguishing characteristics of specific sub-categories.</td></tr>
                <tr><td>Example</td><td>Entities <code>CAR</code> and <code>TRUCK</code> generalized into higher entity <code>VEHICLE</code>.</td><td>Entity <code>EMPLOYEE</code> specialized into <code>SALARIED_EMP</code> and <code>HOURLY_EMP</code>.</td></tr>
            </tbody>
        </table>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q7 (7.5M)</span>Explain Primary Key, Super Key, and Foreign Key with examples.</div>
    <div class="ans-body">
        <strong>Definitions & Relationships:</strong>
        <ul>
            <li><strong>Super Key:</strong> A set of one or more attributes that uniquely identifies a tuple within a relation. May contain redundant attributes (e.g., <code>{EmpID, Name}</code>).</li>
            <li><strong>Primary Key:</strong> A strictly minimal candidate key selected by the database designer to uniquely identify each tuple. No duplicates, no <code>NULL</code> allowed.</li>
            <li><strong>Foreign Key:</strong> An attribute that establishes a referential relationship by referencing the primary key of another table.</li>
        </ul>
        <div class="diagram-box">
Relation: EMPLOYEE(<u>EmpID</u>, EmpName, Email, DeptNo)
Relation: DEPARTMENT(<u>DeptNo</u>, DeptName, Building)

Super Keys: {EmpID}, {EmpID, EmpName}, {Email}, {EmpID, Email}
Candidate Keys: {EmpID}, {Email}
Primary Key: {EmpID}
Foreign Key: {DeptNo} in EMPLOYEE references DeptNo in DEPARTMENT
        </div>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q8 (7.5M)</span>What is Normalization? Explain the importance of Normalization in database design.</div>
    <div class="ans-body">
        <strong>Definition:</strong> <strong>Normalization</strong> is the systematic process of organizing relation schemas based on functional dependencies to eliminate anomalies and avoid redundant storage.<br>
        <strong>Importance:</strong>
        <ul>
            <li>Eliminates Insertion, Deletion, and Modification anomalies.</li>
            <li>Reduces storage space by ensuring each fact is recorded in only one place.</li>
            <li>Prevents data corruption by enforcing referential integrity constraints across smaller, well-structured tables.</li>
        </ul>
    </div>
</div>

<div class="section-divider">SECTION C &mdash; DETAILED ANSWER QUESTIONS (3 &times; 15 = 45 Marks)</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q9 (15M)</span>Draw an ER Diagram for a small Marketing Company database, assuming your own data requirements.</div>
    <div class="ans-body">
        <strong>Enterprise Requirements:</strong>
        <ul>
            <li><strong>CAMPAIGN:</strong> <u>CampaignID</u>, Title, Budget, StartDate, EndDate.</li>
            <li><strong>CLIENT:</strong> <u>ClientID</u>, ClientName, ContactPerson, Email, Phone.</li>
            <li><strong>PRODUCT:</strong> <u>ProductID</u>, ProductName, Category.</li>
            <li><strong>MARKETING_AGENT:</strong> <u>AgentID</u>, AgentName, CommissionRate.</li>
        </ul>
        <strong>Relationships:</strong>
        <ul>
            <li>A Client commissions one or more Campaigns (1:N).</li>
            <li>Each Campaign promotes one or more Products (M:N).</li>
            <li>Agents are assigned to Campaigns (M:N).</li>
        </ul>
        <div class="diagram-box">
 +------------+        (1)                 (M)        +--------------+
 |   CLIENT   | ------------------------------------ |   CAMPAIGN   |
 | <u>ClientID</u>   |          < COMMISSIONS >             | <u>CampaignID</u>   |
 | ClientName |                                      | Title, Budget|
 +------------+                                      +--------------+
                                                            | (M)
                                                      < PROMOTES >
                                                            | (N)
                                                            v
                                                     +--------------+
                                                     |   PRODUCT    |
                                                     | <u>ProductID</u>    |
                                                     | ProductName  |
                                                     +--------------+
        </div>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q10 (15M)</span>Describe the classification of Database Languages. Which type of language is SQL?</div>
    <div class="ans-body">
        <strong>Classification of Database Languages:</strong>
        <ol>
            <li><strong>Data Definition Language (DDL):</strong> Specifies the database schema, storage structure, and constraints (<code>CREATE</code>, <code>ALTER</code>, <code>DROP</code>, <code>TRUNCATE</code>).</li>
            <li><strong>Data Manipulation Language (DML):</strong> Retrieves, inserts, updates, and deletes stored data. Can be procedural (relational algebra) or non-procedural/declarative (relational calculus, SQL).</li>
            <li><strong>Data Control Language (DCL):</strong> Controls permissions and access authorization (<code>GRANT</code>, <code>REVOKE</code>).</li>
            <li><strong>Transaction Control Language (TCL):</strong> Manages the logical unit of work (<code>COMMIT</code>, <code>ROLLBACK</code>, <code>SAVEPOINT</code>).</li>
        </ol>
        <strong>Classification of SQL:</strong>
        SQL is a <strong>comprehensive declarative (non-procedural) language</strong> that integrates DDL, DML, DCL, and TCL in a single standardized unified language.
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q11 (15M)</span>Explain DDL Commands and DML Commands with complete SQL syntax and executable examples.</div>
    <div class="ans-body">
        <strong>1. DDL Commands (Data Definition Language):</strong>
<pre>
-- 1. CREATE TABLE
CREATE TABLE Student (
    RollNo INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Branch VARCHAR(20) DEFAULT 'BCA',
    FeePaid DECIMAL(10,2) CHECK (FeePaid >= 0)
);

-- 2. ALTER TABLE: Add and modify column
ALTER TABLE Student ADD COLUMN Email VARCHAR(100);
ALTER TABLE Student MODIFY COLUMN Name VARCHAR(80);

-- 3. DROP & TRUNCATE
TRUNCATE TABLE Student; -- Deletes all rows, preserves table structure
DROP TABLE Student;     -- Deletes rows and schema permanently
</pre>
        <strong>2. DML Commands (Data Manipulation Language):</strong>
<pre>
-- 1. INSERT
INSERT INTO Student (RollNo, Name, Branch, FeePaid, Email)
VALUES (101, 'Aman Sharma', 'BCA', 25000.00, 'aman@example.com');

-- 2. UPDATE
UPDATE Student 
SET FeePaid = 30000.00 
WHERE RollNo = 101;

-- 3. DELETE
DELETE FROM Student WHERE RollNo = 101;

-- 4. SELECT
SELECT RollNo, Name, FeePaid FROM Student WHERE Branch = 'BCA';
</pre>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q12 (15M)</span>Explain Data Independence with its types: Physical and Logical Data Independence. Why is it significant?</div>
    <div class="ans-body">
        <strong>Definition:</strong> <strong>Data Independence</strong> is the ability to modify schema definitions at one level of the 3-level ANSI/SPARC architecture without altering schemas at the higher level.<br><br>
        <strong>1. Logical Data Independence:</strong>
        <ul>
            <li>The ability to modify the <strong>Conceptual Schema</strong> (e.g., adding/deleting attributes, splitting tables) without having to rewrite external schemas or existing application programs.</li>
            <li><em>How achieved:</em> Using SQL Views that present the original logical schema to old applications.</li>
            <li><em>Difficulty:</em> Harder to achieve because applications are closely tied to logical data models.</li>
        </ul>
        <strong>2. Physical Data Independence:</strong>
        <ul>
            <li>The ability to modify the <strong>Internal/Physical Schema</strong> (e.g., changing file organizations, building B+ Tree indexes, moving to new storage media) without changing the Conceptual Schema.</li>
            <li><em>Ease:</em> Easier to achieve because logical structure remains completely decoupled from disk-level storage.</li>
        </ul>
    </div>
</div>

<div class="q-box">
    <div class="q-title"><span class="badge">Q13 (15M)</span>Who are Data Administrators (DA)? What are the functions of a Database Administrator (DBA)? Differentiate between DA and DBA.</div>
    <div class="ans-body">
        <strong>Data Administrator (DA) vs Database Administrator (DBA):</strong>
        <table class="grid-table">
            <thead><tr><th>Aspect</th><th>Data Administrator (DA)</th><th>Database Administrator (DBA)</th></tr></thead>
            <tbody>
                <tr><td>Role Level</td><td>Managerial and business level</td><td>Technical and operational level</td></tr>
                <tr><td>Focus</td><td>Business data policies, enterprise data dictionary, data governance.</td><td>Physical database design, database server installation, query tuning, security.</td></tr>
                <tr><td>Scope</td><td>Decides <em>what data</em> needs to be collected across the enterprise.</td><td>Decides <em>how data is stored, indexed, secured, and recovered</em>.</td></tr>
            </tbody>
        </table>
        <strong>Key Functions of DBA:</strong>
        <ol>
            <li>Hardware/software installation and database upgrades.</li>
            <li>Creating database users, granting roles, and monitoring access privileges.</li>
            <li>Performance tuning: Analyzing execution plans, optimizing SQL queries, re-indexing.</li>
            <li>Automating database backups and executing disaster recovery drills.</li>
        </ol>
    </div>
</div>
"""

print("Generating DBMS 2023 PDF...")
generate_dbms_pdf("December 2023", "dbms 2023 solved.pdf", YEAR_2023_HTML)
