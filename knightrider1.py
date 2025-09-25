from gpiozero import LED # importeert module LED
from time import sleep # importeert module sleep

led1 = LED(5) # variabele led1 met waarde pin 5
led2 = LED(6) # variabele led1 met waarde pin 5
led3 = LED(13) # variabele led1 met waarde pin 5
led4 = LED(19) # variabele led1 met waarde pin 5
led5 = LED(26) # variabele led1 met waarde pin 5
led6 = LED(16) # variabele led1 met waarde pin 5
led7 = LED(20) # variabele led1 met waarde pin 5
led8 = LED(21) # variabele led1 met waarde pin 5      

while True: # als waarde True is, dan
    led1.on() # led1 aan
    sleep(0.1) # wacht 0.1 sec
    led1.off() # led1 uit
    led2.on() # led2 aan
    sleep(0.1)# wacht 0.1 sec
    led2.off() # led2 uit
    
    led3.on() # led3 aan
    sleep(0.1)# wacht 0.1 sec
    led3.off() # led3 uit
   
    led4.on() # led4 aan
    sleep(0.1)# wacht 0.1 sec
    led4.off() # led4 uit
   
    led5.on() # led5 aan
    sleep(0.1)# wacht 0.1 sec
    led5.off() # led5 uit
  
    led6.on() # led6 aan
    sleep(0.1)# wacht 0.1 sec
    led6.off() # led6 uit
   
    led7.on() # led7 aan
    sleep(0.1)# wacht 0.1 sec
    led7.off() # led7 uit
 
    led8.on() # led8 aan
    sleep(0.1)# wacht 0.1 sec
    led8.off() # led8 uit

    led7.on() # led7 aan
    sleep(0.1)# wacht 0.1 sec
    led7.off() # led7 uit
  
    led6.on() # led6 aan
    sleep(0.1)# wacht 0.1 sec
    led6.off() # led6 uit
   
    led5.on() # led5 aan
    sleep(0.1)# wacht 0.1 sec
    led5.off() # led5 uit
   
    led4.on() # led4 aan
    sleep(0.1)# wacht 0.1 sec
    led4.off() # led4 uit

    led3.on() # led3 aan
    sleep(0.1)# wacht 0.1 sec
    led3.off() # led3 uit
    
    led2.on() # led2 aan
    sleep(0.1)# wacht 0.1 sec
    led2.off() # led2 uit
   

    

