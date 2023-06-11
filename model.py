import xml.etree.ElementTree as ET

src = r".\ISOMetricprofile.xml"
dst = r".\CustomISOMetricprofile.xml"

delta = 0.25

format_str = "%.4f"
tree = ET.parse(src)
root = tree.getroot()

root.find("Name").text = "3D打印螺纹"
root.find("CustomName").text = "3D打印螺纹"

tread = root.findall("ThreadSize/Designation")

for ds in tread:
    tt = ds.findall("Thread")
    for t in tt:
        if t.find("Gender").text == "external":
            ext = t
        elif t.find("Gender").text == "internal":
            int = t
    delta = 0.0
    for i in range(1,9):
        delta += 0.1
        ele = ext.__deepcopy__({})
        ele.find("Class").text = str(i / 10) + " offset"
        ele.find("MajorDia").text = format_str % (float(ext.find("MajorDia").text) - delta)
        ele.find("PitchDia").text = format_str % (float(ext.find("PitchDia").text) - delta)
        ele.find("MinorDia").text = format_str % (float(ext.find("MinorDia").text) - delta)
        ds.append(ele)

        ele = int.__deepcopy__({})
        ele.find("Class").text = str(i / 10) + " offset"
        ele.find("MajorDia").text = format_str % (float(int.find("MajorDia").text) + delta)
        ele.find("PitchDia").text = format_str % (float(int.find("PitchDia").text) + delta)
        ele.find("MinorDia").text = format_str % (float(int.find("MinorDia").text) + delta)
        ds.append(ele)

tree.write(dst,encoding="utf-8")
print("修改完成")