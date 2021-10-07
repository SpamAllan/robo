# -*- coding: utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd2in9
epd = epd2in9.EPD()

import time

from PIL import Image, ImageDraw, ImageFont

epd = epd2in9.EPD() # get the display
epd.init(epd.lut_full_update)   # initialize the display
print("Clear...")    # prints to console, not the display, for debugging
epd.Clear(0xFF)      # clear the display

def printtodisplay(string):
    HBlackImage = Image.new('1', (epd2in9.EPD_HEIGHT, epd2in9.EPD_WIDTH), 255)
    # HRedImage = Image.new('1', (epd2in9.EPD_HEIGHT, epd2in9.EPD_WIDTH), 255)
    draw = ImageDraw.Draw(HBlackImage) # Create draw object and pass in the image layer we want to work with (HBlackImage)
    font = ImageFont.truetype('./font/zig.ttf', 16) # Create our font, passing in the font file and font size
    draw.text((25, 25), string, font = font, fill = 0)
    epd.display(epd.getbuffer(HBlackImage))

printtodisplay("Hello Aria! \n How was your day?? \n1 = bad, 5 = good")

# Respones to input 1 - 5
# a = 'That bad?! \nI hid a present in the board games to cheer you up'
# b = 'Oh no \nmaybe have a G&T'
# c = 'Cosi cosi. \nDinner will make it better!'
# d = 'Pretty good!'
# e = 'Wow! Such a good day. \nI am so happy for you'

# Will take input then slep 15 before displaying these
# printToDisplay("Good chatting but I'm sleepy. \nTalk to you tomorrow")
# printToDisplay("Feel free to give me \na jolt of power to wake me up")

prompt1=raw_input("Hello Aria! \nHow was your day?? \n1 = bad, 5 = good\n")

if prompt1 == '1':
    print 'That bad?! \nI hid a present in \nthe board games to cheer \nyou up.'
    printtodisplay('That bad?! \nI hid a present in \nthe board games to \ncheer you up.')
elif prompt1 == '2':
    print 'Oh no! \nMaybe have a G&T'
    printtodisplay('Oh no! \n\nMaybe have a G&T?')
elif prompt1 == '3':
    print 'Cosi cosi. \nDinner will make \nit better!'
    printtodisplay('Cosi cosi. \nDinner will make \nit better!')
elif prompt1 == '4':
    print '\n \n   Pretty good!'
    printtodisplay('Pretty good!')
elif prompt1 == '5':
    print 'Wow! Such a good day. \nI am so happy for you.'
    printtodisplay('Wow! \nSuch a good day. \nI am happy for you!')

time.sleep(12) 
print 'Good chatting but I am sleepy. \nTalk to you tomorrow.'
printtodisplay('Good chatting but \nI am sleepy. \n\nLets talk tomorrow!')
time.sleep(12)
print 'Feel free to give me \na jolt of power to wake me up.'
printtodisplay('Please switch me \noff so I can rest. \nGive me a jolt of \npower to wake me \nup tomorrow.')
time.sleep(12)
print 'Night friend!'
printtodisplay('\n \n   Night friend!')
time.sleep(8)
printtodisplay('\n \n     0      0        ')

epd.sleep
