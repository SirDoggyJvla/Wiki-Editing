#!/usr/bin/env python3
"""
Convert PDF files to PNG images using pdf2image.
Recursively finds all PDF files in the script's directory and subdirectories.
"""

from pdf2image import convert_from_path
from PIL import Image
import os, sys, yaml

def remove_white_background(image, threshold=240):
    """
    Convert white background to transparent, preserving colored pixels.
    
    Args:
        image (PIL.Image): PIL Image object
        threshold (int): RGB threshold for white color (0-255, default: 240)
    
    Returns:
        PIL.Image: Image with transparent background
    """
    # Convert to RGBA if not already
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    
    data = image.getdata()
    new_data = []
    
    for item in data:
        r, g, b = item[0], item[1], item[2]
        # Only make transparent if all RGB values are close to each other and above threshold (pure white)
        if r > threshold and g > threshold and b > threshold and abs(r - g) < 10 and abs(r - b) < 10:
            new_data.append((255, 255, 255, 0))  # Transparent
        else:
            new_data.append(item)
    
    image.putdata(new_data)
    return image

def pdf_to_png(pdf_path, output_file=None, dpi=100):
    """
    Convert a PDF file to PNG image(s).
    
    Args:
        pdf_path (str): Path to the PDF file
        output_dir (str): Directory to save PNG files (default: same as PDF)
        dpi (int): Resolution in dots per inch (default: 150)
    
    Returns:
        list: Paths to created PNG files
    """
    if not os.path.exists(pdf_path):
        print(f"Error: PDF file '{pdf_path}' not found")
        return []
    
    if output_file is None:
        output_file = os.path.splitext(pdf_path)[0] + ".png"
    
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Converting {os.path.basename(pdf_path)} to PNG...")
    
    try:
        # Convert PDF to images
        images = convert_from_path(pdf_path, dpi=dpi)
        
        # Save images
        output_files = []
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        
        for i, image in enumerate(images):
            if len(images) == 1:
                output_file = output_file
            else:
                output_file = os.path.join(output_dir, f"{pdf_name}_page{i+1}.png")

            # Remove white background and make transparent
            image = remove_white_background(image)
            image.save(output_file, "PNG")
            output_files.append(output_file)
            print(f"  Saved: {os.path.basename(output_file)}")
        
        return output_files
    except Exception as e:
        print(f"  Error converting {pdf_path}: {e}")
        return []

def find_pdf_files(start_dir):
    """
    Recursively find all PDF files in a directory and its subdirectories.
    
    Args:
        start_dir (str): Starting directory path
    
    Returns:
        list: List of PDF file paths
    """
    pdf_files = []
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

if __name__ == "__main__":
    # Get the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    print(f"Searching for PDF files in: {script_dir}\n")

    with open(os.path.join(script_dir, 'convert.yaml'), 'r') as f:
        config = yaml.safe_load(f)
    
    # Find all PDF files
    # pdf_files = find_pdf_files(script_dir)
    pdf_files = config['items']
    
    if not pdf_files:
        print("No PDF files found.")
        sys.exit(0)
    
    print(f"Found {len(pdf_files)} PDF file(s):\n")
    
    total_output_files = []
    
    try:
        for cfg in pdf_files:
            input_file = cfg['files']['input']
            output_file = cfg['files']['output']
            dpi = cfg.get('dpi', 100)
            
            output_files = pdf_to_png(input_file, output_file=output_file, dpi=dpi)
            total_output_files.extend(output_files)
            print()
        
        print(f"Conversion complete! Created {len(total_output_files)} PNG file(s)")
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)
