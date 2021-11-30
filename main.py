import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(input, rotation_factor):
    if not input or not rotation_factor:
            return input
    cap_alpha = [chr(c) for c in range(ord("A"), ord("Z") + 1)]
    alpha = [chr(c) for c in range(ord("a"), ord("z") + 1)]
    res = []
    for c in input:
        if not c.isalnum():
            res.append(c)
        elif c.isalpha():
            if c.isupper():
                idx = cap_alpha.index(c) + rotation_factor
                if idx > 25:
                    idx %= 26
                res.append(cap_alpha[idx])
            else:
                idx = alpha.index(c) + rotation_factor
                if idx > 25:
                    idx %= 26
                res.append(alpha[idx])
        elif c.isdigit():
            res.append(str(int(c) + rotation_factor)[-1])
        ans  = ''
        result = ''
       # print(ans.join(c for c in res))
    return(ans.join(c for c in res))

def str_append_list_join(s, n):
    l1 = []
    i = 0
    while i < n:
        l1.append(s)
        i += 1
    return ''.join(l1)

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
