## FOLDER STRUCTURE:

![alt text](./img_source/image.png)

## Run cell by cell one of these model : [model](./model/)

# You should create venv for your project and install the following package:

- scikit-learn
- tensorflow
- keras
- matplotlib
- seaborn
- pandas
- numpy

or using this command:

```bash
pip install scikit-learn tensorflow keras matplotlib seaborn pandas numpy
```

`There are some others package you have to install while runnning the experiment. You should read the log or error from your terminal or jupyter notebook output to checking for missing packages.`

## datasets: [Link to train set](https://drive.google.com/file/d/1vsbHGtdePzGWAtO-A06kCmxhszG8TPT2/view), [Link to test set](https://drive.google.com/file/d/178lJFzFRqS9olO1sE0bLTFBI_h89DnuW/view)

Video is a raw folder which contain unprocessed video. You should run [extractImgFromVideo](./utils/extractImgFromVideo.py) to extract image from raw video. You can change frame skip as you wish.

After extract images from videos. You should have raw folder contain images from every class in this project. You should use [split_data](./utils/split_data.py) to split the dataset into train, test and validation set.
After that you can run the experiment.
`Some of the function may not work correctly that force you have to create folder yourself, if you're encouted any error when running those two utils file, you should create folder by yourself.`
