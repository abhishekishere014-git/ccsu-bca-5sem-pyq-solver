# 🎓 CCSU BCA 5th Semester — Solved PYQ Portal & Master Question Bank

<div align="center">

[![Live Web Portal](https://img.shields.io/badge/Live%20Web%20Portal-Online%20Demo-38BDF8?style=for-the-badge&logo=githubpages&logoColor=white)](https://abhishekraaj07.github.io/ccsu-bca-5sem-pyq-solver/)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-10B981?style=for-the-badge&logo=github&logoColor=white)](https://github.com/abhishekraaj07/ccsu-bca-5sem-pyq-solver)
[![Status](https://img.shields.io/badge/Status-Complete%20%26%20Verified-blue?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)]()

<br>

> 🌐 **Live Web Application:** [https://abhishekraaj07.github.io/ccsu-bca-5sem-pyq-solver/](https://abhishekraaj07.github.io/ccsu-bca-5sem-pyq-solver/)  
> 📖 Access the complete deduplicated question bank (2013–2025) across DBMS, Java, Computer Networks, and Numerical Methods with exam-style step-by-step solutions, live search, section filters, and instant PDF downloads!

</div>

---

## 🌟 Key Highlights

- **🎯 Zero Duplicates (Cluster-Deduplicated):** All 43 CCSU past year papers (2013–2025) were clustered, removing repeated questions while marking exact repetition frequency (e.g., *Repeated 4× &bull; 2025, 2021, 2018, 2013*).
- **📝 Exam-Style Long Answers:** Every question includes standard textbook definitions, practical examples, architecture diagrams, and step-by-step derivations aligned with university marking schemes.
- **📊 Numerical Methods with Tables & Step Boxes:** Bisection, Regula-Falsi, Gauss-Seidel, Runge-Kutta 4th order, Finite Differences, and Interpolations feature full tabular iterations and signature glowing blue formula badges.
- **💻 Strict Subject Isolation:** Switching between DBMS, Java, Networks, and Numerical Methods shows strictly that subject's content with zero bleed-over.
- **📄 Complete 43 Verified PDFs:** All year-wise solved papers plus a comprehensive 4.4 MB Master Question Bank PDF (`BCA5_Question_Bank.pdf`).
- **🌓 Dark & Light Modes:** Seamless transition between dark and light themes with high-contrast typography and syntax highlighting.

---

## 📚 Subject Breakdown & Statistics

| Subject Code | Subject Name | Paper Code | Exam Years | Section C (15M) | Section B (7.5M) | Section A (3M) | Total Questions |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **BCA-501** | Introduction to DBMS | 18021 | 2013 – 2025 (12 Years) | 38 | 19 | 23 | **80** |
| **BCA-502** | Java Programming & Web Design | 18022 | 2016 – 2025 (9 Years) | 22 | 7 | 21 | **50** |
| **BCA-503** | Computer Networks | 18023 | 2016 – 2025 (9 Years) | 13 | 10 | 25 | **48** |
| **BCA-504** | Numerical Methods | 18024 | 2018 – 2024 (7 Years) | 16 | 9 | 8 | **33** |
| **TOTAL** | **All 4 Core Subjects** | — | **43 Papers Solved** | **89** | **45** | **77** | **211** |

---

## 🗂️ Project Architecture

```text
ccsu-bca-5sem-pyq-solver/
│
├── index.html                           # Single-page web portal application
├── data.js                              # Standalone bundled dataset (352 KB)
│
├── pdfs/                                # Directory containing 43 verified PDFs
│   ├── BCA5_Question_Bank.pdf           # Comprehensive 211-question master PDF (4.41 MB)
│   ├── BCA501_DBMS.pdf                  # Complete DBMS solved bank
│   ├── BCA502_Java.pdf                  # Complete Java solved bank
│   ├── BCA503_Networks.pdf              # Complete Networks solved bank
│   ├── BCA504_Numerical.pdf             # Complete Numerical Methods solved bank
│   └── [40+ Year-wise Solved PDFs]      # Individual solved paper PDFs (2013-2025)
│
├── build_full_web_dedup_data.py         # Main compilation script generating data.js
├── generate_dedup_master_qbank.py       # Clustering and deduplication engine
│
├── enrich_dbms.py                       # Enriched exam solutions for DBMS
├── enrich_java.py                       # Enriched exam solutions for Java
├── enrich_networks.py                   # Enriched exam solutions for Networks
├── enrich_nm_complete.py                # Enriched exam solutions for Numerical Methods
└── enrich_all_remaining.py              # Extended subject enrichments
```

---

## 🔬 Numerical Methods (BCA-504) Formatting Standards

1. **Tabular Iteration Matrices (`<table class="grid-table">`):**
   - **Bisection & Regula-Falsi:** Multi-step convergence tables with midpoint, functional evaluations, and signs.
   - **Gauss-Seidel:** Step-by-step vector convergence tables (`x^(k)`, `y^(k)`, `z^(k)`).
   - **Runge-Kutta 4th Order (RK4):** Structured slope evaluations (`k₁`, `k₂`, `k₃`, `k₄`).
   - **Difference Tables:** Centered columns for Forward, Backward, Divided, Gauss Central, Stirling, and Bessel differences.
2. **Formula & Step Containers (`<div class="step-box">`, `<div class="math-box">`):**
   - Distinct callouts separating problem setup, recurrence formulas, and algebraic derivations.
3. **Glowing Badges (`.math-expr`, `code`):**
   - Distinctive neon-accented inline code and formula badges.
4. **Boxed Final Answers (`<div class="result-box">`):**
   - High-visibility green/cyan boxes stating final numerical answers and percentage error bounds.

---

## 🚀 Running Locally

### 1. Clone the Repository
```bash
git clone https://github.com/abhishekraaj07/ccsu-bca-5sem-pyq-solver.git
cd ccsu-bca-5sem-pyq-solver
```

### 2. View the Web Portal
No build tools or Node.js dependencies are required! Simply open `index.html` in any modern web browser or start a lightweight local server:

```bash
# Python 3
python -m http.server 8000
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

### 3. Rebuild Dataset (Optional)
If you modify any enrichment files or add new papers:
```bash
python build_full_web_dedup_data.py
```
This regenerates `data.js` containing all clustered questions and exam-style solutions.

---

## 📜 University Exam Paper Pattern

Every CCSU BCA paper follows the standard 75-mark structure:
- **Section A (Very Short Answer):** 5 questions &times; 3 marks = **15 Marks** *(Compulsory)*
- **Section B (Short Answer):** Attempt any 2 out of 3 questions &times; 7.5 marks = **15 Marks**
- **Section C (Detailed / Long Answer):** Attempt any 3 out of 5 questions &times; 15 marks = **45 Marks**
- **Grand Total:** **75 Marks** (External) + 25 Marks (Internal) = 100 Marks per course.

---

## 👨‍💻 Author & Contributions

- **Developer:** [Abhishek Raaj (@abhishekraaj07)](https://github.com/abhishekraaj07)
- **Open Source:** Contributions and improvements are welcome via pull requests.

---

<div align="center">

⭐ **Star this repository if you find it helpful for exam preparation!** ⭐

</div>
