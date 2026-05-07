from cyberbot import *

error_sum = 0
error_prev = 0

def proportional(kp, error):
    return kp * error
    
def integral(ki, dt, limit, error):
    global error_sum
    error_sum = error_sum + error
    if error_sum > limit:
        error_sum = limit
    if error_sum < -limit:
        error_sum = -limit
    return ki * (error_sum) / dt

def derivative(kd, dt, error):
    global error_prev
    output = kd * (error - error_prev) / dt
    error_prev = error
    return output

