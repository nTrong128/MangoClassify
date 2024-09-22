import os
import shutil
import random

# Define paths
original_dataset_dir = './raw/'
base_dir = './dataset/'  # Directory where train, test, validation will be created

os.makedirs(base_dir, exist_ok=True)

# Create directories for train, validation, test splits
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')

# Create subdirectories for each class
for class_name in ['chin', 'non', 'song', 'thuiquac']:
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(validation_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)

    # Get list of images in the class folder
    class_dir = os.path.join(original_dataset_dir, class_name)
    images = os.listdir(class_dir)
    
    # Shuffle images
    random.shuffle(images)
    
    # Split: 80% train, 10% validation, 10% test
    train_split = int(0.8 * len(images))
    validation_split = int(0.9 * len(images))

    train_images = images[:train_split]
    validation_images = images[train_split:validation_split]
    test_images = images[validation_split:]
    
    # Copy images to corresponding directories
    for img in train_images:
        shutil.copy(os.path.join(class_dir, img), os.path.join(train_dir, class_name))
    
    for img in validation_images:
        shutil.copy(os.path.join(class_dir, img), os.path.join(validation_dir, class_name))
    
    for img in test_images:
        shutil.copy(os.path.join(class_dir, img), os.path.join(test_dir, class_name))

print("Dataset split completed!")
