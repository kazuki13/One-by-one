import cv2
import os

def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0
    i = 0
    while True:
        ret, frame = cap.read()
        if i%60==0:

            if ret:
                cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
                n += 1
            else:
                return
        i+=1

save_all_frames('/Users/murayama/Desktop/石垣島/Day3/IMG_2491.MOV', 'data/IMG_2491', 'sample_video_img')

save_all_frames('/Users/murayama/Desktop/石垣島/Day3/IMG_2492.MOV', 'data/IMG_2492', 'sample_video_img')

save_all_frames('/Users/murayama/Desktop/石垣島/Day3/IMG_2494.MOV', 'data/IMG_2494', 'sample_video_img')
save_all_frames('/Users/murayama/Desktop/石垣島/Day3/IMG_2495.MOV', 'data/IMG_2495', 'sample_video_img')


