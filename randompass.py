#!/usr/bin/env python3

import argparse
import random
parser = argparse.ArgumentParser()

def main():
    '''
    This is main function.
    '''
    parser.add_argument("-n")
    parser.add_argument("-c")
    args = parser.parse_args()

    psswd = ''
    psswd_len = int(args.n or 12)
    possible_char = args.c or "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXoxYyZz0123456789!@$%"
    possible_len = len(possible_char) - 1

    for i in range(0, psswd_len):
        char_index = random.randint(0, possible_len)
        psswd += possible_char[char_index]

    print("Your password is : {0}".format(psswd))

main()
