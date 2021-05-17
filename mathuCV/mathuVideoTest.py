import cv2
import socket

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 65000))

    cap = cv2.VideoCapture(0)
    def grayscale():
        while cap.isOpened():
            ret, frame = cap.read()
            video = cv2.flip(frame, 1)
            video_grayscale = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
            cv2.imshow("gray", video_grayscale)
            print("succeeded")
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    def normal():
        while cap.isOpened():
            ret, frame = cap.read()
            video = cv2.flip(frame, 1)
            cv2.imshow("video", video)
            msg = s.recv(10)
            if msg.decode("utf-8") == "succeeded":
                grayscale()
                break
            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    normal()