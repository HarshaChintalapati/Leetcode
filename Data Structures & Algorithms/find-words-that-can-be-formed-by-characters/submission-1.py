class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_map = {}
        for c in chars:
            char_map[c] = char_map.get(c, 0) + 1  
        total_length = 0
        for word in words:
            word_map = {}
            for c in word:
                word_map[c] = word_map.get(c, 0) + 1
            can_form = True
            for char, count in word_map.items():
                if char not in char_map or count > char_map[char]:
                    can_form = False
                    break
            if can_form:
                total_length += len(word)
                
        return total_length
        