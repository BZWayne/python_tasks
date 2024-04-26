# directory_heic = 'C:\\Users\\bauka\\Pictures\\iPhone'
# directory_jpg = 'C:\\Users\\bauka\\Pictures\\Jpg'

import os
import numpy as np
import cv2
import pillow_heif

def convert_heic_to_png(input_dir, output_dir):
    # Get list of HEIC files in input directory
    heic_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.heic') or f.lower().endswith('.heif')]
    
    # Process each HEIC file
    for filename in heic_files:
        heic_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, os.path.splitext(filename)[0] + '.png')
        
        try:
            # Open HEIC file with pillow-heif
            heif_file = pillow_heif.open_heif(heic_file_path, convert_hdr_to_8bit=False, bgr_mode=True)
            np_array = np.asarray(heif_file)
            
            # Write the image to PNG file
            cv2.imwrite(output_file_path, np_array)
            print("Conversion complete for:", filename)
        except Exception as e:
            print("Error processing:", filename)
            print(e)

# Example usage:
input_directory = 'C:\\Users\\bauka\\Pictures\\iPhone'  # Change this path accordingly
output_directory = 'C:\\Users\\bauka\\Pictures\\Jpg'  # Change this path accordingly
convert_heic_to_png(input_directory, output_directory)


