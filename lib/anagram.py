# your code goes here!

class Anagram:
    def __init__(self, word):
        self._word = word

    def match(self, word_list):
        result = []

        result = [element for element in word_list if self._are_anagrams        (element, self._word)]
            
        return result
    
    def _are_anagrams(self, word1, word2):
        word1 = word1.lower().replace(" ", "")
        word2 = word2.lower().replace(" ", "")

        return sorted(word1) == sorted(word2)
    
        
