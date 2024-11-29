# import cv2
# import mediapipe as mp
# import pyautogui
# import time
# cam = cv2.VideoCapture(0)
# face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# screen_w, screen_h = pyautogui.size()
# # while True:
# #     _, frame = cam.read()
# #     frame = cv2.flip(frame, 1)
# #     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #     output = face_mesh.process(rgb_frame)
# #     landmark_points = output.multi_face_landmarks
# #     frame_h, frame_w, _ = frame.shape
# #     if landmark_points:
# #         landmarks = landmark_points[0].landmark
# #         for id, landmark in enumerate(landmarks[474:478]):
# #             x = int(landmark.x * frame_w)
# #             y = int(landmark.y * frame_h)
# #             cv2.circle(frame, (x, y), 3, (0, 255, 0))
# #             if id == 1:
# #                 screen_x = screen_w * landmark.x
#             #    screen_y = screen_h * landmark.y
# #                 pyautogui.moveTo(screen_x, screen_y)
# #         left = [landmarks[145], landmarks[159]]
# #         for landmark in left:
# #             x = int(landmark.x * frame_w)
# #             y = int(landmark.y * frame_h)
# #             cv2.circle(frame, (x, y), 3, (0, 255, 255))
# #         if (left[0].y - left[1].y) < 0.004:
# #             pyautogui.click()
# #             pyautogui.sleep(1)
# #     cv2.imshow('Eye Controlled Mouse', frame)
# #     cv2.waitKey(1)


# #  import cv2
# #  import mediapipe as mp
# #  import pyautogui

# #  # Initialize Camera and FaceMesh
# #  face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# #  cam = cv2.VideoCapture(0)
# #  screen_w, screen_h = pyautogui.size()

# #  # Scaling factors
# #  scaling_factor_x = 1.5
# #  scaling_factor_y = 1.5

# #  while True:
# #      _, frame = cam.read()
# #      frame = cv2.flip(frame, 1)
# #      rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# # # #     landmark_points = output.multi_face_landmarks
# # # #     output = face_mesh.process(rgb_frame)
# # # #     frame_h, frame_w, _ = frame.shape

# # # #     if landmark_points:
# # # #         landmarks = landmark_points[0].landmark
# # # #         for id, landmark in enumerate(landmarks[474:478]):
# # # #             x = int(landmark.x * frame_w)
# # # #             y = int(landmark.y * frame_h)
# # # #             cv2.circle(frame, (x, y), 3, (0, 255, 0))

# # # #             if id == 1:  # Focus point for cursor movement
# # # #                 # Scale and map to screen
# # # #                 screen_x = scaling_factor_x * screen_w * landmark.x
# # # #                 screen_y = scaling_factor_y * screen_h * landmark.y

# # # #                 # Clamp to screen boundaries
# # # #                 screen_x = min(max(0, screen_x), screen_w)
# # # #                 screen_y = min(max(0, screen_y), screen_h)

# # # #                 pyautogui.moveTo(screen_x, screen_y)

# # # #         # Blink detection for clicking
# # # #         left = [landmarks[145], landmarks[159]]
# # # #         for landmark in left:
# # # #             x = int(landmark.x * frame_w)
# # # #             y = int(landmark.y * frame_h)
# # # #             cv2.circle(frame, (x, y), 3, (0, 255, 255))
# # # #         if (left[0].y - left[1].y) < 0.004:
# # # #             pyautogui.click()
# # # #             pyautogui.sleep(1)

# # # #     cv2.imshow('Eye Controlled Mouse', frame)
# # # #     if cv2.waitKey(1) & 0xFF == ord('q'):
# # # #         break 


# prev_x, prev_y = 0, 0
# dwell_start_time = None
# dwell_threshold = 6  # in seconds
# tolerance = 25 # in pixels

# while True:
#     _, frame = cam.read()
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = face_mesh.process(rgb_frame)
#     landmark_points = output.multi_face_landmarks
#     frame_h, frame_w, _ = frame.shape
#     if landmark_points:
#         landmarks = landmark_points[0].landmark
#         left = [landmarks[145], landmarks[159]]
#         screen_x = screen_w * ((landmarks[474].x + landmarks[475].x) / 2)
#         screen_y = screen_h * ((landmarks[474].y + landmarks[475].y) / 2)


