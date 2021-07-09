#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-07-07
#-------------------------------------------------------------------------------

"""
이미 다른 버전의 googletrans를 설치했었다면
이것을 아래와 같이 삭제한 후

> pip uninstall googletrans

최신 버전을 설치해야 한다.

> pip install googletrans==4.0.0-rc1

"""

import googletrans

translator = googletrans.Translator()
str1 = "나는 한국인 입니다."
str2 = "I like burger."
result1 = translator.translate(str1, dest='en')
result2 = translator.translate(str2, dest='ko')
print(f"나는 한국인 입니다. => {result1.text}")
print(f"I like burger. => {result2.text}")

ktxt = "이미 다른 버전의 googletrans를 설치했었다면 \
이것을 아래와 같이 삭제한 후 최신 버전을 설치해야 한다."

etxt = translator.translate(ktxt, dest='en')
print(f"\n 원본 : { ktxt }" )
print(f"\n 번역본: { etxt.text }" )