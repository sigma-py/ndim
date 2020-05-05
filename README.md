## Volumes and integrals without the Gamma function

[![green-pi](https://img.shields.io/badge/Rendered%20with-Green%20Pi-00d571?style=flat-square)](https://github.com/nschloe/green-pi?activate&inlineMath=$)

  Description | Closed form   | recurrence
|:-----------:|:-------------:|:-----------:|
Volume of a unit $n$-ball | $$V_n = \frac{\sqrt{\pi}^n}{\Gamma(\frac{n}{2}+1)}$$ | $$V_n = V_{n-2} \times \frac{2\pi}{n},\quad V_0 = 1,\quad V_1 = 2$$
Surface of a unit $n$-sphere | $$S_{n-1} = \frac{n \sqrt{\pi}^n}{\Gamma(\frac{n}{2}+1)}$$ | $$S_n = S_{n-2} \times \frac{2\pi}{n - 1},\quad S_0 = 2,\quad S_1 = 2\pi$$
$$\int_{\mathbb{R}^n} \exp\left(-\sqrt{x_1^2+\dots+x_n^2}\right)$$ | $$E_n = \frac{2 \sqrt{\pi}^n \Gamma(n)}{\Gamma(\frac{n}{2})}$$ | $$E_n = E_{n-2} \times 2\pi(n-1), \quad E_0=1, \quad E_1=2$$
$$\int_{\mathbb{R}^n} \exp\left(-\frac{1}{2}(x_1^2+\dots+x_n^2)\right)$$ | $$E^{(2)}_n = \sqrt{2\pi}^n$$ | $$E_n = E_{n-2} \times 2\pi, \quad E_0=1, E_1=\sqrt{2\pi}$$ or $$E_n = E_{n-1} \times \sqrt{2\pi}, \quad E_0=1$$


  Description | Closed form   | recurrence
|:-----------:|:-------------:|:-----------:|
$$\int_{-1}^1 \frac{x^k}{\sqrt{1 - x^2}} \,dx$$ | $$I_0 =\pi, \quad I_k = \frac{\sqrt{\pi} ((-1)^k + 1)  \Gamma(\frac{k+1}{2})}{k\Gamma(\frac{k}{2})}$$ | $$I_n = I_{n-2} \times \frac{k-1}{k},\quad I_0 = \pi,\quad I_1 = 0$$
