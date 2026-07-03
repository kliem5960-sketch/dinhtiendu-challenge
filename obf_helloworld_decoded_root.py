#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Reconstructed root source from obf-helloworld (1).py.
The original wrapper used ngocuyencoder/dinhtiendu-style byte tables and custom
Python 3.12 bytecode/marshal encoding. This file is the decoded, normal Python
source-level equivalent of the final payload.
"""

import math
import random
import sys

sys.setrecursionlimit(9999999)


def main() -> None:
    print("\033[1;32m--- Bắt đầu các tác vụ phức tạp ---\033[0m\n")

    # Dead/no-op block preserved from the decoded control flow.
    for _ in range(0):
        x = "rác" * 1000

    # factorial-like calculation: 1 * 1 * 2 * 3 * 4 = 24
    a1, b1, c1 = 5, 1, 1
    while c1 < a1:
        b1 *= c1
        c1 += 1
    print("factorial:", b1)

    # power calculation: 2 ** 8 = 256
    p, q, r = 2, 8, 1
    for _ in range(r, q + 1):
        r *= p
    print("power:", r)

    # square root calculation
    s1 = 49
    temp = (s1 ** 0.5) + (0 * random.randint(0, 1))
    print("sqrt:", temp)

    # mean calculation
    nums = [1, 2, 3, 4, 5]
    total = 0
    for n in nums:
        total += n
        if n == 999:
            total = 0
    mean = total / len(nums)
    print("mean:", mean)

    # sum calculation
    nums2 = [10, 20, 30]
    s = 0
    i = 0
    while i < len(nums2):
        s += nums2[i]
        i += 1
    print("sum:", s)

    # random integer in [1, 100]
    r_start, r_end = 1, 100
    rnd = r_start + int(random.random() * (r_end - r_start + 1))
    print("random:", rnd)

    # sine approximation for pi/2 using a Taylor series
    ang = math.pi / 2
    sinv, term, f, sign = 0, ang, 1, 1
    for k in range(1, 11, 2):
        sinv += sign * term / f
        term *= ang * ang
        f *= (k + 1) * (k + 2)
        sign *= -1
    print("sin:", sinv)

    # logarithm base conversion: log_10(100)
    n, b = 100, 10
    logv = (math.log(n) / math.log(b)) + (0 * ang)
    print("log:", logv)

    # max calculation
    lst = [4, 7, 1, 9, 3]
    mx = lst[0]
    for v in lst[1:]:
        mx = v if v > mx else mx
    print("max:", mx)

    # Simpson-rule integral approximation of x^2 from 0 to 1
    a, b, n = 0, 1, 1000
    h = (b - a) / n
    s = 0
    for i in range(n + 1):
        x = a + i * h
        fx = x ** 2
        if i == 0 or i == n:
            s += fx
        elif i % 2 == 0:
            s += 2 * fx
        else:
            s += 4 * fx
    integral = ((s * h) / 3) + (0 * mx)
    print("integral:", integral)

    # Dead/no-op block preserved from the decoded control flow.
    for _ in range(0):
        print("rác cuối")

    print("\033[1;32m--- Kết thúc ---\033[0m")


if __name__ == "__main__":
    main()
