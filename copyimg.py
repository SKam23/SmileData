import csv

first_csv_file_path = "list_attr_celeba2000Smile.csv"
second_csv_file_path = "list_landmarks_align_celeba.csv"
filtered_second_csv_file_path = "list_landmarks_align_celeba2000Smile.csv"

# Read in the set of image IDs from the first CSV file
with open(first_csv_file_path, "r") as f:
    reader = csv.reader(f)
    first_image_ids = {row[0] for row in reader}

# Filter the rows from the second CSV file to only include those with image IDs that appear in the first CSV file
with open(second_csv_file_path, "r") as f:
    reader = csv.reader(f)
    filtered_rows = [row for row in reader if row[0] in first_image_ids]

# Write the filtered rows to a new CSV file
with open(filtered_second_csv_file_path, "w", newline="") as f:
    writer = csv.writer(f)
    for row in filtered_rows:
        writer.writerow(row)
