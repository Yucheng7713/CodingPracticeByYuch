class Solution:
    # Time complexity : O ( # of row * max_word_length )
    # Space complexity : O ( # of words * max_word_length )
    def wordsTyping(self, sentence, rows: int, cols: int) -> int:
        sentence_str = " ".join(sentence) + " "
        start, n = 0, len(sentence_str)
        for i in range(rows):
            # start -> the partition position ( end index ) for a line in th sentence
            start += cols
            # Check if the next character is blank space
            # For case like : abc_de_f_abc_de_f....
            # abc_de
            # f_abc_
            # If couple words are fitted into a line which ends exactly at the last word's last character
            # Then we still need to count the blank which is invisible due to line change.
            if sentence_str[start % n] == ' ':
                # After the partition, if the first letter is blank
                # Don't mess the length with the index !!!
                # the index of the last letter in a line is start - 1
                start += 1
            else:
                # If the line is ended at a letter, which partitions a word.
                # Backtracking, decrease start index until it reaches a blank
                while start > 0 and sentence_str[(start - 1) % n] != ' ':
                    start -= 1
        return start // n

r, c = 2, 8
sentence = ["hello","world"]
print(Solution().wordsTyping(sentence, r, c))