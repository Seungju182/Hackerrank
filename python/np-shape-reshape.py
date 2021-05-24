import numpy as np


def convert(arr):
    return np.reshape(arr, (3, 3))


if __name__ == "__main__":
    arr = np.array(input().split(), int)
    print(convert(arr))
