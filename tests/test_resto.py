from app.operaciones import resto


class TestClass:
    def test_resto(self):
        assert resto(5, 5) == 0
        assert resto(-2, -2) == 0
