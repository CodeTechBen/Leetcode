def isPalindrome(s: int) -> bool:
    left, right = 0, len(s) - 1
    print(left, right)

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


if __name__ == "__main__":
    print(isPalindrome('racecar'))