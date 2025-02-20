#!/usr/bin/env python
# coding: utf-8

# <h1>Assignment 1

# <h3>Q1: Reversing a list

# In[9]:


#following are sample input and corresponding outputs
Input  = [12, 35, 9, 56, 24]
Output = [24, 35, 9, 56, 12]

Input  = [1, 2, 3]
Output = [3, 2, 1]


# In[6]:


def Reverse(lst):
    lst.reverse()
    return lst
      
lst = [1, 2, 3]
print ("output=")
print(Reverse(lst))


# <h3>Q2: Swapping elements in lists

# In[12]:


Input  = [12, 35, 9, 56, 24]
Output = [12, 9, 35, 56, 24]


# In[7]:


def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
List = [12, 35, 9, 56, 24]
pos1, pos2  = 2, 3
 
print(swapPositions(List, pos1-1, pos2-1))


# <h3>Q3: Reversing a string

# In[ ]:


input_str  = 'This is CVL757'
output_str = '757LVC si sihT'


# In[9]:


def reverse(string):
    string = string[::-1]
    return string
  
s = "This is CVL757"
  
print ("The original string  is : ",end="")
print (s)
  
print ("The reversed string is : ",end="")
print (reverse(s))


# <h3>Q4: Reversing the order of words in a string

# In[14]:


input_str  = 'This is CVL757'
output_str = 'CVL757 is This'


# In[10]:


def rev_sentence(sentence): 
  
    
    words = sentence.split(' ') 
  
    
    reverse_sentence = ' '.join(reversed(words)) 
  
   
    return reverse_sentence 
  
if __name__ == "__main__": 
    input = 'This is CVL757'
    print (rev_sentence(input))


# <h3>Q5: Initialise a 3x3 matrix with random values, use numpy

# In[17]:


import numpy as np
array = np.random.rand(3,3)
print(array)


# In[ ]:





# <h3>Q6: Swap the columns of random_matrix

# In[69]:


inp = np.array([[0.13806091, 0.82474243, 0.15646752],
                [0.50029824, 0.45875794, 0.53401557],
                [0.95397773, 0.79407795, 0.07442586]])

out = np.array([[0.15646752, 0.82474243, 0.13806091],
                [0.53401557, 0.45875794, 0.50029824],
                [0.07442586, 0.79407795, 0.95397773]])


# In[20]:


import numpy as np
array = np.random.rand(3,3)
print("Original array:")
print(array)
array[:, [2, 0]] = array[:, [0, 2]]
print("After swapping arrays the last column and first column:")
print(array)


# <h3>Q7: Swap the rows of random_matrix

# In[72]:


inp = np.array([[0.13806091, 0.82474243, 0.15646752],
               [0.50029824, 0.45875794, 0.53401557],
               [0.95397773, 0.79407795, 0.07442586]])

out = np.array([[0.95397773, 0.79407795, 0.07442586],
               [0.50029824, 0.45875794, 0.53401557],
               [0.13806091, 0.82474243, 0.15646752]])


# In[4]:


import numpy as np
array = np.random.rand(3,3)
print("Original array:")
print(array)
array[[2, 0], :] = array[[0,2], :]
print("After swapping arrays the last row and first row:")
print(array)


# <h3>Q8: Plot the sine and cosine curves as shown below

# In[5]:


import matplotlib.pyplot as plt


# In[25]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
x = np.arange(0,2*np.pi,0.01)   
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)
plt.xlabel('x values from 0 to 2pi')  '  '
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 2pi')
plt.legend(['sin(x)', 'cos(x)'])     
plt.show()


# # Q9. Truss

# <h3>Q9: Plot the following truss</h3>
# Length of element 2, 6 and 9 (between nodes 1 and 3, 3 and 5, and 5 and 9) is 5.<br>
# Length of element 3 and 7 is 7m.
#  

# In[8]:


