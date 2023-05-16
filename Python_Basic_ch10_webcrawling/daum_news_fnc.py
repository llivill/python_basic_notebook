import requests
from bs4 import BeautifulSoup

# 함수
# input:URL
# output: 제목, 본문

# 기존: 제목함수, 본문함수
# →이유: 함수만들때 하나의 함수에 다수의 기능을 넣기 X
def get_news_title_and_content(url):


    result = requests.get(url)

    doc = BeautifulSoup(result.text,"html.parser")
    title = doc.select("h3.tit_view")[0].get_text()
    contents = doc.select("section > p")   # section 태그 안에 있는 p 태그들


    content = ""  # 전체 본문을 담을 변수
    # contents.pop(-1)
    for tag in contents :
        content = content + tag.get_text()

    return title, content
