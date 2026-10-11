import urllib.request
import re
import os
import time

url = "https://www.ccsustudy.com/ccsu-bca-papers.html"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')

matches = re.findall(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', html, re.DOTALL | re.IGNORECASE)

base_dir = r"c:\zzzz\CCSU_BCA_5_SEM_PYQ"
os.makedirs(base_dir, exist_ok=True)

subject_folders = {
    "18021": "BCA-501_Introduction_to_DBMS",
    "dbms": "BCA-501_Introduction_to_DBMS",
    "18022": "BCA-502_Java_Programming_and_Dynamic_Webpage_Design",
    "java": "BCA-502_Java_Programming_and_Dynamic_Webpage_Design",
    "18023": "BCA-503_Computer_Networks",
    "network": "BCA-503_Computer_Networks",
    "18024": "BCA-504_Numerical_Methods",
    "numerical": "BCA-504_Numerical_Methods"
}

for folder in set(subject_folders.values()):
    os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

seen_pdfs = set()
download_list = []

for href, text in matches:
    clean_text = re.sub(r'<[^>]+>', '', text).strip()
    href_lower = href.lower()
    text_lower = clean_text.lower()
    
    is_sem5 = ('bca-5-sem' in href_lower or 'bca-5-sem' in text_lower or 
               '18021' in href_lower or '18022' in href_lower or '18023' in href_lower or '18024' in href_lower)
               
    if is_sem5 and href_lower.endswith('.html') and '/papers/' in href_lower:
        pdf_url = href.rsplit('.html', 1)[0] + '.pdf'
        filename = pdf_url.split('/')[-1]
        
        if filename in seen_pdfs:
            continue
        seen_pdfs.add(filename)
        
        # Determine subject folder
        target_folder = None
        for key, folder_name in subject_folders.items():
            if key in filename.lower() or key in text_lower:
                target_folder = folder_name
                break
        
        if not target_folder:
            target_folder = "Other_BCA_5_Sem"
            os.makedirs(os.path.join(base_dir, target_folder), exist_ok=True)
            
        download_list.append((pdf_url, target_folder, filename, clean_text))

print(f"Total unique papers to download: {len(download_list)}")

success_count = 0
failed = []

for idx, (pdf_url, folder, filename, title) in enumerate(download_list, 1):
    dest_path = os.path.join(base_dir, folder, filename)
    print(f"[{idx}/{len(download_list)}] Downloading {filename} -> {folder}...")
    try:
        r = urllib.request.Request(pdf_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(r, timeout=25) as response:
            content = response.read()
            if content.startswith(b'%PDF'):
                with open(dest_path, 'wb') as f:
                    f.write(content)
                size_kb = len(content) / 1024
                print(f"   Success ({size_kb:.1f} KB)")
                success_count += 1
            else:
                print(f"   Warning: Content does not look like PDF (starts with {content[:15]})")
                failed.append((filename, "Not a valid PDF header"))
    except Exception as e:
        print(f"   Error downloading {filename}: {e}")
        failed.append((filename, str(e)))
    time.sleep(0.3)

print("\n" + "="*50)
print(f"Summary: Successfully downloaded {success_count}/{len(download_list)} papers.")
if failed:
    print(f"Failed ({len(failed)}):")
    for fn, err in failed:
        print(f" - {fn}: {err}")