# <img src='q9.svg' alt="Truss Q9" width="500" height="600">


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
nodes= []
bars= []
nodes.append([0,0])
nodes.append([5,7])
nodes.append([5,0])
nodes.append([10,7])
nodes.append([10,0])
nodes.append([15,0])
bars.append([0,1])
bars.append([0,2])
bars.append([1,2])
bars.append([1,3])
bars.append([1,4])
bars.append([2,4])
bars.append([3,4])
bars.append([3,5])
bars.append([4,5])
# convert array to high array
nodes = np.array(nodes).astype(float)
bars = np.array(bars)
# Applied forces
P= np.zeros_like(nodes)
# 1 represents y axis.
P[1,1]= -20
# Support displacements
Ur = [0,0,0,0]
# condition of DOF(1- free, 0- fixed)
DOFCON = np.ones_like(nodes).astype(int)
DOFCON[0,:] = 0 # 0th node in x and y axis
DOFCON[5,:] = 0 # 5th node in x and y axis
# def TrussAnalysis():
# NN= len(nodes)
# NE= len(bars)
# DOF= 2
# NDOF= DOF*NN

def plot(nodes, c, lt, lw, lg):   
    for i in range(len(bars)):
        xi, xf = nodes[bars[i,0],0], nodes[bars[i,1],0]
        yi, yf = nodes[bars[i,0],1], nodes[bars[i,1],1]
        line, = plt.plot([xi,xf], [yi,yf], color=c, linestyle=lt, linewidth=lw)
    line.set_label(lg)
    plt.legend(prop={'size': 8})
plot(nodes,'gray', '-',1,'Undeformed')


# **Q10: Consider the plane truss shown above. Given E = 200GPa and A = 0.005m2, and horizontal load of 20kN at node 2. Both node 1 and node 6 have pin supports:**
# 
# 1. the global stiffness matrix for the structure.
# 2. the horizontal and vertical displacements at nodes 2, 3, 4, and 5.
# 3. the horizontal and vertical reactions at nodes 1 and 6.
# 4. the stress in each element.

# In[6]:


#write solution here
import math
import numpy as np
E=210000000
A=0.005
p1=[0,0]
p2=[5,7]
p3=[5,0]
p4=[10,7]
p5=[10,0]
p6=[15,0]
L1 = round(math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) ),2)
L2=5
L3=7
L4=5
L5 = round(math.sqrt( ((p2[0]-p5[0])**2)+((p2[1]-p5[1])**2) ),2)
L6=5
L7=7
L8 = round(math.sqrt( ((p4[0]-p6[0])**2)+((p4[1]-p6[1])**2) ),2)
L9=5
theta1=round(math.atan(7/5),2)
theta2=0
theta3=math.pi/2
theta4=0
theta5=round(math.atan(5/7),2)+(3*math.pi)/2
theta6=0
theta7=math.pi/2
theta8=round(math.atan(5/7),2)+(3*math.pi)/2
theta9=0
k1_11=math.cos(theta1)**2
k1_12=math.cos(theta1)*math.sin(theta1)
k1_13=-math.cos(theta1)**2
k1_14=-math.cos(theta1)*math.sin(theta1)
k1_21=math.cos(theta1)*math.sin(theta1)
k1_22=math.sin(theta1)**2
k1_23=-math.cos(theta1)*math.sin(theta1)
k1_24=-math.sin(theta1)**2
k1_31=-math.cos(theta1)**2
k1_32=-math.cos(theta1)*math.sin(theta1)
k1_33=math.cos(theta1)**2
k1_34=math.cos(theta1)*math.sin(theta1)
k1_41=-math.cos(theta1)*math.sin(theta1)
k1_42=-math.sin(theta1)**2
k1_43=math.cos(theta1)*math.sin(theta1)
k1_44=math.sin(theta1)**2
k1=(E*A/L1)*np.array([[k1_11,k1_12,k1_13,k1_14],[k1_21,k1_22,k1_23,k1_24],[k1_31,k1_32,k1_33,k1_34],[k1_41,k1_42,k1_43,k1_44]])
print(np.round(k1,2))


# In[9]:


k2_11=math.cos(theta2)**2
k2_12=math.cos(theta2)*math.sin(theta2)
k2_13=-math.cos(theta2)**2
k2_14=-math.cos(theta2)*math.sin(theta2)
k2_21=math.cos(theta2)*math.sin(theta2)
k2_22=math.sin(theta2)**2
k2_23=-math.cos(theta2)*math.sin(theta2)
k2_24=-math.sin(theta2)**2
k2_31=-math.cos(theta2)**2
k2_32=-math.cos(theta2)*math.sin(theta2)
k2_33=math.cos(theta2)**2
k2_34=math.cos(theta2)*math.sin(theta2)
k2_41=-math.cos(theta2)*math.sin(theta2)
k2_42=-math.sin(theta2)**2
k2_43=math.cos(theta2)*math.sin(theta2)
k2_44=math.sin(theta2)**2
k2=((E*A)/L2)*np.array([[k2_11,k2_12,k2_13,k2_14],[k2_21,k2_22,k2_23,k2_24],[k2_31,k2_32,k2_33,k2_43],[k2_41,k2_42,k2_43,k2_44]])
print(k2)


# In[10]:


k3_11=math.cos(theta3)**2
k3_12=math.cos(theta3)*math.sin(theta3)
k3_13=-math.cos(theta3)**2
k3_14=-math.cos(theta3)*math.sin(theta3)
k3_21=math.cos(theta3)*math.sin(theta3)
k3_22=math.sin(theta3)**2
k3_23=-math.cos(theta3)*math.sin(theta3)
k3_24=-math.sin(theta3)**2
k3_31=-math.cos(theta3)**2
k3_32=-math.cos(theta3)*math.sin(theta3)
k3_33=math.cos(theta3)**2
k3_34=math.cos(theta3)*math.sin(theta3)
k3_41=-math.cos(theta3)*math.sin(theta3)
k3_42=-math.sin(theta3)**2
k3_43=math.cos(theta3)*math.sin(theta3)
k3_44=math.sin(theta3)**2
k3=(E*A/L3)*np.array([[k3_11,k3_12,k3_13,k3_14],[k3_21,k3_22,k3_23,k3_24],[k3_31,k3_32,k3_33,k3_34],[k3_41,k3_42,k3_43,k3_44]])
print(np.round(k3,2))


# In[11]:


k4_11=math.cos(theta4)**2
k4_12=math.cos(theta4)*math.sin(theta4)
k4_13=-math.cos(theta4)**2
k4_14=-math.cos(theta4)*math.sin(theta4)
k4_21=math.cos(theta4)*math.sin(theta4)
k4_22=math.sin(theta4)**2
k4_23=-math.cos(theta4)*math.sin(theta4)
k4_24=-math.sin(theta4)**2
k4_31=-math.cos(theta4)**2
k4_32=-math.cos(theta4)*math.sin(theta4)
k4_33=math.cos(theta4)**2
k4_34=math.cos(theta4)*math.sin(theta4)
k4_41=-math.cos(theta4)*math.sin(theta4)
k4_42=-math.sin(theta4)**2
k4_43=math.cos(theta4)*math.sin(theta4)
k4_44=math.sin(theta4)**2
k4=(E*A/L4)*np.array([[k4_11,k4_12,k4_13,k4_14],[k4_21,k4_22,k4_23,k4_24],[k4_31,k4_32,k4_33,k4_34],[k4_41,k4_42,k4_43,k4_44]])
print(k4)


# In[12]:


k5_11=math.cos(theta5)**2
k5_12=math.cos(theta5)*math.sin(theta5)
k5_13=-math.cos(theta5)**2
k5_14=-math.cos(theta5)*math.sin(theta5)
k5_21=math.cos(theta5)*math.sin(theta5)
k5_22=math.sin(theta5)**2
k5_23=-math.cos(theta5)*math.sin(theta5)
k5_24=-math.sin(theta5)**2
k5_31=-math.cos(theta5)**2
k5_32=-math.cos(theta5)*math.sin(theta5)
k5_33=math.cos(theta5)**2
k5_34=math.cos(theta5)*math.sin(theta5)
k5_41=-math.cos(theta5)*math.sin(theta5)
k5_42=-math.sin(theta5)**2
k5_43=math.cos(theta5)*math.sin(theta5)
k5_44=math.sin(theta5)**2
k5=(E*A/L5)*np.array([[k5_11,k5_12,k5_13,k5_14],[k5_21,k5_22,k5_23,k5_24],[k5_31,k5_32,k5_33,k5_34],
[k5_41,k5_42,k5_43,k5_44]])
print(np.round(k5,2))


# In[13]:


k6_11=math.cos(theta6)**2
k6_12=math.cos(theta6)*math.sin(theta6)
k6_13=-math.cos(theta6)**2
k6_14=-math.cos(theta6)*math.sin(theta6)
k6_21=math.cos(theta6)*math.sin(theta6)
k6_22=math.sin(theta6)**2
k6_23=-math.cos(theta6)*math.sin(theta6)
k6_24=-math.sin(theta6)**2
k6_31=-math.cos(theta6)**2
k6_32=-math.cos(theta6)*math.sin(theta6)
k6_33=math.cos(theta6)**2
k6_34=math.cos(theta6)*math.sin(theta6)
k6_41=-math.cos(theta6)*math.sin(theta6)
k6_42=-math.sin(theta6)**2
k6_43=math.cos(theta6)*math.sin(theta6)
k6_44=math.sin(theta6)**2
k6=(E*A/L6)*np.array([[k6_11,k6_12,k6_13,k6_14],[k6_21,k6_22,k6_23,k6_24],[k6_31,k6_32,k6_33,k6_34],
[k6_41,k6_42,k6_43,k6_44]])
print(k6)


# In[14]:


k7_11=math.cos(theta7)**2
k7_12=math.cos(theta7)*math.sin(theta7)
k7_13=-math.cos(theta7)**2
k7_14=-math.cos(theta7)*math.sin(theta7)
k7_21=math.cos(theta7)*math.sin(theta7)
k7_22=math.sin(theta7)**2
k7_23=-math.cos(theta7)*math.sin(theta7)
k7_24=-math.sin(theta7)**2
k7_31=-math.cos(theta7)**2
k7_32=-math.cos(theta7)*math.sin(theta7)
k7_33=math.cos(theta7)**2
k7_34=math.cos(theta7)*math.sin(theta7)
k7_41=-math.cos(theta7)*math.sin(theta7)
k7_42=-math.sin(theta7)**2
k7_43=math.cos(theta7)*math.sin(theta7)
k7_44=math.sin(theta7)**2
k7=(E*A/L7)*np.array([[k7_11,k7_12,k7_13,k7_14],[k7_21,k7_22,k7_23,k7_24],[k7_31,k7_32,k7_33,k7_34],
[k7_41,k7_42,k7_43,k7_44]])
print(np.round(k7,2))


# In[15]:


k8_11=math.cos(theta8)**2
k8_12=math.cos(theta8)*math.sin(theta8)
k8_13=-math.cos(theta8)**2
k8_14=-math.cos(theta8)*math.sin(theta8)
k8_21=math.cos(theta8)*math.sin(theta8)
k8_22=math.sin(theta8)**2
k8_23=-math.cos(theta8)*math.sin(theta8)
k8_24=-math.sin(theta8)**2
k8_31=-math.cos(theta8)**2
k8_32=-math.cos(theta8)*math.sin(theta8)
k8_33=math.cos(theta8)**2
k8_34=math.cos(theta8)*math.sin(theta8)
k8_41=-math.cos(theta8)*math.sin(theta8)
k8_42=-math.sin(theta8)**2
k8_43=math.cos(theta8)*math.sin(theta8)
k8_44=math.sin(theta8)**2
k8=(E*A/L8)*np.array([[k8_11,k8_12,k8_13,k8_14],[k8_21,k8_22,k8_23,k8_24],[k8_31,k8_32,k8_33,k8_34],
[k8_41,k8_42,k8_43,k8_44]])
print(np.round(k8,2))


