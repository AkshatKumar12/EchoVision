# EchoVision

EchoVision is a centralized repository for computer vision models and experiments, ranging from early baseline models to state-of-the-art transformer architectures. The primary focus of this repository is image classification, feature extraction, and human action recognition.

## Flagship Model: Human Action Recognition (ViT)

The latest and most accurate model in this repository is a Vision Transformer (ViT) fine-tuned for complex human action recognition.

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

Detailed metrics, including Precision, Recall, and Weighted F1-scores, can be found in the `Latest_release/` log files.

## Legacy Models

This repository also serves as an archive for previous computer vision iterations and baseline models. 

* **[Insert Old Model 1 Name, e.g., ResNet50 Classifier]:** Brief description of the task and dataset. Accuracy: [X]%.
* **[Insert Old Model 2 Name, e.g., Custom CNN Baseline]:** Brief description of the task and dataset. Accuracy: [X]%.

*(Note: Replace the placeholders above with the actual names and metrics of the older models currently in your repository.)*

## Repository Structure

```text
EchoVision/
├── Latest_release/         # Weights, configs, and logs for the ViT Stanford-40 model
│   ├── config.json
│   ├── model.safetensors
│   ├── preprocessor_config.json
│   ├── eval_results.json
│   └── train_results.json
├── legacy_models/          # Scripts and notebooks for older computer vision models
├── train.ipynb             # Model training and EDA notebook for the latest ViT
├── predict.py              # Standalone inference script for the ViT
├── requirements.txt        # Python dependencies
└── README.md
