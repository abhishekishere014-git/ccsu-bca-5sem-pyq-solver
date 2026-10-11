import os
import re
from pypdf import PdfWriter, PdfReader

base_dir = r"c:\zzzz\CCSU_BCA_5_SEM_PYQ"

def get_sort_key(filename):
    # Extract year (e.g. 2025)
    m = re.search(r'(20\d\d)', filename)
    year = int(m.group(1)) if m else 9999
    # Check if cv3 or special
    has_cv3 = 'cv3' in filename.lower()
    return (year, has_cv3, filename)

def generate_bookmark_title(filename):
    # e.g. bca-5-sem-introduction-to-dbms-18021-dec-2024.pdf -> Dec 2024 (18021)
    m_year = re.search(r'(20\d\d)', filename)
    year = m_year.group(1) if m_year else ""
    
    m_month = re.search(r'(dec|nov|may|june|jan|feb|mar|apr|jul|aug|sep|oct)', filename.lower())
    month = m_month.group(1).upper() if m_month else ""
    
    extra = " [Special/CV3]" if "cv3" in filename.lower() else ""
    
    title = f"{month} {year}{extra}".strip()
    if not title:
        title = filename
    return title

subjects = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

summary = {}

for subj in sorted(subjects):
    subj_path = os.path.join(base_dir, subj)
    pdf_files = [f for f in os.listdir(subj_path) if f.lower().endswith('.pdf') and not f.startswith('MERGED_')]
    
    # Sort chronologically (oldest to newest or newest to oldest? Let's sort chronological: e.g. 2013 -> 2025)
    pdf_files_sorted = sorted(pdf_files, key=get_sort_key)
    
    merger = PdfWriter()
    merged_info = []
    
    current_page = 0
    for pdf_file in pdf_files_sorted:
        full_path = os.path.join(subj_path, pdf_file)
        try:
            reader = PdfReader(full_path)
            num_pages = len(reader.pages)
            bookmark_title = generate_bookmark_title(pdf_file)
            
            # Append pages
            merger.append(reader, outline_item=bookmark_title)
            
            merged_info.append({
                'file': pdf_file,
                'title': bookmark_title,
                'pages': num_pages,
                'start_page': current_page + 1
            })
            current_page += num_pages
        except Exception as e:
            print(f"Error reading {pdf_file}: {e}")
            
    output_filename = f"MERGED_{subj}_PYQ.pdf"
    output_path = os.path.join(subj_path, output_filename)
    # Also save a copy directly in base_dir for quick access!
    base_output_path = os.path.join(base_dir, output_filename)
    
    with open(output_path, "wb") as f_out:
        merger.write(f_out)
    with open(base_output_path, "wb") as f_out:
        merger.write(f_out)
        
    summary[subj] = {
        'total_papers': len(merged_info),
        'total_pages': current_page,
        'output_path': base_output_path,
        'papers': merged_info
    }
    print(f"Merged {subj}: {len(merged_info)} papers, {current_page} pages -> {output_filename}")

print("\nAll merges complete!")
