---
title: Probability distributions
description: Empirical and theoretical distributions, discrete and continuous probability models, and how to assess whether a model is useful.
---

# Probability distributions

Suppose a help desk records the number of calls it receives each hour. A histogram describes the calls it has already observed, but it does not tell us directly how many calls to expect next hour or how uncertain that count is. A probability distribution gives us a mathematical model for the possible values of a random variable and the probabilities associated with them.

This chapter moves from observed data to probability models, then checks whether a model is useful for the question at hand. It follows **Lecture 3: Empirical & Theoretical Probability Distributions** and connects its examples to the random-variable and discrete-distribution material in *Statistics II — Lecture 2*.

By the end, you should be able to distinguish empirical and theoretical distributions, classify random variables as discrete or continuous, interpret probability functions and distribution parameters, select a plausible model from its assumptions, calculate and explain basic probabilities, and compare model implications with observed data.

**How to work through the chapter.** Try each question before opening its answer. Identify the variable and the data-generating process before selecting a formula. The expandable **Reveal answer** controls contain checks, not a substitute for working through the reasoning.

## 3.1 From observed data to a probability model

An **empirical distribution** describes the values actually observed in a sample. It can be summarised by a frequency table, proportions, a histogram, an empirical cumulative distribution function (ECDF), or statistics such as the sample mean $\bar{x}$ and sample variance $s^2$. A new sample from the same process will usually have a different empirical distribution.

A **theoretical distribution** assigns probabilities to the possible outcomes of a random variable under a mathematical model. Its parameters describe features of that model: for example, a population mean $\mu$, standard deviation $\sigma$, success probability $p$, or event rate $\lambda$. The parameters are fixed within a specified model, although their values may be unknown.

| | Empirical distribution | Theoretical distribution |
| --- | --- | --- |
| Built from | Observed sample values | A probability model |
| Centre and spread | Sample statistics such as $\bar{x}$ and $s$ | Model parameters such as $\mu$ and $\sigma$ |
| Variation | Changes from sample to sample | Describes the model's probability structure |
| Main question | What did this sample look like? | What outcomes does the model make plausible? |

A model is a simplification, not a claim that reality follows a formula perfectly. It is useful when its assumptions fit the process well enough to answer a clearly stated question.

## 3.2 Random variables and probability functions

A **random variable** assigns a numerical value to the outcome of a random process. It is **discrete** if its possible values form a finite or countably infinite set, as with the number of calls in an hour. It is **continuous** if it can take any value in an interval, as with a waiting time or a package's weight.

For a discrete random variable $X$, its **probability mass function (PMF)** is

$$
p_X(x) = P(X=x).
$$

Each probability is non-negative, and the probabilities over all possible values sum to one. For a continuous variable, the **probability density function (PDF)** describes probability density, not probability at a point. Probabilities are areas:

$$
P(a < X \leq b) = \int_a^b f_X(x)\,dx.
$$

The **cumulative distribution function (CDF)** works for discrete and continuous variables:

$$
F_X(x) = P(X \leq x).
$$

For a continuous variable, $P(X=a)=0$ at every exact point, even though an interval containing $a$ can have positive probability. A density's height is not itself a probability.

### Expected value and variance

The **expected value** is the probability-weighted long-run centre of a model. For a discrete random variable,

$$
E(X) = \sum_x x\,p_X(x),
\qquad
\operatorname{Var}(X) = \sum_x (x-E(X))^2 p_X(x).
$$

For a continuous random variable with density $f_X$, the corresponding formulas are

$$
E(X)=\int x f_X(x)\,dx,
\qquad
\operatorname{Var}(X)=\int (x-E(X))^2 f_X(x)\,dx,
$$

where the integrals are over the variable's support. The standard deviation is $\operatorname{SD}(X)=\sqrt{\operatorname{Var}(X)}$ and is expressed in the same units as $X$; the variance is in squared units.

An expected value need not be a possible outcome or the most likely outcome. For example, a fair six-sided die has expected value $3.5$, although it cannot show $3.5$.

## 3.3 Discrete probability distributions

The discrete models below all describe counts, but they represent different data-generating processes. Decide how the observations arise before using a formula.

### 3.3.1 Binomial distribution

Use a **binomial distribution** for the number of successes in a fixed number $n$ of trials when:

