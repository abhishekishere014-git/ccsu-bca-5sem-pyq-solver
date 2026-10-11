## Section - A (Very Short Answer Questions — 3 Marks Each, All 5 Mandatory)

### Q1. Define Database Management System (DBMS) and its fundamental purpose.
**Answer:**
A **Database Management System (DBMS)** is system software that enables users to create, maintain, query, and administer structured databases. It acts as an interface between application software and physical storage, ensuring controlled redundancy, data consistency, security, and multi-user concurrent access.

---

### Q2. Distinguish between Simple and Composite Attributes with examples.
**Answer:**
- **Simple (Atomic) Attribute:** Cannot be divided into smaller sub-components (e.g., `Roll_Number`, `Age`, `Gender`).
- **Composite Attribute:** Can be logically divided into smaller, independent sub-attributes (e.g., `Full_Name` divided into `First_Name`, `Middle_Name`, `Last_Name`; `Address` into `Street`, `City`, `State`, `Pincode`).

---

### Q3. Explain Referential Integrity Constraint.
**Answer:**
Referential Integrity requires that a foreign key value in a referencing relation must match an existing primary key value in the referenced relation, or otherwise be `NULL`. It prevents orphan records when parent rows are updated or deleted (managed via `ON DELETE CASCADE` or `ON DELETE SET NULL`).

---

