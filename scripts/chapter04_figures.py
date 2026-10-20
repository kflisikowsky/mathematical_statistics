"""Reproduce chapter 4 figures and animations: python scripts/chapter04_figures.py."""
from pathlib import Path
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'statistics-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np
from scipy import stats

OUT = Path(__file__).resolve().parents[1] / 'docs' / 'images'
OUT.mkdir(parents=True, exist_ok=True)
BLUE, TEAL, ORANGE, PINK, GOLD, INK = '#2563eb', '#087f8c', '#c65d21', '#d6336c', '#e0a800', '#123a63'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'axes.spines.top': False,
                     'axes.spines.right': False, 'axes.labelcolor': INK, 'text.color': INK,
                     'axes.titleweight': 'bold', 'figure.facecolor': 'white', 'axes.facecolor': 'white'})


def save(fig, name):
    fig.savefig(OUT / name, dpi=170, bbox_inches='tight', facecolor='white')
    plt.close(fig)


# Skewed population: exponential with mean 1 and standard deviation 1.
POP_MEAN = POP_SD = 1.0


def sample_means(rng, n, reps):
    return rng.exponential(1.0, (reps, n)).mean(axis=1)


# 1. Statistic varies, parameter does not: ten samples of 25 values from one population.
rng = np.random.default_rng(4)
fig, ax = plt.subplots(figsize=(9.5, 4.6), layout='constrained')
x = np.linspace(0, 6, 400)
ax.fill_between(x, stats.expon.pdf(x), color='#dce6f1', label='Population (right-skewed)')
ax.axvline(POP_MEAN, color=INK, linewidth=2.4, label=r'Parameter $\mu=1$ (fixed)')
colors = plt.cm.plasma(np.linspace(0.05, 0.85, 10))
for i, c in enumerate(colors):
    sample = rng.exponential(1.0, 25)
    ax.scatter(sample, np.full(25, -0.04 - 0.045 * i), s=9, color=c, alpha=.75)
    ax.scatter(sample.mean(), -0.04 - 0.045 * i, marker='D', s=70, color=c, edgecolors='white', zorder=4)
ax.annotate(r'each diamond: the mean $\bar{x}$ of one sample', (2.6, -0.5), fontsize=10, color=INK)
ax.set(xlim=(0, 6), ylim=(-0.58, 1.05), xlabel='Value', yticks=[0, .5, 1], ylabel='Population density',
       title='Ten samples of 25: the parameter stays put, the statistic moves')
ax.legend(frameon=False)
save(fig, '04_statistic_varies.png')

# 2. LLN paths: running means of die rolls.
rng = np.random.default_rng(11)
n_max = 500
fig, ax = plt.subplots(figsize=(9.5, 4.8), layout='constrained')
steps = np.arange(1, n_max + 1)
ax.axhspan(3.4, 3.6, color='#cfeee9', label='±0.1 band around μ')
for c in plt.cm.cool(np.linspace(0, 1, 8)):
    ax.plot(steps, np.cumsum(rng.integers(1, 7, n_max)) / steps, color=c, linewidth=1.5, alpha=.85)
ax.axhline(3.5, color=INK, linewidth=2.2, linestyle='--', label='μ = 3.5')
ax.set(xscale='log', ylim=(1, 6), xlabel='Number of rolls n (log scale)', ylabel='Running mean',
       title='Law of large numbers: eight independent runs of die rolls')
ax.legend(frameon=False)
save(fig, '04_lln_paths.png')

# 3. Standard error shrinks like 1/sqrt(n).
fig, ax = plt.subplots(figsize=(9, 4.6), layout='constrained')
n = np.arange(1, 401)
ax.plot(n, 1 / np.sqrt(n), color=BLUE, linewidth=3, label=r'$\sigma/\sqrt{n}$ with $\sigma=1$')
for k in (1, 4, 16, 64, 256):
    ax.scatter(k, 1 / np.sqrt(k), s=80, color=ORANGE, zorder=4, edgecolors='white')
    ax.annotate(f'n={k}\nSE={1 / np.sqrt(k):.3f}', (k, 1 / np.sqrt(k)), xytext=(8, 8), textcoords='offset points', fontsize=9)
ax.set(xlabel='Sample size n', ylabel='Standard error', ylim=(0, 1.2),
       title='Four times the data, half the error: diminishing returns')
ax.grid(alpha=.15)
ax.legend(frameon=False)
save(fig, '04_se_shrinks.png')

