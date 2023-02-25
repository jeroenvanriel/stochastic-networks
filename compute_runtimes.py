import json
import subprocess
import time
from operator import mul, pow, truediv
from math import factorial
from functools import reduce


def compute(c, rhos):
    # enumerate all lattice points and save to out.json
    subprocess.run("polymake --script points " + " ".join(map(str, c)),
            shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # load the lattice points
    # I think this currently loads all in memory, so doing this in 
    # some 'streaming' fashion could be better.
    with open('out.json') as file:
        raw_data = file.read()
    data = json.loads(raw_data)["data"]

    # compute product for one state
    def term(state, rhos):
        res = list(map(truediv, map(pow, rhos, state), map(factorial, state)))
        return reduce(mul, res)

    # sum over all states
    total = 0
    for state in data:
        state = list(map(int, state[1:5])) # extract the actual integers
        total += term(state, rhos)

    return len(data), total


# run time analysis
rhos = [2, 3, 4, 2]
print(f'rhos = {rhos}')

# we simply consider C = (r,r,r,r) for increasing r

rs = []
Gs = []
points = []
runtimes = []
for r in range(50, 80+1, 5):
    c = [r]*4
    rs.append(r)
    print(f'capacities = {c}')

    start = time.time()
    p, G = compute(c, rhos)
    end = time.time()
    points.append(p)
    Gs.append(G)
    runtimes.append(end - start)

    print(f'number of lattice points = {p}')
    print(f'runtime = {end - start}')
    print(f'G = {G}')

import pickle
pickle.dump( (rhos, rs, Gs, points, runtimes), open( "runtime_result.p", "wb" ) )

