# Image Processing Assignment

This repository contains Python programs to perform various image processing operations.

## Operations Implemented

- Intensity levels refer to the brightness/darkness of pixels
- Color images have 3 channels (RGB), each with 256 levels
- Grayscale images have only 1 channel with 256 intensity levels
- Reducing intensity levels makes more sense on grayscale images where we're dealing with actual brightness levels
- The program automatically converts images to grayscale for intensity level reduction

**Usage**:
```bash
python image_processing_assignment.py input.jpg --levels 2 4 8 16 32 64 128
```

**Output**:
- `input_reduced_2.png` - Grayscale with 2 intensity levels (black/white)
- `input_reduced_4.png` - Grayscale with 4 intensity levels
- `input_reduced_8.png` - Grayscale with 8 intensity levels
- etc.

### 2. Spatial Average Filtering
Performs 3x3, 10x10, and 20x20 neighborhood averaging.

**Output**:
- `input_avg_3x3.png`
- `input_avg_10x10.png`
- `input_avg_20x20.png`

### 3. Image Rotation
Rotates the image by 45° and 90°.

**Output**:
- `input_rot_45.png`
- `input_rot_90.png`

### 4. Block Averaging (Spatial Resolution Reduction)
Replaces each 3×3, 5×5, and 7×7 block with the average of its pixels.

**Output**:
- `input_block_3x3.png`
- `input_block_5x5.png`
- `input_block_7x7.png`

## Quick Test

Run the test script to process your input image with all operations:

```bash
python test_image_processing.py
```

## Requirements

```bash
pip install opencv-python numpy
```

## Command Line Usage

```bash
# Process with default intensity levels (2, 4, 8, 16, 32, 64, 128, 256)
python image_processing_assignment.py input.jpg

# Process with specific intensity levels
python image_processing_assignment.py input.jpg --levels 2 4 8 16

# Process with only 2 intensity levels (black/white)
python image_processing_assignment.py input.jpg --levels 2
```

## Key Points About Intensity Reduction

1. **Grayscale Conversion**: The program automatically converts color images to grayscale for intensity level reduction
2. **Power of 2**: Intensity levels must be powers of 2 (2, 4, 8, 16, 32, 64, 128, 256)
3. **2 Levels**: Using 2 intensity levels creates a pure black and white image
4. **Higher Levels**: More levels preserve more detail but reduce the "posterization" effect

## Example Results

- **2 levels**: Pure black and white (binary image)
- **4 levels**: 4 shades of gray
- **8 levels**: 8 shades of gray
- **16 levels**: 16 shades of gray
- etc. 