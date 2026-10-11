# -*- coding: utf-8 -*-
"""
Master runner to build all DBMS, Java, and Networks PDFs,
and then rebuild the combined Master Book with bookmarks and table of contents.
"""
import os
import subprocess
import pymupdf

def main():
    print("=== STEP 1: Building DBMS Solved Papers ===")
    subprocess.run(["python", r"c:\zzzz\build_all_dbms_papers.py"], check=True)

    print("\n=== STEP 2: Building Java Solved Papers ===")
    subprocess.run(["python", r"c:\zzzz\build_all_java_papers.py"], check=True)

    print("\n=== STEP 3: Building Computer Networks Solved Papers ===")
    subprocess.run(["python", r"c:\zzzz\build_all_networks_papers.py"], check=True)

    print("\n=== STEP 4: Recompiling Master Solved PYQ Book ===")
    target_dir = r"c:\zzzz\solved pyq"
    master_path = os.path.join(target_dir, "CCSU_BCA_5_SEM_ALL_SUBJECTS_SOLVED_MASTER_BOOK.pdf")
    
    subjects = [
        ("BCA-501: Data Base Management System", os.path.join(target_dir, "BCA-501_Introduction_to_DBMS_Solved_PYQ.pdf")),
        ("BCA-502: Java Programming & Web Design", os.path.join(target_dir, "BCA-502_Java_and_Webpage_Design_Solved_PYQ.pdf")),
        ("BCA-503: Computer Networks", os.path.join(target_dir, "BCA-503_Computer_Networks_Solved_PYQ.pdf")),
        ("BCA-504: Numerical Methods", os.path.join(target_dir, "BCA-504_Numerical_Methods_Solved_PYQ.pdf")),
    ]

    doc = pymupdf.open()
    toc = []
    page_num = 1
    for title, path in subjects:
        if os.path.exists(path):
            sub_doc = pymupdf.open(path)
            toc.append([1, title, page_num])
            doc.insert_pdf(sub_doc)
            page_num += len(sub_doc)
            sub_doc.close()
            print(f"[+] Appended {title} ({len(sub_doc)} pages)")
        else:
            print(f"[-] Missing: {path}")

    doc.set_toc(toc)
    doc.save(master_path, garbage=4, deflate=True)
    doc.close()
    print(f"\n[OK] Master Book successfully generated at: {master_path}")
    print(f"Total Master Book Pages: {page_num - 1}, Size: {os.path.getsize(master_path)/1024:.1f} KB")

if __name__ == "__main__":
    main()
