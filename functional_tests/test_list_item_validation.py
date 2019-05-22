# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
   
    def test_cannot_add_empty_list_items(self):
        # 철환이는 홈페이지에 들어갔고, 실수로 빈 list item 을 submit 하기를 시도한다.
        # 철환이는 빈 input box 에다가 엔터를 때린다.
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # 홈페이지는 새로고침 됐고, list item은 빈 칸이어서는 안된다는 에러 메세지가 나타난다.
        self.wait_for(lambda: self.assertEqual(  
            self.browser.find_element_by_css_selector('.has-error').text,
            "당신은 빈 아이템을 가질 수 없어요^^"
        ))

        # 철환이는 아이템에 대한 어떤 텍스트를 가지고 다시 submit을 했고, 이제 정상적으로 동작한다.
        self.get_item_input_box().send_keys('Buy Pencil')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Pencil')

        # 철환이는 고집을 부려서 두번째 빈 list item을 submit을 하기로 결정한다..
        self.get_item_input_box().send_keys(Keys.ENTER)

        # 철환이는 리스트 페이지에서 똑같은 경고를 받는다.
        self.wait_for(lambda: self.assertEqual(  
            self.browser.find_element_by_css_selector('.has-error').text,
            "당신은 빈 아이템을 가질 수 없어요^^"
        ))

        # 그리고 철환이는 규칙에 맞게 어떠한 텍스트를 채운다.
        self.get_item_input_box().send_keys('Write something')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Pencil')
        self.wait_for_row_in_list_table('2: Write something')
        # self.fail('write me!')

    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:invalid'
        ))

        self.get_item_input_box().send_keys('Buy Pencil')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:valid'
        ))

        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Pencil')

        self.get_item_input_box().send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy Pencil')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:invalid'
        ))

        self.get_item_input_box().send_keys('Write something')
        self.wait_for(lambda: self.browser.find_elements_by_css_selector(
            '#id_text:valid'
        ))

        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Pencil')
        self.wait_for_row_in_list_table('2: Write something')
