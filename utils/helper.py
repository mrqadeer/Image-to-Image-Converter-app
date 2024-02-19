import os
def copy_to_project_folder(uploaded_file):
    destination_folder = "images"
    os.makedirs(destination_folder, exist_ok=True)
    destination_path = os.path.join(destination_folder, uploaded_file.name)
    with open(destination_path, "wb") as dest_file:
        dest_file.write(uploaded_file.getvalue())