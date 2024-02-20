import cv2
import sys
from tqdm import tqdm

def process_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) # Get total number of frames
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))), isColor=False)

    for _ in tqdm(range(total_frames)):
        ret, frame = cap.read()
        if not ret: 
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        out.write(edges)

    cap.release()
    out.release()

if __name__ == "__main__":
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    process_video(input_path, output_path)
