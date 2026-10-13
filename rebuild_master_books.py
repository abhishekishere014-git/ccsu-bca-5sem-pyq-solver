import os
import re
import pymupdf
import shutil

SOLVED_DIR = r"c:\zzzz\solved pyq"
PDFS_DIR = r"c:\zzzz\pyq_solver_scripts\pdfs"

subjects = [
    {
        "name": "BCA-501: Introduction to DBMS",
        "folder": os.path.join(SOLVED_DIR, "BCA-501_DBMS"),
        "prefix": "dbms",
        "output_name": "BCA-501_Introduction_to_DBMS_Solved_PYQ.pdf"
    },
    {
        "name": "BCA-502: Java Programming & Dynamic Webpage Design",
        "folder": os.path.join(SOLVED_DIR, "BCA-502_Java"),
        "prefix": "java",
        "output_name": "BCA-502_Java_and_Webpage_Design_Solved_PYQ.pdf"
    },
    {
        "name": "BCA-503: Computer Networks",
        "folder": os.path.join(SOLVED_DIR, "BCA-503_Networks"),
        "prefix": "networks",
        "output_name": "BCA-503_Computer_Networks_Solved_PYQ.pdf"
    },
    {
        "name": "BCA-504: Numerical Methods",
        "folder": os.path.join(SOLVED_DIR, "BCA-504_Numerical_Methods"),
        "prefix": "numerical methods",
        "output_name": "BCA-504_Numerical_Methods_Solved_PYQ.pdf"
    }
]

def extract_year(fn):
    m = re.search(r'(20\d\d)', fn)
    return int(m.group(1)) if m else 0

subject_master_paths = []

for sub in subjects:
    folder = sub["folder"]
    prefix = sub["prefix"]
    out_name = sub["output_name"]
    
    # Get all yearly solved PDFs
    files = [f for f in os.listdir(folder) if f.startswith(prefix) and f.endswith(".pdf")]
    # Sort chronologically (oldest to newest)
    files_sorted = sorted(files, key=extract_year)
    
    print(f"\nBuilding Subject Book: {sub['name']} ({len(files_sorted)} papers)...")
    merged_doc = pymupdf.open()
    toc = []
    current_page = 1
    
    for f in files_sorted:
        yr = extract_year(f)
        fpath = os.path.join(folder, f)
        doc = pymupdf.open(fpath)
        toc.append([1, f"Year {yr} Solved Paper ({len(doc)} pages)", current_page])
        merged_doc.insert_pdf(doc)
        current_page += len(doc)
        doc.close()
        print(f"  + Added {f} ({yr})")
        
    merged_doc.set_toc(toc)
    dest_path1 = os.path.join(folder, out_name)
    dest_path2 = os.path.join(PDFS_DIR, out_name)
    # Also in solved pyq root
    dest_path3 = os.path.join(SOLVED_DIR, out_name)
    
    merged_doc.save(dest_path1, garbage=4, deflate=True)
    merged_doc.close()
    shutil.copy2(dest_path1, dest_path2)
    shutil.copy2(dest_path1, dest_path3)
    
    subject_master_paths.append((sub["name"], dest_path1))
    print(f"  [OK] Saved {out_name}: {current_page - 1} pages, {os.path.getsize(dest_path1)/1024:.1f} KB")

# Compile Mega Master Book
print("\n=== Compiling CCSU BCA 5 SEM ALL SUBJECTS SOLVED MASTER BOOK ===")
mega_doc = pymupdf.open()
mega_toc = []
page_count = 1

for sub_title, sub_path in subject_master_paths:
    doc = pymupdf.open(sub_path)
    sub_toc = doc.get_toc()
    mega_toc.append([1, sub_title, page_count])
    # Add child bookmarks
    for item in sub_toc:
        level, title, pnum = item
        mega_toc.append([level + 1, title, page_count + pnum - 1])
    mega_doc.insert_pdf(doc)
    print(f"  + Merged {sub_title} ({len(doc)} pages)")
    page_count += len(doc)
    doc.close()

mega_doc.set_toc(mega_toc)
mega_out1 = os.path.join(SOLVED_DIR, "Master_Book", "CCSU_BCA_5_SEM_ALL_SUBJECTS_SOLVED_MASTER_BOOK.pdf")
os.makedirs(os.path.join(SOLVED_DIR, "Master_Book"), exist_ok=True)
mega_out2 = os.path.join(PDFS_DIR, "CCSU_BCA_5_SEM_ALL_SUBJECTS_SOLVED_MASTER_BOOK.pdf")
mega_out3 = os.path.join(SOLVED_DIR, "CCSU_BCA_5_SEM_ALL_SUBJECTS_SOLVED_MASTER_BOOK.pdf")

mega_doc.save(mega_out1, garbage=4, deflate=True)
mega_doc.close()
shutil.copy2(mega_out1, mega_out2)
shutil.copy2(mega_out1, mega_out3)

print(f"\n[ALL DONE] Mega Master Book successfully created!")
print(f"Total Pages: {page_count - 1}, File Size: {os.path.getsize(mega_out1)/(1024*1024):.2f} MB")
