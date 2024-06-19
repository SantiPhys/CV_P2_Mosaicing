import os

def rename_files_in_folder(folder_path, img_name):
    # Check if folder exists
    if not os.path.isdir(folder_path):
        print(f"Folder {folder_path} does not exist.")
        return

    for count, filename in enumerate(os.listdir(folder_path)):
        src = os.path.join(folder_path, filename)

        # Check if file exists
        if not os.path.isfile(src):
            print(f"File {src} does not exist.")
            continue

        dst = img_name + str(count).zfill(2) + ".jpg"
        dst = os.path.join(folder_path, dst)

        # rename all the files
        os.rename(src, dst)

# specify your path
path = "images/beach/"
img_name = "beach"
print(f"Current working directory: {os.getcwd()}")
rename_files_in_folder(path, img_name)