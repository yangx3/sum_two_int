#In math, sum of two int
#(a + b) == log(e^a * e^b)
#this func uses no + or -, which means ++ and -- is not used either.


def getSum(self, a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a
    return int(math.log(pow(math.e,a) * pow(math.e,b)))