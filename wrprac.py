# 카카오톡 > 대화내용 > 대화내용 보내기 > 저장하고 opne('')사이에 넣기



from wordcloud import WordCloud
from PIL import Image
import numpy as np

text = ''
with open("KakaoTalk_.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if '] [' in line : #'] [' 이것이 있을 때
            text += line.split('] ')[2].replace('사진\n', '').replace('이모티콘\n', '').replace('삭제된 메시지입니다.\n', '')
# '] ' 걸 기준으로 3번째 ...... 사진과 이모티콘은 제거거



mask = np.array(Image.open('heart.png')) # 모양 이미지 주소
wc = WordCloud(font_path='C:/WINDOWS/Fonts/H2GTRM.TTF', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")#이 파일에 저장
