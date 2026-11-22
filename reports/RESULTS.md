# ConformalLab — measured local run

Synthetic split-conformal binary prediction sets. Exchangeability assumptions do not hold for the concept-shift slice.

## Results

```json
{
  "alpha": 0.1,
  "calibration_quantile": 0.6054954001976884,
  "iid": {
    "coverage": 0.89,
    "mean_set_size": 1.085,
    "empty_sets": 0,
    "cases": 200
  },
  "concept_shift": {
    "coverage": 0.54,
    "mean_set_size": 1.085,
    "empty_sets": 0,
    "cases": 200
  },
  "checks": [
    "Disjoint calibration records",
    "Valid finite-sample quantile"
  ],
  "scope": "Synthetic split-conformal binary prediction sets. Exchangeability assumptions do not hold for the concept-shift slice."
}
```

Local experiment assertions passed. This does not establish production readiness or performance on real customer data. Source fingerprints and dependency versions are in results.json.
