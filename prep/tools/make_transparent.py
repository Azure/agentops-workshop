"""Make white backgrounds transparent in PNG images."""

from PIL import Image
import numpy as np
import os
import glob

def make_transparent(path):
    """Convert white background to transparent."""
    img = Image.open(path).convert('RGBA')
    data = np.array(img)
    # Make white/near-white pixels transparent (RGB > 245)
    white_mask = (data[:,:,0] > 245) & (data[:,:,1] > 245) & (data[:,:,2] > 245)
    data[white_mask, 3] = 0
    Image.fromarray(data).save(path)
    print(f"  OK {os.path.basename(path)}")

if __name__ == '__main__':
    print("Processing images in topic 04-agentops...")
    img_dir = os.path.dirname(os.path.abspath(__file__))
    png_files = glob.glob(os.path.join(img_dir, '*.png'))
    count = 0
    for png_file in sorted(png_files):
        try:
            make_transparent(png_file)
            count += 1
        except Exception as e:
            print(f"  ERROR {os.path.basename(png_file)}: {e}")
    print(f"Processed {count} images.")
