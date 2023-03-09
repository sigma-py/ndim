<p align="center">
  <a href="https://github.com/sigma-py/ndim"><img alt="ndim" src="https://raw.githubusercontent.com/sigma-py/ndim/main/logo/ndim-logo.svg" width="50%"></a>
  <p align="center">Multidimensional volumes and monomial integrals.</p>
</p>

[![PyPi Version](https://img.shields.io/pypi/v/ndim.svg?style=flat-square)](https://pypi.org/project/ndim)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ndim.svg?style=flat-square)](https://pypi.org/pypi/ndim/)
[![GitHub stars](https://img.shields.io/github/stars/sigma-py/ndim.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/sigma-py/ndim)
[![Downloads](https://pepy.tech/badge/ndim/month?style=flat-square)](https://pepy.tech/project/ndim)

[![Discord](https://img.shields.io/static/v1?logo=discord&logoColor=white&label=chat&message=on%20discord&color=7289da&style=flat-square)](https://discord.gg/hnTJ5MRX2Y)

ndim computes all kinds of volumes and integrals of monomials over such volumes in a
fast, numerically stable way, using recurrence relations.

### Installation

Install ndim [from PyPI](https://pypi.org/project/ndim/) with

```
pip install ndim
```

### How to get a license

Licenses for personal and academic use can be purchased
[here](https://buy.stripe.com/aEUg1H38OgDw5qMfZ3).
You'll receive a confirmation email with a license key.
Install the key with

```
plm add <your-license-key>
```

on your machine and you're good to go.

For commerical use, please contact support@mondaytech.com.

### Use ndim

```python
import ndim

val = ndim.nball.volume(17)
print(val)

val = ndim.nball.integrate_monomial((4, 10, 6, 0, 2), lmbda=-0.5)
print(val)

# or nsphere, enr, enr2, ncube, nsimplex
```

<!--pytest-codeblocks:expected-output-->

```
0.14098110691713894
1.0339122278806983e-07
```

All functions have the `symbolic` argument; if set to `True`, computations are performed
symbolically.

```python
import ndim

vol = ndim.nball.volume(17, symbolic=True)
print(vol)
```

<!--pytest-codeblocks:expected-output-->

```
512*pi**8/34459425
```

### The formulas

A PDF version of the text can be found
[here](https://raw.githubusercontent.com/sigma-py/ndim/assets/useful-recurrence-relations.pdf).

This note gives closed formulas and recurrence expressions for many $n$-dimensional
volumes and monomial integrals. The recurrence expressions are often much simpler, more
instructive, and better suited for numerical computation.

#### _n_-dimensional unit cube

```math
C_n = \left\{(x_1,\dots,x_n): -1 \le x_i \le 1\right\}
```

- Volume.

```math
|C_n| = 2^n = \begin{cases}
  1&\text{if $n=0$}\\
  |C_{n-1}| \times 2&\text{otherwise}
\end{cases}
```

- Monomial integration.

```math
\begin{align}
  I_{k_1,\dots,k_n}
  &= \int_{C_n} x_1^{k_1}\cdots x_n^{k_n}\\
    &= \prod_i \frac{1 + (-1)^{k_i}}{k_i+1}
  =\begin{cases}
    0&\text{if any $k_i$ is odd}\\
    |C_n|&\text{if all $k_i=0$}\\
    I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times \frac{k_{i_0}-1}{k_{i_0}+1}&\text{if $k_{i_0} > 0$}
  \end{cases}
\end{align}
```

#### _n_-dimensional unit simplex

```math
 T_n = \left\{(x_1,\dots,x_n):x_i \geq 0, \sum_{i=1}^n x_i \leq 1\right\}
```

- Volume.

```math
|T_n| = \frac{1}{n!} = \begin{cases}
  1&\text{if $n=0$}\\
  |T_{n-1}| \times \frac{1}{n}&\text{otherwise}
\end{cases}
```

- Monomial integration.

```math
\begin{align}
  I_{k_1,\dots,k_n}
  &= \int_{T_n} x_1^{k_1}\cdots x_n^{k_n}\\
  &= \frac{\prod_i\Gamma(k_i + 1)}{\Gamma\left(n + 1 + \sum_i k_i\right)}\\
  &=\begin{cases}
    |T_n|&\text{if all $k_i=0$}\\
    I_{k_1,\dots,k_{i_0}-1,\dots,k_n} \times \frac{k_{i_0}}{n + \sum_i k_i}&\text{if $k_{i_0} > 0$}
  \end{cases}
\end{align}
```

#### Remark

Note that both numerator and denominator in the closed expression will assume very large
values even for polynomials of moderate degree. This can lead to difficulties when
evaluating the expression on a computer; the registers will overflow. A common
countermeasure is to use the log-gamma function,

```math
\frac{\prod_i\Gamma(k_i)}{\Gamma\left(\sum_i k_i\right)}
= \exp\left(\sum_i \ln\Gamma(k_i) - \ln\Gamma\left(\sum_i k_i\right)\right),
```

but a simpler and arguably more elegant solution is to use the recurrence. This holds
true for all such expressions in this note.

#### _n_-dimensional unit sphere (surface)

```math
U_n = \left\{(x_1,\dots,x_n): \sum_{i=1}^n x_i^2 = 1\right\}
```

- Volume.

```math
 |U_n|
 = \frac{n \sqrt{\pi}^n}{\Gamma(\frac{n}{2}+1)}
 = \begin{cases}
   2&\text{if $n = 1$}\\
   2\pi&\text{if $n = 2$}\\
   |U_{n-2}| \times \frac{2\pi}{n - 2}&\text{otherwise}
 \end{cases}
```

- Monomial integral.

```math
\begin{align*}
  I_{k_1,\dots,k_n}
  &= \int_{U_n} x_1^{k_1}\cdots x_n^{k_n}\\
  &= \frac{2\prod_i
    \Gamma\left(\frac{k_i+1}{2}\right)}{\Gamma\left(\sum_i \frac{k_i+1}{2}\right)}\\\\
  &=\begin{cases}
    0&\text{if any $k_i$ is odd}\\
    |U_n|&\text{if all $k_i=0$}\\
    I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times \frac{k_{i_0} - 1}{n - 2 + \sum_i k_i}&\text{if $k_{i_0} > 0$}
  \end{cases}
\end{align*}
```

#### _n_-dimensional unit ball

```math
S_n = \left\{(x_1,\dots,x_n): \sum_{i=1}^n x_i^2 \le 1\right\}
```

- Volume.

  ```math
  |S_n|
  = \frac{\sqrt{\pi}^n}{\Gamma(\frac{n}{2}+1)}
  = \begin{cases}
     1&\text{if $n = 0$}\\
     2&\text{if $n = 1$}\\
     |S_{n-2}| \times \frac{2\pi}{n}&\text{otherwise}
  \end{cases}
  ```

- Monomial integral.

```math
\begin{align}
  I_{k_1,\dots,k_n}
  &= \int_{S_n} x_1^{k_1}\cdots x_n^{k_n}\\
  &= \frac{2^{n + p}}{n + p} |S_n|
  =\begin{cases}
    0&\text{if any $k_i$ is odd}\\
    |S_n|&\text{if all $k_i=0$}\\
    I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times \frac{k_{i_0} - 1}{n + p}&\text{if $k_{i_0} > 0$}
  \end{cases}
\end{align}
```

with $p=\sum_i k_i$.

#### _n_-dimensional unit ball with Gegenbauer weight

$\lambda > -1$.

- Volume.

```math
    \begin{align}
    |G_n^{\lambda}|
      &= \int_{S^n} \left(1 - \sum_i x_i^2\right)^\lambda\\
      &= \frac{%
        \Gamma(1+\lambda)\sqrt{\pi}^n
      }{%
        \Gamma\left(1+\lambda + \frac{n}{2}\right)
      }
      = \begin{cases}
        1&\text{for $n=0$}\\
        B\left(\lambda + 1, \frac{1}{2}\right)&\text{for $n=1$}\\
        |G_{n-2}^{\lambda}|\times \frac{2\pi}{2\lambda + n}&\text{otherwise}
      \end{cases}
  \end{align}
```

- Monomial integration.

```math
\begin{align}
  I_{k_1,\dots,k_n}
    &= \int_{S^n} x_1^{k_1}\cdots x_n^{k_n} \left(1 - \sum_i x_i^2\right)^\lambda\\
    &= \frac{%
      \Gamma(1+\lambda)\prod_i \Gamma\left(\frac{k_i+1}{2}\right)
    }{%
      \Gamma\left(1+\lambda + \sum_i \frac{k_i+1}{2}\right)
    }\\
    &= \begin{cases}
      0&\text{if any $k_i$ is odd}\\
      |G_n^{\lambda}|&\text{if all $k_i=0$}\\
      I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times \frac{k_{i_0}-1}{2\lambda + n + \sum_i k_i}&\text{if $k_{i_0} > 0$}
    \end{cases}
\end{align}
```

#### _n_-dimensional unit ball with Chebyshev-1 weight

Gegenbauer with $\lambda=-\frac{1}{2}$.

- Volume.

```math
\begin{align}
|G_n^{-1/2}|
  &= \int_{S^n} \frac{1}{\sqrt{1 - \sum_i x_i^2}}\\
  &= \frac{%
    \sqrt{\pi}^{n+1}
  }{%
    \Gamma\left(\frac{n+1}{2}\right)
  }
  =\begin{cases}
    1&\text{if $n=0$}\\
    \pi&\text{if $n=1$}\\
    |G_{n-2}^{-1/2}| \times \frac{2\pi}{n-1}&\text{otherwise}
  \end{cases}
\end{align}
```

- Monomial integration.

```math
\begin{align}
I_{k_1,\dots,k_n}
  &= \int_{S^n} \frac{x_1^{k_1}\cdots x_n^{k_n}}{\sqrt{1 - \sum_i x_i^2}}\\
  &= \frac{%
    \sqrt{\pi} \prod_i \Gamma\left(\frac{k_i+1}{2}\right)
  }{%
    \Gamma\left(\frac{1}{2} + \sum_i \frac{k_i+1}{2}\right)
  }\\
  &= \begin{cases}
    0&\text{if any $k_i$ is odd}\\
    |G_n^{-1/2}|&\text{if all $k_i=0$}\\
    I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times \frac{k_{i_0}-1}{n-1 + \sum_i k_i}&\text{if $k_{i_0} > 0$}
  \end{cases}
\end{align}
```

#### _n_-dimensional unit ball with Chebyshev-2 weight

Gegenbauer with $\lambda = +\frac{1}{2}$.

- Volume.

```math
\begin{align}
|G_n^{+1/2}|
  &= \int_{S^n} \sqrt{1 - \sum_i x_i^2}\\
  &= \frac{%
    \sqrt{\pi}^{n+1}
  }{%
    2\Gamma\left(\frac{n+3}{2}\right)
  }
  = \begin{cases}
    1&\text{if $n=0$}\\
    \frac{\pi}{2}&\text{if $n=1$}\\
    |G_{n-2}^{+1/2}| \times \frac{2\pi}{n+1}&\text{otherwise}
  \end{cases}
\end{align}
```

- Monomial integration.

```math
\begin{align}
I_{k_1,\dots,k_n}
  &= \int_{S^n} x_1^{k_1}\cdots x_n^{k_n} \sqrt{1 - \sum_i x_i^2}\\
  &= \frac{%
    \sqrt{\pi}\prod_i \Gamma\left(\frac{k_i+1}{2}\right)
  }{%
    2\Gamma\left(\frac{3}{2} + \sum_i \frac{k_i+1}{2}\right)
  }\\
  &= \begin{cases}
    0&\text{if any $k_i$ is odd}\\
    |G_n^{+1/2}|&\text{if all $k_i=0$}\\
    I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times \frac{k_{i_0}-1}{n + 1 + \sum_i k_i}&\text{if $k_{i_0} > 0$}
  \end{cases}
\end{align}
```

#### _n_-dimensional generalized Cauchy volume

As appearing in the [Cauchy
distribution](https://en.wikipedia.org/wiki/Cauchy_distribution) and [Student's
_t_-distribution](https://en.wikipedia.org/wiki/Student%27s_t-distribution).

- Volume. $2 \lambda > n$.

```math
    \begin{align}
    |Y_n^{\lambda}|
      &= \int_{\mathbb{R}^n} \left(1 + \sum_i x_i^2\right)^{-\lambda}\\
      &= |U_{n-1}| \frac{1}{2} B(\lambda - \frac{n}{2}, \frac{n}{2})\\
      &= \begin{cases}
        1&\text{for $n=0$}\\
        B\left(\lambda - \frac{1}{2}, \frac{1}{2}\right)&\text{for $n=1$}\\
        |Y_{n-2}^{\lambda}|\times \frac{2\pi}{2\lambda - n}&\text{otherwise}
      \end{cases}
  \end{align}
```

- Monomial integration. $2 \lambda > n + \sum_i k_i$.

```math
\begin{align}
  I_{k_1,\dots,k_n}
    &= \int_{\mathbb{R}^n} x_1^{k_1}\cdots x_n^{k_n} \left(1 + \sum_i x_i^2\right)^{-\lambda}\\
    &= \frac{\Gamma(\frac{n+\sum k_i}{2}) \Gamma(\lambda - \frac{n - \sum k_i}{2})}{2 \Gamma(\lambda)}
       \times \frac{2\prod_i \Gamma(\tfrac{k_i+1}{2})}{\Gamma(\sum_i \tfrac{k_i+1}{2})}\\
    &= \begin{cases}
      0&\text{if any $k_i$ is odd}\\
      |Y_n^{\lambda}|&\text{if all $k_i=0$}\\
      I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times \frac{k_{i_0}-1}{2\lambda - \left(n + \sum_i k_i\right)}&\text{if $k_{i_0} > 0$}
    \end{cases}
\end{align}
```

#### _n_-dimensional generalized Laguerre volume

$\alpha > -1$.

- Volume

```math
\begin{align}
  V_n
    &= \int_{\mathbb{R}^n} \left(\sqrt{x_1^2+\cdots+x_n^2}\right)^\alpha \exp\left(-\sqrt{x_1^2+\dots+x_n^2}\right)\\
    &= \frac{2 \sqrt{\pi}^n \Gamma(n+\alpha)}{\Gamma(\frac{n}{2})}
  = \begin{cases}
    2\Gamma(1+\alpha)&\text{if $n=1$}\\
    2\pi\Gamma(2 + \alpha)&\text{if $n=2$}\\
    V_{n-2} \times \frac{2\pi(n+\alpha-1) (n+\alpha-2)}{n-2}&\text{otherwise}
  \end{cases}
\end{align}
```

- Monomial integration.

```math
  \begin{align}
  I_{k_1,\dots,k_n}
  &= \int_{\mathbb{R}^n} x_1^{k_1}\cdots x_n^{k_n}
    \left(\sqrt{x_1^2+\dots+x_n^2}\right)^\alpha \exp\left(-\sqrt{x_1^2+\dots+x_n^2}\right)\\
  &= \frac{%
    2 \Gamma\left(\alpha + n + \sum_i k_i\right)
    \left(\prod_i \Gamma\left(\frac{k_i + 1}{2}\right)\right)
  }{%
    \Gamma\left(\sum_i \frac{k_i + 1}{2}\right)
  }\\
  &=\begin{cases}
    0&\text{if any $k_i$ is odd}\\
    V_n&\text{if all $k_i=0$}\\
    I_{k_1,\dots,k_{i_0}-2,\ldots,k_n} \times \frac{%
      (\alpha + n + p - 1) (\alpha + n + p - 2) (k_{i_0} - 1)
    }{%
        n + p - 2
    }&\text{if $k_{i_0} > 0$}
  \end{cases}
\end{align}
```

with $p=\sum_i k_i$.

#### _n_-dimensional Hermite (physicists')

- Volume.

```math
\begin{align}
  V_n
  &= \int_{\mathbb{R}^n} \exp\left(-(x_1^2+\cdots+x_n^2)\right)\\
  &= \sqrt{\pi}^n
   = \begin{cases}
     1&\text{if $n=0$}\\
     \sqrt{\pi}&\text{if $n=1$}\\
     V_{n-2} \times \pi&\text{otherwise}
   \end{cases}
\end{align}
```

- Monomial integration.

```math
\begin{align}
    I_{k_1,\dots,k_n}
    &= \int_{\mathbb{R}^n} x_1^{k_1}\cdots x_n^{k_n} \exp(-(x_1^2+\cdots+x_n^2))\\
    &= \prod_i \frac{(-1)^{k_i} + 1}{2} \times \Gamma\left(\frac{k_i+1}{2}\right)\\
    &=\begin{cases}
      0&\text{if any $k_i$ is odd}\\
      V_n&\text{if all $k_i=0$}\\
      I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times \frac{k_{i_0} - 1}{2}&\text{if $k_{i_0} > 0$}
    \end{cases}
\end{align}
```

#### _n_-dimensional Hermite (probabilists')

- Volume.

```math
V_n = \frac{1}{\sqrt{2\pi}^n} \int_{\mathbb{R}^n}
\exp\left(-\frac{1}{2}(x_1^2+\cdots+x_n^2)\right) = 1
```

- Monomial integration.

```math
\begin{align}
  I_{k_1,\dots,k_n}
    &= \frac{1}{\sqrt{2\pi}^n} \int_{\mathbb{R}^n} x_1^{k_1}\cdots x_n^{k_n}
    \exp\left(-\frac{1}{2}(x_1^2+\cdots+x_n^2)\right)\\
  &= \prod_i \frac{(-1)^{k_i} + 1}{2} \times
    \frac{2^{\frac{k_i+1}{2}}}{\sqrt{2\pi}} \Gamma\left(\frac{k_i+1}{2}\right)\\
  &=\begin{cases}
    0&\text{if any $k_i$ is odd}\\
    V_n&\text{if all $k_i=0$}\\
    I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times (k_{i_0} - 1)&\text{if $k_{i_0} > 0$}
  \end{cases}
\end{align}
```