#         # Smooth cursor movement
#         screen_x = 0.24 * screen_x + 0.8 * prev_x
#         screen_y = 0.24 * screen_y + 0.8 * prev_y
#         prev_x, prev_y = screen_x, screen_y

#         pyautogui.moveTo(screen_x, screen_y)

#         # Dwell click
#         if abs(prev_x - screen_x) < tolerance and abs(prev_y - screen_y) < tolerance:
#             if dwell_start_time is None:
#                 dwell_start_time = time.time()
#             elif time.time() - dwell_start_time > dwell_threshold:
#                 pyautogui.click()
#                 dwell_start_time = None
#         else:
#             dwell_start_time = None

#     cv2.imshow('Eye Controlled Mouse', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# import cv2
# import mediapipe as mp
# import pyautogui
# import time
# import keyboard  # For detecting keypresses

# # Initialize Camera and FaceMesh
# cam = cv2.VideoCapture(0)
# face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# screen_w, screen_h = pyautogui.size()

# # Smoothing Variables
# prev_x, prev_y = 0, 0

# # Dwell Click Variables
# dwell_start_time = None
# dwell_threshold = 5 # Time in seconds
# tolerance = 20  # Pixel tolerance for dwell detection

# # Mouse Activity Toggle
# mouse_active = False

# print("Press 'S' to start or stop the eye-controlled mouse.")

# while True:
#     # Toggle mouse activity on 'S' key press
#     if keyboard.is_pressed('s'):
#         mouse_active =import not mouse_active
#         print(f"Eye-Controlled Mouse {'Activated' if mouse_active else 'Deactivated'}")
#         time.sleep(0.5)  # Debounce to prevent rapid toggling

#     if not mouse_active:
#         # Show the camera feed without any mouse control
#         _, frame = cam.read()
#         frame = cv2.flip(frame, 1)
#         cv2.putText(frame, "Eye-Controlled Mouse is OFF", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 
#                     1, (0, 0, 255), 2, cv2.LINE_AA)
#         cv2.imshow('Eye-Controlled Mouse', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#         continue

#     # Eye-Controlled Mouse Logic
#     _, frame = cam.read()
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = face_mesh.process(rgb_frame)
#     landmark_points = output.multi_face_landmarks
#     frame_h, frame_w, _ = frame.shape

#     if landmark_points:
#         landmarks = landmark_points[0].landmark
        
#         # Cursor Movement (Average of 2 key landmarks for precision)
#         screen_x = screen_w * ((landmarks[474].x + landmarks[475].x) / 2)
#         screen_y = screen_h * ((landmarks[474].y + landmarks[475].y) / 2)

#         # Smooth cursor movement
#         screen_x = 0.2 * screen_x + 0.8 * prev_x
#         screen_y = 0.2 * screen_y + 0.8 * prev_y
#         prev_x, prev_y = screen_x, screen_y

#         pyautogui.moveTo(screen_x, screen_y)

#         # Dwell-based Click
#         if abs(prev_x - screen_x) < tolerance and abs(prev_y - screen_y) < tolerance:
#             if dwell_start_time is None:
#                 dwell_start_time = time.time()
#             elif time.time() - dwell_start_time > dwell_threshold:
#                 pyautogui.click()
#                 print("Click Triggered")
#                 dwell_start_time = None
#         else:
#             dwell_start_time = None

#         # Blink Detection for Click
#         left_eye = [landmarks[145], landmarks[159]]
#         blink_dist = abs(left_eye[0].y - left_eye[1].y)
#         if blink_dist < 0.004:
#             pyautogui.click()
#             time.sleep(1)  # Prevent multiple clicks

#         # Visual Feedback
#         for id, landmark in enumerate([landmarks[474], landmarks[475]]):
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

#     # Show Camera Feed
#     cv2.putText(frame, "Eye-Controlled Mouse is ON", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 
#                 1, (0, 255, 0), 2, cv2.LINE_AA)
#     cv2.imshow('Eye-Controlled Mouse', frame)

#     # Exit on 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release resources
# cam.release()
# cv2.destroyAllWindows()





# import cv2
# import mediapipe as mp
# import pyautogui
# import time
# import keyboard

