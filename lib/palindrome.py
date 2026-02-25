def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
    if not s or len(s) < 1:
        return ""

    start = 0
    end = 0
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        left1, right1 = expand_around_center(i, i)  
        left2, right2 = expand_around_center(i, i + 1)  

        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    return s[start:end + 1]