# cyberbot_sumo_ir_qti_ring_edge
from cyberbot import *
from qti import *
from navigate import *
from intbits import *

def maneuver(vL, vR, t):
    if vR is not None:
        vR = -vR
    bot(18).servo_speed(vL)
    bot(19).servo_speed(vR)
    sleep(t)

def ir_detect():
    irL = bot(14, 13).ir_detect(38000)
    irR = bot(1, 2).ir_detect(38000)
    display.set_pixel(3, 4, irL*9)
    display.set_pixel(1, 4, irR*9)
    return irL, irR
    
def qti_detect():
    pattern = qti(8, 7).read()
    qtiL = bit.get(pattern, 1)
    qtiR = bit.get(pattern, 0)
    display.set_pixel(4, 2, qtiL*9)
    display.set_pixel(0, 2, qtiR*9)
    return qtiL, qtiR

def scan(motions):
    for motion in motions:
        vL, vR, reps = motion
        for n in range(reps):
            maneuver(vL, vR, 1)
            if qti_detect() !=(1,1) or ir_detect() !=(1,1):
                return
                
while True:
    bot(4).write_digital(0)
    bot(4).read_digital()
    bot(4).write_digital(0)
    t_echo = bot(5).pulse_in(1)
    cm = t_echo * 0.01715
    if cm < 10:
        bot(16)

    qtiL, qtiR = qti_detect()
    irL, irR = ir_detect()
    
    if qtiL == 0 or qtiR == 0:
        maneuver(-75, -75, 300)
        if qtiL == 0 and qtiR == 0:
            maneuver(-75, 75, 500)
        elif qtiL == 0:
            maneuver(75, -75, 400)
        elif qtiR == 0:
            maneuver(-75, 75, 400)
    elif irL == 1 and irR == 1:
        scan(
            [   [ 70, 70, 20],    # Forward 20x30 = 600 ms
                [-70, 70, 20],    # Rotate left 20x30 = 600 ms
                [70, -70, 40],    # Rotate right 40x30 = 1200 ms
                [-70, 70, 20],    # Rotate left 20x30 = 600 ms
                [ 70, 70, 30]   ] # Forward 30x30 = 900 ms
        )
    else:
        if irL == 0 and irR == 0:
            maneuver(75, 75, 1)
        elif irL == 1 and irR ==0:
            maneuver(75, 0, 1)
        elif irL == 0 and irR == 1:
            maneuver(0, 75, 1)
        else:
            maneuver(75, 75, 1)