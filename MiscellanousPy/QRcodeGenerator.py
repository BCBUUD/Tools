#!/bin/bash/python3
import qrcode 


data = input("Enter Text:  ")

img = qrcode.make(data)

img.save("qrcode.png")

