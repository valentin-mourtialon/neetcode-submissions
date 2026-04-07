class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        valid_mapping = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        expected_close = []
        for c in s:
            if not expected_close:
                if c not in valid_mapping:
                    return False
                expected_close.append(valid_mapping[c])
            else:
                if c not in valid_mapping and c != expected_close[-1]:
                    return False
                elif c in valid_mapping:
                    expected_close.append(valid_mapping[c])
                elif c == expected_close[-1]:
                    expected_close.pop()
        return not expected_close