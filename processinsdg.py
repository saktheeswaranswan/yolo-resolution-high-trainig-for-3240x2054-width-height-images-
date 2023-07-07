import glob
import os
from pathlib import Path

dataset_path = '/path/to/Dataset/images'

# Percentage of images to be used for the test set
percentage_test = 10

# Create and/or truncate train.txt and test.txt
with open('train.txt', 'w') as file_train, open('test.txt', 'w') as file_test:
    # Populate train.txt and test.txt
    counter = 1
    index_test = round(100 / percentage_test)
    
    for pathAndFilename in glob.iglob(os.path.join(dataset_path, "*.jpg")):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        file_path = Path(dataset_path) / f"{title}.jpg"
        
        if counter == index_test + 1:
            file_test.write(f"{file_path}\n")
            counter = 1
        else:
            file_train.write(f"{file_path}\n")
            counter += 1

