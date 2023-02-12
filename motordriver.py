from machine import Pin

pwml = PWM(Pin(21))
pwmr = PWM(pin(22))
lin1 = Pin(26, Pin.OUT)
lin2 = Pin(27, Pin.OUT)
rin1 = Pin(24, Pin.OUT)
rin2 = Pin(25, Pin.OUT)

pwml.freq(1000)
pwmr.freq(1000)


def movement(lspeed, rspeed):
    if lspeed < 0:
        lspeed = -lspeed
        lin1.value(0)
        lin2.value(1)
        pwml.duty(lspeed)
        
    elif lspeed>=0:
        lin1.value(1)
        lin2.value(0)
        pwml.duty(lspeed)
        
    elif rspeed<0:
        rspeed = -rspeed
        rin1.value(0)
        rin2.value(1)
        pwmr.duty(rspeed)
    
    elif rspeed>=0:
        rin1.value(1)
        rin2.value(0)
        pwmr.duty(rspeed)
    
    

    