# In[16]:


k9_11=math.cos(theta9)**2
k9_12=math.cos(theta9)*math.sin(theta9)
k9_13=-math.cos(theta9)**2
k9_14=-math.cos(theta9)*math.sin(theta9)
k9_21=math.cos(theta9)*math.sin(theta9)
k9_22=math.sin(theta9)**2
k9_23=-math.cos(theta9)*math.sin(theta9)
k9_24=-math.sin(theta9)**2
k9_31=-math.cos(theta9)**2
k9_32=-math.cos(theta9)*math.sin(theta9)
k9_33=math.cos(theta9)**2
k9_34=math.cos(theta9)*math.sin(theta9)
k9_41=-math.cos(theta9)*math.sin(theta9)
k9_42=-math.sin(theta9)**2
k9_43=math.cos(theta9)*math.sin(theta9)
k9_44=math.sin(theta9)**2
k9=(E*A/L9)*np.array([[k9_11,k9_12,k9_13,k9_14],[k9_21,k9_22,k9_23,k9_24],[k9_31,k9_32,k9_33,k9_34],
[k9_41,k9_42,k9_43,k9_44]])
print(k9)


# In[17]:


TSM=np.zeros((12,12))
np.set_printoptions(edgeitems=12,linewidth=10000)
TSM[0:4,0:4]+=k1
TSM[0:2,0:2]+=k2[0:2,0:2]
TSM[0:2,4:6]+=k2[0:2,2:4]
TSM[4:6,0:2]+=k2[2:4,0:2]
TSM[4:6,4:6]+=(k2[2:4,2:4] + k3[2:4,2:4] + k6[0:2,0:2])
TSM[2:4,2:4]+=(k3[0:2,0:2] + k4[0:2,0:2] + k5[0:2,0:2])
TSM[2:4,4:6]+=k3[0:2,2:4]
TSM[4:6,2:4]+=k3[2:4,0:2]
TSM[2:4, 6:8]+=k4[0:2,2:4]
TSM[6:8, 2:4]+=k4[2:4,0:2]
TSM[6:8,6:8]+=(k4[2:4,2:4] + k7[0:2,0:2] + k8[0:2,0:2])
TSM[2:4,8:10]+=k5[0:2,2:4]
TSM[8:10,2:4]+=k5[2:4,0:2]
TSM[8:10,8:10]+=(k5[2:4,2:4] + k6[2:4,2:4] + k7[2:4,2:4] + k9[0:2,0:2])
TSM[4:6,8:10]+=k6[0:2,2:4]
TSM[8:10,4:6]+=k6[2:4,0:2]
TSM[6:8,8:10]+=k7[0:2,2:4]
TSM[8:10,6:8]+=k7[2:4,0:2]
TSM[6:8,10:12]+=k8[0:2,2:4]
TSM[10:12,6:8]+=k8[2:4,0:2]
TSM[10:12,10:12]+=(k8[2:4,2:4]+k9[2:4,2:4])
TSM[8:10,10:12]+=k9[0:2,2:4]
TSM[10:12,8:10]+=k9[2:4,0:2]
np.round(TSM,0)


# In[18]:


eightbyeight=TSM[2:10,2:10]
eightbyeight


# In[19]:


test=np.array([20,0,0,0,0,0,0,0]).reshape((8,1))
test


# In[20]:


np.round((np.linalg.inv(eightbyeight) * test)*1000,9)
np.linalg.solve(eightbyeight,test)


# In[21]:


disp=np.zeros((12,1))
disp[2:10]=np.linalg.solve(eightbyeight,test)
disp


# In[22]:


np.round(np.matmul(TSM,disp),4)


# In[23]:


u1=disp[0:4]
u1


# In[24]:


