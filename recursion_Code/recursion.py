import bpy

length=2

def createGroup(length):
    if length<26:
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, -length)})
        bpy.ops.transform.translate(value=(length/2,0,0))
        bpy.ops.transform.translate(value=(0,length/2,0))
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(-length, 0, 0)})
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, -length, 0)})
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(length, 0, 0)})
        
        bpy.ops.object.select_by_type(type='MESH')
        bpy.ops.object.join()
        
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action="TOGGLE")
        bpy.ops.mesh.remove_doubles()
        bpy.ops.mesh.select_all(action="TOGGLE")
        bpy.ops.object.editmode_toggle()
        
        length=length*2
        createGroup(length)
    return length
    
createGroup(length)
