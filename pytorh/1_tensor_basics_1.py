# -*- coding: utf-8 -*-


import torch

"""
x=torch.empty(2,3)
p=torch.empty(2,3)
z=torch.ones(2,3,dtype=torch.int)
y=torch.rand(2,3)
j=torch.rand(2,3)
k=torch.tensor([2,3])

q=x+y   #q=torch.add(x,y)
print(x)
print(y)
print(z)
print(x.dtype)
print(z.dtype)
print(k)
print(q) 

p.add_(x)
print(p)

z=torch.mul(j,y) #z.mul_(j,y)
print(z)"""

h=torch.rand(4,4)
print(h)
print(h[:, 0])
print(h[1,1])
print(h[0,:])

ç=h.view(16)
print(ç)
u=h.view(-1,8)
print(u)
print(u.size())
