# Face Recognition Project (Python + OpenCV + face_recognition)

This project implements real-time face recognition using a webcam. It
uses the **face_recognition** library for encoding faces and **OpenCV**
for video capture and drawing bounding boxes.

## Features

-   Real-time webcam face detection
-   Face recognition using pre-encoded images
-   Bounding box and name overlay
-   Automatic camera index detection
-   Loads all face images from an `images/` directory

## Requirements

    pip install opencv-python face_recognition dlib numpy

## Project Structure

    project_folder/
    ├── main.py
    ├── simple_facerec.py
    └── images/

## Running

    python main.py

## Adding Faces

Place clear, single-face images inside `images/`.

## Troubleshooting

Try camera indexes 0,1,2 if webcam appears black.
