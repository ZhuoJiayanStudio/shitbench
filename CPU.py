# This Source Code Form is subject to the terms of the Mozilla Public License version 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
import psutil

def is_sushu(aa) -> bool:
    for i in range(2, int(aa ** 0.5) + 1):
        if aa % i == 0:
            return False
    return True

def CPU() -> int:
    p = psutil.Process()
    p.cpu_affinity([0])
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
    return int(10000 // (time.time() - theTime))
