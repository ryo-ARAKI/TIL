########################################################################
#
#  F2PYのサンプルプログラム
#
########################################################################

import test
import numpy as np

x = np.empty((3, 2), dtype=float)

for j in range(x.shape[1]):
    for i in range(x.shape[0]):
        x[i, j] = i ** 2 + (j/2)

print(x.shape[0], x.shape[1])
print(x)

y = test.cal_test(x)

print("x is ")
print(x)
print("y is ")
print(y)
