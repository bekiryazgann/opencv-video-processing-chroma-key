import cv2
import numpy as np
from tqdm import tqdm

# Videonun okunması
video = cv2.VideoCapture('video.mp4')

# Yeşil renk aralığının tanımlanması
lower_green = np.array([0, 100, 0])
upper_green = np.array([100, 255, 100])

# Video dosyasının özelliklerinin alınması
fps = int(video.get(cv2.CAP_PROP_FPS))
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Yeni video dosyasının yazılması
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (frame_width, frame_height))

with tqdm(total=total_frames) as pbar:
    while True:
        # Videodan bir frame okunması
        ret, frame = video.read()

        if not ret:
            break

        # Yeşil ekranın kaldırılması
        mask = cv2.inRange(frame, lower_green, upper_green)
        mask = cv2.bitwise_not(mask)
        frame = cv2.bitwise_and(frame, frame, mask=mask)

        # Yeni video dosyasına yazılması
        out.write(frame)

        pbar.update(1)  # İlerleme çubuğunu güncelle

# Kaynakların serbest bırakılması
video.release()
out.release()
cv2.destroyAllWindows()
