import torch
import numpy as np
"""
a=torch.ones(5)

print(a)

b=a.numpy()
print(b)
print(type(b))

a.add_(1)
print(a)
print(b)"""

a=np.ones(5)
b=torch.from_numpy(a)
print(b)

a+=1
print(a)
print(b)