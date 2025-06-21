import cv2
import numpy as np
import sys
import os

def convert_to_grayscale(image):
    """Convert color image to grayscale if it's not already grayscale"""
    if len(image.shape) == 3:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image

def reduce_intensity_levels(image, levels):
    # Convert to grayscale first for proper intensity level reduction
    gray_image = convert_to_grayscale(image)
    
    # levels must be a power of 2
    if levels < 2 or (levels & (levels - 1)) != 0:
        raise ValueError("Levels must be a power of 2 and >= 2")
    
    factor = 256 // levels
    reduced = (gray_image // factor) * factor
    return reduced.astype(np.uint8)

def average_filter(image, ksize):
    return cv2.blur(image, (ksize, ksize))

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - center[0]
    M[1, 2] += (nH / 2) - center[1]
    return cv2.warpAffine(image, M, (nW, nH))

def block_average_strict(image, block_size):
    h, w = image.shape[:2]
    out = image.copy()
    for y in range(0, h - block_size + 1, block_size):
        for x in range(0, w - block_size + 1, block_size):
            block = image[y:y+block_size, x:x+block_size]
            avg = np.mean(block, axis=(0,1), dtype=np.float32)
            out[y:y+block_size, x:x+block_size] = avg.astype(np.uint8)
    return out

def parse_levels_arg():
    # Parse optional intensity levels from command line (multiple values allowed)
    if '--levels' in sys.argv:
        idx = sys.argv.index('--levels')
        levels = []
        i = idx + 1
        while i < len(sys.argv) and sys.argv[i].isdigit():
            val = int(sys.argv[i])
            if val < 2 or (val & (val - 1)) != 0:
                print(f"Error: {val} is not a power of 2 >= 2.")
                sys.exit(1)
            levels.append(val)
            i += 1
        if not levels:
            print("Error: --levels must be followed by one or more power of 2 integers >= 2.")
            sys.exit(1)
        return levels
    return [2, 4, 8, 16, 32, 64, 128, 256]

def main():
    if len(sys.argv) < 2:
        print("Usage: python image_processing_assignment.py <image_path> [--levels <power_of_2> ...]")
        sys.exit(1)
    image_path = sys.argv[1]
    if not os.path.exists(image_path):
        print(f"Image file {image_path} does not exist.")
        sys.exit(1)
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image {image_path}.")
        sys.exit(1)
    base = os.path.splitext(os.path.basename(image_path))[0]

    # 1. Intensity reduction: user-specified or default
    # Note: Images are converted to grayscale for intensity level reduction
    levels_list = parse_levels_arg()
    for levels in levels_list:
        # Grayscale version (recommended for intensity level reduction)
        reduced_gray = reduce_intensity_levels(image, levels)
        out_path_gray = f"{base}_reduced_{levels}.png"
        cv2.imwrite(out_path_gray, reduced_gray)
        print(f"Saved: {out_path_gray} (grayscale, {levels} intensity levels)")

    # 2. Average filter: 3x3, 10x10, 20x20
    for k in [3, 10, 20]:
        avg = average_filter(image, k)
        out_path = f"{base}_avg_{k}x{k}.png"
        cv2.imwrite(out_path, avg)
        print(f"Saved: {out_path}")

    # 3. Rotation: 45 and 90 degrees
    for angle in [45, 90]:
        rot = rotate_image(image, angle)
        out_path = f"{base}_rot_{angle}.png"
        cv2.imwrite(out_path, rot)
        print(f"Saved: {out_path}")

    # 4. Block average: 3x3, 5x5, 7x7 (strict, ignore incomplete blocks)
    for b in [3, 5, 7]:
        blk = block_average_strict(image, b)
        out_path = f"{base}_block_{b}x{b}.png"
        cv2.imwrite(out_path, blk)
        print(f"Saved: {out_path}")

if __name__ == "__main__":
    main() 