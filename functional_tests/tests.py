# -*- coding: utf-8 -*-
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import unittest

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            "C:\\Users\\chulkim\\Downloads\\chromedriver_win32\\chromedriver.exe")
        # self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 철환이는 쩌는 새로운 온라인 to-do app이 있다는 것을 들었다.
        # 그래서 그 홈페이지를 확인하러 갔다.
        self.browser.get("http://localhost:8000")

        # 철환이는 그 홈페이지의 제목과 헤더에 to-do lists로 명시되어있는 것을
        # 알아차렸다.

        self.assertIn("To-Do", self.browser.title)
        # self.fail("Finish the test!")
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("To-Do", header_text)

        # 철환이는 당장 to-do 아이템을 입력하러 갔다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 철환이는 "그램을 살거야" 라고 텍스트 박스에 입력한다. (철환이의 취미는 갖고 싶은게 있으면 막 지른다..(??))
        inputbox.send_keys("Buy gram")

        # 철환이가 엔터를 치면 그 페이지가 업데이트 되고 업데이트가 되고 난 페이지에는
        # "1: Buy gram" 이 to-do list 테이블 내의 하나의 아이템으로 생긴다.
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy gram')
        # 여전히 다른 아이템을 추가할 수 있는 텍스트 박스가 존재한다.
        # 철환이는 그램을 사고 윈도우를 깔 것이라고 엔터친다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Install Windows on gram!')
        inputbox.send_keys(Keys.ENTER)
        
        
        # 페이지가 또 업데이트 되면, 방금 전에 입력한 데이터도 같이 리스트에 보인다.
        self.wait_for_row_in_list_table('2: Install Windows on gram!')
        self.wait_for_row_in_list_table('1: Buy gram')
        #[...]
        self.fail("Finish the test!!!")

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

    def test_can_start_a_list_for_one_user(self):
        # 철환이는 쩌는 새로운 온라인 to-do app이 있다는 것을 들었다.
        # 그래서 그 홈페이지를 확인하러 갔다.
        # [...]
        # 페이지가 또 업데이트 되면, 방금 전에 입력한 데이터도 같이 리스트에 보인다.
        self.wait_for_row_in_list_table('2: Install Windows on gram!')
        self.wait_for_row_in_list_table('1: Buy gram')

        # 철환이는 만족했고 자러갔다.

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # 철환이는 새로운 to-do list를 시작한다.
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy gram')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy gram')

        # 철환이는 철환이의 리스트가 고유한 URL을 갖고 있다는 것을 알아차린다.
        chulphan_list_url = self.browser.current_url
        self.assertRegex(chulphan_list_url, '/lists/.+')

        # 새로운 유저인 병철이와 형언이가 그 사이트에 방문한다.

        ## 우리는 철환이가 쿠키 등으로 부터 온 정보가 없는 새로운 브라우저 세션을 이용한다.
        self.browser.quit()
        self.browser =  webdriver.Chrome(
            "C:\\Users\\chulkim\\Downloads\\chromedriver_win32\\chromedriver.exe")
        
        # 병철이는 그 홈페이지를 방문한다. 그 곳에는 철환이의 리스트의 흔적이 없다.
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy gram', page_text)
        self.assertNotIn('Install Windows on gram', page_text)

        # 병철이는 새로운 아이템을 입력하는 것으로 새로운 리스트를 시작한다.
        # 병철이는 철환이보다 흥미가 없어보인다...ㅠㅠ
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy Coffee')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Coffee')

        # 병철이는 병철이만의 고유한 URL을 얻는다.
        byungchul_list_url = self.browser.current_url
        self.assertRegex(byungchul_list_url, '/lists/.+')
        self.assertNotEqual(byungchul_list_url, chulphan_list_url)

        # 다시, 철환이의 리스트의 흔적이 없는지 본다.
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy gram', page_text)
        self.assertIn('Buy Coffee', page_text)

        # 만족해서 자러간다.






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
