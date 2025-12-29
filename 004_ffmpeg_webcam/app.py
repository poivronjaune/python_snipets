# Fucking Slow, do not add FPS display on old PC
# (Even drawing text costs CPU/GPU time)
#
# https://thingino.com/
# RTSP Mainstream (/ch0) -> High Quality video (1920x1080)
# RTSP Substream (/ch1)  -> Low Quality video (640x360) — better for slow machines
#
# Requires "C:\ffmpeg\ffmpeg.exe" to be in the system PATH
# (OpenCV uses FFmpeg to decode RTSP streams)
#

import time      # Used for FPS calculation
import sys       # Used to read command-line arguments
import os        # Not used here, but often helpful for PATH/debugging

import cv2       # OpenCV for video capture and display

# Number of frames to skip before displaying one, to reduce CPU load on PC without GPU
# python rtsp_viewer.py 5, skip 5 frames if provided as a command-line argument, default is 3
SKIP_FRAMES = int(sys.argv[1]) if len(sys.argv) > 1 else 3


def main():
    print(f"Starting RTSP Stream on Windows -> SKIP_FRAMES: {SKIP_FRAMES}")

    # RTSP URL with:
    # - username: thingino
    # - password: thingino
    # - camera IP: 192.168.1.16
    # - port: 554 (default RTSP)
    # - stream: /ch1 (low-quality substream)
    rtsp_url = "rtsp://thingino:thingino@192.168.1.16:554/ch1"

    # Open the RTSP stream using FFmpeg backend
    # FFmpeg is required for stable RTSP decoding on Windows
    cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)

    # Reduce internal buffering to avoid latency
    # Only keep 1 frame in buffer → closer to real-time
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    # Check if the stream opened successfully
    if not cap.isOpened():
        raise RuntimeError("❌ Unable to open RTSP stream")

    # Query stream resolution (may come from RTSP metadata)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"✅ RTSP stream opened at {width} x {height}")

    # Create a display window
    # AUTOSIZE → window size matches frame size
    # WINDOW_NORMAL would allow resizing but adds overhead
    cv2.namedWindow("RTSP Stream", cv2.WINDOW_AUTOSIZE)

    # Frame counters
    grab_count = 0            # Total frames grabbed
    fps_count = 0             # Frames counted for FPS calculation
    fps = 0.0                 # Current FPS value
    start_time = time.time()  # Timer start for FPS calculation
        
    while True:
        # Instead of cap.read(), we split the operation:
        # - grab(): grabs the latest frame (fast, no decode yet)
        # - retrieve(): decodes only when needed
        #
        # This reduces lag on slow PCs
        cap.grab()
        ret, frame = cap.retrieve()

        # If frame retrieval fails, stop the loop
        if not ret:
            print("⚠️ Failed to grab frame")
            break

        grab_count += 1
        fps_count += 1

        # Skip frames to reduce processing load
        # Only process/display every Nth frame
        if grab_count % SKIP_FRAMES != 0:
            continue

        # Time elapsed since last FPS update
        elapsed = time.time() - start_time

        # Update FPS once per second
        if elapsed >= 1.0:
            fps = int(fps_count / elapsed)
            fps_count = 0
            start_time = time.time()


        # frame is a NumPy array:
        # shape = (height, width, channels)
        # Example: (360, 640, 3)
        # print(frame.shape)


        # Display the frame
        cv2.imshow("RTSP Stream", frame)

        # Wait 1 ms and check if 'q' key was pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        if key == ord('f'):
            print(f"⚠️  FPS: {fps} on image (height, width, channel) {frame.shape}")
            

    # Release RTSP stream and free resources
    cap.release()
    cv2.destroyAllWindows()


# Standard Python entry point
# Ensures main() runs only when script is executed directly
if __name__ == "__main__":
    main()
