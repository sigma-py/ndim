## Volumes and integrals without the Gamma function

[![green-pi](https://img.shields.io/badge/Rendered%20with-Green%20Pi-00d571?style=flat-square)](https://github.com/nschloe/green-pi?activate&inlineMath=$)


## _n_-dimensional unit sphere
$$
  U_n = \left\\{(x_1,\dots,x_n): \sum_{i=1}^n x_i^2 = 1\right\\}
$$

 * Volume.
 $$
  |U_n|
  = \frac{n \sqrt{\pi}^n}{\Gamma(\frac{n}{2}+1)}
  = \begin{cases}
    2&\text{if $n = 1$}\\\\
    2\pi&\text{if $n = 2$}\\\\
    |U_{n-2}| \times \frac{2\pi}{n - 2}&\text{otherwise}
  \end{cases}
  $$
  * Monomial integral.
  $$
  \begin{align*}
    I_{k_1,\dots,k_n}
    &= \int_{U_n} x_1^{k_1}\cdots x_n^{k_n}\\\\
    &= \frac{2\prod_{i=1}^n
      \Gamma\left(\frac{k_i+1}{2}\right)}{\Gamma\left(\sum_{i=1}^n\frac{k_i+1}{2}\right)}\label{sphere:closed}\\\\
    &=\begin{cases}
      0&\text{if any $k_i$ is odd}\\\\
      |U_n|&\text{if all $k_i=0$}\\\\
      I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times \frac{k_{i_0} - 1}{n - 2 + \sum_{i=1}^n k_i}&\text{if $k_{i_0} > 0$}
    \end{cases}
  \end{align*}
  $$


## _n_-dimensional unit ball
$$
  S_n = \left\\{(x_1,\dots,x_n): \sum_{i=1}^n x_i^2 \le 1\right\\}
$$

* Volume.
  $$
  |S_n|
  = \frac{\sqrt{\pi}^n}{\Gamma(\frac{n}{2}+1)}
  = \begin{cases}
     1&\text{if $n = 0$}\\\\
     2&\text{if $n = 1$}\\\\
     |S_{n-2}| \times \frac{2\pi}{n}&\text{otherwise}
  \end{cases}
  $$

* Monomial integral.
$$
\begin{align}\nonumber
  I_{k_1,\dots,k_n}
  &= \int_{S_n} x_1^{k_1}\cdots x_n^{k_n}\\\\
  &= \frac{2^{n + p}}{n + p} |S_n|
  =\begin{cases}
    0&\text{if any $k_i$ is odd}\\\\
    |S_n|&\text{if all $k_i=0$}\\\\
    I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times \frac{k_{i_0} - 1}{n - 2 + p}&\text{if $k_{i_0} > 0$}
  \end{cases}
\end{align}
$$
with $p=\sum_{i=1}^n k_i$.


## _n_-dimensional unit ball with Gegenbauer weight
  $\lambda > -1$.

* Volume.
$$
    \begin{align}\nonumber
    |G_n^{\lambda}|
      &= \int_{S^n} \left(1 - \sum_{i=1}^n x_i^2\right)^\lambda\\\\
      &= \frac{%
        \Gamma(1+\lambda)\sqrt{\pi}^n
      }{%
        \Gamma\left(1+\lambda + \frac{n}{2}\right)
      }
      = \begin{cases}
        1&\text{for $n=0$}\\\\
        \frac{\Gamma(1+\lambda)\sqrt{\pi}}{\Gamma\left(\frac{3}{2} + \lambda\right)}&\text{for $n=1$}\\\\
        |G_{n-2}^{\lambda}|\times \frac{2\pi}{2\lambda + n}&\text{otherwise}
      \end{cases}
  \end{align}
$$
* Monomial integration.
$$
  \begin{align}\nonumber
    I_{k_1,\dots,k_n}
      &= \int_{S^n} x_1^{k_1}\cdots x_n^{k_n} \left(1 - \sum_{i=1}^n
      x_i^2\right)^\lambda\\\\
      &= \frac{%
        \Gamma(1+\lambda)\prod_{i=1}^n \Gamma\left(\frac{k_i+1}{2}\right)
      }{%
        \Gamma\left(1+\lambda + \sum_{i=1}^n \frac{k_i+1}{2}\right)
      }\\\\
      &= \begin{cases}
        0&\text{if any $k_i$ is odd}\\\\
        |G_n^{\lambda}|&\text{if all $k_i=0$}\\\\
        I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times \frac{k_{i_0}-1}{2\lambda + n + \sum_{i=1}^n k_i}&\text{if $k_{i_0} > 0$}
      \end{cases}
  \end{align}
$$

## _n_-dimensional unit ball with Chebyshev-1 weight
Gegenbauer with $\lambda=-\frac{1}{2}$.

* Volume.
$$
    \begin{align}\nonumber
    |G_n^{-1/2}|
      &= \int_{S^n} \frac{1}{\sqrt{1 - \sum_{i=1}^n x_i^2}}\\\\
      &= \frac{%
        \sqrt{\pi}^{n+1}
      }{%
        \Gamma\left(\frac{n+1}{2}\right)
      }
      =\begin{cases}
        1&\text{if $n=0$}\\\\
        \pi&\text{if $n=1$}\\\\
        |G_{n-2}^{-1/2}| \times \frac{2\pi}{n-1}&\text{otherwise}
      \end{cases}
    \end{align}
$$
* Monomial integration.
$$
    \begin{align}\nonumber
    I_{k_1,\dots,k_n}
      &= \int_{S^n} \frac{x_1^{k_1}\cdots x_n^{k_n}}{\sqrt{1 - \sum_{i=1}^n x_i^2}}\\\\
      &= \frac{%
        \sqrt{\pi} \prod_{i=1}^n \Gamma\left(\frac{k_i+1}{2}\right)
      }{%
        \Gamma\left(\frac{1}{2} + \sum_{i=1}^n \frac{k_i+1}{2}\right)
      }\\
      &= \begin{cases}
        0&\text{if any $k_i$ is odd}\\\\
        |G_n^{-1/2}|&\text{if all $k_i=0$}\\\\
        I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times \frac{k_{i_0}-1}{n-1 + \sum_{i=1}^n k_i}&\text{if $k_{i_0} > 0$}
      \end{cases}
    \end{align}
$$


$$ _n_-dimensional unit ball with Chebyshev-2 weight
Gegenbauer with $\lambda = +\frac{1}{2}$.

* Volume.
$$
    \begin{align}\nonumber
    |G_n^{+1/2}|
      &= \int_{S^n} \sqrt{1 - \sum_{i=1}^n x_i^2}\\\\
      &= \frac{%
        \sqrt{\pi}^{n+1}
      }{%
        2\Gamma\left(\frac{n+3}{2}\right)
      }
      = \begin{cases}
        1&\text{if $n=0$}\\\\
        \frac{\pi}{2}&\text{if $n=1$}\\\\
        |G_{n-2}^{+1/2}| \times \frac{2\pi}{n+1}&\text{otherwise}
      \end{cases}
    \end{align}
$$
* Monomial integration.
$$
    \begin{align}\nonumber
    I_{k_1,\dots,k_n}
      &= \int_{S^n} x_1^{k_1}\cdots x_n^{k_n} \sqrt{1 - \sum_{i=1}^n
      x_i^2}\\\\
      &= \frac{%
        \sqrt{\pi}\prod_{i=1}^n \Gamma\left(\frac{k_i+1}{2}\right)
      }{%
        2\Gamma\left(\frac{3}{2} + \sum_{i=1}^n \frac{k_i+1}{2}\right)
      }\\
      &= \begin{cases}
        0&\text{if any $k_i$ is odd}\\\\
        |G_n^{+1/2}|&\text{if all $k_i=0$}\\\\
        I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times \frac{k_{i_0}-1}{n + 1 + \sum_{i=1}^n k_i}&\text{if $k_{i_0} > 0$}
      \end{cases}
    \end{align}
$$

## _n_-dimensional generalized Laguerre volume

$\alpha > -1$.

* Volume
$$
    \begin{align}\nonumber
  V_n
    &= \int_{\mathbb{R}^n} \left(\sqrt{x_1^2+\cdots+x_n^2}\right)^\alpha \exp\left(-\sqrt{x_1^2+\dots+x_n^2}\right)\\\\
    &= \frac{2 \sqrt{\pi}^n \Gamma(n+\alpha)}{\Gamma(\frac{n}{2})}
  = \begin{cases}
    2\Gamma(1+\alpha)&\text{if $n=1$}\\\\
    2\pi\Gamma(2 + \alpha)&\text{if $n=2$}\\\\
    V_{n-2} \times \frac{2\pi(n+\alpha-1) (n+\alpha-2)}{n-2}&\text{otherwise}
  \end{cases}
\end{align}
$$
* Monomial integration.
$$
  \begin{align}\nonumber
  I_{k_1,\dots,k_n}
  &= \int_{\mathbb{R}^n} x_1^{k_1}\cdots x_n^{k_n}
    \left(\sqrt{x_1^2+\dots+x_n^2}\right)^\alpha \exp\left(-\sqrt{x_1^2+\dots+x_n^2}\right)\\\\
  &= \frac{%
    2 \Gamma\left(\alpha + n + \sum_{i=1}^n k_i\right)
    \left(\prod_{i=1}^n\Gamma\left(\frac{k_i + 1}{2}\right)\right)
  }{%
    \Gamma\left(\sum_{i=1}^n\frac{k_i + 1}{2}\right)
  }\\\\
  &=\begin{cases}
    0&\text{if any $k_i$ is odd}\\\\
    V_n&\text{if all $k_i=0$}\\\\
    I_{k_1,\dots,k_{i_0}-2,\ldots,k_n} \times \frac{%
      (\alpha + n + p - 1) (\alpha + n + p - 2) (k_{i_0} - 1)
    }{%
        n + p - 2
    }&\text{if $k_{i_0} > 0$}
  \end{cases}
\end{align}
$$
with $p=\sum_{k=1}^n k_i$.

## _n_-dimensional Hermite (physicists')
* Volume.
$$
\begin{align}\nonumber
  V_n
  &= \int_{\mathbb{R}^n} \exp\left(-(x_1^2+\cdots+x_n^2)\right)\\\\
  &= \sqrt{\pi}^n
   = \begin{cases}
     1&\text{if $n=0$}\\\\
     \sqrt{\pi}&\text{if $n=1$}\\\\
     V_{n-2} \times \pi&\text{otherwise}
   \end{cases}
\end{align}
$$

* Monomial integration.
$$
\begin{align}\nonumber
    I_{k_1,\dots,k_n}
    &= \int_{\mathbb{R}^n} x_1^{k_1}\cdots x_n^{k_n} \exp(-(x_1^2+\cdots+x_n^2))\\\\
    &= \prod_{i=1}^n \frac{(-1)^{k_i} + 1}{2} \times \Gamma\left(\frac{k_i+1}{2}\right)\\\\
    &=\begin{cases}
      0&\text{if any $k_i$ is odd}\\\\
      V_n&\text{if all $k_i=0$}\\\\
      I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times \frac{k_{i_0} - 1}{2}&\text{if $k_{i_0} > 0$}
    \end{cases}
\end{align}
\end{itemize}
$$


## _n_-dimensional Hermite (probabilists')

* Volume.
$$
    V_n = \frac{1}{\sqrt{2\pi}^n} \int_{\mathbb{R}^n}
    \exp\left(-\frac{1}{2}(x_1^2+\cdots+x_n^2)\right) = 1
$$

* Monomial integration.
$$
  \begin{align}\nonumber
    I_{k_1,\dots,k_n}
      &= \frac{1}{\sqrt{2\pi}^n} \int_{\mathbb{R}^n} x_1^{k_1}\cdots x_n^{k_n}
      \exp\left(-\frac{1}{2}(x_1^2+\cdots+x_n^2)\right)\\\\
    &= \prod_{i=1}^n \frac{(-1)^{k_i} + 1}{2} \times
      \frac{2^{\frac{k_i+1}{2}}}{\sqrt{2\pi}} \Gamma\left(\frac{k_i+1}{2}\right)\\\\
    &=\begin{cases}
      0&\text{if any $k_i$ is odd}\\\\
      V_n&\text{if all $k_i=0$}\\\\
      I_{k_1,\dots,k_{i_0}-2,\dots,k_n} \times (k_{i_0} - 1)&\text{if $k_{i_0} > 0$}
    \end{cases}
  \end{align}
\end{itemize}
$$
