from unittest import TestCase
from app import app

class TestEndpoints(TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False
        self.testapp = app.test_client()

    def tearDown(self):
        pass

    def test_patent_id_http_200_ok(self):
        res = self.testapp.get('/patent/id/8')
        self.assertEqual(res.status_code, 200)

    def test_patent_name_http_200_ok(self):
        res = self.testapp.get('/patent/name/AAAA007')
        self.assertEqual(res.status_code, 200)

    def test_patent_id_http_204_no_content(self):
        res = self.testapp.get('/patent/id/30999')
        self.assertEqual(res.status_code, 204)

    def test_patent_name_http_204_no_content(self):
        res = self.testapp.get('/patent/name/WXYZ999')
        self.assertEqual(res.status_code, 204)                    

if __name__ == '__main__':
    TestCase.main()             