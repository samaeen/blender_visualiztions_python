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