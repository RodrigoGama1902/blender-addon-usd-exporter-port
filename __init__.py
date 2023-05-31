bl_info = {
    "name": "USD Exporter Port",
    "description": "A simple USD exporter for Blender 3.4 and below",
    "author": "Rodrigo Gama",
    "version": (0, 1, 1),
    "blender": (3, 4, 0),
    "location": "View3D",
    "category": "3D View"
}


def register():
    from .addon.register import register_addon
    register_addon()


def unregister():
    from .addon.register import unregister_addon
    unregister_addon()