# # Initialize Phone Camera Stream (Replace with your app's URL)
# cam = cv2.VideoCapture('http://192.168.140.242:4747/video')  # Example IP Webcam URL
# face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
# screen_w, screen_h = pyautogui.size()

# # Smoothing Variables
# prev_x, prev_y = 0, 0

# # Dwell Click Variables
# dwell_start_time = None
# dwell_threshold = 1.5  # Time in seconds
# tolerance = 20  # Pixel tolerance for dwell detection

# # Mouse Activity Toggle
# mouse_active = False

# print("Press 'S' to start or stop the eye-controlled mouse.")

# while True:
#     # Toggle mouse activity on 'S' key press
#     if keyboard.is_pressed('s'):
#         mouse_active = not mouse_active
#         print(f"Eye-Controlled Mouse {'Activated' if mouse_active else 'Deactivated'}")
#         time.sleep(0.5)  # Debounce to prevent rapid toggling

#     if not mouse_active:
#         # Show the camera feed without any mouse control
#         _, frame = cam.read()
#         frame = cv2.flip(frame, 1)
#         cv2.putText(frame, "Eye-Controlled Mouse is OFF", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 
#                     1, (0, 0, 255), 2, cv2.LINE_AA)
#         cv2.imshow('Eye-Controlled Mouse', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#         continue

#     # Eye-Controlled Mouse Logic
#     _, frame = cam.read()
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     output = face_mesh.process(rgb_frame)
#     landmark_points = output.multi_face_landmarks
#     frame_h, frame_w, _ = frame.shape

#     if landmark_points:
#         landmarks = landmark_points[0].landmark
        
#         # Cursor Movement (Average of 2 key landmarks for precision)
#         screen_x = screen_w * ((landmarks[474].x + landmarks[475].x) / 2)
#         screen_y = screen_h * ((landmarks[474].y + landmarks[475].y) / 2)

#         # Smooth cursor movement
#         screen_x = 0.2 * screen_x + 0.8 * prev_x
#         screen_y = 0.2 * screen_y + 0.8 * prev_y
#         prev_x, prev_y = screen_x, screen_y

#         pyautogui.moveTo(screen_x, screen_y)

#         # Dwell-based Click
#         if abs(prev_x - screen_x) < tolerance and abs(prev_y - screen_y) < tolerance:
#             if dwell_start_time is None:
#                 dwell_start_time = time.time()
#             elif time.time() - dwell_start_time > dwell_threshold:
#                 pyautogui.click()
#                 print("Click Triggered")
#                 dwell_start_time = None
#         else:
#             dwell_start_time = None

#         # Blink Detection for Click
#         left_eye = [landmarks[145], landmarks[159]]
#         blink_dist = abs(left_eye[0].y - left_eye[1].y)
#         if blink_dist < 0.004:
#             pyautogui.click()
#             time.sleep(1)  # Prevent multiple clicks

#         # Visual Feedback
#         for id, landmark in enumerate([landmarks[474], landmarks[475]]):
#             x = int(landmark.x * frame_w)
#             y = int(landmark.y * frame_h)
#             cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

#     # Show Camera Feed
#     cv2.putText(frame, "Eye-Controlled Mouse is ON", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 
#                 1, (0, 255, 0), 2, cv2.LINE_AA)
#     cv2.imshow('Eye-Controlled Mouse', frame)

#     # Exit on 'q'
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release resources
# cam.release()
# cv2.destroyAllWindows()




# from flask import Flask, render_template
# from flask_cors import CORS
# from flask_socketio import SocketIO

# # Initialize Flask app
# app = Flask(__name__)

# # Enable CORS for all routes
# CORS(app)

# # Initialize Socket.IO with CORS allowed for all origins
# socketio = SocketIO(app, cors_allowed_origins="*")

# # Route to serve the main page
# @app.route('/')
# def index():
#     return render_template('index.html')  # Ensure this points to your HTML file

# # Define any additional Socket.IO events if required
# @socketio.on('message')
# def handle_message(data):
#     print(f"Message received: {data}")
#     socketio.send(f"Echo: {data}")

# # Start the server
# if __name__ == '__main__':
#     socketio.run(app, host='0.0.0.0', port=5000, debug=True)


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

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
