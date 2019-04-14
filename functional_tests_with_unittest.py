# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # self.browser = webdriver.Chrome(
        #     "D:\\chromedriver_win32\\chromedriver.exe")
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

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
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy gram' for row in rows)
        )

        # 여전히 다른 아이템을 추가할 수 있는 텍스트 박스가 존재한다.
        # 철환이는 그램을 사고 윈도우를 깔 것이라고 엔터친다.
        self.fail("Finish the test!!!")
        
        # 페이지가 또 업데이트 되면, 방금 전에 입력한 데이터도 같이 리스트에 보인다.
        #[...]


if __name__ == "__main__":
    unittest.main(warnings="ignore")
