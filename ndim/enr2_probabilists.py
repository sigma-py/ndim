"""
exp(-(x_1^2 + ... + x_n^2)/2) / sqrt(2*pi) ** n
"""


def volume(n):
    return 1


def integrate_monomial(exponents):
    if any(k % 2 == 1 for k in exponents):
        return 0

    if all(k == 0 for k in exponents):
        n = len(exponents)
        return volume(n)

    # find first nonzero
    idx, k0 = next((i, k) for i, k in enumerate(exponents) if k > 0)
    k2 = exponents.copy()
    k2[idx] -= 2
    return integrate_monomial(k2) * (k0 - 1)
