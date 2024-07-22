from scipy.integrate import solve_ivp
import numpy as np
from numpy import sin, cos

# general function to generate data
def generate_data(equation, t_span, y0, t_eval, args=()):
    sol = solve_ivp(equation, t_span, y0, t_eval=t_eval, args=args)
    print(sol.message)
    return sol.t, sol.y.T

# Restricted three-body problem
def restricted_three_body(t, state, m1, m2, x1, y1, x2, y2):
    # x, y, vx, vy
    x, y, vx, vy = state
    r1 = np.sqrt((x - x1) ** 2 + (y - y1) ** 2) + 1e-50
    r2 = np.sqrt((x - x2) ** 2 + (y - y2) ** 2) + 1e-50
    ax = - m1 * ((x - x1) / r1 ** 3) - m2 * ((x - x2) / r2 ** 3)
    ay = - m1 * ((y - y1) / r1 ** 3) - m2 * ((y - y2) / r2 ** 3)
    return [vx, vy, ax, ay]

def van_der_pol(t, state):
    x, dx = state
    mu = 0.1
    ddx = mu*(1-x**2)*dx-x
    return [dx, ddx]


def double_pendulum(t, state):
    m1=m2=1
    l1=l2=1
    g=9.81
    theta1, theta2, dtheta1, dtheta2 = state

    ddtheta1 = ( -g*(2*m1+m2)*sin(theta1)-m2*g*sin(theta1-2*theta2)-2*sin(theta1-theta2)*m2*(l2*dtheta2**2+l1*cos(theta1-theta2)*dtheta1**2) ) / l1*(2*m1+m2-m2*cos(2*theta1-2*theta2)) 
    ddtheta2 = ( 2*sin(theta1-theta2)*((m1+m2)*l1*dtheta1**2+g*(m1+m2)*cos(theta1)+l2*m2*cos(theta1-theta2)*dtheta2**2) ) / l2*(2*m1+m2-m2*cos(2*theta1-2*theta2)) 

    return [dtheta1, dtheta2, ddtheta1, ddtheta2]