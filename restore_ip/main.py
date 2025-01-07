"""
Return valid IP addresses from a list of ip addresses

Step 1) If length is less than 4 or greater than 12 than return nothing
Step 2) Check if all are digits
Step 3) Check first digit for a 0
Step 4) If it is a 0 . is immediately after
Step 5) iterate through every permutation and check if valid
Substrings can not be above 255
Step 6) return every successful iteration in a list of strings

"""
import re

def validate_string(s:str) -> bool:
    """Check if all are digits, length is between 4 and 12 inclusive, check type"""
    if not isinstance(s, str):
        return False
    return s.isdigit() and 4 <= len(s) <= 12

def validate_segment(substring:str) -> bool:
    """Checks a segment of the string and returns True if valid"""
    return re.match(r"^(25[0-5]|2[0-4]\d|1\d{2}|[1-9]\d|\d)$", substring) is not None


def combine_segments(substrings:list[str]) -> str:
    """Combines the segments together and returns it with dots in between"""
    return f'{substrings[0]}.{substrings[1]}.{substrings[2]}.{substrings[3]}'

def iterate_string(string:str) -> str:
    """iterates through each permutation and returns the finalized string"""
    valid_ips = []
    n = len(string)
    for i in range(1,min(4, n-2)):
        for j in range(i+1,min(i+4, n-1)):
            for k in range(j+1, min(j+4, n)):
                segments = [string[:i], string[i:j], string[j:k], string[k:]]
                if all(validate_segment(seg) for seg in segments):
                    valid_ips.append(combine_segments(segments))
    return valid_ips