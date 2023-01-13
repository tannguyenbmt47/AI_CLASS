import cv2
import os
label = "10000"

cap = cv2.VideoCapture(0)

# Biến đếm, để chỉ lưu dữ liệu sau khoảng 60 frame, tránh lúc đầu chưa kịp cầm tiền lên
i=0
while(True):
    # Capture frame-by-frame
    #
    i+=1
    ret, frame = cap.read()
    if not ret:
        continue
    frame = cv2.resize(frame, dsize=None,fx=0.3,fy=0.3)

    # Hiển thị
    

    # Lưu dữ liệu
    if i>=60:
        # Tạo thư mục nếu chưa có
        if not os.path.exists('moneydata/' + str(label)):
            os.mkdir('moneydata/' + str(label))
            
        cv2.imwrite('moneydata/' + str(label) + "/" + str(i) + ".png",frame)