import streamlit as st 
import os
import cv2
from utils.helper import copy_to_project_folder

st.set_page_config("Image File Converter",page_icon="🗃️")
st.header("Image Converter App made by Qadeer")
css_path = os.path.join("static", "style.css")
with open(css_path) as style:
    st.markdown(f"<style>{style.read()}</style>",unsafe_allow_html=True)



def converter(file_path, format):
    """
    Converts an image file to a specified format.

    Parameters
    ----------
    file_path : str
        Path to the image file to be converted.
    format : str
        The format to which the image should be converted.

    Returns
    -------
    str
        The path to the converted image file.

    Raises
    ------
    Exception
        If an error occurs during the conversion process.
    """
    name = file_path.split(".")[0]
    image = cv2.imread(file_path)
    try:
        cv2.imwrite(f'{name}.{format}', image)
    except Exception as e:
        st.error("Failed to convert!")
        st.stop()
    else:
        
        return f'{name}.{format}'

def main():
    with st.sidebar:
        file = st.file_uploader("Upload your file", type=['jpg', 'png', 'jpeg', 'webp'])

        # st.markdown("<h4>Made by Qadeer</h4>",unsafe_allow_html=True)

            
    if file is not None :

        formats = ["JPG", "JPEG", "PNG","WEBP","TIF","GIF"]
        selected = st.selectbox("Select format", formats)
        
        name=file.name.split(".")[0]
        cols=st.columns(2)
        with cols[0]:
            st.markdown("### Orignal Image")
            st.image(file)
        convert = st.button("Convert")
        if convert:
            
            copy_to_project_folder(file)
            file_path = f"images/{file.name}"
            with st.spinner("Converting"):
                converted_file_path = converter(file_path, selected)
                st.success("Image converted successfully!")
                    
            with cols[1]:
                st.markdown("### Converted Image")
                    # Display converted image
                st.image(converted_file_path)
        else:
            st.warning("Please convert the image!")
            st.stop()
        # Download button for the converted image
        with open(converted_file_path, "rb") as file:
            converted_image_bytes = file.read()
            st.download_button(
            label="Download Converted Image",
                    data=converted_image_bytes,
                    file_name=f"converted_{name}.{selected.lower()}",
                    mime="image"
                )
                    
    else:st.warning("Complete the setup to proceed!")
if __name__ == "__main__":
    main()
