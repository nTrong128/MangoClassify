import cv2
import os
import glob

# Path to the folder containing the video files
video_folder = './video/non'

# Directory to save all frames
output_dir = './raw/non'
os.makedirs(output_dir, exist_ok=True)

# Define the frame rate skip (skip every other frame to get half the FPS, i.e., from 30 FPS to 15 FPS)
skip_every_other_frame = 2  # Skip one frame, save the next

# Get a list of all video files in the folder
video_files = glob.glob(os.path.join(video_folder, '*.MOV'))  # Add more extensions if needed

frame_index = 0  # To keep track of all frames across videos

# Loop through each video file
for video_file in video_files:
    # Open the video file
    cap = cv2.VideoCapture(video_file)
    
    video_name = os.path.splitext(os.path.basename(video_file))[0]
    
    frame_count = 0
    
    # Process each frame in the video
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # If no more frames, exit the loop
        
        # Save only every other frame (i.e., skip one frame, capture the next)
        if frame_count % skip_every_other_frame == 0:
            # Save frames in one folder, using an overall frame index
            frame_filename = os.path.join(output_dir, f'{video_name}_frame_{frame_index:05d}.jpg')
            cv2.imwrite(frame_filename, frame)
            frame_index += 1
        
        frame_count += 1
    
    # Release the video capture object
    cap.release()

print(f'Extracted frames from {len(video_files)} videos, skipping every other frame, and saved them in {output_dir}.')
