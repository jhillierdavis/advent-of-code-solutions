
"""
CRT (Chinese Number Therom) from AI (LLM) via CoPilot (see https://copilot.microsoft.com/chats )
Prompt: "Implement CRT in python"

# Ref.: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
"""

def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find modular inverse"""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return gcd, x, y


def mod_inverse(a, m):
    """Find modular inverse of a modulo m"""
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"No modular inverse for {a} mod {m}")
    return x % m


def chinese_remainder_theorem(remainders, moduli):
    """Solve system of congruences using CRT"""
    if len(remainders) != len(moduli):
        raise ValueError("Lists must be of equal length")

    N = 1
    for mod in moduli:
        N *= mod

    result = 0
    for ai, ni in zip(remainders, moduli):
        Ni = N // ni
        inverse = mod_inverse(Ni, ni)
        result += ai * Ni * inverse

    return result % N

"""
# Example usage
remainders = [2, 3, 2]
moduli = [3, 5, 7]
solution = chinese_remainder_theorem(remainders, moduli)
print(f"Solution: x ≡ {solution} (mod {3*5*7})")
"""
