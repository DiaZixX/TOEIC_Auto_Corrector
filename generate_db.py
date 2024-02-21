#!/usr/bin/env python3

"""
Generate database to train AI
"""

import random as rd
from PIL import Image, ImageDraw

COORD_TOP_LEFT_1 = (543,1006)
COORD_TOP_LEFT_2 = (511,1975)
CIRCLE_RADIUS = 20
CIRCLE_COLOR = (0, 0, 0) 

ANSWERS = [0, 1, 2, 3]

PROB_DOUBLE = 1/500

def mark(n, three) :
    possibilities = [i for i in ANSWERS]
    if three :
        possibilities.pop()
    ret = []
    for k in range(0, n) : 
        temp = possibilities.pop(rd.randint(0, (len(possibilities)-1)))
        ret.append(temp)
    return ret

def generate_circles():
    circle_coords = []
    droite1 = 0
    bas2 = 0
    label = []
    for i in range(0, 200): 
        if i in [40, 60, 70, 90, 150, 170, 180, 190]:
            droite1 += 1
        if i in [110, 120, 130, 140, 150, 160, 170, 180, 190] :
            bas2 += 4
        if 10 <= i <= 39 :
            if rd.random() < PROB_DOUBLE :
                ans = mark(2, True)
            else : 
                ans = mark(1, True)
        else :
            if rd.random() < PROB_DOUBLE :
                ans = mark(2, False)
            else : 
                ans = mark(1, False)
        for k in ans :
            if i < 100 :
                circle_coords.append((COORD_TOP_LEFT_1[0]+k*47+(i // 10)*(289+droite1)-(i % 10)*(1.5), COORD_TOP_LEFT_1[1]+(i % 10)*52))
            else : 
                circle_coords.append((COORD_TOP_LEFT_2[0]+k*47+((i-100) // 10)*(289+droite1)-(i % 10)*(1.5), COORD_TOP_LEFT_2[1]+(i % 10)*52+bas2))
        if len(ans) == 2 : 
            label.append("ERR")
        else : 
            match ans[0] :
                case 0 : 
                    label.append("A")
                case 1 : 
                    label.append("B")  
                case 2 : 
                    label.append("C")  
                case 3 : 
                    label.append("D")   
    return (circle_coords,label)
                
def main() :
    image_path = "blank.jpg"
    image = Image.open(image_path)

    draw = ImageDraw.Draw(image)

    (circle_coordinates, label) = generate_circles()

    print(label)
    for coord in circle_coordinates:
        x, y = coord
        draw.ellipse((x - CIRCLE_RADIUS, y - CIRCLE_RADIUS, x + CIRCLE_RADIUS, y + CIRCLE_RADIUS), fill=CIRCLE_COLOR)
    image.save("image_modifiee.jpg")
    image.show()
    return 0


if __name__ == '__main__' :
    main()
