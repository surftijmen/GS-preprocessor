# GS-preprocessor

## Overview

This repository contains the code and resources developed for my Bachelor's thesis on deblurring and preprocessing images for 3D Gaussian Splatting. The project focuses on applying deblurring and denoising techniques to prepare images for 3D rendering and analysis.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

In the context of my Bachelor's thesis, I have developed a set of tools and scripts to preprocess images for 3D Gaussian Splatting. This includes methods for deblurring, denoising, and applying various image filters to enhance the quality of the 3D rendered output.

## Features

- **Deblurring**: Techniques to reduce blur in images caused by motion or defocusing.
- **Denoising**: Methods to remove noise from images, improving clarity and detail.
- **3D Gaussian Splatting**: Preprocessing images to be used in 3D Gaussian splatting techniques for rendering.

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/surftijmen/GS-preprocessor.git
   cd GS-preprocessor

2. **Create a virtual environment**:
   ```sh
   python -m venv venv

3. **Activate the virtual environment**:
  - On Windows:
    `sh
    venv\Scripts\activate`
    
  - On macOS/Linux:
  `sh
  source venv/bin/activate`

4. **Install the required dependencies**
`sh
pip install -r requirements.txt`

## Usage

1. **Preprocess Images**:
   Use the provided scripts to preprocess your images. You can adjust parameters such as blur intensity and noise level as needed.

2. **Run the scripts**:
   `sh python main.py`

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.
   

