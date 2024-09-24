import cv2
import os
import glob



video_folder = ['/unripe', '/ripe'  ,'/rotten']
skip_every_other_frame = 2     


for folder in range(len(video_folder)):
    input_folder = './video' + video_folder[folder]
    output_dir = './raw' + video_folder[folder]
    print(input_folder)

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
            
            if frame_count % skip_every_other_frame == 0:
                frame_filename = os.path.join(output_dir, f'{video_name}_frame_{frame_index:05d}.jpg')
                cv2.imwrite(frame_filename, frame)
                frame_index += 1
            
            frame_count += 1
        
        cap.release()
    print(f'Extracted frames from {len(video_files)} videos, skipping every other frame, and saved them in {output_dir}.')
