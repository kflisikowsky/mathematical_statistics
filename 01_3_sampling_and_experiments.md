---
title: Sampling strategies and experimental design
description: Probability sampling, design weights and randomized experiments in Python.
---

# Sampling strategies and experimental design

Run the Python examples in this section in order. They are independent of the other sections.

```python
import numpy as np
import pandas as pd
```

A sampling frame is the list from which units can be selected. Its coverage matters before any random numbers are generated. Sampling from a list containing only campus residents cannot represent all enrolled students without addressing the missing commuters. A census also faces missing responses and measurement problems, even though it attempts to include everyone.

## Four sampling strategies

| Design | Selection rule | Practical consideration |
| --- | --- | --- |
| Simple random sampling | Every subset of the specified size has equal selection probability | Requires a usable list of individual units |
| Stratified sampling | Sample separately from every stratum | Ensures planned representation of groups |
| Cluster sampling | Select clusters, then include all their units | Reduces collection costs but often gives correlated observations |
| Multistage sampling | Select clusters, then sample units within them | Adds flexibility but requires tracking selection probabilities at each stage |

Strata are often constructed to make units similar on relevant characteristics within each stratum. Clusters are often existing groups, such as classes or buildings. Similarity among units inside a cluster can reduce the information gained per observation, so a cluster sample should not automatically be analysed as a simple random sample.

## A reproducible sampling frame

The next example constructs a fictional register of 120 students. It contains three faculties of unequal size and 12 tutorial groups of ten students each. Treat the register as complete for this exercise.

```python
register = pd.DataFrame({
    "student_id": [f"U{i:03d}" for i in range(1, 121)],
    "faculty": np.repeat(["Engineering", "Business", "Science"], [60, 40, 20]),
    "tutorial_group": np.repeat(np.arange(1, 13), 10),
})

srs = register.sample(n=12, replace=False, random_state=2026)
print(srs.sort_values("student_id"))
print(srs["faculty"].value_counts())
```

`replace=False` prevents selecting the same row twice. Each student has inclusion probability 12/120 = 0.10. A fixed `random_state` makes the result reproducible for the same data and software environment; changing it changes the realised sample. Reproducibility does not establish representativeness.

## Stratification and unequal sampling fractions

```python
stratified = (
    register.groupby("faculty", sort=True)
    .sample(n=4, replace=False, random_state=2026)
    .copy()
)
print(stratified["faculty"].value_counts())

population_sizes = register["faculty"].value_counts()
stratified["selection_probability"] = stratified["faculty"].map(
    4 / population_sizes
)
stratified["design_weight"] = 1 / stratified["selection_probability"]
print(stratified.groupby("faculty")["design_weight"].first())
```

All three faculties contribute four students, but their population sizes differ. The inclusion probabilities are 4/60, 4/40 and 4/20; the corresponding design weights are **15, 10 and 5**. A raw sample average would give every faculty equal influence, even though Engineering contains half the population. With complete responses, a population mean can instead be estimated by weighting each stratum's sample mean by its population share.

Proportional allocation of a 12-student sample would select six from Engineering, four from Business and two from Science. That yields the same 10% sampling fraction in each faculty. Equal allocation can be useful for subgroup comparisons, while proportional allocation reflects population composition.

## Selecting groups and then individuals

```python
rng_sampling = np.random.default_rng(2026)
selected_groups = rng_sampling.choice(
    register["tutorial_group"].unique(), size=3, replace=False
)
cluster_sample = register.loc[
    register["tutorial_group"].isin(selected_groups)
].copy()
multistage_sample = (
    cluster_sample.groupby("tutorial_group")
    .sample(n=4, replace=False, random_state=2027)
)
print("Selected groups:", selected_groups)
print("Cluster sample size:", len(cluster_sample))
print("Multistage sample size:", len(multistage_sample))
```

The cluster design includes 30 students from three groups; the multistage design includes 12. Because all groups here have size ten, individual inclusion probabilities are 3/12 for the cluster design and (3/12)(4/10) = 0.10 for the multistage design. Equal probabilities do not make the latter a simple random sample: many possible sets of 12 students cannot occur under this design.

## Designing an experiment

Consider a study of whether a weekly reminder increases completion of a practice quiz. Recruit participants before assigning treatment. Define completion in advance and measure it identically in both groups.

| Principle | Application to the reminder experiment |
| --- | --- |
| Control | Compare the reminder with a no-reminder group using the same quiz, deadline and access |
| Randomize | Allocate reminders by chance, rather than letting students choose |
| Replicate | Include multiple independent participants per condition; repeat the study in another cohort when feasible |
| Block | Group participants by a relevant baseline characteristic, then randomize within those groups |

Repeatedly measuring one student does not create additional independent students. Blinding can also help when feasible: an analyst could receive masked treatment labels until the analysis is specified. Students may notice the reminder, so participant blinding is unlikely in this example.

## Random assignment in Python

The fictional participants below have either low or high prior quiz completion. Twelve participants allow six assignments to each condition.

```python
participants = pd.DataFrame({
    "student_id": [f"P{i:02d}" for i in range(1, 13)],
    "prior_completion": ["low"] * 6 + ["high"] * 6,
})
rng_assignment = np.random.default_rng(2026)
completely_randomized = participants.copy()
completely_randomized["treatment"] = rng_assignment.permutation(
    ["reminder"] * 6 + ["control"] * 6
)
print(pd.crosstab(
    completely_randomized["prior_completion"],
    completely_randomized["treatment"],
))
```

The overall treatment counts are fixed at six each, but the numbers within prior-completion groups need not balance. Blocking imposes that additional balance:

```python
rng_blocking = np.random.default_rng(2026)
blocked = participants.copy()
blocked["treatment"] = pd.Series(index=blocked.index, dtype="string")
for _, indices in blocked.groupby("prior_completion", sort=True).groups.items():
    # Each block in this example contains exactly six participants.
    labels = np.array(["reminder"] * 3 + ["control"] * 3)
    blocked.loc[indices, "treatment"] = rng_blocking.permutation(labels)
print(pd.crosstab(blocked["prior_completion"], blocked["treatment"]))
```

Each block now contributes three participants to each condition. Analyse outcomes with the blocking structure in mind. Stratification governs recruitment from a population; blocking governs treatment allocation among recruited participants. Neither procedure repairs an incomplete sampling frame.

**Practice.** A researcher selects four tutorial groups at random and surveys every student in them. Another selects two students from every tutorial group. Name the designs. Then explain why randomly assigning volunteers to reminders does not make those volunteers a random sample of the university.

**Check.** The first is cluster sampling; the second is stratified sampling with tutorial groups as strata. Treatment assignment takes place after recruitment and cannot change who volunteered.
