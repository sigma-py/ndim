## Volumes and integrals without the Gamma function

[![green-pi](https://img.shields.io/badge/Rendered%20with-Green%20Pi-00d571?style=flat-square)](https://github.com/nschloe/green-pi?activate&inlineMath=$)

 x        | Closed form   | recurrence
|:-------:|:-------------:|:-----------:|
Volume of a unit $n$-ball | $$V_n = \frac{\sqrt{\pi}^n}{\Gamma(\frac{n}{2}+1)}$$ | $$V_n = V_{n-2} \frac{2\pi}{n},\quad V_0 = 1,\quad V_1 = 2$$
Surface of a unit $n$-sphere | $$S_{n-1} = \frac{n \sqrt{\pi}^n}{\Gamma(\frac{n}{2}+1)}$$ | $$S_n = S_{n-2} \frac{2\pi}{n - 1},\quad S_0 = 2,\quad S_1 = 2\pi$$
$$\int_{\mathbb{R}^n} \exp(-\sqrt(x_1+\dots+x_n))$$ | $$E_n = \frac{2 \sqrt(\pi)^n \Gamma(n)}{\Gamma(frac{n}{2})}$$ | $$E_n = E_{n-2} 2\pi(n-1), \quad E_1=2, \quad E_2=2\pi$$
