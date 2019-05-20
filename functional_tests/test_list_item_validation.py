# -*- coding: utf-8 -*-
from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
   
    def test_cannot_add_empty_list_items(self):
        # 철환이는 홈페이지에 들어갔고, 실수로 빈 list item 을 submit 하기를 시도한다.
        # 철환이는 빈 input box 에다가 엔터를 때린다.

        # 홈페이지는 새로고침 됐고, list item은 빈 칸이어서는 안된다는 에러 메세지가 나타난다.

        # 철환이는 고집을 부려서 두번째 빈 list item을 submit을 하기로 결정한다..

        # 철환이는 리스트 페이지에서 똑같은 경고를 받는다.

        # 그리고 철환이는 규칙에 맞게 어떠한 텍스트를 채운다.
        self.fail('write me!')
