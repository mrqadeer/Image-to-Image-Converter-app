import os
def copy_to_project_folder(uploaded_file):
    """
    Copies an uploaded file to a folder named "images" in the current project.
    
    Parameters
    ----------
    uploaded_file : UploadedFile
        The file to be copied.
    
    """
    
    destination_folder = "images"
    os.makedirs(destination_folder, exist_ok=True)
    destination_path = os.path.join(destination_folder, uploaded_file.name)
    with open(destination_path, "wb") as dest_file:
        dest_file.write(uploaded_file.getvalue())