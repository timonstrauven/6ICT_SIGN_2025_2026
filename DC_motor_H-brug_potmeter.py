from gpiozero import Motor, MCP3008# importeert motor en mcp van module gpiozero
from time import sleep# importeert sleep van module time
motor = Motor(forward = 17, backward = 14, pwm = True)# variabele motor, voorwaarts op pin 17 en achterwaarts op pin 14 met pwm
pot = MCP3008(channel=0)# variabele pot met channel 0 van de mcp
while True:# while loop
    sleep(5)# 5 seconden pauze
    motor.backward(pot.value)# motor achterwaards met waarde van de potmeter
  