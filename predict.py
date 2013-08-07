# A program to predict a user's random selections with low entropy.


# user supplies a string of 1s and 0s. We predict the next bit using,
# for now, 2-gram markov chain.

import itertools

def predict_next(counts,prev):
    # counts is a dict of freq(xyz)
    return max('01',key = lambda z: counts[prev+z])
    
def predict(s):
    successes = []
    score, total = 0, 0
    if len(s) < 2:
        return score, total
    counts = dict()
    for x,y,z in itertools.product('01',repeat=3):
        counts[x+y+z] = 1
    x0, x1 = s[0], s[1]
    for x2 in s[2:]:
        # regular predict, then update
        my_x2 = predict_next(counts,x0+x1)
        total += 1
        if my_x2 == x2:
            score += 1
            successes.append(1)
        else:
            successes.append(0)
        counts[x0+x1+x2] += 1
        x0, x1 = x1, x2
    return score,total, successes

#s = '011010010100101010001010010101001010100101011100010101'
#print predict(s)[2]


#s = '1000101011101010010101011110101010010101011010101000101010110'
#print predict(s)[2]

import random
s = ''
for i in range(10000):
    if random.random() < .7:
        s += '0'
    else:
        s += '1'
a,b, _ = predict(s)
print float(a)/b
