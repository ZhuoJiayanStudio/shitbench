# This Source Code Form is subject to the terms of the Mozilla Public License version 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

import time
import sys

def VRM() -> int:
    theTime: int = time.time()
    sys.set_int_max_str_digits(1000000)
    for i in range(20):
        99999 ** 99999
        time.sleep(0.05)
    return int(10000 // (time.time() - theTime))
