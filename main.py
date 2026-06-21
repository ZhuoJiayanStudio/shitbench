# This Source Code Form is subject to the terms of the Mozilla Public License version 2.0.
# If a copy of the MPL was not distributed with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

from InquirerPy import inquirer
from InquirerPy.base import Choice
import CPU
import RAM
import VRM
import os

def main() -> int:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
      _     _ _   _                     _     
     | |   (_) | | |                   | |    
  ___| |__  _| |_| |__   ___ _ __   ___| |__  
 / __| '_ \| | __| '_ \ / _ \ '_ \ / __| '_ \ 
 \__ \ | | | | |_| |_) |  __/ | | | (__| | | |
 |___/_| |_|_|\__|_.__/ \___|_| |_|\___|_| |_|
                                              
                                              
""")
        print("Copyright (C)2026 Zhuo Jiayan")
        print("This program licensed under Mozilla Public License version 2.0")
        mode = inquirer.select(
            message="Please choose a mode",
            choices=[
                Choice(value=0, name="Exit"),
                Choice(value=1, name="1. Benchmark")
            ],
        ).execute()
        if mode == 0:
            if inquirer.confirm(message="Do you want to exit?").execute():
                break
        if mode == 1:
            print("we'll test:")
            print("1. CPU")
            print("2. RAM")
            print("3. VRM")
            print("""
************************************************************************
*                                                                      *
*  6. Disclaimer of Warranty                                           *
*  -------------------------                                           *
*                                                                      *
*  Covered Software is provided under this License on an "as is"       *
*  basis, without warranty of any kind, either expressed, implied, or  *
*  statutory, including, without limitation, warranties that the       *
*  Covered Software is free of defects, merchantable, fit for a        *
*  particular purpose or non-infringing. The entire risk as to the     *
*  quality and performance of the Covered Software is with You.        *
*  Should any Covered Software prove defective in any respect, You     *
*  (not any Contributor) assume the cost of any necessary servicing,   *
*  repair, or correction. This disclaimer of warranty constitutes an   *
*  essential part of this License. No use of any Covered Software is   *
*  authorized under this License except under this disclaimer.         *
*                                                                      *
************************************************************************

************************************************************************
*                                                                      *
*  7. Limitation of Liability                                          *
*  --------------------------                                          *
*                                                                      *
*  Under no circumstances and under no legal theory, whether tort      *
*  (including negligence), contract, or otherwise, shall any           *
*  Contributor, or anyone who distributes Covered Software as          *
*  permitted above, be liable to You for any direct, indirect,         *
*  special, incidental, or consequential damages of any character      *
*  including, without limitation, damages for lost profits, loss of    *
*  goodwill, work stoppage, computer failure or malfunction, or any    *
*  and all other commercial damages or losses, even if such party      *
*  shall have been informed of the possibility of such damages. This   *
*  limitation of liability shall not apply to liability for death or   *
*  personal injury resulting from such party's negligence to the       *
*  extent applicable law prohibits such limitation. Some               *
*  jurisdictions do not allow the exclusion or limitation of           *
*  incidental or consequential damages, so this exclusion and          *
*  limitation may not apply to You.                                    *
*                                                                      *
************************************************************************
""")
            if inquirer.confirm(message="Can you accept the Disclaimer of Warranty and Limitation of Liability?").execute():
                print("Running the shit code, please wait")
                print(f"Your CPU's score is {CPU.CPU()}/10000")
                print(f"Your RAM's score is {RAM.RAM()}/10000")
                print(f"Your VRM's score is {VRM.VRM()}/10000")
                input("Press enter to exit")
    return 0
if __name__ == "__main__":
    main()
