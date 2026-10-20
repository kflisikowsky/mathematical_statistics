---
title: Interactive dice-sampling demonstration
description: Explore empirical and theoretical dice distributions and simulate sample means in your browser.
---

# 4.10 Interactive dice-sampling demonstration

The app below runs in your browser without an account, server connection, or package installation. Its observations stay in the current browser tab: the class board is a local demonstration, not a shared live board. Reload the page to start fresh.

Use the controls to:

1. add observed sums by rolling virtually or entering physical dice;
2. click a sum to record outcomes called out by a group;
3. compare observed proportions with the exact distribution of two fair dice; and
4. simulate sample means for different numbers of dice and compare their spread with the CLT prediction.

The theoretical sum probabilities are proportional to $1,2,3,4,5,6,5,4,3,2,1$ for sums 2 through 12. Thus 7 is the most likely sum: six of the 36 equally likely ordered dice pairs add to 7. For one fair die, $\mu=3.5$ and $\sigma^2=35/12$, so the standard error of the mean of $n$ dice is $\sqrt{35/(12n)}$.

<iframe
  src="https://kflisikowsky.github.io/mathematical_statistics/dice_sampling.html"
  title="Interactive dice-sampling demonstration"
  width="100%"
  height="1660"
  loading="lazy"
  style="border: 0; border-radius: 1rem;"
></iframe>

If the embedded view does not load, [open the dice-sampling app directly](https://kflisikowsky.github.io/mathematical_statistics/dice_sampling.html).
