import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

# pip install requests // 웹사이트에 request(송신)을 보내기 위한 라이브러리
# pip install BeautifulSoup // 웹사이트에서 가져온 HTML을 파싱해주기 위한 라이브러리 - 파싱이란 구문해석 - 분석을 뜻함

# 쉽게 말해 requests 라이브러리로 가져온 HTML 요소들을 BeautifulSoup 라이브러리를 사용해 데이터들을 가공함 



def get_blog_title_category():
    post_title_list = []
    post_category_list = []
    post_create_at = []

    def get_page_info(url: str):
        page_html = requests.get(url)

        parser_page_info = bs(page_html.text, "html.parser")

        post_list = parser_page_info.select(".area-common > article")

        # range는 반복문을 길이로 지정하기 때문에 enumerate를 사용 
        for i, post in enumerate(post_list):
            post_category_html = post.select(".link-category")
            post_create_at_html = post.select(".date")

            post_title_text = post.find("strong").text
            post_category_text = post_category_html[0].text
            post_create_at_text = post_create_at_html[0].text

            post_title_list.append(post_title_text)
            post_category_list.append(post_category_text)
            post_create_at.append(post_create_at_text)
        return
    # https://naithar01.tistory.com/
    url = "https://naithar01.tistory.com/?page="

    # 1 ~ 2 페이지를 크롤링할 예정 
    for i in range(2) :
    # 해당 웹사이트의 page Query를 이용하여 각 페이지의 요소들을 가져옴 
    # 페이지는 { i } 변수로 구분 
        now_url = url + str(i + 1)

        get_page_info(now_url)

    return post_title_list, post_category_list, post_create_at







        
post_title, post_category, post_create_at = get_blog_title_category()

post_data = {
    "title": post_title,
    "category": post_category
}

post_data_table = pd.DataFrame(data=post_data, index=post_create_at)

print(post_data_table)

post_data_table.to_csv("a.csv", encoding="utf-8-sig")