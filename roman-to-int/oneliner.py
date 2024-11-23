def romanToInt(s: str) -> int:
    point_map = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    return sum(
        -point_map[s[i]] if point_map[s[i]] < point_map[s[i + 1]] else point_map[s[i]]
        for i in range(len(s) - 1)
    ) + point_map[s[-1]]
