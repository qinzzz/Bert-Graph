'''import torch

x = torch.Tensor([1, 2, 3])
print(x.repeat(384, 1))
print(x)
'''

temp = []
a = [1,2,3]
for _ in range(384):
    temp.append(a)

print(temp)