### Q4. Differentiate between DDL and DML commands with syntax.
**Answer:**
- **DDL (Data Definition Language):** Defines and alters database schema structures. Statements auto-commit (e.g., `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, `TRUNCATE`).
- **DML (Data Manipulation Language):** Manages data stored within relations (e.g., `INSERT INTO table VALUES (...)`, `UPDATE table SET ...`, `DELETE FROM table WHERE ...`). Can be rolled back via TCL.

---

### Q5. Explain Functional Dependency (FD) and Multivalued Dependency (MVD).
**Answer:**
- **Functional Dependency (X -> Y):** For any two tuples having identical values for attribute set X, their values for attribute set Y must also be identical.
- **Multivalued Dependency (X ->-> Y):** Given a tuple, attribute set Y depends only on X and is completely independent of other attributes in the relation. MVD leads to 4NF decomposition.

---

## Section - B (Short Answer Questions — 7.5 Marks Each, Attempt Any Two)

### Q6. Discuss Anomalies associated with Relational Database (Insertion, Deletion, Update).
**Answer:**
1. **Insertion Anomaly:** Inability to record certain entity data without improperly recording unrelated data (e.g., cannot add a new course until a student enrolls).
2. **Deletion Anomaly:** Deleting one piece of data causes unintentional loss of critical unrelated data (e.g., deleting the last student in a department deletes the department itself).
3. **Update / Modification Anomaly:** When duplicate redundant copies exist, updating one copy while missing another causes conflicting inconsistent states.

---

### Q7. Explain Super Key, Candidate Key, and Primary Key with suitable examples.
**Answer:**
Consider `Student(RollNo, RegNo, Email, Name, Age)`:
- **Super Key:** Any set of attributes that uniquely identifies a row (e.g., `{RollNo}`, `{RegNo}`, `{RollNo, Name}`).
- **Candidate Key:** A minimal Super Key containing no redundant attributes (e.g., `{RollNo}`, `{RegNo}`, `{Email}`).
- **Primary Key:** The single candidate key chosen by the database designer as the principal unique identifier (`{RollNo}`). Cannot contain `NULL`.

---

### Q8. What is Normalization? Explain Second Normal Form (2NF) and Third Normal Form (3NF).
**Answer:**
Normalization decomposes relations to reduce redundancy and avoid anomalies:
- **2NF:** Relation is in 1NF and contains **no partial dependencies** (every non-prime attribute depends on the whole candidate key, not a proper subset).
- **3NF:** Relation is in 2NF and contains **no transitive dependencies** (X -> Y requires X is a superkey or Y is a prime attribute).

---

## Section - C (Long Answer Questions — 15 Marks Each, Attempt Any Three)

### Q9. Define Boyce-Codd Normal Form (BCNF). Compare 3NF and BCNF with a suitable example.
**Answer:**
**BCNF Definition:** A relation is in BCNF if for every non-trivial functional dependency X -> Y, **X MUST be a Super Key**.
**Key Distinction:** In 3NF, X -> Y is valid if Y is a prime attribute even when X is not a super key. In BCNF, this is strictly disallowed.
- *Example:* Relation `StudentAdvisor(StudentID, Subject, Advisor)` where:
  - `(StudentID, Subject) -> Advisor`
  - `Advisor -> Subject`
  - Keys: `(StudentID, Subject)` and `(StudentID, Advisor)`.
  - In 3NF: `Advisor -> Subject` is valid because `Subject` is a prime attribute.
  - In BCNF: `Advisor` is not a super key, so table must be decomposed into `(Advisor, Subject)` and `(StudentID, Advisor)`.

---

### Q10. Explain Relational Algebra Fundamental Operations with examples.
**Answer:**
1. **Selection (sigma):** Filters rows meeting predicate: `sigma_{Marks > 75}(Student)`.
2. **Projection (pi):** Filters columns and drops duplicates: `pi_{Name, RollNo}(Student)`.
3. **Cartesian Product (x):** Combines every tuple from R with every tuple from S: `R x S`.
4. **Union (U):** Combines unique tuples from two union-compatible relations.
5. **Set Difference (-):** Tuples in R but not in S.
6. **Rename (rho):** Renames relation or attributes: `rho_{S}(R)`.
7. **Natural Join (|><|):** Combines Cartesian product and equality selection on common attributes.

---

### Q11. Explain SQL Characteristics and Five Aggregate Functions with SQL queries.
**Answer:**
SQL is a non-procedural declarative query language.
**Five Core Aggregate Functions:**
1. `COUNT()`: Counts number of rows matching criteria:
   `SELECT COUNT(*) FROM Employee WHERE Dept = 'IT';`
2. `SUM()`: Calculates total sum of numeric column:
   `SELECT SUM(Salary) FROM Employee;`
3. `AVG()`: Calculates average value:
   `SELECT AVG(Salary) FROM Employee;`
4. `MIN()`: Finds minimum value:
   `SELECT MIN(Salary) FROM Employee;`
5. `MAX()`: Finds maximum value:
   `SELECT MAX(Salary) FROM Employee;`

---

### Q12. Explain Concurrency Control and Two-Phase Locking (2PL) Protocol with its pitfalls.
**Answer:**
Concurrency control ensures database consistency when multiple transactions execute simultaneously.
**Two-Phase Locking (2PL):**
1. **Growing Phase:** Transaction acquires shared/exclusive locks but cannot release any.
2. **Shrinking Phase:** Transaction releases locks but cannot acquire any new ones.
**Pitfalls:**
- Can lead to **Cascading Aborts** (prevented by *Strict 2PL*).
- Does not prevent **Deadlocks** (two transactions each waiting for locks held by the other). Resolved using Wait-For Graphs or Timestamping (Wait-Die / Wound-Wait).

---

### Q13. Write detailed notes on: (a) Three-Schema Architecture, (b) Data Independence, and (c) Role of DBA.
**Answer:**
**(a) Three-Schema Architecture:**
- Physical Level: Internal file storage, indexes, clustering.
- Conceptual / Logical Level: Community view of tables, columns, relations.
- External / View Level: Individual user/application custom views.

**(b) Data Independence:**
- Physical Data Independence: Altering disk storage/indexes does not affect logical tables.
- Logical Data Independence: Adding/altering tables does not affect external views.

**(c) Database Administrator (DBA):**
- Schema definition, physical access methods, security authorization, performance monitoring, routine backups, and crash disaster recovery.
