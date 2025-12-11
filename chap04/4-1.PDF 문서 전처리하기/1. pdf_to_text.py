# pip install PyMuPDF
# PDF 파일에 있는 텍스트를 추출하여 txt 파일로 저장
import pymupdf
import os

pdf_file_path = "chap04/data/과정기반 작물모형을 이용한 웹 기반 밀 재배관리 의사결정 지원시스템 설계 및 구축.pdf"
doc = pymupdf.open(pdf_file_path)

full_text = ''

for page in doc: # 문서 페이지 반복하면서 텍스트 추출
    text = page.get_text()
    full_text += text

pdf_file_name = os.path.basename(pdf_file_path)    # PDF -> txt 로 변환하기 위해 파일 이름 추출
pdf_file_name = os.path.splitext(pdf_file_name)[0] # 확장자 제거

txt_file_path = f"chap04/output/{pdf_file_name}.txt" # output 폴더에 텍스트 파일 형식으로 저장
with open(txt_file_path, 'w', encoding='utf-8') as f:
    f.write(full_text)
