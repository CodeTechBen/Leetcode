def isValid(s: str) -> bool:
    stack = []

    for char in s:
        if char in ["{","[", "("]:
            stack.append(char)
        if char in [")"]:
            complement = stack.pop()
            if complement != "(":
                return False
        if char in ["}"]:
            complement = stack.pop()
            if complement != "{":
                return False
        if char in ["]"]:
            complement = stack.pop()
            if complement != "[":
                return False
            
        if not stack:
            return True


