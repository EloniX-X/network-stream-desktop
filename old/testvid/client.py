import cv2
import socket
import struct
from mss import mss
import numpy as np
import zlib

def send_video(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with mss() as sct:
            while True:
                
                img = np.array(sct.grab(sct.monitors[1]))

                _, buffer = cv2.imencode('.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 80])
                compressed_img = zlib.compress(buffer, level=6)

                s.sendall(struct.pack(">L", len(compressed_img)))

                s.sendall(compressed_img)

# Example usage
send_video('localhost', 12345)
