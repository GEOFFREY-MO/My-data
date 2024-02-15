import streamlit as st
from rembg import remove
from PIL import Image
import numpy as np

# Function to remove background from the image
def remove_background(input_image):
    output_image = remove(input_image)
    return output_image

# Function to apply color as background to the image
def apply_color_as_background(input_image, color):
    # Create a solid color image
    background = Image.new("RGBA", input_image.size, color)
    
    # Convert input image to RGBA mode
    input_image_rgba = input_image.convert("RGBA")
    
    # Create a mask from the alpha channel of the input image
    mask = input_image_rgba.split()[3]
    
    # Paste the input image onto the colored background using the mask
    background.paste(input_image_rgba, (0, 0), mask)
    
    return background

# Main function
def main():
    st.title("Image Background Remover & Color Changer")

    # File uploader
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    # Select color for background
    color = st.selectbox("Select a color for background", ["Blue", "Yellow", "Pink", "Sky Blue", "Red", "Black", "Green"])

    if uploaded_file is not None:
        # Read the uploaded image file
        input_image = Image.open(uploaded_file)

        # Display the uploaded image
        st.image(input_image, caption="Uploaded Image", use_column_width=True)

        # Check if the user clicked the 'Apply Background Color' button
        if st.button('Apply Background Color'):
            colors = {
                "Blue": (0, 0, 255, 255),
                "Yellow": (255, 255, 0, 255),
                "Pink": (255, 192, 203, 255),
                "Sky Blue": (135, 206, 235, 255),
                "Red": (255, 0, 0, 255),
                "Black": (0, 0, 0, 255),
                "Green": (0, 128, 0, 255)
            }
            background_color = colors[color]
            output_image = apply_color_as_background(input_image, background_color)

            # Display the output image with the background color applied
            st.image(output_image, caption="Output Image", use_column_width=True)

if __name__ == "__main__":
    main()
