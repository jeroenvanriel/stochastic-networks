## Requirements

Lattice point counting and enumeration is done by [polymake](https://polymake.org/), which is available as package for many Linux distributions.
When using Poetry, use `poetry install` and `poetry run python script.py` to execute the scripts.

## Scripts

- Use `compute_runtimes.py` to measure actual runtimes for capacities `C=(r,r,r,r)`.
The script calls the `points` polymake script to get a list of lattice points (stored in `out.json`), which are used to compute the normalization constant `G`.
- The `compute_points.py` script calls the `count` polymake script that computes cardinality of the state space for various larger values of `r`.
- Both script store their results in Python pickle files `runtime_result.p` and `points_result.p`, which are read by `estimate_plot.py` to produce the final figure.

