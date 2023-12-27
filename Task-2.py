import arcpy
import os

gdb_path = r"D:\Programming for GIS-3\P6_Working_with_Cursor_2\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name = "MajorAttractions"

fc_path = os.path.join(gdb_path, fc_name)

fields_list = ["NAME", "ESTAB", "ADDR", "CITYNM", "ZIP", "EMP", "ACRES"]

record = ("New Town Restaurant", 2021, "841 STREET", "SAN DIEGO", 92101, 150, 10)

i_cursor = arcpy.da.InsertCursor(fc_path, fields_list)
i_cursor.insertRow(record)

print("Process Completed")