f11=-math.cos(theta1)
f12=-math.sin(theta1)
f13=math.cos(theta1)
f14=math.sin(theta1)
f1=(E*A/L1)*np.array([f11,f12,f13,f14])
np.matmul(f1,u1)
sigma1=np.matmul(f1,u1)/A
np.round(sigma1,2)


# In[25]:


u2=np.zeros((4,1))
u2[0:2]=disp[0:2]
u2[2:4]=disp[4:6]
u2


# In[26]:


f21=-math.cos(theta2)
f22=-math.sin(theta2)
f23=math.cos(theta2)
f24=math.sin(theta2)
f2=(E*A/L2)*np.array([f21,f22,f23,f24])
np.matmul(f2,u2)
sigma2=np.matmul(f2,u2)/A
np.round(sigma2,2)


# In[27]:


u3=disp[2:6]
u3


# In[28]:


f31=-math.cos(theta3)
f32=-math.sin(theta3)
f33=math.cos(theta3)
f34=math.sin(theta3)
f3=(E*A/L3)*np.array([f31,f32,f33,f34])
np.matmul(f3,u3)
sigma3=np.matmul(f3,u3)/A
np.round(sigma3,2)


# In[29]:


u4=np.zeros((4,1))
u4[0:2]=disp[2:4]
u4[2:4]=disp[6:8]
u4


# In[30]:


f41=-math.cos(theta4)
f42=-math.sin(theta4)
f43=math.cos(theta4)
f44=math.sin(theta4)
f4=(E*A/L4)*np.array([f41,f42,f43,f44])
np.matmul(f4,u4)
sigma4=np.matmul(f4,u4)/A
np.round(sigma4,2)


# In[31]:


u5=np.zeros((4,1))
u5[0:2]=disp[2:4]
u5[2:4]=disp[8:10]
u5


# In[32]:


f51=-math.cos(theta5)
f52=-math.sin(theta5)
f53=math.cos(theta5)
f54=math.sin(theta5)
f5=(E*A/L5)*np.array([f51,f52,f53,f54])
np.matmul(f5,u5)
sigma5=np.matmul(f5,u5)/A
np.round(sigma5,2)


# In[33]:


u6=np.zeros((4,1))
u6[0:2]=disp[4:6]
u6[2:4]=disp[8:10]
u6


# In[34]:


f61=-math.cos(theta6)
f62=-math.sin(theta6)
f63=math.cos(theta6)
f64=math.sin(theta6)
f6=(E*A/L6)*np.array([f61,f62,f63,f64])
np.matmul(f6,u6)
sigma6=np.matmul(f6,u6)/A
np.round(sigma6,2)


# In[35]:


u7=disp[6:10]
u7


# In[36]:


f71=-math.cos(theta7)
f72=-math.sin(theta7)
f73=math.cos(theta7)
f74=math.sin(theta7)
f7=(E*A/L7)*np.array([f71,f72,f73,f74])
np.matmul(f7,u7)
sigma7=np.matmul(f7,u7)/A
np.round(sigma7,2)


# In[37]:


u8=np.zeros((4,1))
u8[0:2]=disp[6:8]
u8[2:4]=disp[10:12]
u8


# In[38]:


f81=-math.cos(theta8)
f82=-math.sin(theta8)
f83=math.cos(theta8)
f84=math.sin(theta8)
f8=(E*A/L8)*np.array([f81,f82,f83,f84])
np.matmul(f8,u8)
sigma8=np.matmul(f8,u8)/A
np.round(sigma8,2)


# In[39]:


u9=disp[8:12]
u9


# In[40]:


f91=-math.cos(theta9)
f92=-math.sin(theta9)
f93=math.cos(theta9)
f94=math.sin(theta9)
f9=(E*A/L9)*np.array([f91,f92,f93,f94])
np.matmul(f9,u9)
sigma9=np.matmul(f9,u9)/A
np.round(sigma9,2)


# In[ ]:





# In[ ]:





# <H1>BONUS QUESTION</H1>
# Plot the deformed shape of truss obtained in Q10

# In[ ]:





# In[ ]:


#write solution here

