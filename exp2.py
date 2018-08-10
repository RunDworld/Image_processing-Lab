from PIL import Image
import matplotlib.pyplot as plt

class histogram_Equalization:
  def __init__(self,wd,ht,im):

    self.w = wd
    self.h = ht
    self.img = im
    self.new_img = Image.new("RGB",(wd,ht),"white")
    self.pixels = self.new_img.load()
    self.new_img = Image.new("RGB",(wd,ht),"white")
    self.pixels = self.new_img.load()
  

  def plotly(self,lst,n):
    x = [i for i in range(256)]
    plt.plot(x,lst)
    plt.xlabel('Grey-Level')
    plt.ylabel('No. of Pixels')
    if n == 1:
      plt.title("Original Image")
    else:
      plt.title("Equalised Image")
    plt.show()

  def generate(self,sk):
    
    for wd in range(self.w):
      for ht in range(self.h):
        pix = self.img.getpixel((wd,ht))
        r = pix[0]
        self.pixels[wd,ht] = (round(sk[r]),round(sk[r]),round(sk[r]))
    self.new_img.show()
  def equalise(self):

    gLevel = [0]*256
    pdf = [0]*256
    cf = [0]*256
    sk = [0]*256
    new_gLevel = [0]*256
    for wd in range(self.w):
      for ht in range(self.h):
        pix = self.img.getpixel((wd,ht))
        r = pix[0]
        g = pix[1]
        b = pix[2]
        x = (r+b+g)/3
        # x = r
        gLevel[round(x)] = gLevel[round(x)] + 1
    self.plotly(gLevel,1)
    nk = self.w*self.h
    for i in range(len(gLevel)):
      pdf[i] = gLevel[i]/nk
      if i >= 1:
        cf[i] = pdf[i]+cf[i-1]
      else:
        cf[i] = pdf[0] 
      sk[i] = 255*cf[i]
      new_gLevel[round(sk[i])] += gLevel[i]
    print(new_gLevel)
    self.plotly(new_gLevel,2)
    self.generate(sk)


def main():
  img = Image.open("img1.jpg")
  pixel = img.getpixel((50,50))
  print(pixel)
  w,h = img.size
  histe = histogram_Equalization(w,h,img)
  histe.equalise()
  
if __name__=='__main__':
  main()