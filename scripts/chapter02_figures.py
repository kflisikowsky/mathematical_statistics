"""Reproduce chapter 2 figures: python scripts/chapter02_figures.py."""
from pathlib import Path
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'statistics-mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parents[1] / 'docs' / 'images'
OUT.mkdir(parents=True, exist_ok=True)
BLUE, TEAL, ORANGE, INK = '#2563eb', '#087f8c', '#c65d21', '#123a63'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'axes.spines.top': False,
                     'axes.spines.right': False, 'axes.labelcolor': INK, 'text.color': INK,
                     'axes.titleweight': 'bold', 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
def save(fig, name):
    fig.savefig(OUT / name, dpi=180, bbox_inches='tight', facecolor='white')
    plt.close(fig)

# The eight observations supplied in Lab 1, in their original order.
hours = np.array([5, 8, 6, 10, 7, 4, 9, 6])
scores = np.array([62, 78, 71, 88, 75, 55, 82, 69])
fig, ax = plt.subplots(figsize=(9, 4.6), layout='constrained')
ax.scatter(hours, scores, s=95, color=BLUE, edgecolors='white', linewidth=1.2, zorder=3)
for i, (x, y) in enumerate(zip(hours, scores), 1):
    ax.annotate(str(i), (x, y), xytext=(8, 3 if i != 8 else -12), textcoords='offset points', fontsize=10)
ax.set(xlabel='Study time (hours)', ylabel='Exam score', xlim=(3.5, 10.8), ylim=(50, 94),
       title='Eight students: a pattern worth investigating')
ax.grid(alpha=.13)
save(fig, '02_students.png')

# Exactly the population construction in Lab 1.
rng = np.random.default_rng(42)
age = rng.integers(18, 70, 10_000)
income = 2500 + age * 90 + rng.normal(0, 1000, 10_000)
population = pd.DataFrame({'age': age, 'income': income})
mu = income.mean()
young = population.loc[population.age < 30, 'income'].to_numpy()
random_sample = population.sample(100, random_state=42)
young_sample = population.loc[population.age < 30].sample(100, random_state=42)
fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), sharex=True, sharey=True, layout='constrained')
bins = np.linspace(income.min(), income.max(), 31)
for ax, values, label, color in [(axes[0], random_sample.income, 'Random sample', BLUE),
                                  (axes[1], young_sample.income, 'Under-30 sample', ORANGE)]:
    ax.hist(income, bins=bins, density=True, color='#dce6f1', label='Whole population')
    ax.hist(values, bins=bins, density=True, histtype='step', linewidth=2.3, color=color, label=label)
    ax.axvline(mu, color=INK, linestyle='--', label='Population mean')
    ax.set(xlabel='Income (simulation units)', ylabel='Density', title=label + ' · n = 100')
    ax.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
    ax.legend(frameon=False, fontsize=9)
save(fig, '02_income_samples.png')

# Repeated independent simple random samples without replacement.
sim_rng = np.random.default_rng(2026)
means = {}
fig, axes = plt.subplots(2, 2, figsize=(11, 7), sharex=True, sharey=True, layout='constrained')
bins = np.linspace(3000, 8500, 90)
for row, (frame, label, color) in enumerate([(income, 'Whole-population sampling', BLUE),
                                           (young, 'Under-30-only sampling', ORANGE)]):
    for col, n in enumerate([20, 500]):
        estimates = np.array([sim_rng.choice(frame, n, replace=False).mean() for _ in range(1000)])
        means[(row, n)] = estimates
        ax = axes[row, col]
        ax.hist(estimates, bins=bins, color=color, alpha=.85)
        ax.axvline(mu, color=INK, linestyle='--', linewidth=2)
        ax.set_title(f'{label}\nn = {n}', fontsize=12, loc='left')
        ax.set_xlabel('Sample mean income')
        ax.set_ylabel('Number of samples')
        ax.grid(axis='y', alpha=.12)
fig.suptitle('A larger sample narrows the spread\nThe sampling frame determines what it centres on', fontsize=16, weight='bold')
save(fig, '02_bias_variability.png')

# Bias decomposition as a quantitative dot-and-interval figure.
fig, ax = plt.subplots(figsize=(10, 4.5), layout='constrained')
labels = []
for i, (key, estimates) in enumerate(means.items()):
    row, n = key
    lo, hi = np.percentile(estimates, [2.5, 97.5])
    centre = estimates.mean()
    color = BLUE if row == 0 else ORANGE
    ax.plot([lo,hi], [i,i], color=color, linewidth=5, solid_capstyle='round')
    ax.scatter([centre], [i], s=75, color=color, edgecolors='white', zorder=4)
    labels.append(f'{"Whole population" if row == 0 else "Under 30 only"}, n = {n}')
ax.axvline(mu, color=INK, linestyle='--', label=f'Population mean = {mu:,.1f}')
ax.set(yticks=range(4), yticklabels=labels, xlabel='Sample mean income (simulation units)',
       title='Stable estimates can still miss the target')
ax.invert_yaxis()
ax.legend(frameon=False, loc='lower right')
ax.grid(axis='x', alpha=.12)
save(fig, '02_precision.png')
print(f'Population mean: {mu:.4f}; under-30 mean: {young.mean():.4f}')
print(f'Random sample mean: {random_sample.income.mean():.4f}; young sample mean: {young_sample.income.mean():.4f}')
print('Student mean:', scores.mean(), 'pass proportion:', 7/8)
for k,v in means.items(): print(k, 'mean', v.mean(), 'SD', v.std(ddof=1))
