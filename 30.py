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
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        logger.debug("s:{}, word: {}".format(s, words))
        TargetDict = {}
        for word in words:
            if word not in TargetDict:
                TargetDict[word] = 0
            TargetDict[word] += 1
        nr_word = len(words)
        if len(words) <= 0:
            return []
        word_length = len(words[0])
        index = []

        for i in range(len(s) - (word_length - 1)):
            word = s[i:i+word_length]
            if word not in words:
                continue

            #incefficient left char for concation
            if len(s) - i < nr_word*word_length:
                break
            result = self.trySearch(s, i, i+nr_word*word_length, TargetDict, word_length)
            if result >= 0:
                index.append(result)
        return index

    def trySearch(self, s, start, end, TargetDict, word_length):
        logger.info("search: {}".format(s[start:end]))
        tmpDict = {}
        for i in range(start, end, word_length):
            word = s[i:i+word_length]
            if word not in TargetDict:
                return -1
            if word not in tmpDict:
                tmpDict[word] = 0
            tmpDict[word] += 1
            if word in tmpDict and tmpDict[word] > TargetDict[word]:
                return -1
        return start



if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    try:
        result = Solution().findSubstring(s, words)
        assert result == [0, 9]
    except AssertionError:
        logger.error(result)
    s = "barfoobarfoobar"
    words = ["foo","bar"]
    try:
        result = Solution().findSubstring(s, words)
        assert result == [0,3,6,9]
    except AssertionError:
        logger.error(result)

    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    try:
        result = Solution().findSubstring(s, words)
        answer = []
        assert result == answer
    except AssertionError:
        logger.error(result)
        logger.error("should be {}".format(answer))
    s = "aaaaaaaa"
    words = ["aa","aa","aa"]
    try:
        result = Solution().findSubstring(s, words)
        assert result == [0,1,2]
    except AssertionError:
        logger.error(result)
    s = "a"
    words = ["a"]
    try:
        result = Solution().findSubstring(s, words)
        assert result == [0]
    except AssertionError:
        logger.error(result)
