import streamlit as st
from rembg import remove
from PIL import Image
import io

# Function to remove background from the image
def remove_background(input_image):
    output_image = remove(input_image)
    return output_image

# Function to apply background color to the image
def apply_background_color(image, color):
    # Create a solid color image with the same size as the input image
    background = Image.new("RGB", image.size, color)
    
    # Paste the input image on top of the solid color background
    result = Image.alpha_composite(background.convert('RGBA'), image.convert('RGBA'))
    
    return result

# Main function
def main():
    st.title("Image Background Remover")

    # File uploader
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the uploaded image file
        input_image = Image.open(uploaded_file)

        # Display the uploaded image
        st.image(input_image, caption="Uploaded Image", use_column_width=True)

        # Check if the user clicked the 'Remove Background' button
        if st.button('Remove Background'):
            output_image = remove_background(input_image)

            # Display the output image with the background removed
            st.image(output_image, caption="Output Image", use_column_width=True)

            # Sidebar for selecting background color
            st.sidebar.title("Background Color")
            color = st.sidebar.selectbox("Select background color", ["Red", "Blue", "Green", "Black"])

            # Apply background color to the output image
            if color == "Red":
                background_color = (255, 0, 0)  # Red
            elif color == "Blue":
                background_color = (0, 0, 255)  # Blue
            elif color == "Green":
                background_color = (0, 255, 0)  # Green
            elif color == "Black":
                background_color = (0, 0, 0)    # Black
            
            output_with_color = apply_background_color(output_image, background_color)
            st.image(output_with_color, caption=f"Output Image with {color} background", use_column_width=True)

            # Download options
            st.sidebar.title("Download Options")
            format = st.sidebar.selectbox("Select format", ["JPEG", "PNG"])
            quality = st.sidebar.selectbox("Select quality", ["Basic", "Standard", "High"])

            # Convert output image to bytes for downloading
            img_bytes = io.BytesIO()
            try:
                if format == "JPEG":
                    output_with_color.save(img_bytes, format="JPEG", quality=get_quality(quality))
                elif format == "PNG":
                    output_with_color.save(img_bytes, format="PNG")
            except Exception as e:
                st.error(f"Error occurred while saving the image: {str(e)}")
                st.write("Please try again.")

            # Generate download button if image bytes exist
            if img_bytes.tell() > 0:
                img_bytes.seek(0)
                st.sidebar.download_button("Download Image", img_bytes.getvalue(), f"output_image.{format.lower()}")

# Function to get quality based on user selection
def get_quality(quality):
    if quality == "Basic":
        return 70
    elif quality == "Standard":
        return 80
    elif quality == "High":
        return 90

if __name__ == "__main__":
    main()
