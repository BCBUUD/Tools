#!/bin/bash/python3
import qrcode 

data = "PUT TEXT HERE TO CONVERT TO QR CODE"

img = qrcode.make(data)

img.save("qrcode.png")

