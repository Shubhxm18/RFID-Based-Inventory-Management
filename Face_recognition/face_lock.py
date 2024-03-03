import cv2
import face_recognition
import time

img_path1 = r"C:\Users\DIVYA\OneDrive\Desktop\Face_recognition\Shubham.jpg"
img1 = cv2.imread(img_path1)
rgb_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img_encoding1 = face_recognition.face_encodings(rgb_img1)[0]

img_path2 = r"C:\Users\DIVYA\OneDrive\Desktop\Face_recognition\Karan.jpg"
img2 = cv2.imread(img_path2)
rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

print(img_encoding1)

img_path3 = r"C:\Users\DIVYA\OneDrive\Desktop\Face_recognition\Archit.jpg"
img3 = cv2.imread(img_path3)
rgb_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
img_encoding3 = face_recognition.face_encodings(rgb_img3)[0]

img_path4 = r"C:\Users\DIVYA\OneDrive\Desktop\Face_recognition\Divya.jpg"
img4 = cv2.imread(img_path4)
rgb_img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
img_encoding4 = face_recognition.face_encodings(rgb_img4)[0]

img_path5 = r"C:\Users\DIVYA\OneDrive\Desktop\Face_recognition\Shakti.jpg"
img5 = cv2.imread(img_path5)
rgb_img5 = cv2.cvtColor(img5, cv2.COLOR_BGR2RGB)
img_encoding5 = face_recognition.face_encodings(rgb_img5)[0]

vid = cv2.VideoCapture(0)
width,height = int(vid.get(3)), int(vid.get(4))
while True:
    ret, frame = vid.read()

    font=cv2.FONT_HERSHEY_SIMPLEX

    current_frame_encoding = face_recognition.face_encodings(frame)
    if current_frame_encoding:
        result1 = face_recognition.compare_faces([img_encoding1], current_frame_encoding[0])
        result2 = face_recognition.compare_faces([img_encoding2], current_frame_encoding[0])
        result3 = face_recognition.compare_faces([img_encoding3], current_frame_encoding[0])
        result4 = face_recognition.compare_faces([img_encoding4], current_frame_encoding[0])
        result5 = face_recognition.compare_faces([img_encoding5], current_frame_encoding[0])
        
        if result1[0]:
            cv2.putText(frame,"Shubham",(20,height-12),font,2,(250,250,250),3,cv2.LINE_AA)
            print("Result for Shubham:", "Faces match" )
        elif result2[0]:
            cv2.putText(frame,"Karan",(20,height-12),font,2,(250,250,250),3,cv2.LINE_AA)
            print("Result for Karan:", "Faces match" )
        elif result3[0]:
            cv2.putText(frame,"Divya",(20,height-12),font,2,(250,250,250),3,cv2.LINE_AA)
            print("Result for Divya:", "Faces match" )
        elif result4[0]:
            cv2.putText(frame,"Archit",(20,height-12),font,2,(250,250,250),3,cv2.LINE_AA)
            print("Result for Archit:", "Faces match" )
        elif result5[0]:
            cv2.putText(frame,"Shakti",(20,height-12),font,2,(250,250,250),3,cv2.LINE_AA)
            print("Result for Shakti:", "Faces match" )
        else :
            cv2.putText(frame,"face doesn't match",(20,height-12),font,2,(250,250,250),3,cv2.LINE_AA)
            print("Faces do not match")
    # time.sleep(2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow("Video", frame)

vid.release()
cv2.destroyAllWindows()