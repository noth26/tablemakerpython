from prettytable import PrettyTable
import random
import string
import os
from time import sleep
import time
import random
import string
from colorama import Fore
print(f" {Fore.LIGHTBLUE_EX}[ T ] Table Maker  ")
print(f" {Fore.LIGHTMAGENTA_EX}[ T ] GitHub : https://github.com/noth26 ")
print(f" {Fore.LIGHTCYAN_EX} ----------------------------------- ")
print(f"{Fore.LIGHTCYAN_EX} [ T ] If Colorama Error -- Type [pip install colorama] To Terminal Or Cmd")
print(f" {Fore.LIGHTGREEN_EX} ----------------------------------- ")

table = PrettyTable(["Type", "Whatever","You", ])
table.add_row(["Want", ":)", "<3"])

print(table)