1. the number of trials is fixed;
2. each trial has two outcomes, labelled success and failure;
3. the trials are independent; and
4. the success probability $p$ is the same on every trial.

If $X$ is the number of successes, then $X\sim\operatorname{Binomial}(n,p)$ and

$$
P(X=k) = \binom{n}{k}p^k(1-p)^{n-k},
\quad k=0,1,\ldots,n.
$$

Its mean and variance are

$$
E(X)=np,
\qquad
\operatorname{Var}(X)=np(1-p).
$$

**Example.** Suppose 40% of students belong to a specified category. If the category status of ten students can be treated as independent with the same probability, the probability that exactly six belong to it is

$$
P(X=6)=\binom{10}{6}(0.4)^6(0.6)^4 \approx 0.1115.
$$

The model's expected count is $np=4$. This is a long-run average, not a prediction that exactly four of these ten students must belong to the category. If sampling from a small class without replacement, independence and a constant success probability may not be reasonable; consider the hypergeometric model instead.

### 3.3.2 Poisson distribution

Use a **Poisson distribution** to model the number of events in a specified interval of time, distance, area, volume, or another exposure when events occur at a roughly stable rate and are suitably independent. The interval must be stated because changing its size changes the expected count.

For $X\sim\operatorname{Poisson}(\lambda)$,

$$
P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!},
\quad k=0,1,2,\ldots,
\qquad
E(X)=\operatorname{Var}(X)=\lambda.
$$

Here $\lambda$ is the expected number of events **in the chosen interval**. If a stable rate is two power failures per week, the probability of exactly one in a week is

$$
P(X=1)=e^{-2}\frac{2^1}{1!}\approx 0.2707.
$$

For a half-week interval at the same rate, the parameter is $\lambda=1$, not 2. A rate that changes substantially across the interval, or events that cluster or inhibit one another, can make the simple Poisson model inappropriate.

### 3.3.3 Hypergeometric distribution

Use a **hypergeometric distribution** when sampling a fixed number of items from a finite population **without replacement**. The draws are dependent because each selected item changes the composition of the remaining population.

Suppose the population has size $N$, with $K$ successes, and a sample of size $n$ is drawn without replacement. The probability of exactly $k$ successes is

$$
P(X=k)=
\frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}.
$$

The expected value and variance are

$$
E(X)=n\frac{K}{N},
\qquad
\operatorname{Var}(X)=n\frac{K}{N}\left(1-\frac{K}{N}\right)
\frac{N-n}{N-1}.
$$

**Example.** A box contains five male and five female hamsters. Two are selected without replacement. The probability that both are the same sex is

$$
P(\text{same sex}) =
\frac{\binom{5}{2}+\binom{5}{2}}{\binom{10}{2}}
=\frac{4}{9}\approx 0.4444.
$$

If the population is very large relative to the sample, the change in composition may be negligible and a binomial approximation can sometimes be useful. The actual sampling scheme still determines which model is exact.

## 3.4 Continuous probability distributions

For continuous distributions, probability is area under a density curve. The total area over the variable's support is one, and the CDF accumulates area from the left. This interpretation underlies the uniform, normal, exponential, and log-normal models below.

### 3.4.1 Uniform distribution

A **continuous uniform distribution** on $[a,b]$ assigns constant density across that interval:

$$
f_X(x)=\frac{1}{b-a},\quad a\leq x\leq b;
\qquad
E(X)=\frac{a+b}{2},
\qquad
\operatorname{Var}(X)=\frac{(b-a)^2}{12}.
$$

For $a\leq c\leq d\leq b$,

$$
P(c\leq X\leq d)=\frac{d-c}{b-a}.
$$

If a time is equally likely to fall anywhere from 0 to 10 minutes, the probability it falls between 2 and 4 minutes is the interval's length divided by the whole range: $(4-2)/(10-0)=0.20$. Equal-length intervals have equal probabilities; individual exact values still have probability zero.

### 3.4.2 Normal distribution

The **normal distribution** is a symmetric, bell-shaped continuous model. Its mean $\mu$ sets the centre and its standard deviation $\sigma$ sets the spread. Write $X\sim N(\mu,\sigma^2)$; the second parameter is the **variance**, not the standard deviation.

Its density is

$$
f_X(x)=\frac{1}{\sigma\sqrt{2\pi}}
\exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right),
\quad -\infty < x < \infty.
$$

