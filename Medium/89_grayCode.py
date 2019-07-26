class Solution:
    def grayCode(self, n: int) -> List[int]:
        def backTracking(seqs):
            if len(seqs) == 2**n:
                return seqs
            for i in range(n):
                # Modify 1 digit and check if it will get to the right sequence
                mask = 1 << i
                next_code = seqs[-1] ^ mask
                # The modified value has already been seen -> Modify other digits instead
                if next_code in seqs:
                    continue
                # Explore gray code sequence with the current valid sequence
                new_seqs = backTracking(seqs + [next_code])
                # If the return result is the answer, return it
                if len(new_seqs) == 2**n:
                    return new_seqs
            return
        # The gray code starts at 0
        return backTracking([0])