# 4. CLT: skewed population, then means of n = 1, 2, 5, 30.
rng = np.random.default_rng(2026)
fig, axes = plt.subplots(1, 4, figsize=(13, 3.6), sharey=False, layout='constrained')
for ax, n_ in zip(axes, (1, 2, 5, 30)):
    means = sample_means(rng, n_, 20_000)
    ax.hist(means, bins=60, density=True, color=TEAL, alpha=.75)
    xs = np.linspace(means.min(), means.max(), 300)
    ax.plot(xs, stats.norm.pdf(xs, POP_MEAN, POP_SD / np.sqrt(n_)), color=PINK, linewidth=2.4)
    ax.set(title=f'n = {n_}', xlabel=r'sample mean $\bar{x}$')
    ax.set_xlim(0, 3.5 if n_ < 5 else 2.5)
axes[0].set_ylabel('Density')
fig.suptitle('CLT: means of a skewed (exponential) population approach the pink normal curve', fontweight='bold')
save(fig, '04_clt_shapes.png')

# 5. Polling: sampling distribution of p-hat for p = 0.4, n = 1000.
fig, ax = plt.subplots(figsize=(9.5, 4.6), layout='constrained')
p, n_ = 0.4, 1000
se = np.sqrt(p * (1 - p) / n_)
xs = np.linspace(p - 4 * se, p + 4 * se, 400)
ax.plot(xs, stats.norm.pdf(xs, p, se), color=INK, linewidth=2.5)
inside = (xs > p - 1.96 * se) & (xs < p + 1.96 * se)
ax.fill_between(xs[inside], stats.norm.pdf(xs[inside], p, se), color=BLUE, alpha=.35, label='central 95% of polls')
for tail in (xs <= p - 1.96 * se, xs >= p + 1.96 * se):
    ax.fill_between(xs[tail], stats.norm.pdf(xs[tail], p, se), color=ORANGE, alpha=.6,
                    label='unusual polls (5%)' if tail[0] else None)
rng = np.random.default_rng(5)
polls = rng.binomial(n_, p, 40) / n_
ax.scatter(polls, np.full(40, 1.5), s=26, color=PINK, alpha=.8, label='40 simulated polls')
ax.axvline(p, color=INK, linestyle='--')
ax.set(xlabel=r'poll result $\hat{p}$', ylabel='Density',
       title=rf'p = 0.40, n = 1000: SE ≈ {se:.4f}, so about 95% of polls fall in 0.370–0.430')
ax.legend(frameon=False)
save(fig, '04_poll_distribution.png')

# 6. When does the normal approximation for p-hat work? p = 0.1.
fig, axes = plt.subplots(1, 3, figsize=(13, 3.8), layout='constrained')
for ax, n_ in zip(axes, (10, 50, 300)):
    k = np.arange(0, n_ + 1)
    pmf = stats.binom.pmf(k, n_, 0.1)
    ax.bar(k / n_, pmf * n_, width=0.8 / n_, color=TEAL, alpha=.8)
    xs = np.linspace(0, min(1, 0.1 + 5 * np.sqrt(.09 / n_)), 300)
    ax.plot(xs, stats.norm.pdf(xs, .1, np.sqrt(.09 / n_)), color=PINK, linewidth=2.4)
    ok = n_ * .1 >= 5
    ax.set(title=f'n = {n_}: np = {n_ * .1:.0f} ' + ('(rule met)' if ok else '(rule fails)'),
           xlabel=r'$\hat{p}$', xlim=(0, min(1, 0.1 + 5 * np.sqrt(.09 / n_))))
axes[0].set_ylabel('Density')
fig.suptitle('Rule of thumb check, p = 0.10: the skewed shape becomes symmetric as np grows', fontweight='bold')
save(fig, '04_proportion_rule.png')

# 7. chi-square, t and F families.
fig, axes = plt.subplots(1, 3, figsize=(14, 3.9), layout='constrained')
x = np.linspace(0, 25, 400)
for df, c in zip((2, 5, 10), (BLUE, TEAL, ORANGE)):
    axes[0].plot(x, stats.chi2.pdf(x, df), color=c, linewidth=2.4, label=fr'$\nu={df}$')
axes[0].set(title=r'$\chi^2$: nonnegative, right-skewed', ylim=(0, .5), xlabel='value')
axes[0].legend(frameon=False)
x = np.linspace(-4.5, 4.5, 400)
axes[1].plot(x, stats.norm.pdf(x), color=INK, linestyle='--', linewidth=2.2, label='N(0,1)')
for df, c in zip((2, 5, 30), (PINK, ORANGE, TEAL)):
    axes[1].plot(x, stats.t.pdf(x, df), color=c, linewidth=2.2, label=f't, df={df}')
