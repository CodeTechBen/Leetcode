def isValid(s: str) -> bool:
    map = {")": "(", 
           "}": "{",
           "]": "["}
    stack = []
    
    for i in s:
        if i not in map:
            stack.append(i)
        else:
            if not stack or map[i] != stack.pop():
                return False
    
    return not stack