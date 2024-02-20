import streamlit as st 
import os
import cv2
from utils.helper import copy_to_project_folder
from utils.auth import validate_name
st.set_page_config("Image File Converter",page_icon="🗃️")
st.header("Image Converter App made by Qadeer")
css_path = os.path.join("static", "style.css")
with open(css_path) as style:
    st.markdown(f"<style>{style.read()}</style>",unsafe_allow_html=True)



def converter(file_path, format):
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
        username=st.text_input("Enter your name",max_chars=20)
        file = st.file_uploader("Upload your file", type=['jpg', 'png', 'jpeg', 'webp'])
        if 'username' not in st.session_state:
            st.session_state.username=""
        # st.markdown("<h4>Made by Qadeer</h4>",unsafe_allow_html=True)
        submit=st.button("Submit")
        if submit:
            
            
            if (file is not None) and ((len(username)>=3) and validate_name(username)) :
                st.success(f"Welcome dear {username.title()}")
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
                        st.success(f"Dear {username} your file {file.name} is converted.")
                        st.balloons()
                    
                    with cols[1]:
                        st.markdown("### Converted Image")
                        # Display converted image
                        st.image(converted_file_path)

                    # Download button for the converted image
                    with open(converted_file_path, "rb") as file:
                        converted_image_bytes = file.read()
                    st.download_button(
                        label="Download Converted Image",
                        data=converted_image_bytes,
                        file_name=f"converted_{name}.{selected.lower()}",
                        mime="image"
                    )
                    
            else:st.warning("Complete the setup.")
if __name__ == "__main__":
    main()
