from gpiozero import LEDBoard # importeert module LEDBoard
from time import sleep # importeert module sleep

leds = LEDBoard(5,6,13,19,26,16,20,21)# variabele leds met waarde alle pins waarop de leds aangesloten zijn

while True: # als waarde True is, dan

    leds.value = (1, 0, 0, 0, 0, 0, 0, 0)# zet de waarde van led 1 op 1 de rest op 0
    sleep(0.1)# wacht 0.1 sec
    leds.value = (0, 1, 0, 0, 0, 0, 0, 0)# zet de waarde van led 2 op 1 de rest op 0
    sleep(0.1)# wacht 0.1 sec
    leds.value = (0, 0, 1, 0, 0, 0, 0, 0)# zet de waarde van led 3 op 1 de rest op 0
    sleep(0.1)# wacht 0.1 sec
    leds.value = (0, 0, 0, 1, 0, 0, 0, 0)# zet de waarde van led 4 op 1 de rest op 0
    sleep(0.1)# wacht 0.1 sec
    leds.value = (0, 0, 0, 0, 1, 0, 0, 0)# zet de waarde van led 5 op 1 de rest op 0
    sleep(0.1)# wacht 0.1 sec
    leds.value = (0, 0, 0, 0, 0, 1, 0, 0)# zet de waarde van led 6 op 1 de rest op 0
    sleep(0.1)# wacht 0.1 sec
    leds.value = (0, 0, 0, 0, 0, 0, 1, 0)# zet de waarde van led 7 op 1 de rest op 0
    sleep(0.1)# wacht 0.1 sec
    leds.value = (0, 0, 0, 0, 0, 0, 0, 1)# zet de waarde van led 8 op 1 de rest op 0
    sleep(0.1)# wacht 0.1 sec
    leds.value = (0, 0, 0, 0, 0, 0, 1, 0)# zet de waarde van led 7 op 1 de rest op 0
    sleep(0.1)# wacht 0.1 sec
    leds.value = (0, 0, 0, 0, 0, 1, 0, 0)# zet de waarde van led 6 op 1 de rest op 0
    sleep(0.1)# wacht 0.1 sec
    leds.value = (0, 0, 0, 0, 1, 0, 0, 0)# zet de waarde van led 5 op 1 de rest op 0
    sleep(0.1)# wacht 0.1 sec
    leds.value = (0, 0, 0, 1, 0, 0, 0, 0)# zet de waarde van led 4 op 1 de rest op 0
    sleep(0.1)# wacht 0.1 sec
    leds.value = (0, 0, 1, 0, 0, 0, 0, 0)# zet de waarde van led 3 op 1 de rest op 0
    sleep(0.1)# wacht 0.1 sec
    leds.value = (0, 1, 0, 0, 0, 0, 0, 0)# zet de waarde van led 2 op 1 de rest op 0
    sleep(0.1)# wacht 0.1 sec
