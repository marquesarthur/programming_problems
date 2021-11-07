class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if tx == 0 or ty == 0: return (sx, sy) == (tx, ty)
        while not (sx == tx and sy == ty):
            if sx > tx or sy > ty:
                return False
            elif tx == ty:
                return ((0, ty) == (sx, sy) or (tx, 0) == (sx, sy))

            if ty > tx:
                if tx == sx: return (ty - sy) % sx == 0
                ty %= tx
            else:
                if ty == sy: return (tx - sx) % sy == 0
                tx %= ty

        return True
