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
        tSet = set(words)

        # build indexed hint list
        # hit[offset] -> ['word1', 'word2']
        hit = [[] for i in range(len(s))]
        indices = []
        acct = {}
        for word in set(words):
            i = 0
            while True:
                try:
                    index = s.index(word, i)
                except ValueError:
                    break
                hit[index].append(word)
                i = index + 1
        logger.debug(hit)
        for word in words:
            if word not in acct:
                acct[word] = 0
            acct[word] += 1

        for offset in range(len(s)):
            if self.startToSearch(hit, offset, acct, len(words)):
                indices.append(offset)
        return indices
                    

    def startToSearch(self, hit, index, acct, length):
        logger.debug("[{}]: {}".format(index, acct))
        result = False
        if index >= len(hit):
            return False
        for word in hit[index]:
            if acct[word] <= 0:
                return False
            if length-1  == 0:
                return True
            acct[word] -= 1
            result = self.startToSearch(hit, index+len(word), acct, length-1)
            acct[word] += 1
            if result:
                break
        return result



if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    assert Solution().findSubstring(s, words) == [0, 9]
    s = "wordgoodstudentgoodword"
    words = ["word","student"]
    assert Solution().findSubstring(s, words) == []
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
        assert result == [0,3,6,9]
    except AssertionError:
        logger.error(result)
    s = "aaaaaaaa"
    words = ["aa","aa","aa"]
    try:
        result = Solution().findSubstring(s, words)
        assert result == [0,1,2]
    except AssertionError:
        logger.error(result)
    s = "a"*10000
    words = list(s)
    try:
        result = Solution().findSubstring(s, words)
        assert result == [0,1,2]
    except AssertionError:
        logger.error(result)
