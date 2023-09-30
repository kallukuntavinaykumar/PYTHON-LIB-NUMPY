# Initializing Arrays
# How to use zeros() function 
import numpy as np
a=np.zeros(4)
print(a)


b=np.zeros([2,3])
print(b)

c=np.zeros([2,3,4])
print(c)
 
# How to use full() function

d=np.full([2,3],4)
print(d)

e=np.full([3,3,4],5)
print(e)

# How to use random.rand() function
 
f=np.random.rand(2,3,3)
print(f)

g=np.random.randint(1)
print(g)

# How to use ones() function

h=np.ones(5)
print(h)

i=np.ones([3,3,3])
print(i)

# How to use eye() function

j=np.eye(5)
print(j)

# How to use aramge() function

k=np.arange(1,10,2)
print(k)

l=np.arange(0,15,2,dtype=float)
print(l)

# How to use linspace() function

m=np.linspace(1,100,5)
print(m)

# linspace() function with endpoint attribute

n=np.linspace(1,10,5,endpoint=False)
print(n)

#  linspace() function with endpoint and retstep attribute

o=np.linspace(1,10,5,endpoint=False,retstep=True)
print(o)

# How to use logspace() function

p=np.logspace(1,10,10)
print(p)
 
# logspace() function using base attribute

q=np.logspace(1,10,10,base=2)
print(q)