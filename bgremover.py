import streamlit as st
from rembg import remove
from PIL import Image
import io
from streamlit import SessionState

# Function to remove background and apply color
def remove_and_apply_color(input_image, color):
    # Your logic to remove background and apply color goes here
    pass

def main():
    st.title('Background Remover with Color Change')
    
    # Initialize session state
    if 'color' not in st.session_state:
        st.session_state.color = 'red'  # Default color

    # Upload image
    uploaded_image = st.file_uploader("Upload Image", type=['jpg', 'png'])
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        # Button to remove background and apply color
        if st.button("Remove Background and Apply Color"):
            # Call function to remove background and apply color
            result_image = remove_and_apply_color(uploaded_image, st.session_state.color)
            st.image(result_image, caption="Processed Image", use_column_width=True)

    # Select background color
    st.sidebar.subheader("Select Background Color")
    st.session_state.color = st.sidebar.radio("Color", options=['red', 'blue', 'green'])

if __name__ == "__main__":
    main()
