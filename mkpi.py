
def n_pi(n):
    s = 0
    for k in range(n + 1):
        q, w, e, r = (8 * k + 1, 8 * k + 4, 8 * k + 5, 8 * k + 6)
        s += 4 * (pow(16, n - k, q) / q) - 2 * (pow(16, n - k, w) / w) - (pow(16, n - k, e) / e) - (pow(16, n - k, r) / r)
    return hex(int((s * 16) % 16))[2:]


print(n_pi(0), n_pi(1), (-5.86666 * 16) % 16)