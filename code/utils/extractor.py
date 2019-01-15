import os
import cv2

R_PATH = '/Users/a1bs4yq5/codes/personal/summariser.ai/datasets/VSUMM/new_database'
W_PATH = '/Users/a1bs4yq5/codes/personal/summariser.ai/datasets/Frames'


def extract_frames_from_video(video_path, video_name, save_path, stride):

    frames_path = os.path.join(save_path, video_name)
    if not os.path.exists(frames_path):
        os.makedirs(frames_path)

    vidcap = cv2.VideoCapture(video_path)
    suc, image = vidcap.read()
    c = 0
    while suc:
        if c % stride == 0:
            cv2.imwrite(os.path.join(save_path, video_name, "f" + str(c) + ".jpg"), image)
        suc, image = vidcap.read()
        c += 1

def extract_frames_from_dataset(data_path, save_path):
    videos = os.listdir(data_path)
    for video in videos:
        extract_frames_from_video(os.path.join(data_path, video), video, save_path, 10)
        print(".", end="")
    print()

extract_frames_from_dataset(R_PATH, W_PATH)
