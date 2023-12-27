import arcpy
import os

gdb_path = r"D:\Programming for GIS-3\P6_Working_with_Cursor_2\Practical_5_6_ProProject\05_06_Working_with_Cursors.gdb"
fc_name ="MajorAttractions"

fc_path = os.path.join(gdb_path, fc_name)

fields_list = ["NAME", "ESTAB", "HISTORIC"]

with arcpy.da.UpdateCursor(fc_path, fields_list) as u_cursor:
    for row in u_cursor:
        establishment_year = row[1]

        if establishment_year < 1970:
            row[2] = "YES"
        else:
            row[2] = "NO"

        u_cursor.updateRow(row)

print("Process Completed")








