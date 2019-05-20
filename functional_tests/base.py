# -*- coding: utf-8 -*-
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import os
import time

MAX_WAIT = 10

DESKTOP_CHROME_DRIVER_PATH = "D:\\chromedriver_win32\\chromedriver.exe"
LAPTOP_CHROME_DRIVER_PATH =  "C:\\Users\\chulkim\\Downloads\\chromedriver_win32\\chromedriver.exe"

class FunctionalTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(
            LAPTOP_CHROME_DRIVER_PATH)
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server
        else:
            self.live_server_url = 'http://' + 'localhost:8000'
        # self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


# from selenium import webdriver

# # 철환이는 새로나온 개멋진 온라인 to-do app이 있다는 소식을 들었다.
# # 철환이는 그 홈피를 확인하러간다.
# # browser = webdriver.Chrome("/Users/chulkim/Downloads/chromedriver")
# browser = webdriver.Chrome("D:\\chromedriver_win32\\chromedriver")
# browser.get("http://localhost:8000")

# # 철환이는 그 페이지의 타이틀과 헤더에 to-do lists 라고 명시된 것을 알아챈다.
# assert "To-Do" in browser.title

# # 철환이는 당장 to-do item 을 치러 들어갔다

# # 철환이는 "그램을 사야되겠다"라고 텍스트 박스 안에 타이핑한다.

# # 철환이가 엔터를 눌렀을때, 그 페이지는 업데이트 되고 현재 페이지 리스트에는
# # "1: 그램을 사야되겠다" 라는 아이템이 to-do list에 표시된다.

# # 철환이는 다른 아이템을 입력하러 텍스트박스에 남아있는다.
# # 철환이는 "그램을 사서 윈도우를 설치해야 한다" 고 친다.

# # 그 페이지는 또 업데이트 되고, 현재 두 개의 아이템이 철환이의 리스트에 보인다.

# # 철환이는 이 사이트가 내 to-do list를 기억해놓길 바란다.
# # 그럼 철환이는 그 사이트가 철환이를 위해 고유한 URL을 생성한다는 것을 안다.
# # 거기에는 어떤 그ㅓ한 효과를 위한 설명문구가 있다.

# # 철환이는 그 URL로 접속한다 - 철환이는 철환이가 생성했던 리스트가 여전히 남아있다.

# # 철환이는 만족했고 자러갔다..
# browser.quit()
