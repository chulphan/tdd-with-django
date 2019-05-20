# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # 철환이는 그 홈페이지를 방문한다.
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # 철환이는 input box가 나이스하게 중앙에 위치한걸 알아차린다.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )
