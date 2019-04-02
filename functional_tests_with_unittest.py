# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class newVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            "D:\\chromedriver_win32\\chromedriver.exe")

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 철환이는 쩌는 새로운 온라인 to-do app이 있다는 것을 들었다.
        # 그래서 그 홈페이지를 확인하러 갔다.
        self.browser.get("http://localhost:8000")

        # 철환이는 그 홈페이지의 제목과 헤더에 to-do lists로 명시되어있는것을
        # 알아차렸다.

        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

        # 철환이는 당장 to-do 아이템을 입력하러 갔다.
        # [...rest of comments as before]


if __name__ == "__main__":
    unittest.main(warnings="ignore")
