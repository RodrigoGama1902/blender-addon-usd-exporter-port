import bpy
import sys

output_filepath : str = ""
selected_objects_only : bool = False

for agr in sys.argv:
    if agr.startswith("output_filepath:"):
        output_filepath = agr[16:]
    if agr.startswith("selected_objects_only:"):
        selected_objects_only = agr[22:]

print("output_filepath: " + output_filepath)
print("selected_objects_only: " + str(selected_objects_only))

bpy.ops.wm.usd_export(
    filepath = output_filepath, 
    selected_objects_only = selected_objects_only
    )
