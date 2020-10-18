import numpy


scores = [2,3,4,53,54,32,5]

mean = sum(scores) / len(scores)
variance = sum([((x - mean) ** 2) for x in scores]) / len(scores)
res = variance ** 0.5
print(res)

print(numpy.std.scores)
