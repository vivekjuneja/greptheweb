"Example of a generator"
 
from __future__ import generators
 
def primes(upto):
    for current in xrange(2,upto):
        for factor in xrange(2,current-1):
            if not current%factor: break
        else: yield current
 
for interesting in primes(50):
        print interesting,"is an interesting number"