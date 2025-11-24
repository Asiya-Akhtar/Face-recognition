import cv2
from simple_facerec import SimpleFaceRec

# Encode Faces from a Folder
sfr = SimpleFaceRec()
sfr.load_encoding_images("images/")

# Try camera indexes 0, 1, 2 until one works
for cam_index in [0, 1, 2, 3]:
    cap = cv2.VideoCapture(cam_index)
    if cap.isOpened():
        print(f"Camera found at index {cam_index}")
        break
else:
    print("ERROR: No working camera found.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame — camera index might be wrong.")
        break

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)

    for face_loc, name in zip(face_locations, face_names):
        # face_recognition returns (top, right, bottom, left)
        top, right, bottom, left = face_loc

        # Draw bounding box
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw name above box
        cv2.putText(frame, name, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:   # ESC key
        break

cap.release()
cv2.destroyAllWindows()
