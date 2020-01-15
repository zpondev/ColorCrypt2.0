import math, os
import base64 as b64
from PIL import Image, ImageDraw 
import random as rand


def encode():
	path = input("Enter path of file: ")
	if (path[-1:] == "\'" and path[:1] == "\'") or (path[-1:] == "\"" and path[:1] == "\""): path = path[1:-1]

	f = open(path, "rb")
	file = f.read()
	f.close()

	l = []
	for i in b64.b64encode(file):
		l.append(i)

	l.append(1)
	for i in b64.b64encode(str.encode(os.path.basename(path))): l.append(i)


	if (len(l) % 3) != 0: l.append(0)
	if (len(l) % 3) != 0: l.append(0)
	
	wh = math.ceil(math.sqrt(math.ceil(len(l)/3)))

	img = Image.new("RGB", (wh, wh))
	draw = ImageDraw.Draw(img)

	for x in range(img.size[0]):
		for y in range(img.size[1]):

			if len(l) > 0:
				r = l.pop()
				g = l.pop()
				b = l.pop()
			else:
				r, g, b = 0, 0, 0

			draw.point((x, y), (r*2, g*2, b*2)) #Colored!

	img.save("result.png", "PNG")
	print("\nSuccess! File \"result.png\" are saved!" )


def decode():
	path = input("Enter path of file: ")
	if (path[-1:] == "\'" and path[:1] == "\'") or (path[-1:] == "\"" and path[:1] == "\""): path = path[1:-1]

	l = []
	img = Image.open(path)
	pix = img.load()

	for x in range(img.size[0]):
		for y in range(img.size[1]):

			l.append(pix[x, y][0])
			l.append(pix[x, y][1])
			l.append(pix[x, y][2])

	l.reverse()
	l = [i for i in l if i != 0]

	a, name = [], []
	c = 0
	for i in l:
		i = int(i / 2)
		if i == 1:
			c = 1
			continue
		if c == 0:
			a.append(i)
		else:
			name.append(i)

	l = b64.b64decode(str.encode("".join(map(chr, list(a)))))
	name = b64.b64decode(str.encode("".join(map(chr, name)))).decode("utf-8")

	f = open("result-"+name, "wb")
	f.write(l)
	f.close()

	print( "\nSuccess! File "+name+" are saved.")


r = input("1 - Encode file;\n2 - Decode file;\n3 - About author;\n-")
if(r == "1"):
	encode()
elif(r == "2"):
	decode()
elif(r == "3"):
	print("\n © Andrey Ivanov\nEmail: andreie5555@gmail.com\n15.01.2020")
else:
	print("Error")
