import os
import glob

import cv2
import face_recognition
import numpy as np


class SimpleFaceRec:
    def __init__(self):
        # Encodings (numbers that represent each face)
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize factor (smaller frame = faster)
        self.frame_resizing = 0.25

    def load_encoding_images(self, images_path):
        """
        Load all images from the given folder, compute encodings,
        and store them with their names.
        """
        images_path_list = glob.glob(os.path.join(images_path, "*.*"))

        print(f"{len(images_path_list)} images found in '{images_path}'")

        for img_path in images_path_list:
            img = cv2.imread(img_path)
            if img is None:
                print(f"Could not read image: {img_path}")
                continue

            # Convert BGR (OpenCV) to RGB (face_recognition)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Compute encodings (may return empty list if no face)
            encodings = face_recognition.face_encodings(rgb_img)
            if len(encodings) == 0:
                print(f"No face found in: {img_path}")
                continue

            img_encoding = encodings[0]

            # Get filename only (without folder & extension)
            basename = os.path.basename(img_path)
            name, _ = os.path.splitext(basename)

            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(name)

            print(f"Encoded image for: {name}")

        print("All encodings loaded!")

    def detect_known_faces(self, frame):
        """
        Detect and recognize known faces in a frame.
        Returns:
          - face_locations (y1, x2, y2, x1)
          - face_names (list of names)
        """
        # Resize frame for speed
        small_frame = cv2.resize(
            frame,
            (0, 0),
            fx=self.frame_resizing,
            fy=self.frame_resizing
        )

        # Convert BGR to RGB
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Detect faces and encodings on the small frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations
        )

        face_names = []

        for face_encoding in face_encodings:
            # Compare against known faces
            matches = face_recognition.compare_faces(
                self.known_face_encodings, face_encoding
            )
            name = "Unknown"

            # Use distance to choose best match
            face_distances = face_recognition.face_distance(
                self.known_face_encodings, face_encoding
            )

            if len(face_distances) > 0:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]

            face_names.append(name)

        # Scale back up face locations to original frame size
        face_locations = np.array(face_locations)
        face_locations = (face_locations / self.frame_resizing).astype(int)

        return face_locations, face_names
