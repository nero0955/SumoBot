from cyberbot import *

def sr04_cm(trig, echo):
    bot(trig).write_digital(0)
    bot(trig).read_digital()
    bot(trig).write_digital(0)
    t_echo = bot(echo).pulse_in(1)
    cm = t_echo * 0.01715 
    #print('cm:', cm)
    #sleep(750)
    return cm

