#!/bin/bash/python3
from stegano import lsb 


# resources 

inImgPNG = 'JAH.png'
inImgJPG = 'image1.jpg'

outImgPNG = 'topSecret.png'
outImgJPG = 'topSecret2.jpg'

msg = 'You gotta stop farting so much bro, you a febreeze fart freshener.'

lsb.hide(inImgPNG, message=msg).save(outImgPNG)

message = lsb.reveal(outImgPNG)

print(f'Reveal message: {message}')

