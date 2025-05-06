# DICOM Viewer with ROI Analysis

##  Project Overview

This project is a simple DICOM image viewer that displays image with basic patient information. It also supports selecting a region of interest (ROI) to compute the average pixel intensity and allows exporting the image as PNG or JPG.

## Motivation

DICOM is the standard format for medical imaging. A entry level widget to open, view, and analyze DICOM images gives me a rough concept regarding preprocessing for medical professionals.

## Dataset and Data Outputs

Input:
Any standard .dcm DICOM image file

Displayed Information: 
Image in grayscale, Patient ID, Age, and Study Date

ROI Analysis:
Users can draw a rectangle (ROI) on the image
The average pixel intensity within the ROI is calculated and displayed

Output:
Save the image as .png or .jpg
Useful for sharing or embedding into reports

## Project Worksteps

-Load a DICOM file using pydicom

-Display the image in a Tkinter-based GUI with:

Patient data

Embedded matplotlib canvas for image

Use mouse to draw ROI (RectangleSelector)

Average pixel intensity of selected region

## Screenshots
![分析圖](images/截圖%202025-05-05%20下午7.20.29.png)

## How to use?

-Run each cell step by step with Jupyter notebook to understand the process.
-Upload DICOM file to find average pixel intensity of ROI 

