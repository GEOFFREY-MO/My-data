import streamlit as st
from rembg import remove
from PIL import Image

# Function to remove background from the image
def remove_background(input_image):
    output_image = remove(input_image)
    return output_image

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

if __name__ == "__main__":
    main()
