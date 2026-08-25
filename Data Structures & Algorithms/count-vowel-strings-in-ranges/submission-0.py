class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        # vowels
        def is_vowel(ch: str):
            return (
                ch == 'a' or
                ch == 'e' or
                ch == 'i' or
                ch == 'o' or
                ch == 'u'
            )

        # precompute
        num_of_vowel_words = [0] * len(words)
        for i, word in enumerate(words):
            if is_vowel(word[0]) and is_vowel(word[-1]):
                if i > 0:
                    num_of_vowel_words[i] = num_of_vowel_words[i-1] + 1
                else:
                    num_of_vowel_words[i] = 1
            else:
                if i > 0:
                    num_of_vowel_words[i] = num_of_vowel_words[i-1]
        
        print(num_of_vowel_words)

        # query
        ans = []
        for l, r in queries:
            if is_vowel(words[l][0]) and is_vowel(words[l][-1]):
                ans.append(num_of_vowel_words[r] - num_of_vowel_words[l] + 1)
            else:
                ans.append(num_of_vowel_words[r] - num_of_vowel_words[l])
            
        return ans