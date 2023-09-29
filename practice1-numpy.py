# How tom import numpy module
import numpy as np

# How to know numpy version

#print(np.__version__)

# How to create numpy

# create numpy using array()
#import numpy as np 
a=np.array(20)        # zero dimensional array
print(a)

b= np.array([10,20,30,40])   # one dimensional array
print(b)


c=np.array([[1,2,3,],[4,5,6]])  # two dimensional array
print(c)


d=np.array([[[2,3,4],[5,6,7]],[[7,8,9],[9,1,2]]]) # three dimensional array
print(d)                                  

# create numpy using asarray() with data type float

e=np.asarray([10,20,30], dtype=float)
print(e)

# create numpy using asarray() with order attribute

f=[[1,2,3,],[4,5,6]]
g=np.asarray(f,order="F")       # column major order
print(g)

for i in np.nditer(g):
    print(i)


f=[[1,2,3,],[4,5,6]]
g=np.asarray(f,order="c")       # Row major order
print(g)

for i in np.nditer(g):
    print(i)


# Create array using frombuffer()

h=b"welcome to numpy"
k=np.frombuffer(h)
print(k)

m=np.frombuffer(h,dtype="S1")
print(m)

 # Create array using frombuffer() with count and offset attribute

n=np.frombuffer(h,dtype="S1",count=5,offset=2)
print(n)



# Create array using fromiter()

x=[10,30,40,50]
y=np.fromiter(x,dtype=int)
print(y)

# Create array using frombuffer() with count attribute

z=np.fromiter(x,dtype=int,count=3)
print(z)






