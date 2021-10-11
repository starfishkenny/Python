def total(scores):
    ret = 0
    for v in scores:
        ret += v
    return ret

def average(scores):
    sum = total(scores)
    return (sum // len(scores))
