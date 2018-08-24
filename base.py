from PIL import Image

def main():
    img = Image.open("img.jpg")
    pixel = img.getpixel((50,50))
    print(pixel)
  
    w,h = img.size
    new_img = Image.new("RGB",(w,h),"white")

    pixels = new_img.load()
    for i in range(w):
        for j in range(h):
            if i > 100 and j > 100:
                pix = img.getpixel((i,j))
                pixels[i,j] = (0,0,0)
            else:
                pixels[i,j] = img.getpixel((i,j))
    print(new_img)
    new_img.show()
    


if __name__ == '__main__':
    main()
    # https://www.codementor.io/isaib.cicourel/image-manipulation-in-python-du1089j1u
    # https://dzone.com/articles/image-processing-in-python-with-pillow
    # http://www.bogotobogo.com/python/python_image_processing_with_Pillow_library.php
    # https://pythonprogramming.net/loading-images-python-opencv-tutorial/
  
