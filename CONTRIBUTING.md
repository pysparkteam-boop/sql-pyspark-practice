# Contributing

Issues and pull requests are welcome: corrections, clearer explanations, alternative solutions, new problems.

For a new problem, add a folder under `problems/` with `README.md`, `schema.json`, `data/*.csv`, `expected.csv`,
`solution.sql` and `solution_pyspark.py`, then run `pytest -q`. Both reference solutions must pass on both engines.

Keep datasets small, synthetic and free of real personal data.
