from app.operaciones import division


class TestClass:
    def test_division(self):
        assert division(6, 3) == 2
        assert division(-2, -2) == 1
