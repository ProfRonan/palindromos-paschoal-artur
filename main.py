"""Main functions"""
def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    string = string.replace("!", "").lower()
    string = string.replace(".", "").lower()
    if(string==string[::-1]):
        return True

