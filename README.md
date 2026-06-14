# Invisible Cloak using OpenCV

A Computer Vision project that creates an invisibility effect using OpenCV and Python.

## Technologies Used

* Python
* OpenCV
* NumPy

## Features

* Real-time webcam processing
* Background capture
* HSV color detection
* Image masking
* Invisible cloak effect

## How It Works

1. Capture the background.
2. Detect the red cloth using HSV color segmentation.
3. Create a mask for the red cloth.
4. Replace the detected area with the saved background.
5. Display the final invisibility effect.

## Installation

Install the required libraries:

pip install -r requirements.txt

Run the project:

python invisible_cloak.py

## Project Structure

Invisible-Cloak-Computer-Vision

├── invisible_cloak.py

├── README.md

├── requirements.txt

└── demo.mp4

## Author

Kavin Prasanna S S
