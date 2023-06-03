import pyautogui
from PIL import Image, ImageGrab
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)

def iscollide(data):
    for i in range(300,415):
        for j in range(600,650):
            if data[i,j] < 100:
                return True
    return False               

if __name__ == "__main__":
    print("Hey... Dino game about to start in 3 seconds")
    time.sleep(3)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if iscollide(data):
            hit("up")
        # print(asarray(image))
        for i in range(300,415):
            for j in range(600,650):
                data[i,j] = 0    
        image.show()
        break        