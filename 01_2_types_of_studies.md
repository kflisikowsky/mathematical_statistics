---
title: Types of studies and the scope of inference
description: Observational studies, experiments, scope of inference and Simpson’s paradox.
---

# Types of studies and the scope of inference

Run the Python examples in this section in order. They are independent of the other sections.

```python
import pandas as pd
```

An observational study records conditions without assigning an intervention. In an experiment, investigators impose treatments; a randomized experiment allocates them by chance. An explanatory variable describes the exposure or treatment being compared, while a response variable records the outcome. These labels alone do not establish causation.

## Choosing a design for a question

Suppose a campus team asks whether bicycle access reduces commuting time. Recording existing bike users and bus users gives an observational comparison. Those groups might also differ in distance, timetable and access to safe cycling routes. Distance could confound the comparison if it influences both mode choice and journey duration.

Alternatively, consenting students could be randomly offered access to a bicycle service or assigned to a comparison group. The treatment would be the **offer of access**. Some offered students might never use a bicycle, so the effect of the offer must be distinguished from the effect of actually cycling.

Random allocation balances other characteristics in expectation, not perfectly in every realised experiment. Consistent outcome measurement, follow-up and an analysis that respects assignment are still necessary.

## Sampling and assignment answer different questions

| | Random assignment | No random assignment |
| --- | --- | --- |
| Probability sample from the target population | Supports population-level causal inference under a well-conducted design | Supports population descriptions and associations with suitable design-based analysis |
| No probability sample | Supports causal inference for studied units; wider generalisation needs justification | Describes associations among observed units; wider and causal claims need further assumptions |

Sampling determines who enters a study. Assignment determines which treatment enrolled units receive. Neither protects against every later problem: substantial nonresponse can compromise a probability sample, and differential dropout can compromise a randomized experiment.

## Simpson's paradox through a worked example

Consider fictional records from two parcel-delivery services. Each parcel has a service, a route type and an on-time indicator. The following table stores counts rather than individual parcel records.

```python
reversal = pd.DataFrame({
    "service": ["A", "B", "A", "B"],
    "route": ["urban", "urban", "rural", "rural"],
    "on_time": [81, 19, 4, 40],
    "total": [90, 20, 10, 80],
})
reversal["rate"] = reversal["on_time"] / reversal["total"]
conditional = reversal.pivot(index="route", columns="service", values="rate")
totals = reversal.groupby("service")[["on_time", "total"]].sum()
totals["rate"] = totals["on_time"] / totals["total"]
reversal["late"] = reversal["total"] - reversal["on_time"]
print("Outcome counts:\n", reversal.groupby("service")[["on_time", "late"]].sum())
print("Within routes (%):\n", (100 * conditional).round(1))
print("Overall (%):\n", (100 * totals["rate"]).round(1))
```

A achieves 90% versus B's 95% on urban routes, and 40% versus 50% on rural routes. Nevertheless, A achieves **85% overall**, compared with **59% for B**. A handles mostly the easier urban routes, whereas B handles mostly rural routes. This reversal between aggregate and conditional comparisons is Simpson's paradox.

The overall rate is a weighted average. For A it is

$$
0.90\times0.90+0.10\times0.40=0.85,
$$

where the first factor in each product is a route's share of A's parcels. For B, the different weights give

$$
0.20\times0.95+0.80\times0.50=0.59.
$$

Neither table is arithmetically wrong. They answer different questions. Overall rates describe each service's actual workload; route-specific rates compare more similar settings. Whether adjustment supports a causal conclusion depends on how service and route were determined and what else differs between parcels.

**Practice.** Compare both services for a common workload containing 50% urban and 50% rural parcels. Does the overall ranking persist? Would this calculation alone prove that changing service improves delivery performance?

**Check.** The standardized rates are 65% for A and 72.5% for B. These describe a common route mix, but other differences between shipments may still explain some of the association.
