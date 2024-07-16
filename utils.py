from numpy.random import randint

def D(n, samples = 1):
    return randint(1, n+1, samples)  

def Test(value, dice, samples, return_crits = False):
    if return_crits:
        rolls = D(6, samples)
        return rolls >= value,  rolls == 6
    return D(dice, samples) >= value

def ClipTest(x):
    # Clips x to the range [2,7]
    # So that 1 is always a fail (1+ does not exist)
    # And some test can always fail (7+, 8+ etc)
    return max(2, min(x, 7))

def ClipSave(x,x_old):
    x = max(2, x) # 1 is always a fail
    x = max(x_old - 1, x) # Save cannot be worse than the original save - 1
    x = min(x, 7) # Some save always miss (we set the test to 7+)
    return x