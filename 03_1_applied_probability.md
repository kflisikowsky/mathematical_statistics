---
title: Applied probability calculations
description: Choosing probability models and translating practical questions into events that can be calculated and interpreted.
---

# 3.8 Applied probability calculations

Probability calculations begin with a question about a process, not with a function call. Define the random variable, identify how its values are generated, and express the question as an event. Only then choose a model and calculate the probability.

## From a question to an event

The wording of a question determines which part of a distribution is needed:

- **Exactly $k$ outcomes**, such as exactly seven successful attempts, asks for a point probability, $P(X=k)$.
- **At most $k$ outcomes** asks for $P(X\leq k)$, while **fewer than $k$** asks for $P(X<k)$. For a discrete variable, $P(X<k)=P(X\leq k-1)$.
- **More than $k$ outcomes** asks for $P(X>k)=1-P(X\leq k)$.
- **No greater than a threshold** for a continuous measurement asks for a cumulative probability such as $P(X\leq c)=F_X(c)$.
- **Between two values** asks for a difference of cumulative probabilities. For continuous $X$, $P(a\leq X\leq b)=F_X(b)-F_X(a)$; including or excluding endpoints does not change the answer.

These distinctions matter. For instance, “fewer than three” successes does not include the outcome of three successes, whereas “at most three” does.

## Match the model to the process

The number of successes in a fixed set of independent attempts with a common success probability can be modelled by a binomial distribution. This describes repeated attempts such as shots at a basket only when the success probability is reasonably stable and the attempts can be treated as independent.

Counts of arrivals over a stated time or distance can be modelled by a Poisson distribution when events occur at a stable average rate and are suitably independent. The parameter $\lambda$ is the expected count over the **whole interval being considered**. At a rate of 1.6 items per minute, a five-minute interval has parameter $\lambda=8$, not 1.6. Changing the exposure interval changes the parameter proportionally when the rate is constant.

When a fixed-size sample is drawn without replacement from a finite batch, the draws are dependent. A hypergeometric model accounts for the changing composition of the batch. For example, inspecting a few cylinders from a known production batch with a fixed number of defective items is different from treating each inspected cylinder as an independent trial with an unchanging defect probability.

For a continuous measurement such as braking distance, a normal model may be appropriate if its shape is plausible in context. A standards question can then be expressed as the probability that the measurement falls below a limit. Check both parameters and units: in $N(\mu,\sigma^2)$, $\sigma$ is the standard deviation and the second parameter in the notation is its square, the variance.

## Calculating and checking results in Python

The `scipy.stats` distributions provide cumulative probabilities and point probabilities. For example:

```python
from scipy.stats import binom, poisson, hypergeom, norm

# Cumulative probability and point probability for a binomial model
binom.cdf(3, n=10, p=0.7)
binom.pmf(7, n=10, p=0.7)

# Poisson count over five minutes at 1.6 arrivals per minute
poisson.cdf(7, mu=5 * 1.6)

# Exactly two defectives in a sample of six from a batch of 100 with five defectives
hypergeom.pmf(2, M=100, n=5, N=6)

# Probability that a normally distributed measurement is at most 29
norm.cdf(29, loc=26.4, scale=2.34)
```

The parameter names vary by distribution. In `hypergeom`, `M` is the population size, `n` the number of successes in the population, and `N` the sample size. In `norm`, `loc` is the mean and `scale` is the standard deviation. Read the function signature rather than assuming that parameter names mean the same thing across distributions.

For a strict upper-tail event, a survival function can express the calculation directly:

```python
poisson.sf(5, mu=1.6)  # P(X > 5)
```

As a basic check, probabilities should lie between zero and one. Also check whether a result is plausible: a threshold far above a model's centre should generally have a larger lower-tail probability than a threshold close to or below the centre. For a count over a longer interval, the expected count should increase if the rate stays the same.

## Interpreting model-based probabilities

A calculated probability is conditional on the model and its assumptions. A binomial answer relies on a fixed number of trials, independence, and a common success probability. A Poisson answer relies on a stable rate over the specified exposure. A hypergeometric answer relies on a finite population composition and sampling without replacement. A normal answer relies on a plausible normal model for the measurement.

State the event, the model, its relevant parameters, and the result in the context of the question. Do not interpret a probability as a guarantee about the next observation, and do not treat a model as established merely because it produces a numerical answer. Compare the assumptions with how the data were generated and, when observations are available, check whether the model's implications are reasonably consistent with them.