axes[1].set(title='Student t: heavier tails, tends to N(0,1)', xlabel='value')
axes[1].legend(frameon=False)
x = np.linspace(0.001, 5, 400)
for (a, b), c in zip(((3, 10), (10, 10), (30, 60)), (BLUE, PINK, TEAL)):
    axes[2].plot(x, stats.f.pdf(x, a, b), color=c, linewidth=2.4, label=fr'$\nu_1={a},\ \nu_2={b}$')
axes[2].set(title='F: ratio of scaled chi-squares', xlabel='value')
axes[2].legend(frameon=False)
save(fig, '04_chi_t_f.png')

# 8. Difference of two normal scores: variances add.
fig, axes = plt.subplots(1, 2, figsize=(12, 4.3), layout='constrained')
x = np.linspace(85, 165, 500)
axes[0].plot(x, stats.norm.pdf(x, 130, 6), color=BLUE, linewidth=2.4, label='A ~ N(130, 6)')
axes[0].plot(x, stats.norm.pdf(x, 120, 9), color=ORANGE, linewidth=2.4, label='B ~ N(120, 9)')
axes[0].set(xlabel='score', ylabel='Density', title='Two universities')
axes[0].legend(frameon=False)
sd = np.sqrt(117)
d = np.linspace(-30, 50, 500)
axes[1].plot(d, stats.norm.pdf(d, 10, sd), color=INK, linewidth=2.4)
shade = d >= 5
axes[1].fill_between(d[shade], stats.norm.pdf(d[shade], 10, sd), color=PINK, alpha=.4,
                     label=r'$P(D\geq5)\approx0.678$')
axes[1].axvline(10, color=INK, linestyle='--')
axes[1].set(xlabel='D = A − B', title=r'Difference: $N(10,\ \sqrt{117}\approx10.82)$')
axes[1].legend(frameon=False)
save(fig, '04_difference.png')


# Animation 1: sampling distribution of the mean builds up as n grows.
def animate_clt():
    rng = np.random.default_rng(7)
    sizes = [1, 2, 3, 5, 8, 12, 20, 30, 50]
    fig, ax = plt.subplots(figsize=(8.5, 4.6), layout='constrained')

    def draw(i):
        ax.clear()
        n_ = sizes[i]
        means = sample_means(rng, n_, 15_000)
        ax.hist(means, bins=70, range=(0, 3.5), density=True, color=TEAL, alpha=.8)
        xs = np.linspace(0.01, 3.5, 400)
        ax.plot(xs, stats.norm.pdf(xs, POP_MEAN, POP_SD / np.sqrt(n_)), color=PINK, linewidth=3)
        ax.axvline(1, color=INK, linestyle='--')
        ax.set(xlim=(0, 3.5), ylim=(0, 4.2 if n_ > 20 else 2.2 if n_ > 5 else 1.5), xlabel=r'sample mean $\bar{x}$', ylabel='Density',
               title=f'Means of n = {n_} exponential values · SE = {1 / np.sqrt(n_):.3f}')
        ax.spines[['top', 'right']].set_visible(False)

    anim = FuncAnimation(fig, draw, frames=len(sizes), interval=900)
    anim.save(OUT / '04_clt_animation.gif', writer=PillowWriter(fps=1.1), dpi=90)
    plt.close(fig)


# Animation 2: a running mean wandering into the ±0.1 band.
def animate_lln():
    rng = np.random.default_rng(3)
    n_max = 400
    rolls = rng.integers(1, 7, n_max)
    running = np.cumsum(rolls) / np.arange(1, n_max + 1)
    fig, ax = plt.subplots(figsize=(8.5, 4.4), layout='constrained')
    frames = list(range(2, 60, 3)) + list(range(60, n_max + 1, 12))

    def draw(k):
        ax.clear()
        ax.axhspan(3.4, 3.6, color='#cfeee9')
        ax.axhline(3.5, color=INK, linestyle='--', linewidth=2)
        ax.plot(np.arange(1, k + 1), running[:k], color=BLUE, linewidth=2.4)
        ax.scatter(k, running[k - 1], color=PINK, s=70, zorder=4)
        ax.set(xlim=(0, n_max), ylim=(1.5, 5.5), xlabel='Number of rolls n', ylabel='Running mean',
               title=f'n = {k}: running mean = {running[k - 1]:.3f}')
        ax.spines[['top', 'right']].set_visible(False)

    anim = FuncAnimation(fig, draw, frames=frames, interval=120)
    anim.save(OUT / '04_lln_animation.gif', writer=PillowWriter(fps=8), dpi=90)
    plt.close(fig)


animate_clt()
animate_lln()
print('Chapter 4 figures written to', OUT)
