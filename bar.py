import cv2
import matplotlib.pyplot as plt
import numpy as np


cap = cv2.VideoCapture("youtube.mp4")
try:
    frames = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    width  = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
except AttributeError:
    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fig, ax = plt.subplots(1,1)
plt.ion()
plt.show()

#Setup a dummy path
x = np.linspace(0,width,frames)
y = x/2. + 100*np.sin(2.*np.pi*x/1200)

for i in range(frames):
    fig.clf()
    flag, frame = cap.read()

    plt.imshow(frame)
    plt.plot(x,y,'k-', lw=2)
    plt.plot(x[i],y[i],'or')
    plt.pause(0.01)

    if cv2.waitKey(1) == 27:
        break
    
