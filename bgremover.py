import streamlit as st
from rembg import remove
from PIL import Image

def remove_background(input_image):
    # Remove the background from the input image
    output_image = remove(input_image)
    return output_image

def main():
    st.title('DAVETECH-BG-REMOVER')

    # Add sidebar with service options
    service = st.sidebar.selectbox("Select Service", ["HOME", "SELECT COLOR", "DOWNLOAD"])

    if service == "HOME":
        st.markdown("Welcome to DAVETECH-BG-REMOVER!")
    elif service == "SELECT COLOR":
        st.markdown("This service is under construction. Please check back later!")
    elif service == "DOWNLOAD":
        st.markdown("This service is under construction. Please check back later!")
    
    st.markdown('Upload an image and remove its background!')

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the uploaded image file
        input_image = Image.open(uploaded_file)

        # Display the uploaded image
        st.image(input_image, caption="Uploaded Image", use_column_width=True)

        # Check if the user clicked the 'Remove Background' button
        if st.button('Remove Background'):
            # Call the function to remove the background
            output_image = remove_background(input_image)

            # Display the output image with the background removed
            st.image(output_image, caption="Output Image", use_column_width=True)
            st.success('Background removed successfully!')

if __name__ == "__main__":
    main()
