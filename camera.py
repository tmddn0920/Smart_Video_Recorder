import cv2

cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'avc1') 
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

recording = False
    
while True:
    ret, frame = cam.read()
    if not ret:
        break
    
            
    if recording:
        out.write(frame)
        cv2.circle(frame, (50, 50), 22, (0, 0, 0), -1)
        cv2.circle(frame, (50, 50), 18, (0, 0, 255), -1)
        cv2.putText(frame, "Recording..", (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

    
    cv2.imshow("Camera", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    elif key == 32:
        recording = not recording

cam.release()
out.release()
cv2.destroyAllWindows()
cv2.waitKey(0)