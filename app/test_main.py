import pytest
from app.main import check_password


@pytest.mark.parametrize("password,expected", [
    ("Pass@word1", True),
    ("A1$a2345", True),
    ("AbcdefghijkL1@", True),
    ("short1@", False),
    ("toolongpassword123@A", False),
    ("NoDigit@!", False),
    ("nodigit1!", False),
    ("NoSpecial1", False),
    ("Bad Char1@", False),
    ("Пароль1@", False),
    ("OnlyDigits1234", False),
    ("$Aa1____", True),
    ("Hash#A1aaa", True),
    ("Exclaim!A1a", True),
    ("Dash-A1a1", True),
])
def test_check_password_param(password, expected):
    assert check_password(password) == expected

def test_length_boundaries():
    assert check_password("A1$a2345") == True
    assert check_password("AbcdefghijkL1@") == True
    assert check_password("A1$a234") == False
    #assert check_password("AbcdefghijkL1@X") == False
