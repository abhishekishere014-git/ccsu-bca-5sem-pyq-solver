# CCSU BCA 5th Semester PYQ Solver & PDF Generator Pipeline

> 🌐 **Live Web Portal:** [https://abhishekishere014-git.github.io/ccsu-bca-5sem-pyq-solver/](https://abhishekishere014-git.github.io/ccsu-bca-5sem-pyq-solver/)  
> 📖 Access all solved past year questions (2013–2025) across BCA-501, 502, 503 & 504 with instant search, section filters, and in-browser PDF previews!

[![GitHub Pages Deployment](https://img.shields.io/badge/GitHub%20Pages-Live%20Online-brightgreen?style=for-the-badge&logo=github)](https://abhishekishere014-git.github.io/ccsu-bca-5sem-pyq-solver/)
[![Repository](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/abhishekishere014-git/ccsu-bca-5sem-pyq-solver)

An automated suite of Python scripts and templates designed to download, OCR-extract, solve, format, and generate publication-quality examination papers for **Chaudhary Charan Singh University (CCSU)**, Meerut — **Bachelor of Computer Applications (BCA) 5th Semester**.

---

## 📚 Subjects Covered

| Course Code | Subject Name | Paper Code | Solved Exam Sessions |
| :--- | :--- | :---: | :---: |
| **BCA-501** | Introduction to DBMS | 18021 | 2013 &ndash; 2025 (12 Years) |
| **BCA-502** | Java Programming & Dynamic Webpage Design | 18022 | 2016 &ndash; 2025 (9 Years) |
| **BCA-503** | Computer Networks | 18023 | 2016 &ndash; 2025 (9 Years) |
| **BCA-504** | Numerical Methods | 18024 | 2018 &ndash; 2024 (7 Years) |

Every generated paper includes all **13 examination questions**:
- **Section A:** Q1 to Q5 (3 Marks each &bull; All 5 compulsory)
- **Section B:** Q6 to Q8 (7.5 Marks each &bull; Attempt any 2)
- **Section C:** Q9 to Q13 (15 Marks each &bull; Attempt any 3)

---

## 🛠️ Pipeline Architecture & Scripts

```
pyq_solver_scripts/
│
├── 1. Downloader & Scraper
│   └── download_pyqs.py                   # Automated downloader from ccsustudy.com
│
├── 2. PDF Merger
│   └── merge_pyqs.py                      # Merges papers subject-wise with bookmarks
│
├── 3. OCR Extraction
│   └── extract_all_questions_ocr.py       # High-accuracy OCR using Windows Media OCR (winsdk)
│
├── 4. Subject-Wise Builders
│   ├── build_all_dbms_papers.py           # DBMS papers (relational algebra, normal forms)
│   ├── build_all_java_papers.py           # Java papers (syntax-highlighted code, JVM architecture)
│   ├── build_all_networks_papers.py       # Networks papers (OSI 7-layer stack, Shannon capacity)
│   └── build_all_numerical_methods_papers.py # Numerical Methods (fractions, matrices, iteration tables)
│
├── 5. Master Book Compiler & Helpers
│   ├── build_all_subjects_and_master.py   # Master runner compiling all subjects & 27-page book
│   └── pdf_complete_helper.py             # Headless Chrome PDF printing utility
│
└── 6. Solution Source Markdowns
    ├── complete_dbms_solution.md
    ├── complete_java_solution.md
    ├── complete_networks_solution.md
    └── complete_numerical_solution.md
```

---

## 🎨 Advanced Formatting Highlights

1. **Numerical Methods (BCA-504):**
   - **Cambria Math & Inter** typography.
   - Vertically aligned fractional expressions (`<span class="frac">`).
   - Bracketed linear system matrices with dashed partition lines.
   - Alternating row-shaded numerical iteration tables (Bisection, False Position, Gauss-Seidel, Simpson's Rules).

2. **DBMS (BCA-501):**
   - Exact Relational Algebra mathematical notation ($\sigma, \pi, \times, \cup, -, \rho, \bowtie$).
   - Proper functional dependency arrows ($X \to Y$ and $X \twoheadrightarrow Y$).
   - Normalization comparisons (1NF, 2NF, 3NF, BCNF) and ANSI/SPARC 3-schema architecture breakdown.

3. **Java Programming (BCA-502):**
   - Dark-themed syntax containers for multi-line Java programs.
   - JVM subsystem architecture breakdowns (ClassLoader, Runtime Data Areas, Execution Engine/JIT/GC).
   - Applet & Servlet life-cycle transition flows.

4. **Computer Networks (BCA-503):**
   - TCP 3-Way Handshake step-by-step sequence exchange.
   - Complete 7-layer ISO/OSI reference stack with PDU, functions, and protocols.
   - Shannon Capacity Theorem formula and step-by-step $34.88\text{ kbps}$ calculation.

---

## 🚀 Setup & Execution

### Prerequisites
- Python 3.10+
- Google Chrome (installed at standard path `C:\Program Files\Google\Chrome\Application\chrome.exe`)

### Install Dependencies
```bash
pip install pymupdf winsdk markdown
```

### Run the Pipeline
```bash
# Build all subjects and compile the Master Solved PYQ Book:
python build_all_subjects_and_master.py

# Or build individual subjects:
python build_all_numerical_methods_papers.py
python build_all_dbms_papers.py
python build_all_java_papers.py
python build_all_networks_papers.py
```
