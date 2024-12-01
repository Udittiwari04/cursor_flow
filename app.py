
from flask import Flask, render_template
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import cv2
import mediapipe as mp
import pyautogui
import time
import threading

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Global variables for thread control
mouse_active = False
thread = None

def eye_controlled_mouse():
    global mouse_active
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()
    prev_x, prev_y = 0, 0
    dwell_start_time = None
    dwell_threshold = 2  # Seconds
    tolerance = 20

    while True:
        if not mouse_active:
            time.sleep(0.1)  # Idle when inactive
            continue

        ret, frame = cam.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks

        if landmark_points:
            landmarks = landmark_points[0].landmark
            screen_x = screen_w * ((landmarks[474].x + landmarks[475].x) / 2)
            screen_y = screen_h * ((landmarks[474].y + landmarks[475].y) / 2)

            # Smooth movement
            screen_x = 0.2 * screen_x + 0.8 * prev_x
            screen_y = 0.2 * screen_y + 0.8 * prev_y
            prev_x, prev_y = screen_x, screen_y

            pyautogui.moveTo(screen_x, screen_y)

            # Dwell click
            if abs(prev_x - screen_x) < tolerance and abs(prev_y - screen_y) < tolerance:
                if dwell_start_time is None:
                    dwell_start_time = time.time()
                elif time.time() - dwell_start_time > dwell_threshold:
                    pyautogui.click()
                    dwell_start_time = None
            else:
                dwell_start_time = None

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mobi-mouse')
def mobimouse():
    return render_template('mobi-mouse.html')


@app.route('/vanni')
def vanni():
    return render_template('vanni.html')

@app.route('/dristi')
def dristi():
    return render_template('dristi.html')


@socketio.on('toggle_mouse')
def toggle_mouse(data):
    global mouse_active, thread
    mouse_active = data['active']
    emit('status', {'active': mouse_active})

    if mouse_active and thread is None:
        thread = threading.Thread(target=eye_controlled_mouse)
        thread.start()

