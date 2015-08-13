a_z = "_abcdefghijklmnopqrstuvwxyz"
def rabbit_total(rabbit):
    total = 0
    for letter in rabbit:
        total += a_z.index(letter)
    return total

def rabbit_compare(r1, r2):
    r1t = rabbit_total(r1)
    r2t = rabbit_total(r2)
    print('Comparing "%s" (%d) to "%s" (%d)' % (r1, r1t, r2, r2t))
    if (r1t == r2t):
        print('...the total was the same, lexigraphically: %r' % (r1 > r2,))
        return 1 if r2 > r1 else -1
    else:
        print('...the total was different, yeilding: %d' % (r1t - r2t,))
        return r2t - r1t

def sort_rabbits(rabbits):
    return sorted(rabbits, cmp=rabbit_compare)

r1 = ["annie", "bonnie", "liz"]
print('*** Result of sorting: %r:\n%r' % (r1, sort_rabbits(r1)))

r2 = ["abcdefg", "vi"]
print('*** Result of sorting: %r:\n%r' % (r2, sort_rabbits(r2)))
        
