import pytest
from ..palindrome import longest_palindromic_substring

class TestLongestPalindromicSubstring:
    """Test suite for longest_palindromic_substring function"""
    
    def test_single_character(self):
        result = longest_palindromic_substring("a")
        assert result == "a"
    
    def test_two_identical_characters(self):
        result = longest_palindromic_substring("aa")
        assert result == "aa"
    
    def test_two_different_characters(self):
        result = longest_palindromic_substring("ab")
        assert result in ["a", "b"]
    
    def test_typical_case_1(self):
        result = longest_palindromic_substring("babad")
        assert result in ["bab", "aba"]
    
    def test_typical_case_2(self):
        result = longest_palindromic_substring("cbbd")
        assert result == "bb"
    
    def test_full_palindrome(self):
        result = longest_palindromic_substring("racecar")
        assert result == "racecar"
    
    def test_no_palindrome_longer_than_one(self):
        result = longest_palindromic_substring("abc")
        assert len(result) == 1
        assert result in ["a", "b", "c"]
