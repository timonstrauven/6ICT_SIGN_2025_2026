import busio #importeert module busio
import digitalio #importeert module digitalio
import board #importeert module board
import adafruit_mcp3xxx.mcp3008 as MCP #importeert module adafruit_mcp3xxxmcp3008 als MCP
from adafruit_mcp3xxx.analog_in import AnalogIn #importeert AnalogIn van module adafruit_mcp3xxx.analog_in
from gpiozero import RGBLED #importeert RGBLED van module gpiozero
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI) #variabele spi aangesloten op de pinnen SCK, MISO, en MOSI op je bord
cs = digitalio.DigitalInOut(board.D5) #variabele cs aangesloten op pin D5 op je bord
mcp = MCP.MCP3008(spi,cs) #variabele mcp op vorige variabelen spi en cs
channel1 = AnalogIn(mcp, MCP.P0) #variabele channel1 is potentiometer 1
channel2 = AnalogIn(mcp, MCP.P1) #variabele channel2 is potentiometer 2
channel3 = AnalogIn(mcp, MCP.P2) #variabele channel3 is potentiometer 3
rgb_led = RGBLED(red= 14, green= 15, blue= 18) #variabele RGBLED aangesloten op pin 14, 15 en 18
while True: #als waarde True is,
    rood = channel1.value/65535 #waarde van potmeter1 delen door 65535 zodat het 0 of 1 is, is kleur rood
    groen = channel2.value/65535  #waarde van potmeter2 delen door 65535 zodat het 0 of 1 is, is kleur groen
    blauw = channel3.value/65535  #waarde van potmeter3 delen door 65535 zodat het 0 of 1 is, is kleur blauw
    rgb_led.color =(rood, groen, blauw) #variabele rgb_led.color met waarde van de kleuren

    
                                                                                                                                                                                                                                                                                                                                                                                                 






































































