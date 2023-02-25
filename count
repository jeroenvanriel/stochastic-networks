use application "polytope";

# turn off credits of external software tools
$Verbose::credits = false;

for(@ARGV) {

  my $c1 = $_;
  my $c2 = $_;
  my $c3 = $_;
  my $c4 = $_;

  my $p = new Polytope(INEQUALITIES=>[
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

  print $p->N_LATTICE_POINTS;
  print ", ";
}

