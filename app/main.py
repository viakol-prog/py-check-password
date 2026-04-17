from string import ascii_lowercase
SPECIAL = set("$@#&!-_")


def check_password(password: str) -> bool:
    if len(password) < 8 or len(password) > 16:
        return False
    has_upper = False
    has_digit = False
    has_special = False
    for ch in password:
        if ch.isalpha():
            if ch.lower() not in ascii_lowercase:
                return False
            if ch.isupper():
                has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in SPECIAL:
            has_special = True
        else:
            return False
    return has_upper and has_digit and has_special
