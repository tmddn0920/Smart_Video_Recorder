import cv2

cam = cv2.VideoCapture(0)
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cam.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

recording = False
dark_mode = False
flip_mode = False
    
while True:
    ret, frame = cam.read()
    if not ret:
        break
    
    if flip_mode:
        frame = cv2.flip(frame, 1)
    
    if dark_mode:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    
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
    elif key == ord('d'):  
        dark_mode = not dark_mode
    elif key == ord('f'): 
        flip_mode = not flip_mode

cam.release()
out.release()
cv2.destroyAllWindows()
cv2.waitKey(0)