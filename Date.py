import bpy

class dateInput(bpy.types.Panel):
    bl_idname = "wm.date_input"
    bl_category = "Date"
    bl_label = "Date Range"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    #bl_context = "scene"
    
    def draw(self, context):
        self.layout.label(text="Format: Jan 25 2025")
        self.layout.prop(context.scene, "my_string1")
        self.layout.prop(context.scene, "my_string2")
        self.layout.prop(context.scene, "my_string3")

bl_info = {
    "name": "Date Input",
    "blender": (2, 80, 0),
    "category": "Object",
}

p1 = "Phase 1"
p2 = "Phase 2"
p3 = "Phase 3"

p1data = bpy.data.collections.get(p1)
p2data = bpy.data.collections.get(p2)
p3data = bpy.data.collections.get(p3)
view_layer = bpy.context.view_layer

    
def register():
    bpy.utils.register_class(dateInput)
    bpy.types.Scene.my_string1 = bpy.props.StringProperty(
        name="Date 1",
        description="A custom text field",
        default="Apr 02 2024"
    )
    bpy.types.Scene.my_string2 = bpy.props.StringProperty(
        name="Date 2",
        description="A custom text field",
        default="Current Date"
    )
    
    bpy.types.Scene.my_string3 = bpy.props.StringProperty(
        name="Date 3",
        description="A custom text field",
        default="Current Date"
    )

def unregister():
    bpy.utils.unregister_class(dateInput)
    del bpy.types.Scene.my_string1
    del bpy.types.Scene.my_string2
    del bpy.types.Scene.my_string3

if __name__ == "__main__":
    register()
    
