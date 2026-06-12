import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class BackendApiTest(unittest.TestCase):
    def test_ping_returns_ok(self):
        from app import app

        client = app.test_client()
        response = client.get("/api/ping")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")


if __name__ == "__main__":
    unittest.main()
