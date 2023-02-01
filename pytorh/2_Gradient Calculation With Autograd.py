
import torch
"""
x=torch.randn(3, requires_grad=True) #türev almamın sebebi true

print(x)

y=x+2
print(y)
z=y*y*2
print(z)
#z=z.mean()
print(z)
v= torch.tensor([0.1,1.,0.001], dtype=torch.float32)
z.backward(v)  #dz/dy

print(x.grad)

#x.requires_grad_(false)
#x.detach()
#with torch.no_grad()
x.requires_grad_(False)
print(x)

y=x.detach()
print(y)


with torch.no_grad():
    y=x+2
    print(y)
"""   

weights=tprch.ones(4,requires_grad=True)
for epoch in range(1):
    model_output=(weights*3).sum()
    model_output.backward()
    print(weights.grad)
 