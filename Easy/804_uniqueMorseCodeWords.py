class Solution:
    def uniqueMorseRepresentations(self, words):
        morseMap = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
                    "e": ".", "f": "..-.", "g": "--.", "h": "....",
                    "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
                    "m": "--", "n": "-.", "o": "---", "p": ".--.",
                    "q": "--.-", "r": ".-.", "s": "...", "t": "-",
                    "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                    "y": "-.--", "z": "--.."}
        transform = set()

        for word in words:
            morse = ""
            for w in word:
                morse += morseMap[w]
            transform.add(morse)
        return len(transform)