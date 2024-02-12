import streamlit as st
from rembg import remove
from PIL import Image
import os

# Function to apply color to the image
def apply_color_to_image(input_image, color):
    output_image = input_image.copy()
    width, height = output_image.size
    for x in range(width):
        for y in range(height):
            pixel = list(output_image.getpixel((x, y)))
            alpha = pixel[3] if len(pixel) > 3 else 255
            if alpha > 0:
                pixel[:3] = color
            output_image.putpixel((x, y), tuple(pixel))
    return output_image

# Function to download the image
def download_image(image, format):
    img_path = "processed_image." + format.lower()
    image.save(img_path)
    return img_path

# Main function
def main():
    st.title("Image Color Changer")

    # File uploader
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    # Select color
    color = st.selectbox("Select a color", ["Blue", "Yellow", "Pink", "Sky Blue", "Red", "Black", "Green"])

    # Select image quality
    quality = st.selectbox("Select image quality", ["Low", "Standard", "High"])

    if uploaded_file is not None:
        # Read the uploaded image file
        input_image = Image.open(uploaded_file)

        # Display the uploaded image
        st.image(input_image, caption="Uploaded Image", use_column_width=True)

        # Check if the user clicked the 'Apply Color' button
        if st.button('Apply Color'):
            colors = {
                "Blue": (0, 0, 255),
                "Yellow": (255, 255, 0),
                "Pink": (255, 192, 203),
                "Sky Blue": (135, 206, 235),
                "Red": (255, 0, 0),
                "Black": (0, 0, 0),
                "Green": (0, 128, 0)
            }
            color_rgb = colors[color]
            output_image = apply_color_to_image(input_image, color_rgb)

            # Display the output image with the color changed
            st.image(output_image, caption="Output Image", use_column_width=True)
            
            # Download options
            if st.button("Download Image"):
                img_format = st.selectbox("Select image format", ["JPEG", "PNG", "BMP", "TIFF"])
                
                # Set image quality based on user selection
                if quality == "Low":
                    output_image.save("temp_image.png", quality=30)
                elif quality == "Standard":
                    output_image.save("temp_image.png", quality=70)
                elif quality == "High":
                    output_image.save("temp_image.png", quality=100)

                # Download the image
                img_path = download_image(output_image, img_format)
                st.markdown(f"### [Download Processed Image]({img_path})")

if __name__ == "__main__":
    main()
