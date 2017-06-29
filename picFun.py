from PIL import Image
#average
#import the image
myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixellist = list(imageData)

newPixellist=[]

#pixel manipulation
for pixel in pixellist:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    #average =(red + green + blue)//3
    #newRed = average
    #newGreen = average
    #newBlue = average
    newRed = 255 - red #or average
    if newRed > 255: #this the restriction/can't go over or under
        newRed = 255

    newGreen = 255 - green #or average
    if newGreen > 255:
        newGreen = 255

    newBlue = 255 - blue #or average
    if newBlue > 255:
        newBlue = 255

    p = (newRed,newGreen,newBlue)

    #add pixel to new pixel list
    newPixellist.append(p)


#open image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixellist)
newImage.show()
