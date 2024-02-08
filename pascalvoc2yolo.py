import xml.etree.ElementTree as ET
import os

def convert_pascal_to_yolo(xml_path, classes):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    width = int(root.find("size/width").text)
    height = int(root.find("size/height").text)

    yolo_lines = []
    for obj in root.findall("object"):
        class_name = obj.find("name").text
        if class_name not in classes:
            continue

        class_id = classes.index(class_name)

        xmin = float(obj.find("bndbox/xmin").text)
        ymin = float(obj.find("bndbox/ymin").text)
        xmax = float(obj.find("bndbox/xmax").text)
        ymax = float(obj.find("bndbox/ymax").text)

        x_center = (xmin + xmax) / (2.0 * width)
        y_center = (ymin + ymax) / (2.0 * height)
        box_width = (xmax - xmin) / width
        box_height = (ymax - ymin) / height

        yolo_line = f"{class_id} {x_center:.8f} {y_center:.8f} {box_width:.8f} {box_height:.8f}"
        yolo_lines.append(yolo_line)

    return os.path.splitext(os.path.basename(xml_path))[0] + ".txt", yolo_lines

def main():
    xml_folder = "/home/pc_5053/TEKNOFEST_UYZ/DATASET/labels"
    classes = ["İnsan", "Taşıt", "UAP", "UAP_İnemez", "UAİ", "UAİ_İnemez", "Motor", "Kamyon", "Otobüs", "İşMakinesi", "Tren"]
    output_folder = "/home/pc_5053/TEKNOFEST_UYZ/YOLO_OUTPUT"
    os.makedirs(output_folder, exist_ok=True)

    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith(".xml"):
            xml_path = os.path.join(xml_folder, xml_file)
            yolo_filename, yolo_lines = convert_pascal_to_yolo(xml_path, classes)

            yolo_path = os.path.join(output_folder, yolo_filename)

            with open(yolo_path, "w") as yolo_file:
                yolo_file.write("\n".join(yolo_lines))

if __name__ == "__main__":
    main()
