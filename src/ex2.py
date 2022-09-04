import pathlib
from PIL import Image
import numpy as np
import math
from tqdm import tqdm
import cv2

script_location = pathlib.Path(__file__)
assets = script_location.parent.joinpath("../assets/")
results = script_location.parent.joinpath("../results/")

CAT =Image.open(assets.joinpath("cat.jpg"))

DOG = np.array(Image.open(assets.joinpath("dog.jpg")))
#DOG = CAT.convert('L')
#DOG = np.array(DOG)
CHIHIRO = np.array(Image.open(assets.joinpath("chihiro.jpg")))

def contrast_stretching(img):

    i = img.convert('L')
    width, height = i.size
    higher = 0 
    lower = 256

    for w in range(width):
        for h in range(height):
            if (i.getpixel((w,h))) > higher:
                higher = i.getpixel((w,h)) 
               
    for w in range(width):
        for h in range(height):
            if (i.getpixel((w,h))) < lower:
                lower = i.getpixel((w,h))

    for w in tqdm(range(width)):
        for h in range(height):
                p = i.getpixel((w,h)) 
                p = int((255*(p - lower))/(higher-lower))
                i.putpixel((w,h), p)
    return i



print("Contrast Stretching")
img = contrast_stretching(CAT)
img.save(results.joinpath('cat-cs.jpg'))
print()
img.show()


    
