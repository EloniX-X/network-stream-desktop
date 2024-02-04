import cv2
import socket
import struct
import zlib
import numpy as np

def receive_video(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        conn, _ = s.accept()
        with conn:
            while True:
               
                size = struct.unpack(">L", conn.recv(4))[0]


                compressed_img = conn.recv(size, socket.MSG_WAITALL)


                frame_data = zlib.decompress(compressed_img)
                frame = cv2.imdecode(np.frombuffer(frame_data, dtype='uint8'), 1)

            
                cv2.imshow('Video Stream', frame)
                if cv2.waitKey(1) == ord('q'):
                    break

receive_video('0', 12345)
