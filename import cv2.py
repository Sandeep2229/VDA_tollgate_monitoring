import cv2
import pytesseract

# Load the video file
cap = cv2.VideoCapture("/Users/apple/Downloads/yolo-coco/Camera4_20230327073000.avi")

# Set the time stamp to extract the frame
cap.set(cv2.CAP_PROP_POS_MSEC, 5000)

# Read the frame
ret, frame = cap.read()

# Convert the frame to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Use pytesseract to extract the text from the frame
text = pytesseract.image_to_string(gray)

# Process the text to extract the date and time information
# Example string: "Date: 01/01/2023 Time: 09:30:00"
date_str = text.split('Date: ')[1].split(' ')[0]
time_str = text.split('Time: ')[1].strip()

print('Date:', date_str)
print('Time:', time_str)
