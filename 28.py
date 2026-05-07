class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # If needle is empty, return 0
        if needle == "":
            return 0
        
        n = len(haystack)
        m = len(needle)

        # Traverse through haystack
        for i in range(n - m + 1):
            # Check substring match
            if haystack[i:i + m] == needle:
                return i
        
        return -1