import cv2
import os
import glob

# Define specific frame-skip intervals for each label
frame_skip = {
    'unripe': 8,
    'ripe': 5,
    'rotten': 5
}

video_folder = ['/unripe', '/ripe', '/rotten']

for folder in video_folder:
    label = folder.strip('/')  # Get label name (unripe, ripe, rotten)
    input_folder = './video_test' + folder
    output_dir = './raw_to_test1' + folder
    print(f'Processing {label} videos from {input_folder} with frame skip: {frame_skip[label]}')

    os.makedirs(output_dir, exist_ok=True)

    video_files = glob.glob(os.path.join(input_folder, '*.MOV')) # Can add more video formats here

    frame_index = 0
    
    for video_file in video_files:
        cap = cv2.VideoCapture(video_file)
    
        video_name = os.path.splitext(os.path.basename(video_file))[0]
    
        frame_count = 0
    
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Use the label-specific frame-skip interval
            if frame_count % frame_skip[label] == 0:
                frame_filename = os.path.join(output_dir, f'{video_name}_frame_{frame_index:05d}.jpg')
                cv2.imwrite(frame_filename, frame)
                frame_index += 1
            
            frame_count += 1
        
        cap.release()

    print(f'Extracted frames from {len(video_files)} videos, with frame skip {frame_skip[label]}, and saved them in {output_dir}.')
