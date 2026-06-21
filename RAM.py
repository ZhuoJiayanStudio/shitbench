# This Source Code Form is subject to the terms of the Mozilla Public License version 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time

def RAM() -> int:
    theTime = time.time()
    a = [100000]
    for i in range(1, 100000):
        a.append(i)
    for i in range(1, 100001):
        a.append(a[0])
        a.pop(0)
    return int(10000 // (time.time() - theTime))
