import api
import materials
import numpy as np

'''Gets dataset from Materials Cloud Database'''

mc2D_data = api.get_mc2D_data()
mc2D_materials = api.compounds_dict_to_materials_list(mc2D_data)

x_data = materials.get_vector_x_data(mc2D_materials)
y_data = materials.get_vector_y_data(mc2D_materials, "point_group")

np.save("v1_mc2D_x_data.npy", x_data)
np.save("v1_mc2D_y_data.npy", y_data)