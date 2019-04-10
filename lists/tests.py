from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # HttpRequest 객체 생성.
        # 유저의 브라우저가 해당 페이지를 요청했을 때.
        request = HttpRequest()
        # home_page 함수에 request 인자를 넣어서 리턴값을 response에 할당.
        response = home_page(request)
        # utf-8 형식인지
        html = response.content.decode('utf8')
        # html이 <html> 태그로 시작하고 있는지
        self.assertTrue(html.startswith('<html>'))
        # '<title>To-Do lists</title>' 가 html 내에 포함되어 있는지
        self.assertIn('<title>To-Do lists</title>', html)
        # html의 끝이 </html>로 끝나는지.
        self.assertTrue(html.endswith('</html>'))