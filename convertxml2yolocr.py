import os
import xml.etree.ElementTree as ET

# Define the class labels (in lowercase)
classes = ['missing_hole', 'mouse_bite', 'open_circuit', 'short', 'spur', 'spurious_copper']

# Define the path to the XML files folder
xml_folder = '/home/josva/Music/pcbdefects/xmlconv'

# Create a separate folder for YOLO annotations
output_folder = 'YOLO_annotations'
os.makedirs(output_folder, exist_ok=True)

# Convert each XML file in the folder
for xml_file in os.listdir(xml_folder):
    if xml_file.endswith('.xml'):
        # Parse the XML file
        xml_path = os.path.join(xml_folder, xml_file)
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # Extract image dimensions
        width = int(root.find('size/width').text)
        height = int(root.find('size/height').text)

        # Create a text file to store the YOLO annotations
        output_file = os.path.join(output_folder, os.path.splitext(xml_file)[0] + '.txt')

        with open(output_file, 'w') as f:
            for obj in root.findall('object'):
                # Extract object details
                class_name = obj.find('name').text.lower()  # Convert to lowercase

                if class_name not in classes:
                    print(f"Warning: Class '{class_name}' not found in the list of classes.")

                # Get the class index
                class_index = classes.index(class_name) if class_name in classes else -1

                # Extract bounding box coordinates
                xmin = int(obj.find('bndbox/xmin').text)
                ymin = int(obj.find('bndbox/ymin').text)
                xmax = int(obj.find('bndbox/xmax').text)
                ymax = int(obj.find('bndbox/ymax').text)

                # Convert coordinates to YOLO format
                x = (xmin + xmax) / 2 / width
                y = (ymin + ymax) / 2 / height
                w = (xmax - xmin) / width
                h = (ymax - ymin) / height

                # Write the YOLO annotation to the file
                line = f"{class_index} {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n"
                f.write(line)

        print(f"YOLO annotation for {xml_file} has been exported successfully.")

print("All XML files have been converted to YOLO format.")
