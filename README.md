# Face Recognition Project Readme

## Face Recognition Project (Python + OpenCV + face_recognition)

This project implements real-time face recognition using a webcam. It
uses the `face_recognition` library for encoding faces and OpenCV for
video capture and drawing bounding boxes.

## 📌 Features

-   Real-time webcam face detection
-   Face recognition using pre-encoded images
-   Bounding box and name overlay on each detected face
-   Automatic camera index detection (0,1,2...)
-   Loads all face images from an `images/` directory

## 🛠 Requirements

Install the following: - Python 3.8 or 3.9 (64-bit recommended) -
OpenCV - face_recognition - dlib

Install dependencies:

    pip install opencv-python face_recognition dlib numpy

## 📁 Project Structure

    project_folder/
    │
    ├── main.py
    ├── simple_facerec.py
    ├── images/
    │     ├── person1.jpg
    │     ├── person2.png
    │
    └── README.md

## 📷 How It Works

1.  `simple_facerec.py` loads and encodes all faces from the `images/`
    folder.
2.  `main.py` opens the webcam and captures frames.
3.  The system detects all faces in the frame.
4.  It compares detected face encodings with known encodings.
5.  A bounding box and name are drawn around matches.

## ▶️ Running the Project

Run:

    python main.py

The webcam will open automatically. Press **ESC** to exit.

## 📁 Adding Your Own Faces

Add clear images (one face per image) to the `images/` folder.

Name the files as labels:

    images/
       ali.png   → "ali"
       john.jpg  → "john"

Run the project again.

## ❗ Common Issues & Fixes

### Black Camera Window

Try different camera indexes:

    cap = cv2.VideoCapture(0)
    cap = cv2.VideoCapture(1)
    cap = cv2.VideoCapture(2)

### "No face found in image"

Use: - Clear images - Only one face per picture - Good lighting

### dlib Installation Errors

Make sure you are using Python 3.8 or 3.9 (64-bit).

## 🧩 Credits

This project is based on OpenCV and the excellent `face_recognition`
library.

## 📌 License

This project is for educational purposes and free to modify.
