# PDF 파일에 있는 텍스트를 추출하여 txt 파일로 저장
# 단, 중간의 페이지 번호와 학회지 이름 등 페이지 헤더와 푸터는 제외(전처리 과정)
import pymupdf
import os

pdf_file_path = "chap04/data/과정기반 작물모형을 이용한 웹 기반 밀 재배관리 의사결정 지원시스템 설계 및 구축.pdf"
doc = pymupdf.open(pdf_file_path)

# 헤더와 푸터 높이를 설정하여, page.rect를 사용해 확인한 후 폭(rect.width)과 높이(rect.height)를 이용해 텍스트를 추출할 영역을 clip 으로 지정
header_height = 80
footer_height = 80

full_text = ''

for page in doc: # 문서 페이지 반복하면서 텍스트 추출
    rect = page.rect # 페이지 크기 가져오기
    
    header = page.get_text(clip=(0, 0, rect.width , header_height))
    footer = page.get_text(clip=(0, rect.height - footer_height, rect.width , rect.height))
    text = page.get_text(clip=(0, header_height, rect.width , rect.height - footer_height))

    full_text += text + '\n------------------------------------\n'

pdf_file_name = os.path.basename(pdf_file_path) # PDF -> txt 로 변환하기 위해 파일 이름 추출
pdf_file_name = os.path.splitext(pdf_file_name)[0] # 확장자 제거

txt_file_path = f'chap04/output/{pdf_file_name}_with_preprocessing.txt'

with open(txt_file_path, 'w', encoding='utf-8') as f:
    f.write(full_text)
