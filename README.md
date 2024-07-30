Breast Cancer Classification - Mohamed Hesham
Project Overview

This project aims to develop and compare multiple machine learning models to classify breast cancer as either benign or malignant. The classification is based on various features extracted from the Wisconsin Breast Cancer Dataset. The project demonstrates the effectiveness of different models in medical diagnosis, highlighting the best-performing algorithms for this task.
Table of Contents

    Project Overview
    Dataset
    Installation
    Usage
    Models
    Results
    Contributing
    License
    Acknowledgements

Dataset

The dataset used in this project is the Wisconsin Breast Cancer Dataset. It contains features computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. These features describe characteristics of the cell nuclei present in the image.
Installation

Clone the repository:

    git clone https://github.com/yourusername/miniProject_breastCancer_MohamedHesham.git

Navigate to the project directory:

    cd miniProject_breastCancer_MohamedHesham

Install the required dependencies:

    pip install -r requirements.txt

Usage

To run the model comparisons and make predictions, execute the miniProject_breastCancer_MohamedHesham.py script:

    python miniProject_breastCancer_MohamedHesham.py

Ensure that the dataset is available in the appropriate directory or modify the script to point to the dataset's location.
Models

The project uses several machine learning algorithms to classify breast cancer cases, including:

    Support Vector Machines (SVM) with various kernels: 'linear', 'poly', 'rbf', 'sigmoid'
    Decision Tree Classifier
    Random Forest Classifier
    Gradient Boosting Classifier
    Logistic Regression
    K-Nearest Neighbors (KNN)

Each model's performance is evaluated to determine the best classifier for the dataset.
Results

The results of the model comparisons, including metrics such as accuracy, precision, recall, and confusion matrix, are presented in the script's output. These metrics provide a comprehensive evaluation of each model's effectiveness in classifying breast cancer cases.
Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your improvements. For major changes, please open an issue to discuss what you would like to change.


This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgements
    Dataset: Wisconsin Breast Cancer Dataset
    Author: Mohamed Hesham

Feel free to reach out if you have any questions or suggestions!
