from PIL import Image

##FUNCTIONS

def negative(pixel):
   for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
   
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
    newPixelList.append(p)
    
def overExpose (pixel):
 for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
   
    newRed = 255*2 
    if newRed > 255: 
        newRed = 255

    newGreen = 255*2 
    if newGreen > 255:
        newGreen = 255

    newBlue = 255*2 
    if newBlue > 255:
        newBlue = 255

    p = (newRed,newGreen,newBlue)

    #add pixel to new pixel list
    newPixelList.append(p)

#RUNNING CODE
#import the image
myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList=[]

length = len(pixelList)
halfway = length//2

counter = 0

for pixel in pixelList:
    

    #pixel manipulation
    if (counter < halfway): #this is the top half of the photo
        overExpose(pixel)
    else: #this is the bottom half of the photo
        negative(pixel)
    counter = counter + 1


    #create new pixel


    #add pixel to new pixel list
   


#open image
newImage = Image.new("RGB",myImage.size)
newImage.putdata(newPixellist)
newImage.show()

