import os

def reorder_images_in_folder(folder_path, img_name):
    # Check if folder exists
    if not os.path.isdir(folder_path):
        print(f"Folder {folder_path} does not exist.")
        return

    # Get the sorted list of filenames
    filenames = sorted(os.listdir(folder_path))

    for count, filename in enumerate(filenames):
        src = os.path.join(folder_path, filename)

        # Check if file exists
        if not os.path.isfile(src):
            print(f"File {src} does not exist.")
            continue

        # Assign new names in reverse order
        dst = img_name + str(len(filenames) - count - 1).zfill(2) + ".jpg"
        dst = os.path.join(folder_path, dst)

        # rename all the files
        os.rename(src, dst)

# specify your path
path = "images/beach/"
img_name = "beach_ordered"
print(f"Current working directory: {os.getcwd()}")
reorder_images_in_folder(path, img_name)