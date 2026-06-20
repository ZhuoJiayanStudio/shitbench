# This Source Code Form is subject to the terms of the Mozilla Public License version 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

try:
    import psutil
    import time
    import sys
except Exception as Error:
    print(f"There an error in import:{Error}")
    quit()

def is_sushu(aa) -> bool:
    for i in range(2, int(aa ** 0.5) + 1):
        if aa % i == 0:
            return False
    return True

def CPU() -> int:
    n: int = 5000
    theTime: int = time.time()
    for i in range(4, n + 1, 2):
        b: bool = True
        for j in range(2, i + 1):
            if b == True and is_sushu(j):
                for k in range(2, i + 1):
                    if b == True and is_sushu(k):
                        if j + k == i:
                            b = False
    print(f"The CPU's score is {int(10000 // (time.time() - theTime))}/10000")
    return 0

def RAM() -> int:
    theTime = time.time()
    a = [100000]
    for i in range(1, 100000):
        a.append(i)
    for i in range(1, 100001):
        a.append(a[0])
        a.pop(0)
    print(f"The RAM's score is {int(10000 // (time.time() - theTime))}/10000")
    return 0
def VRM() -> int:
    theTime: int = time.time()
    sys.set_int_max_str_digits(1000000)
    for i in range(20):
        99999 ** 99999
        time.sleep(0.05)
    print(f"The VRM's score is {int(10000 // (time.time() - theTime))}/10000")

def main() -> int:
    print("Welcome to shitbench")
    print("Copyright (C)2026 Zhuo Jiayan")
    print("This program licensed under Mozilla Public License version 2.0")
    print("We'll test:")
    print("1. CPU")
    print("2. RAM")
    print("3. VRM")
    p = psutil.Process()
    p.cpu_affinity([0])
    if input("OK?(Press \"OK\")") == "OK":
        print("Running the shit code......")
        CPU()
        RAM()
        VRM()
        input("Press enter to quit")
        quit()
    else:
        quit()

if __name__ == "__main__":
    main()
