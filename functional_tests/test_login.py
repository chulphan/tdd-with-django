from django.core import mail
from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

TEST_EMAIL = 'loveskywhy@naver.com'
SUBJECT = 'Your login link for Tddtutorials'

class LoginTest(FunctionalTest):

    def test_can_get_email_link_to_login(self):
        # 철환이는 쩌는 to-do list 로 갔다.
        # 그리고 알아 차린다 처음 접속했을때 네비게이션에 로그인 섹션이 있는걸 봤다
        # 그 로그인 섹션은 철환이에게 이메일주소를 입력하라고 말하고있다. 그래서 철환이는 이메일을 입력한다.
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_name('email').send_keys(TEST_EMAIL)
        self.browser.find_element_by_name('email').send_keys(Keys.ENTER)

        # 이메일이 발송되었다는 메세지가 나타난다.
        self.wait_for(lambda: self.assertIn(
            'Check your email',
            self.browser.find_element_by_tag_name('body').text
        ))

        # 철환이는 이메일에 들어가서 메세지를 찾는다.
        # mail.outbox = []... 어떻게 할 수가 없어.. settings에서 EMAIL_BACKEND 설정해줘도 안됨
        email = mail.outbox[0]  
        self.assertIn(TEST_EMAIL, email.to)
        self.assertEqual(email.subject, SUBJECT)

        # 그 이메일 내용에는 url link가 포함되어있다.
        self.assertIn('Use this link to login', email.body)
        url_search = re.search(r'http://.+/.+$', email.body)
        if not url_search:
            self.fail(f'Could not find url in email body:\n{{email.body}}')
        url = url_search.group(0)
        self.assertIn(self.live_server_url, url)

        # 철환이는 그걸 클릭한다.
        self.browser.get(url)
        # 철환이는 로그인이 된다!!!!
        self.wait_for(
            lambda: self.browser.find_element_by_link_text('Log out')
        )
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(TEST_EMAIL, navbar.text)