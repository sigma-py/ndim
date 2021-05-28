import sympy


def volume(n, symbolic=False):
    n = sympy.S(n) if symbolic else n

    def _recurrence(n):
        if n == 0:
            return 1
        return _recurrence(n - 1) / n

    return _recurrence(n)


def integrate_monomial(exponents, symbolic=False):
    """The integrals of monomials over the standard triangle and tetrahedron are
    given by

    \\int_T x_0^k0 * x1^k1 = (k0!*k1!) / (2+k0+k1)!,
    \\int_T x_0^k0 * x1^k1 * x2^k2 = (k0!*k1!*k2!) / (3+k0+k1+k2)!,

    see, e.g.,
    A set of symmetric quadrature rules on triangles and tetrahedra,
    Linbo Zhang, Tao Cui and Hui Liu,
    Journal of Computational Mathematics,
    Vol. 27, No. 1 (January 2009), pp. 89-96,
    <https://www.jstor.org/stable/43693493>.

    See, e.g., <https://math.stackexchange.com/q/207073/36678> for a formula in
    all dimensions.

    To cope with the huge terms in numerator and denominator, it might make sense to use
    exp(lgamma()). It's even easier though to represent the above expression by the
    recurrence with the simple factor k_i / (sum(k) + n) which will never overflow. It's
    also well-suited for symbolic computation.
    """
    frac = sympy.Rational if symbolic else lambda a, b: a / b
    exponents = list(exponents)
    n = len(exponents)

    def _recurrence(exponents):
        if all(k == 0 for k in exponents):
            return volume(n, symbolic)

        # find first nonzero
        idx, k0 = next((i, k) for i, k in enumerate(exponents) if k > 0)
        k2 = exponents.copy()
        k2[idx] -= 1
        return _recurrence(k2) * frac(k0, sum(exponents) + n)

    return _recurrence(exponents)
