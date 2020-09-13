#Import the required packages
import cv2 #for capturing the video
import time #for halting the while loop using sleep function


try:

    #face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    #Initialize the camera
    cap=cv2.VideoCapture(0)

    #Set the video resolution to half of the possible max resolution for better performance
    cap.set(3, 1920/2)
    cap.set(4, 1000/2)
    x=1
    for x in range(0,30): #Loop for capturing frames for 30 seconds
        print("Getting the image")
        ret, image =cap.read() #reading from the live webcam
        name='img/Execution-{}.jpg'.format(x) #Naming each frame image
        cv2.imwrite(name,image)
        time.sleep(1) #halting the loop for 1.0 seconds
        cv2.imshow("Window Capture", image) #Displaying the frames on the screen
        k=cv2.waitKey(30) & 0xff
        if k==27: #If user presses escape key before 30 seconds the loop will stop
            break
    cap.release()
    cv2.destroyAllWindows()
except Exception as error:
    print("Looks like something is wrong. Please check your camera and re run the program again")
    print("The error is :"+ str(error))


