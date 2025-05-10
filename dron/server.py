from flask import Flask, Response
import cv2

app = Flask(__name__)


def generate_frame():
    cam = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = cam.read()
            if not ret:
                break
            _, buffer = cv2.imencode(".jpg",frame)
            frame = buffer.tobytes()    
            yield(b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")
    finally:
        cam.release()

@app.route("/")
def video_feed():
     return Response(generate_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)