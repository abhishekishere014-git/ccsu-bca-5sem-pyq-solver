import asyncio
import os
import re
import json
import pymupdf
import winsdk.windows.media.ocr as ocr
import winsdk.windows.graphics.imaging as imaging
import winsdk.windows.storage as storage

base_pyq = r"c:\zzzz\CCSU_BCA_5_SEM_PYQ"
cache_file = r"c:\zzzz\ocr_extracted_questions.json"
temp_img = r"c:\zzzz\ocr_temp_page.png"

engine = ocr.OcrEngine.try_create_from_user_profile_languages()

async def ocr_page(img_path):
    f = await storage.StorageFile.get_file_from_path_async(img_path)
    s = await f.open_async(storage.FileAccessMode.READ)
    d = await imaging.BitmapDecoder.create_async(s)
    b = await d.get_software_bitmap_async()
    res = await engine.recognize_async(b)
    return [l.text for l in res.lines]

async def process_all():
    extracted_data = {}
    
    for subj_dir in sorted(os.listdir(base_pyq)):
        subj_path = os.path.join(base_pyq, subj_dir)
        if not os.path.isdir(subj_path):
            continue
            
        print(f"=== Scanning {subj_dir} ===")
        for fname in sorted(os.listdir(subj_path)):
            if not fname.endswith(".pdf") or fname.startswith("MERGED"):
                continue
                
            pdf_path = os.path.join(subj_path, fname)
            doc = pymupdf.open(pdf_path)
            all_text_lines = []
            
            for p_idx, page in enumerate(doc):
                pix = page.get_pixmap(dpi=150)
                pix.save(temp_img)
                lines = await ocr_page(temp_img)
                all_text_lines.extend(lines)
                
            extracted_data[fname] = all_text_lines
            print(f"  {fname}: {len(all_text_lines)} lines extracted across {len(doc)} pages")
            
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=2)
    print(f"\nAll papers OCR'd and saved to {cache_file}!")

asyncio.run(process_all())
