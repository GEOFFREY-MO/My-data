import streamlit as st
from rembg import remove
from PIL import Image
import os

# Dictionary mapping color names to their RGB values
COLORS = {
    "Blue": (0, 0, 255),
    "Black": (0, 0, 0),
    "Green": (0, 128, 0),
    "Pink": (255, 192, 203),
    "White": (255, 255, 255),
    "Yellow": (255, 255, 0),
    "Brown": (165, 42, 42),
    "Sky Blue": (135, 206, 235),
    "Red": (255, 0, 0)
}

# Dictionary mapping file extensions to image formats
IMAGE_FORMATS = {
    "JPEG": "jpeg",
    "PNG": "png",
    "BMP": "bmp",
    "TIFF": "tiff"
}

def apply_color_to_image(input_image, color):
    # Apply the selected color to the input image
    output_image = input_image.copy()
    width, height = output_image.size
    for x in range(width):
        for y in range(height):
            pixel = list(output_image.getpixel((x, y)))
            alpha = pixel[3]  # Alpha channel value
            if alpha > 0:
                pixel[:3] = color  # Replace RGB values
            output_image.putpixel((x, y), tuple(pixel))
    return output_image

def main():
    st.sidebar.title('DAVETECH-BG-REMOVER')
    service = st.sidebar.radio("Select Service", ["HOME", "SELECT COLOUR", "DOWNLOAD"])

    if service == "HOME":
        st.title('Welcome to DAVETECH-BG-REMOVER')
        st.write("This is the home page of the DAVETECH-BG-REMOVER web app. Select different services from the sidebar.")

    elif service == "SELECT COLOUR":
        st.title('Select Colour Service')
        st.write("Choose a color from the sidebar to apply to the image.")

        selected_color = st.sidebar.selectbox("Choose a color", list(COLORS.keys()))

        input_image = Image.open("your_image.jpg")

        st.image(input_image, caption="Original Image", use_column_width=True)

        if st.button("Apply Color"):
            color_rgb = COLORS[selected_color]
            output_image = apply_color_to_image(input_image, color_rgb)
            st.image(output_image, caption="Image with Selected Color", use_column_width=True)

    elif service == "DOWNLOAD":
        st.sidebar.subheader("Download Image")

        input_image = Image.open("your_image.jpg")

        st.image(input_image, caption="Original Image", use_column_width=True)

        if st.button("Remove Background"):
            output_image = remove(input_image)
            st.image(output_image, caption="Background Removed", use_column_width=True)

        if st.button("Download Processed Image"):
            output_path = "processed_image.png"
            output_image.save(output_path)
            st.success("Image processed and saved successfully!")
            st.markdown(f"### [Download Processed Image]({output_path})")

if __name__ == "__main__":
    main()
