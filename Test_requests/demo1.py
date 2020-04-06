import requests
import unittest


class TestRequests(unittest.TestCase):

    def setUp(self):
        self.url1 = 'https://testing-studio.com/'
        self.url2 = 'https://www.baidu.com/'

    def test_requests_get(self):
        r = requests.get(self.url1)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.encoding, 'UTF-8')

    def test_request_post(self):
        payload = {'wd': 'MP3'}
        r = requests.post(self.url2, data=payload)
        self.assertEqual(r.status_code, 302)
        self.assertEqual(r.status_code, 200)






