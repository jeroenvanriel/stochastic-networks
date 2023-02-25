import subprocess
import pickle

# now extrapolate using number of lattice points only
rs = list(range(85, 150+1, 5))

# use polymake perl script to compute number of lattice points
# for the varying values of r
res = subprocess.run("polymake --script count " + " ".join(map(str, rs)),
        shell=True, stdout=subprocess.PIPE)

# parse the returned comma-separated string
points = list(map(int, res.stdout.decode("utf-8").split(", ")[:-1]))

pickle.dump((rs, points), open("points_result.p", "wb"))

