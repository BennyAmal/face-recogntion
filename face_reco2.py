import face_recognition

# Load the images
binu_image = face_recognition. load_image_file ("binu.jpg")
amal_image = face_recognition. load_image_file ("amal.jpg")
anu_image = face_recognition. load_image_file ("anu.jpg")
joseph_image = face_recognition. load_image_file ("joseph.jpg")
varun_image = face_recognition. load_image_file ("varun.jpg")
unknown_image = face_recognition. load_image_file ("try5.jpg")

# creating the encodings for each faces
try:
     binu_face_encoding = face_recognition.face_encodings(binu_image)[0]
     amal_face_encoding = face_recognition.face_encodings(amal_image)[0]
     anu_face_encoding = face_recognition.face_encodings(anu_image)[0]
     joseph_face_encoding = face_recognition.face_encodings(joseph_image)[0]
     varun_face_encoding = face_recognition.face_encodings(varun_image)[0]
     unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("no faces found in the image")
    quit()

known_faces = [
    binu_face_encoding,
    amal_face_encoding,
    anu_face_encoding,
    joseph_face_encoding,
    varun_face_encoding
]

# results is an array of True/False 
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

names = ["binu", "amal", "anuraj","joseph","varun"]

print("the face might be of ")

for i in range(len(names)):
    if results[i]:
        print(names[i])
        break
else:
    print("i have not seen this face")
# printing the name from array where result array is having a true value
