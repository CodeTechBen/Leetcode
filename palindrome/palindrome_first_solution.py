def isPalindrome(x: int) -> bool:
    return True if str(x)[::-1] == str(x) else False

if __name__ == "__main__":
    print(isPalindrome(12321))