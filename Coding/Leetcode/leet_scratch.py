import sys
from typing import List
from operator import *
from itertools import accumulate

class Solution(object):
    # 217. Contains Duplicate
    """
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.

    Example 1:
    Input: nums = [1,2,3,1]
    Output: true

    Example 2:
    Input: nums = [1,2,3,4]
    Output: false

    Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true
    """
    # My Solution
    # =================================================
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i, x in enumerate(nums):
            if x in nums[i + 1:]:
                return True
        return False

    # NeetCode Solution
    # =================================================
    def containsDuplicate(self, nums) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

    # -------------------------------------------------------------------------------------
    # 242. Valid Anagram
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word
    or phrase, typically using all the original letters exactly once.

    Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

    Example 2:
    Input: s = "rat", t = "car"
    Output: false
    """
    # My Solution
    # =================================================
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))

        if sorted_t == sorted_s:
            return True
        return False

    # NeetCode Solution
    # =================================================
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}

        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        for c in count_s:
            if count_s[c] != count_t.get(c, 0):
                return False

        return True

    # -------------------------------------------------------------------------------------
    # 1. Two Sum
    """
    Given an array of integers nums and an integer target, return indices of the two
    numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use
    the same element twice.
    You can return the answer in any order.

    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]
    """
    # My Solution
    # =================================================
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i == j:
                    break
                if nums[i] + nums[j] == target:
                    return [j, i]

    # NeetCode Solution
    # =================================================
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapped = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in mapped:
                return [mapped[diff], i]
            mapped[x] = i

    # -------------------------------------------------------------------------------------
    # 49. Group Anagrams
    """
    Given an array of strings strs, group the anagrams together. You can return the answer
    in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or
    phrase, typically using all the original letters exactly once.

    Example 1:

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
    Example 2:

    Input: strs = [""]
    Output: [[""]]
    Example 3:

    Input: strs = ["a"]
    Output: [["a"]]
    """
    # My Solution
    # =================================================
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ana_dict = {}
        output_list = []
        index_count = 0
        for i, word in enumerate(strs):
            sorted_ana = ''.join(sorted(word))
            if sorted_ana not in ana_dict:
                ana_dict[sorted_ana] = index_count
                index_count += 1
                output_list.append([word])
            else:
                output_list[ana_dict[sorted_ana]].append(word)

        return output_list

    # NeetCode Solution
    # =================================================
    def groupAnagrams(self, strs):
        import collections
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()

    # -------------------------------------------------------------------------------------
    # 347. Top K Frequent Elements
    """
    Given an integer array nums and an integer k, return the k most frequent elements.
    You may return the answer in any order.

    Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    Example 2:
    Input: nums = [1], k = 1
    Output: [1]
    """
    # My Solution
    # =================================================
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Todo: Doesn't work for all use cases i.e [3,0,1,0]
        k_count = 0
        unique_dict = {}
        for x in nums:
            if k_count < k:
                if x not in unique_dict:
                    unique_dict[x] = nums.count(x)
                    k_count += 1
            else:
                break

        return list(unique_dict.keys())

    # NeetCode Solution
    # =================================================
    def topKFrequent(self, nums, k):
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    # -------------------------------------------------------------------------------------
    # 238. Product of Array Except Self
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the
    product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation.
    Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]
    """
    # My Solution
    # =================================================
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i, n in enumerate(nums):
            temp_nums = nums.copy()
            temp_nums.remove(n)
            temp_prod = 1
            for j in temp_nums:
                temp_prod = temp_prod * j
            answer.append(temp_prod[-1])

        return answer

    # NeetCode Solution
    # ================================================
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

    # -------------------------------------------------------------------------------------
    # 36. Valid Sudoku
    """
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
    according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without
    repetition.
    Note:
    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

    Example 1:
    Input: board =
    [["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: true

    Example 2:

    Input: board =
    [["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: Same as Example 1, except with the 5 in the top left corner being modified
    to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
    """
    # My Solution
    # =================================================
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_sod_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        break_flag = False
        for item in board:
            tmp_valid_list = []
            for n in item:
                if n == ".":
                    continue
                if int(n) > 9 or int(n) < 1:
                    break_flag = True
                    break
                if n in tmp_valid_list:
                    break_flag = True
                    break
                else:
                    tmp_valid_list.append(n)
                tmp_valid_list.append(n)
            if break_flag:
                return False

        for item in board:
            item[1]

        return True

    # NeetCode Solution
    # ================================================
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     return board


if __name__ == '__main__':
    input = ' '.join(sys.argv[1:])
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    solution = Solution()
    result = Solution.isValidSudoku(solution, board)

    print(result)
