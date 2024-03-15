import cv2


def get_video_quality(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    duration = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) / frame_rate
    bitrate = int(cap.get(cv2.CAP_PROP_FORMAT))

    print("Video Resolution:", f"{width}x{height}")
    print("Frame Rate:", frame_rate, "fps")
    print("Duration:", duration, "seconds")
    print("Bitrate:", bitrate, "bps")

    cap.release()
