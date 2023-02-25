use application "polytope";

# read capacity parameters
my ($c1, $c2, $c3, $c4) = @ARGV;

declare $p = new Polytope(INEQUALITIES=>[
  # capacity constraints
  [$c1, -1,-1,-1,-1],   # n_1 + n_2 + n_3 + n_4 <= C_1
  [$c2,  0,-1,-1, 0],   # n_2 + n_3 <= C_2
  [$c3,  0, 0,-1,-1],   # n_3 + n_4 <= C_3
  [$c4,  0, 0, 0,-1],   # n_4 <= C_4
  # non-zero constraints
  [0, 1,0,0,0],         # n_1 >= 0
  [0, 0,1,0,0],         # etc.
  [0, 0,0,1,0],
  [0, 0,0,0,1]
]);     

save($p->LATTICE_POINTS, "out.json");

