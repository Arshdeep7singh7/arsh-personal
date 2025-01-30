import numpy as np
arshdeep=np.linspace(10,100,25)
print(arshdeep)
print(np.ndim(arshdeep))
print(np.shape(arshdeep))
for i in arshdeep:
    print(np.dtype(i))
print(np.size(arshdeep))
print(np.transpose(arshdeep))
print('using t attribute')
print(arshdeep.T)