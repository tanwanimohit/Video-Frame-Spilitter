#Open CV for Video Parsing
import cv2
# import the os module  for folder creation
import os

# define the name of the directory to be created
pwd=os.getcwd();
path = pwd+"/frames"

try:  
    os.mkdir(path)
except OSError:  
    print ("Maybe Frames Folder Already Exists if not Create it manually than run the Program")
else:  
    print ("Successfully created the directory %s " % path)

#Video Location
string = input("Enter the video location or URL : ")
vidcap = cv2.VideoCapture(string)
image = vidcap.read()

#To Maintain the Frames Count
count = 0

success=True
print("Spliting Video Frames")

#Main Logic
while success:
  success,image = vidcap.read()
  if(success):
      cv2.imwrite("frames/frame%d.jpg" % count, image)
      count += 1 
else:
  pass

print("Done!")
print ("Total ",count-1," images Generated ")
