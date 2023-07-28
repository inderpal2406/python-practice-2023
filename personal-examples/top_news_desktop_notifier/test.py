import xml.etree.ElementTree as ET

filename = ".\\testdata.xml"
tree = ET.parse(filename)
root = tree.getroot()
print(root.tag)
print(root.attrib)
for child in root:
    print(child.tag)
    print(child.attrib)
    for grandchild in child:
        print(grandchild.tag)
        print(grandchild.attrib)
