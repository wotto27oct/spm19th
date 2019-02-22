import numpy as np
import sys
import random

def main():
    # inputs
    args = sys.argv[1:]
    dim = int(args[0])
    if(dim < 1):
        print("dim must be natural number.")
        return

    farray = None
    if random.randint(0,1) == 0:
        farray = np.zeros(2**dim)
    else:
        zeros = np.zeros(2**(dim-1))
        ones = np.ones(2**(dim-1))
        farray = np.hstack((zeros,ones))
        np.random.shuffle(farray)

    def function(x):
        # arg x must be (dim)-d vector
        xarg = 0
        for i in range(dim):
            xarg += x*(2**i)
        return farray[xarg]

        

    return


if __name__ == '__main__':
    main()
