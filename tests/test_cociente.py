from app.operaciones import cociente


class TestClass:
    def test_cociente(self):
        assert cociente(5, 5) == 1
        assert cociente(-2, -2) == 1
