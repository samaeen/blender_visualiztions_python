import bpy

positions=(0,3,2),(4,1,6),(3,5,8),(6,8,2),(1,8,1)
start_pos=(0,0,0)

ob=bpy.data.objects["Sphere"]

frame_num=0

for position in positions:
    bpy.context.scene.frame_set(frame_num)
    ob.location=position
    ob.keyframe_insert(data_path="loaction",index=-1)
    frame_num+=20



bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "mirror":False},
								 TRANSFORM_OT_translate={"value":(3.51466e-18, 1.07635, 0.0158286), 
								 "orient_type":'GLOBAL', 
								 "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), 
								 "orient_matrix_type":'GLOBAL', 
								 "constraint_axis":(False, False, False), 
								 "mirror":False, "use_proportional_edit":False, 
								 "proportional_edit_falloff":'SMOOTH', 
								 "proportional_size":1, 
								 "use_proportional_connected":False, 
								 "use_proportional_projected":False, 
								 "snap":False, 
								 "snap_target":'CLOSEST', 
								 "snap_point":(0, 0, 0), 
								 "snap_align":False, 
								 "snap_normal":(0, 0, 0), 
								 "gpencil_strokes":False, 
								 "cursor_transform":False, 
								 "texture_space":False, 
								 "remove_on_cancel":False, 
								 "release_confirm":False, 
								 "use_accurate":False})


