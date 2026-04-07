import bpy
import os

class OBJECT_OT_CustomFileImport2(bpy.types.Operator):
    bl_idname = "object.custom_file_import"
    bl_label = "Select File to Import"
    bl_options = {'REGISTER', 'UNDO'}

    # This property is used by Blender's file browser
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    filter_glob: bpy.props.StringProperty(default="*.obj;*.fbx;*.stl;*.glb;*.gltf", options={'HIDDEN'})

    def execute(self, context):
        if not self.filepath:
            self.report({'ERROR'}, "No file selected.")
            return {'CANCELLED'}

        # Get file extension to determine the correct import operator
        extension = os.path.splitext(self.filepath)[1].lower()
        
        if extension == '.obj':
            bpy.ops.wm.obj_import(filepath=self.filepath)
            imported = bpy.context.selected_objects
            for obj in imported:
                print(obj.name)
            
        else:
            self.report({'ERROR'}, f"Unsupported file type: {extension}")
            return {'CANCELLED'}

        self.report({'INFO'}, f"Imported: {self.filepath}")
        return {'FINISHED'}

    def invoke(self, context, event):
        # Open the file browser
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class SimpleInputOperator4(bpy.types.Operator):
    bl_label = "Save to CSV"
    bl_idname = "wm.csvinputter"

    # Define properties to store user input
    accession: bpy.props.StringProperty(name="Accession #", default="00000")
    genus: bpy.props.StringProperty(name="Genus", default="")
    dob: bpy.props.IntProperty(name="Age", default=0, min=1, max=100)  
    dop: bpy.props.StringProperty(name="Date of Pictures (01/01/2025): ")

    def invoke(self, context, event):
        # This displays the pop-up dialog
        return context.window_manager.invoke_props_dialog(self)

    def execute(self, context):
        # This function runs when the user clicks "OK" in the dialog
        self.save_to_csv()
        
        return {'FINISHED'}

    def save_to_csv(self):
        import csv
        import os

        # Define the file path (e.g., in the same directory as the .blend file)
        blend_file_dir = os.path.dirname(bpy.data.filepath)
        if not blend_file_dir:
            self.report({'ERROR'}, "Save your Blender file first to define a path.")
            return

        self.file_name = 'jewelmine'
        file_path = os.path.join(blend_file_dir, f"{self.file_name}.csv")

        # Data to be written
        data_row = [self.accession, self.genus, self.dob, 1, self.dop]
        header = ["Accession", "Genus", "Age", "Model #", "Model Date"]

        # Open the file in append mode ('a')
        file_exists = os.path.isfile(file_path)
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write header only if the file is new
            if not file_exists:
                writer.writerow(header)

            # Write the data row
            writer.writerow(data_row)

        print(f"Data saved to {file_path}")
        self.report({'INFO'}, f"Data saved to {file_path}")





class SimpleInputOperator5(bpy.types.Operator):
    bl_label = "Upload 3D Model"
    bl_idname = "wm.modelupload"

    # Define properties to store user input
    accession: bpy.props.StringProperty(name="Accession #", default="")
        
    def invoke(self, context, event):
        # This displays the pop-up dialog
        return context.window_manager.invoke_props_dialog(self)



class CustomPanel2(bpy.types.Panel):
    bl_label = "Add info to CSV"
    bl_idname = "PT_CustomPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Add New Coral' # Name of the tab in the N-panel

    def draw(self, context):
        layout = self.layout
        # Add a button that calls the operator defined above
        layout.operator("wm.csvinputter", text="Add Coral Info")
        layout.operator("object.custom_file_import", text="Upload Model")      


# Register and Unregister functions
def register():
    bpy.utils.register_class(OBJECT_OT_CustomFileImport2)
    bpy.utils.register_class(SimpleInputOperator4)
    bpy.utils.register_class(SimpleInputOperator5)
    bpy.utils.register_class(CustomPanel2)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_CustomFileImport2)
    bpy.utils.unregister_class(SimpleInputOperator4)
    bpy.utils.unregister_class(SimpleInputOperator5)
    bpy.utils.unregister_class(CustomPanel2)

if __name__ == "__main__":
    register()
