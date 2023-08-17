import cv2


input_video_path = 'main_video.mp4'
cap = cv2.VideoCapture(input_video_path)


frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


output_video_path = 'reverse1_slow_motion_output.mp4'
out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'XVID'), fps // 2, (frame_width, frame_height))

frames = []
for _ in range(frame_count):
    ret, frame = cap.read()
    if ret:
        frames.append(frame)
    else:
        break


for frame in reversed(frames):
    out.write(frame)
    out.write(frame)


cap.release()
out.release()

print(f"Reverse slow-motion video saved as '{output_video_path}'")
