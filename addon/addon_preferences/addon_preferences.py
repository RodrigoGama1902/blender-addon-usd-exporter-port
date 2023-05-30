import bpy

from ..utility.constants import ADDON_NAME

from .draw_preferences import draw_preferences

class USDPORT_AddonPrefs(bpy.types.AddonPreferences):    
    bl_idname = ADDON_NAME
    
    blender_binary_path : bpy.props.StringProperty(name = "Blender 3.5 path (Or higher)", subtype="FILE_PATH",default = r"C:\Program Files\Blender Foundation\Blender 3.5\blender.exe") # type:ignore

    def draw(self, context):
        draw_preferences(self, context)
        


              
            
            

            
            
 
            
            