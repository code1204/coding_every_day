def distinctSubseqII(self, s: str) -> int:
        res, end = 0, collections.Counter()
        for c in s:
            res, end[c] = res * 2 + 1 - end[c], res + 1
        return res % (10**9 + 7)
