import numpy as np
import sys
import random
import math

def main():
    # 1-bit Deutsch-Jozsa's algorithm
    U_f = None
    if random.randint(0, 1) == 0:
        # f(x) = 0 for all x
        U_f = np.matrix([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]])
        print("f: constant function")
    else:
        U_f = np.matrix([[1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 0, 1],
                        [0, 0, 1, 0]])
        print("f: balanced function")

    zero_bit = np.matrix([[1, 0]]).T
    one_bit = np.matrix([[0, 1]]).T

    Pauli_x = np.matrix([[0, 1],
                        [1, 0]])

    Hadamard = np.matrix([[1, 1],
                         [1, -1]]) / math.sqrt(2)

    # initialization
    bit_array = np.kron(zero_bit, zero_bit)

    # STEP1
    print("----step1----")
    U_step1 = np.kron(np.eye(2), Pauli_x)
    bit_array = np.dot(U_step1, bit_array)
    print(bit_array)

    # STEP2
    print("----step2----")
    U_step2 = np.kron(Hadamard, Hadamard)
    bit_array = np.dot(U_step2, bit_array)
    print(bit_array)

    # STEP3
    print("----step3----")
    U_step3 = U_f
    bit_array = np.dot(U_step3, bit_array)
    print(bit_array)

    # STEP4
    print("----step4----")
    U_step4 = np.kron(Hadamard, np.eye(2))
    bit_array = np.dot(U_step4, bit_array)
    print(bit_array)

    # measure
    pro = 0.0

    measure_vec = np.kron(zero_bit, zero_bit)
    pro += (np.dot(measure_vec.T, bit_array))**2
    measure_vec = np.kron(zero_bit, one_bit)
    pro += (np.dot(measure_vec.T, bit_array))**2

    if random.random() < pro:
        print("get 0")
    else:
        print("get 1")


    return

if __name__ == '__main__':
    main()
