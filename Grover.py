import numpy as np
import sys
import random
import math

def main():
    # inputs
    args = sys.argv[1:]
    dim = int(args[0])
    if(dim < 1):
        print("dim must be natural number.")

    U_f = np.eye(2**(dim+1))

    f_one = random.randint(0, 2**(dim) -1)
    print("answer is :{}".format(f_one))
    U_f[[2*f_one, 2*f_one+1]] = U_f[[2*f_one+1, 2*f_one]]

    zero_bit = np.matrix([[1, 0]]).T
    one_bit = np.matrix([[0, 1]]).T

    Hadamard = np.matrix([[1, 1],
                         [1, -1]]) / math.sqrt(2)
    Hadamard_n_1 = Hadamard
    for i in range(dim):
        Hadamard_n_1 = np.kron(Hadamard_n_1, Hadamard)

    D_N = np.ones((2**(dim), 2**(dim))) / 2**(dim-1) - np.eye(2**(dim))
    U_DN = np.kron(D_N, np.eye(2))

    shita = math.asin(math.sqrt(1/2**(dim)))
    rep = math.floor(math.pi / (4 * shita))

    # initialization
    bit_array = zero_bit
    for i in range(dim-1):
        bit_array = np.kron(bit_array, zero_bit)
    bit_array = np.kron(bit_array, one_bit)

    # step1
    bit_array = np.dot(Hadamard_n_1, bit_array)

    for i in range(rep):
        # step3
        bit_array = np.dot(U_f, bit_array)

        # step4
        bit_array = np.dot(U_DN, bit_array)

    # measurement
    prob = [0] * 2**(dim)
    measure_vec = 1
    for i in range(2**dim):
        measure_vec = 1
        for j in range(dim):
            if i >> (dim-j-1) & 0b1 == 1:
                measure_vec = np.kron(measure_vec, one_bit)
            else:
                measure_vec = np.kron(measure_vec, zero_bit)
        measure_vec0 = np.kron(measure_vec, zero_bit)
        prob[i] = (np.dot(measure_vec0.T, bit_array))**2
        measure_vec1 = np.kron(measure_vec, one_bit)
        prob[i] += (np.dot(measure_vec1.T, bit_array))**2

    prob_sum = 0
    rnd_num = random.random()
    for i in range(2**(dim)):
        prob_sum += prob[i]
        if prob_sum > rnd_num:
            print("get: {}".format(i))
            break

    return

if __name__ == '__main__':
    main()
