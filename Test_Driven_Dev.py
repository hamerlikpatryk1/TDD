#source venv/bin/activate
#pytest -q Test_Driven_Dev.py
import pytest

class TestClass: 
    def test_hello_world(self):
        x = "Hello world"
        assert "Hello world" in x

    def test_2(self):
        y = 5
        z = 5
        assert y == z

"""
class MyHelloWorld:
    def my_hello_world(self):
        x = "Hello world"
        return x

class TestHelloWorld:
    def test_hello_world(self, x):
        assert "Hello world" in x
        return


def main():
    x = MyHelloWorld().my_hello_world()
    TestHelloWorld(x).test_hello_world(x)
    return

if __name__ == "__main__":
    main()
"""