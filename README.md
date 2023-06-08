# Sign Classification Project

This project aims to classify traffic signs using machine learning techniques. It utilizes a convolutional neural network (CNN) to train a model on a labeled dataset of traffic sign images and make predictions on unseen test images.

## Dataset

The dataset used in this project is the German Traffic Sign Recognition Benchmark (GTSRB) dataset. It consists of thousands of images belonging to various traffic sign categories. The dataset is divided into training and testing sets.
Link to dataset: https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign

## Prerequisites

To run this project, you need the following prerequisites:

- Python 3.x
- TensorFlow 2.x (or higher)
- Keras 2.x (or higher)
- Numpy
- Matplotlib
- OpenCV
- PIL
- Jupyter Notebook

In venv.yml you have all librares nessesery to run everything. I was usuing anaconda env

## Usage

1. Prepare the dataset:

- Download the GTSRB dataset and place it in the appropriate directory.
- Preprocess the dataset (e.g., resize images, normalize pixel values).

2. Train the model:

- Run the Jupyter Notebook `Sign_Classification.ipynb`.
- Follow the instructions in the notebook to load and preprocess the dataset, build and train the CNN model.

3. Evaluate the model:

- Evaluate the trained model on the test dataset.
- Calculate metrics such as accuracy, precision, and recall.

4. Make predictions:

- Use the trained model to make predictions on new, unseen images.
- Visualize the predictions and compare them with the ground truth labels.

U can also download trainded model if u dont want to spend time on traing and only use program in GUI version
Here is google drive link to trained model: https://drive.google.com/drive/u/1/folders/1VnDrOXS2kCb0J_M7lt3Eni6BmqxhaPTU

