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
    return score/float(total)

print "Type in a string of 0s and 1s, then hit enter."
print "The program will predict your next entry based on the previous two."
s = raw_input()
if all(x == '0' or x == '1' for x in s):
    print "success rate:", predict(s)
else:
    print "Non-0/1 characters entered. Try again."


