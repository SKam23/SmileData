import csv
import os
import random
import shutil

source_csv_file = "list_attr_celeba.csv"
destination_csv_file = "list_attr_celeba2000Smile.csv"
num_young_images = 5000
num_not_young_images = 5000
images_folder = "img_align_celeba/img_align_celeba/"
young_label = "1"

# Read the CSV file and get a list of image IDs and their attributes
image_data = []
with open(source_csv_file, "r") as csv_file:
    reader = csv.reader(csv_file)
    headers = next(reader)  # Save the header row
    for row in reader:
        image_data.append(row)

# Check if each selected image file exists in the images folder
def check_image_file_exists(image_id):
    image_file_path = os.path.join(images_folder, image_id)
    return os.path.exists(image_file_path)

# Split the image data into "young" and "not young" lists based on the "age_group" column
young_images = [image for image in image_data if image[headers.index("Smiling")] == young_label and check_image_file_exists(image[0])]
not_young_images = [image for image in image_data if image[headers.index("Smiling")] != young_label and check_image_file_exists(image[0])]
print(len(young_images))
print(len(not_young_images))


# Select exactly 1000 random "young" and "not young" images
selected_young_images = random.sample(young_images, min(num_young_images, len(young_images)))
selected_not_young_images = random.sample(not_young_images, min(num_not_young_images, len(not_young_images)))
while len(selected_young_images) < num_young_images:
    selected_young_images.append(random.choice(young_images))
while len(selected_not_young_images) < num_not_young_images:
    selected_not_young_images.append(random.choice(not_young_images))

# Copy the selected images to a new folder
destination_folder = "selected_images"
os.makedirs(destination_folder, exist_ok=True)
for image in selected_young_images + selected_not_young_images:
    source_path = os.path.join(images_folder, image[0])
    destination_path = os.path.join(destination_folder, image[0])
    shutil.copy2(source_path, destination_path)

# Create a new CSV file with the selected image data and headers
with open(destination_csv_file, "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(headers)
    for image in selected_young_images:
        writer.writerow(image)
    for image in selected_not_young_images:
        writer.writerow(image)

print("Done!")
