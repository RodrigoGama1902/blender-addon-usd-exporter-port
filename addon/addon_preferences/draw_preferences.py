import os

def draw_preferences(self, context):
    
    layout = self.layout
    
    row = layout.row()
    if not os.path.exists(self.blender_binary_path):
        row.alert = True
    
    row.prop(self, "blender_binary_path")

