import bpy

from .usd_exporter_port import USDPORT_OT_USDExporterPort


classes = (
    USDPORT_OT_USDExporterPort,
)

def draw_export_operator(self, context):
    self.layout.operator("usdport.export_usdz")

def register_operators():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)
        
    bpy.types.TOPBAR_MT_file_export.append(draw_export_operator)

def unregister_operators():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
        
    bpy.types.TOPBAR_MT_file_export.remove(draw_export_operator)