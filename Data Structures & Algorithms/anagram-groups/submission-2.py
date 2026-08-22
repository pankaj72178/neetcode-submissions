class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for original_word in strs:
            # Sorting the letters of a word creates a unique signature for all its anagrams.
            # This signature acts as the label for our boxes.
            sorted_word_tuple = tuple(sorted(original_word))

            # Place the original word into the box corresponding to its sorted letter signature.
            anagram_groups[sorted_word_tuple].append(original_word)

        return list(anagram_groups.values())