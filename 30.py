#!/usr/bin/env python
"""
30. Substring with Concatenation of All Words
You are given a string, s, and a list of words, words, that are all of the same length.
Find all starting indices of substring(s) in s that is a concatenation of each word in
words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]
Output: []

Note:
    1. words are same length
"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        wTable = {}
        indices = []
        # build hash table for words
        WORDLENGTH = 0
        for word in words:
            char = word[0]
            if char not in wTable:
                wTable[char] = []
            wTable[char].append(word)
            WORDLENGTH += len(word)

        i = 0
        while i < len(s):
            char = s[i]
            if char in wTable:
                indice = self.minConcatenString(wTable, s, i)
                if indice >= 0
                    indices.append(indice)
                    init += WORDLENGTH
            i++

    def minConcatenString(self, wTable, s, start):
        """docstring for minConcatenString"""
        pass
        


if __name__ == '__main__':
    main()
