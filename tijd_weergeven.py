import time as time


while True:
    huidige_tijd = time.ctime()
    print(huidige_tijd)

    tijd_in_seconden = time.time()
    print(tijd_in_seconden) 

    tijdzone = time.tzname
    print(tijdzone)
    time.sleep(1.0)



