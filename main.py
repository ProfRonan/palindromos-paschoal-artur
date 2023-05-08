"""Main functions"""


def is_palindrome(string: str) -> bool:
    string.lower()
    string.replace(" ", "")
    string.replace("!", "")
    if(string==string[::-1]):
        return True
    return False