Standardise a value using

$$
z=\frac{x-\mu}{\sigma}.
$$

The $z$-score gives the distance from the mean in standard-deviation units. A positive score is above the mean; a negative score is below it. A larger $z$-score means a higher position relative to that particular distribution, not necessarily a higher raw measurement or an overall better performance.

For a normal model, about 68% of values lie within one standard deviation of the mean, 95% within two, and 99.7% within three. These are approximate proportions, not exact cut-offs.

**Example.** Student A scores 1800 on a test with $\mu=1500$ and $\sigma=300$, so $z_A=1$. Student B scores 24 on a different test with $\mu=21$ and $\sigma=5$, so $z_B=0.6$. Relative to their respective distributions, A's score is further above the mean.

A normal model can be plausible for approximately symmetric measurements or the combined effect of many small influences. Check the shape and context; a bell-shaped curve is not justified merely because a variable is numerical.

### 3.4.3 Exponential distribution

The **exponential distribution** models a positive waiting time until the next event in a constant-rate Poisson process. With rate parameter $\lambda>0$,

$$
f_X(x)=\lambda e^{-\lambda x},\quad x\geq 0;
\qquad
E(X)=\frac{1}{\lambda},
\qquad
\operatorname{Var}(X)=\frac{1}{\lambda^2}.
$$

Its CDF is $F_X(x)=1-e^{-\lambda x}$ for $x\geq0$. The rate and waiting time must use compatible units: if $\lambda$ is events per minute, the expected waiting time is measured in minutes.

The exponential model is memoryless: conditional on having waited so far, the distribution of the additional waiting time is unchanged. This is a strong assumption, not a general property of all waiting times.

### 3.4.4 Log-normal distribution

A positive random variable is **log-normal** when its natural logarithm is normally distributed: $\ln(X)\sim N(\mu,\sigma^2)$. The parameters $\mu$ and $\sigma$ describe the distribution of $\ln(X)$, not the arithmetic mean and standard deviation of $X$.

Its density is

$$
f_X(x)=\frac{1}{x\sigma\sqrt{2\pi}}
\exp\left(-\frac{(\ln x-\mu)^2}{2\sigma^2}\right),
\quad x>0.
$$

The log-normal distribution is positive and typically right-skewed. It can be useful when multiplicative effects generate measurements such as some sizes, incomes, or lifetimes. Its arithmetic mean and variance are

$$
E(X)=e^{\mu+\sigma^2/2},
\qquad
\operatorname{Var}(X)=(e^{\sigma^2}-1)e^{2\mu+\sigma^2}.
$$

The exponential and log-normal distributions can both be right-skewed and positive, but their mechanisms differ. Exponential waiting times arise from a constant event rate and have the memoryless property; log-normal values arise when the logarithm is approximately normal, often reflecting multiplicative influences. Skewness alone does not choose between them.

## 3.5 Choosing and checking a model

Use this sequence before interpreting a calculated probability:

1. **Define the variable.** What is counted or measured, and in what units or interval?
2. **Describe the process.** Are there a fixed number of independent trials, a stable event rate, sampling without replacement, or a continuous measurement?
3. **Check the assumptions.** Are probabilities constant? Are events independent? Is the support and shape plausible?
4. **Compare with the data.** Look at an appropriate histogram or empirical distribution, the centre and spread, and relevant proportions. For a proposed normal model, a Q–Q plot can help assess whether the observed quantiles are approximately consistent with normality.
5. **Interpret the result.** State the event, the model and its assumptions, the probability, and the population or process to which the conclusion applies.

A theoretical model and an empirical distribution will not match perfectly in a finite sample. The question is whether discrepancies are plausible under sampling variation and whether the model is adequate for the intended purpose. A model is a claim to check, not a label to attach after seeing a histogram.

## 3.6 Practice: distributions and model choice

Try these tasks before expanding the answers. For probability calculations, show which distribution and parameters you used.

**1. Empirical or theoretical?** A histogram summarises 80 measured waiting times. A model assigns probabilities to the number of calls arriving in the next hour. Which is empirical and which is theoretical?

<details>
<summary>Reveal answer</summary>
<p>The histogram is an empirical description of the 80 observed waiting times. The call-count model is theoretical: it assigns probabilities to outcomes under specified assumptions.</p>
</details>

