# EchoVision

EchoVision is a centralized repository for computer vision models and experiments, spanning from foundational convolutional baselines to state-of-the-art transformer architectures. The primary focus of this repository is image classification, feature extraction, and human action recognition.

## Flagship Model: Human Action Recognition (ViT)

The primary and most accurate model in this repository is a Vision Transformer (ViT) fine-tuned for complex human action recognition. 

* **Architecture:** google/vit-base-patch16-224-in21k
* **Task:** Multi-class Image Classification (40 Classes)
* **Dataset:** Stanford-40 Actions Dataset
* **Frameworks:** PyTorch, Hugging Face transformers, datasets

### Performance Metrics

The model was fine-tuned for 5 epochs using FP16 mixed-precision training and achieved the following results on the validation split:

| Metric | Score |
| :--- | :--- |
| **Validation Accuracy** | 88.53% |
| **Validation Loss** | 1.046 |
| **Training Loss** | 1.394 |
| **Training Runtime** | ~18 minutes (T4x2 GPU) |

Detailed metrics, including Precision, Recall, and Weighted F1-scores, are stored within the validation logs in the release folder.

## Legacy Models

This repository also serves as an archive for previous computer vision iterations and baseline convolutional models. 

* **EfficientNetB0 Baseline:** Located in the `Model_Training` directory. Achieved 78.00% accuracy.
* **MobileNet Baseline:** Early lightweight iteration. Achieved 72.00% accuracy.
* **EchoVision Keras Model (`EchoVIsion_1.h5`):** Legacy deployment format for earlier convolutional experiments.
* **Action Recognition (Initial Version):** Located in the `Action_Recognization` directory.

## Guide for Visitors: Navigating to the New Model

To find, inspect, or use the latest 88.53% accuracy Vision Transformer model, navigate to the following core files in the repository:

1. **Model Weights and Configuration:** Go to the `Latest_Release/vit_stanford_40_model/` folder. This directory contains `model.safetensors` (the trained weights via Git LFS), `config.json` (architecture parameters), and `preprocessor_config.json` (image transformation settings).
2. **Training Pipeline:** Open `Latest_Release/train.ipynb` to view the full Kaggle training execution, exploratory data analysis, and hyperparameter choices.
3. **Inference Script:** Locate `Latest_Release/predict.py`. This script is pre-configured to load the weights from the release folder and run predictions on local images.

## Repository Structure

```text
EchoVision/
├── Action_Recognization/           # Initial action recognition experiments
├── Documentaion/                   # Project documentation
├── Latest_Release/                 # Flagship ViT Stanford-40 model deployment
│   ├── vit_stanford_40_model/      # Core model artifacts (weights, configurations)
│   │   ├── config.json
│   │   ├── model.safetensors
│   │   └── preprocessor_config.json
│   ├── all_results.json            # Combined training and evaluation logs
│   ├── predict.py                  # Standalone inference script for the ViT model
│   └── train.ipynb                 # Full training notebook with EDA
├── Model_Training/                 # Older training notebooks (EfficientNetB0, MobileNet)
├── Structured_Image_Dataset/       # Dataset structuring and preprocessing scripts
├── public/                         # Public assets and legacy files
├── .gitattributes                  # Git LFS tracking configuration for large files
├── EchoVIsion_1.h5                 # Legacy Keras/TensorFlow model weights
└── README.md
