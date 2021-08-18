import unittest
from app import parser_nginx_error_log

class TestNginxErrorLog(unittest.TestCase):
    def test_parser_nginx_error_log(self):
        test_data = """2021/08/12 07:52:56 [error] 2780496#2780496: *19351835 open() "/data/project/waynecorp-connect/static/waynecorpid/images/icons/icons.png" failed (2: No such file or directory), client: 192.168.2.181, server: connect.waynecorp.com, request: "GET /static/waynecorpid/images/icons/icons.png HTTP/1.1", host: "connect.waynecorp.com", referrer: "https://connect.waynecorp.com/static/waynecorpid/css/waynecorpid.css"""

        r = parser_nginx_error_log(test_data)
        self.assertEqual(True,  r["_is_parsed"])

if __name__ == '__main__':
    unittest.main()