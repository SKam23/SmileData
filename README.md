# README
This repository contains a subset of the [CelebA dataset](https://www.kaggle.com/datasets/jessicali9530/celeba-dataset), which includes 10,000 face images of various celebrities, with 5,000 images of smiling faces and 5,000 images of non-smiling faces.

# Dataset Details
The dataset is partitioned into training, validation, and testing sets according to the list_eval_partition10kSmile.csv file. The bounding box information for each image is provided in the list_bbox_celeba10kSmile.csv file. The bounding box coordinates for the upper left point are provided by x_1 and y_1 attributes. The width and height attributes represent the width and height of the bounding box, respectively.

The list_landmarks_align_celeba10kSmile.csv file provides the landmark information for each image. There are 5 landmarks: left eye, right eye, nose, left mouth, and right mouth. Finally, the list_attr_celeba10kSmile.csv file contains attribute labels for each image, with "1" representing a positive attribute and "-1" representing a negative attribute.

# Usage
The dataset can be used for various purposes such as facial expression recognition, smile detection, and attribute recognition. To use the dataset, you can download or clone the repository and load the necessary files in your code.

# Citation
If you use this dataset in your research, please consider citing the original CelebA dataset paper:

Liu, Z., Luo, P., Wang, X., & Tang, X. (2015). Deep learning face attributes in the wild. In Proceedings of the IEEE international conference on computer vision (pp. 3730-3738).

# Acknowledgements
We would like to thank the authors of the CelebA dataset for making the data available to the public and allowing us to use it for our research.
