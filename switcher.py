#!/usr/bin/python
# A script to switch mic using ReSpeaker's button

from gpiozero import Button
import alsaaudio
import time

button = Button(17)

try:
    mixer = alsaaudio.Mixer('Capture')
except Exception, e:
    print("error: can't find capture devices")
    exit(1)

last = time.time()
while True:
    if button.is_pressed:
        now = time.time()
        if (now - last) > 0.5:
            if mixer.getrec() == [1, 1]:
                print('mic is disabled')
                mixer.setrec(0)
            else:
                print('mic is enabled')
                mixer.setrec(1)
            last = now
    time.sleep(0.010)
