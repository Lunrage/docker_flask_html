import argparse

import numpy as np
import pandas as pd

import compute_stuff as cs

def main(value_1, value_2, operation):
    # load the data
    result = cs.main(value_1, value_2, operation)

    #print("Result: ", result)

    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # indicate the first value
    parser.add_argument('--v1', type=int, required=True)
    # indicate the second value
    parser.add_argument('--v2', type=int, required=True)
    # indicate operation to perform
    parser.add_argument('--op', type=str, choices=['/', '*', '+', '-'], default='+')

    args = parser.parse_args()

    value_1 = args.v1
    value_2 = args.v2
    operation = args.op

    main(value_1, value_2, operation)