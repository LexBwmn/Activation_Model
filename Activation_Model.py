import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

#inital condiotion gene 1 = 0 gene 2 = 0
y0 = [0,0]

# time 
t = np.linspace(0,200, num=100)

#varuables used for equation 
k_1 = 0.5
gamma_1 = 0.1
k_2 = 0.5
gamma_2 = 0.05
n = 5
c = 5

# array of variables
params = [k_1, gamma_1, k_2, gamma_2, n, c]

def sim(variables, t, params):

    # assigning gene 1 and gene 2
    G1 = variables[0]
    G2 = variables[1]

    #defenition of params 
    k_1 = params[0]
    gamma_1 = params[1]
    k_2 = params[2]
    gamma_2 = params[3]
    n = params[4]
    c = params[5]

    #ODE
    dG1dt = k_1 - gamma_1 * G1

    dG2dt = (G1**n / (c**n + G1**n)) * k_2 - gamma_2 * G2

    return([dG1dt, dG2dt])

y = odeint(sim, y0, t, args=(params,))

f,ax = plt.subplots(1)

#plotting lines
#first element of y 
line1, = ax.plot(t,y[:,0], color="b", label="M")

#second element of y
line2, = ax.plot(t,y[:,1], color="r", label="P")

#labels of x and y axis 
ax.set_ylabel("Abundance")
ax.set_xlabel("Time")

# legend label line 
ax.legend(handles=[line1, line2])

plt.show()

