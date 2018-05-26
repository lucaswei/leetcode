class Solution(object):
    def minWindow(self, s, t):
        from collections import defaultdict
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tTable = defaultdict(int)
        sTable = defaultdict(int)
        for i in t:
            tTable[i] += 1

        count = 0
        begin = 0
        result = ""
        for i in range(len(s)):
            char = s[i]
            if char in tTable:
                if sTable[char] < tTable[char]:
                    count += 1
                sTable[char] += 1

                # push begin to increment
                while count == len(t):
                    c = s[begin]
                    if c in t:
                        sTable[c] -= 1
                        if sTable[c] < tTable[c]:
                            count -= 1;
                            if result == "" or len(result) > (i+1 - begin):
                                result = s[begin:i+1]
                    begin += 1
        return result


if __name__ == '__main__':
    print "Result: " + Solution().minWindow("ADOBECODEBANC", "ABC")
    print "Result: " + Solution().minWindow("a", "aa")
    print "Result: " + Solution().minWindow("ADOBECODEBANC", "ABC")
    
