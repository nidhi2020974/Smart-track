import face_recognition
import cv2

# Load an image from file
image = face_recognition.load_image_file("gauth.jpg")

# Find all face locations in the image
face_locations = face_recognition.face_locations(image)

print(f"Found {len(face_locations)} face(s) in this photograph.")

# Show the image using OpenCV with the faces highlighted
image_cv = cv2.imread("gauth.jpg")

# Draw rectangles around each face
for top, right, bottom, left in face_locations:
    cv2.rectangle(image_cv, (left, top), (right, bottom), (0, 255, 0), 2)

# Display the image with the faces highlighted
cv2.imshow("Face Recognition", image_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()
