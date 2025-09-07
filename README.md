# EchoVision
## Project Description

EchoVision is an AI-based human activity recognition system designed to assist visually impaired users. By analyzing images captured from cameras or videos, the system can detect human actions and convert the outputs into audio alerts, enabling users to “see” the environment through sound.

This project is particularly useful for:

Visually impaired individuals needing real-time environment awareness

Developers exploring computer vision, deep learning, and accessibility applications

Researchers building AI-powered assistive technologies

## Key Features

Human Activity Recognition
Uses a trained CNN model (EfficientNetB0) to classify activities like walking, eating, using a phone, and more.

Audio Feedback
Converts recognized actions into speech output, providing real-time auditory information.

Frame Extraction & Preprocessing
Processes video frames or images to accurately detect activities.

Extensible
New activity classes can be added, and the model can be retrained to improve recognition accuracy.

Lightweight & Fast
Optimized for quick predictions on single images, making it suitable for real-time usage.

## Tech Stack

Python 3.10+

TensorFlow / Keras (EfficientNetB0 model)

OpenCV (image/video processing)

Pyttsx3 / gTTS (text-to-speech audio feedback)

NumPy / Pandas (data handling)

## How It Works

Load the trained EfficientNetB0 model (efficientnetb0_har_model.h5).

Feed an image or video frame into the system.

The CNN model predicts the human activity.

The predicted activity is converted to audio output for the user.

Users receive real-time feedback about the surroundings.
