from chess import *
from time import time

position = '11 25 38 46 53 67 72 84'

start = time()
get_all_positions()
# check_position(position)
end = time()

print((end - start) * 10 ** 3, "ms")
