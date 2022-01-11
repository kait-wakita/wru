import cv2
import datetime

print('simple video capture (usage: python3 JetsonVideoCapture.py), HIT q for exit')

#ww, hh = 640, 360
#ww, hh = 1280, 720
ww, hh = 1920, 1080

t_delta=datetime.timedelta(hours=9)
JST=datetime.timezone(t_delta,'JST')
tm=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y%m%d%H%M%S")

camera = cv2.VideoCapture(0)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, ww)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, hh)

fps = int(camera.get(cv2.CAP_PROP_FPS))
#w = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
#h = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter("video-"+tm+".mp4", fourcc, fps, (ww, hh))

while True:
    ret, frame = camera.read()
    cv2.imshow('camera', frame)
    video.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
