#SparseBinaryDecomposition: Decompose int into sum of ints having no consecutive 1s in binary form.
import math
def sparseBinaryDecomposition(N):
    if N <= 2:
      return N
    return N & calAlterMask(N)
    pass

def calAlterMask(N):
    binary_index = math.ceil(math.log2(N))
    alternating_mask = 2 ** binary_index - 1
    
    zero_bit = 1
    while binary_index >= 0:
        if (zero_bit == 1):
            alternating_mask -= 2 ** binary_index
        
        zero_bit ^= 0b1
        binary_index -= 1
    
    return alternating_mask
    pass

# 26 = 8,9,17,18,5,10,16 or 21
# return −1 if there is no sparse decomposition of N
print("The decomposition of 26 into sum of ints having no consecutive 1s in binary is", str(sparseBinaryDecomposition(26)))
