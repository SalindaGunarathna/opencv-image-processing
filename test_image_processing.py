#!/usr/bin/env python3
"""
Test script for image processing operations
"""

import cv2
import numpy as np
import os
from image_processing_assignment import *

def test_with_input_image():
    """Test all operations with the input image"""
    
    # Check if input image exists
    input_image = "input.jpg"
    if not os.path.exists(input_image):
        print(f"Input image {input_image} not found. Please make sure it exists.")
        return
    
    print("Loading image...")
    image = cv2.imread(input_image)
    if image is None:
        print(f"Failed to load image {input_image}")
        return
    
    print(f"Image loaded successfully. Shape: {image.shape}")
    base = os.path.splitext(os.path.basename(input_image))[0]
    
    print("\n=== 1. Intensity Level Reduction ===")
    print("Note: Converting to grayscale for proper intensity level reduction")
    
    # Test with different intensity levels
    test_levels = [2, 4, 8, 16, 32, 64, 128]
    for levels in test_levels:
        # Grayscale version
        reduced_gray = reduce_intensity_levels(image, levels)
        out_path_gray = f"{base}_reduced_{levels}.png"
        cv2.imwrite(out_path_gray, reduced_gray)
        print(f"✓ Saved: {out_path_gray} ({levels} intensity levels)")
    
    print("\n=== 2. Spatial Average Filtering ===")
    for k in [3, 10, 20]:
        avg = average_filter(image, k)
        out_path = f"{base}_avg_{k}x{k}.png"
        cv2.imwrite(out_path, avg)
        print(f"✓ Saved: {out_path}")
    
    print("\n=== 3. Image Rotation ===")
    for angle in [45, 90]:
        rot = rotate_image(image, angle)
        out_path = f"{base}_rot_{angle}.png"
        cv2.imwrite(out_path, rot)
        print(f"✓ Saved: {out_path}")
    
    print("\n=== 4. Block Averaging (Spatial Resolution Reduction) ===")
    for b in [3, 5, 7]:
        blk = block_average_strict(image, b)
        out_path = f"{base}_block_{b}x{b}.png"
        cv2.imwrite(out_path, blk)
        print(f"✓ Saved: {out_path}")
    
    print("\n=== Processing Complete ===")
    print("All output images have been saved in the current directory.")
    print("\nKey points about intensity reduction:")
    print("- Grayscale version is recommended for intensity level reduction")
    print("- Intensity levels are reduced in powers of 2 (2, 4, 8, 16, 32, 64, 128)")

if __name__ == "__main__":
    test_with_input_image() 