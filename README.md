# Image File Converter App

### Live Demo: [Image Converter App](https://image-to-image-coverter-app.streamlit.app/)

## Overview

This Image File Converter App allows you to easily convert images from one format to another. It supports popular image formats such as JPG, PNG, JPEG, WEBP, TIF, and GIF. The app is built using Python, Streamlit, and OpenCV, providing a user-friendly interface for seamless image conversion.

## Features

- Upload image files in various formats (JPG, PNG, JPEG, WEBP)
- Convert images to different formats: JPG, JPEG, PNG, WEBP, TIF, GIF
- Preview the original and converted image side by side
- Download the converted image with a single click

## Requirements

- Python 3.9+
- Streamlit
- OpenCV

## Installation
### Clone the repository

```bash
git clone https://github.com/mrqadeer/Image-to-Image-Converter-app.git
cd Image-to-Image-Converter-app
```
### Using Conda

1. Create a new conda environment:

   ```bash
   conda create --name image_converter python=3.9
   conda activate image_converter
   ```
### Using pip
```bash
python -m venv image_converter_env
image_converter_env\Scripts\activate
```
For Linux
```bash
source image_converter_env/bin/activate 
``` 

2. Install the required dependencies:

```python
pip install -r requirements.txt
```
#### Run the Streamlit app:
```bash
streamlit run app.py
```
1. Open the app in your browser by visiting http://localhost:8501.

2. Upload an image in JPG, PNG, JPEG, or WEBP format.

3. Select the target format (JPG, JPEG, PNG, WEBP, TIF, or GIF) from the dropdown menu.

4. Click the Convert button to convert the image.

5. Preview the original and converted images side by side, and click the Download Converted Image button to download the output.
### File Structure
image-converter-app/
│
├── static/
│   └── style.css               # Custom CSS for styling
│
├── images/                     # Folder where uploaded and converted images are stored
│
├── utils/
│   └── helper.py               # Helper functions like copy_to_project_folder
│
├── app.py                      # Main Streamlit app
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
└── .gitignore                  # Git ignore file
### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.