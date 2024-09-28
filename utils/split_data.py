import os
import shutil
import random

input_dir = './raw/'
out_dir = './dataset/'
class_names = ['ripe', 'unripe', 'rotten']

os.makedirs(out_dir, exist_ok=True)

train_dir = os.path.join(out_dir, 'train')
validation_dir = os.path.join(out_dir, 'validation')
test_dir = os.path.join(out_dir, 'test')

for class_name in class_names:
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(validation_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)

    class_dir = os.path.join(input_dir, class_name)
    images = os.listdir(class_dir)
    
    random.shuffle(images)
    
    # Split: 80% train, 10% validation, 10% test
    train_split = int(0.8 * len(images))
    validation_split = int(0.9 * len(images))

    train_images = images[:train_split]
    validation_images = images[train_split:validation_split]
    test_images = images[validation_split:]
    
    for img in train_images:
        shutil.copy(os.path.join(class_dir, img), os.path.join(train_dir, class_name))
    
    for img in validation_images:
        shutil.copy(os.path.join(class_dir, img), os.path.join(validation_dir, class_name))
    
    for img in test_images:
        shutil.copy(os.path.join(class_dir, img), os.path.join(test_dir, class_name))

print("Dataset split completed!")
