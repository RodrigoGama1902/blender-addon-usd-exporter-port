import bpy
import os
import subprocess

from bpy_extras.io_utils import ExportHelper
from ..utility.functions import get_prefs

from pathlib import Path

class USDPORT_OT_USDExporterPort(bpy.types.Operator, ExportHelper):
    """USDZ Exporter"""
    
    bl_idname = "usdport.export_usdz"
    bl_label = "Universal Scene Description [Port] (.usd*)"
    bl_options = {'REGISTER', 'UNDO'}
    
    filename_ext = ".usd"
    selected_objects_only : bpy.props.BoolProperty(name = "Selection Only", default = False) #type: ignore

    def check_binary_version(self, blender_binary_path):

        exe_dir = os.path.dirname(blender_binary_path)
        data_version_folder = [f for f in os.listdir(exe_dir) if os.path.isdir(os.path.join(exe_dir, f)) and "." in f and len(f) == 3]

        try:
            float_version = float(data_version_folder[0])
        except IndexError:
            return False
        except ValueError:
            return False

        if float_version < 3.5:
            return False
        
        return True
  
    def execute(self, context):
        
        blender_binary_path = get_prefs().blender_binary_path
        
        if not os.path.exists(blender_binary_path):
            self.report({'ERROR'}, "Blender 3.5 .exe not found, check the add-on preferences")
            return {'CANCELLED'}
        
        if not self.check_binary_version(blender_binary_path):
            self.report({'ERROR'}, "Blender 3.5 (Or higher) not found, check the add-on preferences")
            return {'CANCELLED'}
        
        generator_path = Path(__file__).parent  / "generator" / "usd_exporter_port_generator.py"
        cmd = [
            blender_binary_path, 
            "--background", 
            bpy.data.filepath, 
            "--python", 
            str(generator_path), 
            "--", 
            "output_filepath:" + self.filepath,
            "selected_objects_only:" + str(self.selected_objects_only)]

        subprocess.run(cmd, check=True)
        
        self.report({'INFO'},"FINISHED")
        return {'FINISHED'}

