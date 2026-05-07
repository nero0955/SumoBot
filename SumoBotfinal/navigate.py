from cyberbot import *

def maneuver(vL, vR, t):
    if vR is not None:
        vR = -vR
    bot(18).servo_speed(vL)
    bot(19).servo_speed(vR)
    sleep(t)

