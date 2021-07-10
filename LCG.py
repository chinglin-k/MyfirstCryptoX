from functools import reduce
from Crypto.Util.number import GCD


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(GCD, zeroes))
    return crack_unknown_multiplier(states, modulus)

def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment

def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * modinv(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)

def next_state(s0, m, inc, N):
    return (m*s0 + inc) % N

states = [15017509946098832771
,15124579160039492440
,15472925640891320616
,38114629134274242
,2948866201570354398
,3753737287032175650
,15046504952114087560
,194647690542408530
,1225780854132722636
,4013014980629339934
,13449159198226705850
,14220130235020001721
,13183859804543703356
,11850731162465520686
,8189996643791134442
,11962273554780984216
,11975201758538349117
,1433420360059014742
,16167029535121166235
,4937294321112803794]
N, m, c = crack_unknown_modulus(states)

states = states[-1]
for i in range(100) :
    seed = next_state(seed, m, c, N)
    states.append(seed)

print(f"BreakAll{{{states[100]}}}")

#BreakAll{9188636602399943250}
