import cv2
import os

def save_specific_frame(video_path, frame_number):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)

    if not video_capture.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    # Set the video capture object to the desired frame number
    video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    # Read the specific frame
    ret, frame = video_capture.read()

    if not ret:
        print(f"Error: Could not read frame {frame_number} from the video")
        return

    # Construct the output path for the specific frame
    output_dir = os.path.dirname(video_path)  # Same directory as the video file
    output_file = os.path.join(output_dir, f'frame_{frame_number}.jpg')

    # Save the frame
    cv2.imwrite(output_file, frame)
    print(f"Frame {frame_number} saved as {output_file}")

    # Release the video capture object
    video_capture.release()

if __name__ == "__main__":
    # Path to your video file (modify this as needed)
    video_path = 'comboio.mp4'
    # Frame number you want to capture (modify this as needed)
    frame_number = 280
    save_specific_frame(video_path, frame_number)

