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
    return 0

def main() -> int:
    print("Welcome to shitbench")
    print("Copyright (C)2026 Zhuo Jiayan")
    print("This program licensed under Mozilla Public License version 2.0")
    print("Please choose a mode:")
    print("1. bench")
    try:
        mode = int(input())
    except ValueError:
        quit()
        
    if mode == 1:
        print("We'll test:")
        print("1. CPU")
        print("2. RAM")
        print("3. VRM")
        print("Disclaimer of Warranty(From MPL)")
        print("Covered Software is provided under this License on an \"as is\" basis, without warranty of any kind, either expressed, implied, or statutory, including, without limitation, warranties that the Covered Software is free of defects, merchantable, fit for a particular purpose or non-infringing. The entire risk as to the quality and performance of the Covered Software is with You. Should any Covered Software prove defective in any respect, You (not any Contributor) assume the cost of any necessary servicing, repair, or correction. This disclaimer of warranty constitutes an essential part of this License. No use of any Covered Software is authorized under this License except under this disclaimer.")
        print("Limitation of Liability(From MPL)")
        print("Under no circumstances and under no legal theory, whether tort (including negligence), contract, or otherwise, shall any Contributor, or anyone who distributes Covered Software as permitted above, be liable to You for any direct, indirect, special, incidental, or consequential damages of any character including, without limitation, damages for lost profits, loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses, even if such party shall have been informed of the possibility of such damages. This limitation of liability shall not apply to liability for death or personal injury resulting from such party's negligence to the extent applicable law prohibits such limitation. Some jurisdictions do not allow the exclusion or limitation of incidental or consequential damages, so this exclusion and limitation may not apply to You.")
                
        if input("Can you accept the Disclaimer of Warranty and Limitation of Liability?(y/n)") == "y":
            cores: int = psutil.cpu_count()
            try:
                core: int = int(input(f"Please choose you want run the benchmark's CPU core:(0 ~ {cores - 1})"))
            except Exception as Error:
                print(f"There is an error in choose CPU core:{Error}")
                quit()
            print("Running the shit code......")
            p = psutil.Process()
            try:
                p.cpu_affinity([core])
            except Exception as Error:
                print(f"There is an error in choose CPU core:{Error}")
                quit()
            CPU()
            RAM()
            VRM()
            input("Press enter to quit")
            quit()
        else:
            quit()
    else:
        quit()

if __name__ == "__main__":
    main()
