#!/bin/bash/python3
import qrcode 


data = input("PUT TEXT HERE TO CONVERT TO QR CODE")

img = qrcode.make(data)

img.save("qrcode.png")

