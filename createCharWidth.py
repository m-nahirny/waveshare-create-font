import os
import sys
from PIL import Image, ImageDraw, ImageFont

SANS_FONT = '/usr/share/fonts/truetype/freefont/FreeSans.ttf'
SANS_BOLD_FONT = '/usr/share/fonts/truetype/freefont/FreeSansBold.ttf'
SERIF_FONT = '/usr/share/fonts/truetype/freefont/FreeSerif.ttf'

FONT_SIZE_MAX_SA = 64
FONT_SIZE_MAX_PCTG = 38
FONT_SIZE_RECENT_SA = 32
FONT_SIZE_STATUS = 24
FONT_SIZE_STATUS_RECENT = 20
FONT_SIZE_CLOCK = 24
FONT_SIZE_DATE = 20

FONT_64_OFFSET = 10
FONT_32_OFFSET = 6
FONT_24_OFFSET = 4
FONT_20_OFFSET = 3

BUFFER_WIDTH = 40
BUFFER_HEIGHT = 50

WHITE = 1
BLACK = 0

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def getBuffer(image):
    buf = [0xFF] * (int(BUFFER_WIDTH/8) * BUFFER_HEIGHT)
    image_monocolor = image.convert('1')
    imwidth, imheight = image_monocolor.size
    pixels = image_monocolor.load()
    # logging.debug("imwidth = %d, imheight = %d",imwidth,imheight)
    if(imwidth == BUFFER_WIDTH and imheight == BUFFER_HEIGHT):
        for y in range(imheight):
            for x in range(imwidth):
                # Set the bits for the column of pixels at the current position.
                if pixels[x, y] == 0:
                    buf[int((x + y * BUFFER_WIDTH) / 8)] &= ~(0x80 >> (x % 8))
    elif(imwidth == BUFFER_HEIGHT and imheight == BUFFER_WIDTH):
        for y in range(imheight):
            for x in range(imwidth):
                newx = y
                newy = BUFFER_HEIGHT - x - 1
                if pixels[x, y] == 0:
                    buf[int((newx + newy*BUFFER_WIDTH) / 8)] &= ~(0x80 >> (y % 8))
    return buf

def print_font_bitmap(c):
	max_sa_font = ImageFont.truetype(SANS_FONT, FONT_SIZE_MAX_SA)
	recent_sa_font = ImageFont.truetype(SANS_FONT, FONT_SIZE_RECENT_SA)
	status_font = ImageFont.truetype(SANS_FONT, FONT_SIZE_STATUS)
	status_recent_font = ImageFont.truetype(SANS_FONT, FONT_SIZE_STATUS_RECENT)

	# initially set all white background
	image = Image.new('1', (BUFFER_WIDTH, BUFFER_HEIGHT), WHITE)

	# prepare for drawing
	draw = ImageDraw.Draw(image)

	draw.text((0, FONT_32_OFFSET), c, fill=BLACK, font=recent_sa_font)
	buffer = getBuffer(image)
	max_width = 0
	for i in range(0, int(BUFFER_HEIGHT)):
		for j in range(0, int(BUFFER_WIDTH // 8)):
			char = buffer[i * BUFFER_WIDTH // 8 + j]
			if char >> 7 & 1 == 0:
				if max_width < j * 8 + 1:
					max_width = j * 8 + 1
			if char >> 6 & 1 == 0:
				if max_width < j * 8 + 2:
					max_width = j * 8 + 2
			if char >> 5 & 1 == 0:
				if max_width < j * 8 + 3:
					max_width = j * 8 + 3
			if char >> 4 & 1 == 0:
				if max_width < j * 8 + 4:
					max_width = j * 8 + 4
			if char >> 3 & 1 == 0:
				if max_width < j * 8 + 5:
					max_width = j * 8 + 5
			if char >> 2 & 1 == 0:
				if max_width < j * 8 + 6:
					max_width = j * 8 + 6
			if char >> 1 & 1 == 0:
				if max_width < j * 8 + 7:
					max_width = j * 8 + 7
			if char & 1 == 0:
				if max_width < j * 8 + 8:
					max_width = j * 8 + 8
	if c == '\\':
		line = hex(max_width) + ", // back slash"
	else:
		line = hex(max_width) + ", // " + c 
	print(line)

def main():
	for c in char_range(' ','~'):
		print_font_bitmap(c)



if __name__ == '__main__':
	main()
	