**2. Discrete or continuous?** Classify the number of calls in an hour, the waiting time for the next call, the number of defective products in a batch, and the weight of a package.

<details>
<summary>Reveal answer</summary>
<p>The two counts are discrete. Waiting time and package weight are continuous measurements, even if a device records them to a finite number of decimal places.</p>
</details>

**3. Choose the discrete model.** Match each situation to a binomial, Poisson, or hypergeometric model: (a) successes in 20 independent trials with the same success probability; (b) failures per week at a stable rate; (c) four items drawn from a finite box without replacement.

<details>
<summary>Reveal answer</summary>
<p>(a) Binomial: fixed number of independent trials and constant success probability. (b) Poisson: an event count over a specified interval at a stable rate. (c) Hypergeometric: a fixed-size sample without replacement from a finite population.</p>
</details>

**4. Calculate with a binomial model.** If $X\sim\operatorname{Binomial}(10,0.4)$, find the probability of exactly six successes and the expected number of successes.

<details>
<summary>Reveal answer</summary>
<p>Use P(X = 6) = C(10, 6)(0.4)^6(0.6)^4, approximately 0.1115. The expected count is np = 10(0.4) = 4.</p>
</details>

**5. Calculate with a Poisson model.** Events occur at a stable average rate of three per 100 yards. Under a Poisson model, find the probability of exactly five events in the next 100 yards. What is the parameter for the next 50 yards?

<details>
<summary>Reveal answer</summary>
<p>For 100 yards, lambda = 3, so P(X = 5) = e^(-3) 3^5 / 5!, approximately 0.1008. For 50 yards at the same rate, lambda = 1.5.</p>
</details>

**6. Compare without replacement.** A box contains five red and five blue cards. Two cards are drawn without replacement. Find the probability that both are red or both are blue. Why is the hypergeometric model appropriate?

<details>
<summary>Reveal answer</summary>
<p>The probability is [C(5, 2) + C(5, 2)] / C(10, 2) = 4/9, approximately 0.4444. The finite box is sampled without replacement, so the composition and success probability change after the first draw.</p>
</details>

**7. Standardise two scores.** Student A scores 1800 on a test with mean 1500 and standard deviation 300. Student B scores 24 on a test with mean 21 and standard deviation 5. Calculate both z-scores and compare their relative positions.

<details>
<summary>Reveal answer</summary>
<p>z_A = (1800 - 1500) / 300 = 1. z_B = (24 - 21) / 5 = 0.6. A is further above the mean relative to the relevant test distribution.</p>
</details>

**8. Read a uniform model.** A time is uniformly distributed between 0 and 10 minutes. Find the probability it is between 2 and 4 minutes. Explain why the probability at exactly 3 minutes is zero.

<details>
<summary>Reveal answer</summary>
<p>The interval probability is its length divided by the full length: (4 - 2) / (10 - 0) = 0.20. A single point has zero area under a continuous density, so P(X = 3) = 0.</p>
</details>

**9. Choose between positive, right-skewed models.** Which model is more closely connected to waiting time until the next event at a stable rate? Which can represent a positive measurement whose logarithm is approximately normal? Why is right-skew alone insufficient?

<details>
<summary>Reveal answer</summary>
<p>The exponential model describes waiting time under a constant-rate Poisson process. The log-normal model describes a positive variable whose natural logarithm is normal. Both can be right-skewed, so the data-generating mechanism and assumptions—not skewness alone—must guide the choice.</p>
</details>

**10. Assess a model.** Name three checks you would make before using a theoretical distribution to describe observed data.

<details>
<summary>Reveal answer</summary>
<p>Define the variable and data-generating process; check assumptions such as independence, constant probability or rate, support, and shape; compare empirical and theoretical implications using a histogram or ECDF, centre and spread, relevant proportions, and—for a normal model—a Q–Q plot. The checks should be relevant to the intended use.</p>
</details>

## 3.7 Take-home message

Start with what the data show, describe the process that could have generated them, choose a distribution whose assumptions make sense, and compare its implications with the observations. The calculation is only as useful as the model and the interpretation behind it.

The examples and practice in this chapter are adapted from **Lecture 3 Workbook: Empirical & Theoretical Probability Distributions**, **Lecture 3 slides**, and the discrete random-variable and distribution material in **Statistics II — Lecture 2**. The next chapter develops estimation and uncertainty using these probability models.
