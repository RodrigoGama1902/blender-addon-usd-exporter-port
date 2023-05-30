

def register_addon():
    
    from ..operator import register_operators
    register_operators()
    
    from ..addon_preferences import register_addon_preferences
    register_addon_preferences()
    
def unregister_addon():

    from ..operator import unregister_operators
    unregister_operators()
        
    from ..addon_preferences import unregister_addon_preferences
    unregister_addon_preferences()


