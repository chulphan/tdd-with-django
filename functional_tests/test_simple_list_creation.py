# -*- coding: utf-8 -*-
from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):

    # def check_for_row_in_list_table(self, row_text):
    #     table = self.browser.find_element_by_id('id_list_table')
    #     rows = table.find_elements_by_tag_name('tr')
    #     self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 철환이는 쩌는 새로운 온라인 to-do app이 있다는 것을 들었다.
        # 그래서 그 홈페이지를 확인하러 갔다.
        self.browser.get(self.live_server_url)

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
        self.browser.refresh()
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