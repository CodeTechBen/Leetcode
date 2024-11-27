def remove_punctuation(string: str) -> str:
    new_word = ""
    for char in string:
        if char.isalpha():
            new_word += char
    return new_word

def string_palindrome(string: str) -> bool:
    left, right = 0, len(string) -1
  
    while left < right:
        if not string[left].isalpha():
            left =+ 1
        if not string[right].isalpha():
            right =- 1
        
        if string[left] == string[right]:
            left =+ 1
            print("hello World")
            right =- 1
        else:
            return False
    return True

def is_palindrome(list_string:list[str]) -> list[str]:
    result = [] 
    for string in list_string:
        new_word = remove_punctuation(string)
        if string_palindrome(new_word.lower()):
            result.append(new_word.lower())
    return result

if __name__ == "__main__":
    is_palindrome("abba")

