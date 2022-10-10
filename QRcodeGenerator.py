#!/bin/bash/python3
import qrcode 

data = "0xDA31928c8Bd47d3f9489F63c71E76862F232A609"

img = qrcode.make(data)

img.save("qrcode.png")

