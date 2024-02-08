# Pascal VOC to YOLO
This script converts a PascalVOC dataset to YOLO format.

## How to use?
Before running the script you need to edit a few variables.

 1. Modify the  `classes`  variable at line 35. Make sure to keep the order of classes correct.
 2. Point where your PascalVOC dataset is by changing  `xml_folder`  at line 36.
 3. Edit the  `output_folder`  at line 37 to set the output folder.
 
 Finally run the script. How long it takes to run depends on your dataset and your environment.

    python pascalvoc2yolo.py
