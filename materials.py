import numpy as np
import materials_cloud_params as mcp
'''Functions to save and load materials as well as to embed them as as vectors
MC: Materials Cloud'''


class Crystal_Material():
    '''Container class for crystal materials'''
    def __init__(self, name, property_dict):
        self.name = name
        self.properties = property_dict
    def __repr__(self):
        return self.name
    def get_property(self, property_name):
        return self.properties[property_name]
    def get_property_vector(self,property_list=mcp.MC_PROPERTY_LIST_V1):
        sub_keys = property_list
        property_vector = np.zeros(len(sub_keys))
        for i in np.arange(sub_keys):
            sub_key = sub_keys[i]
            if sub_key in self.properties:
                property_vector[i] = self.properties[sub_key]
            else:
                property_vector[i] = np.nan
        return property_vector

def get_vector_x_data(material_list, property_list=mcp.MC_PROPERTY_LIST_V1):
    '''Get x data for vector embedding'''
    x_data = np.zeros((len(material_list), len(property_list)))
    for i in np.arange(len(material_list)):
        material = material_list[i]
        x_data[i,:] = material.get_property_vector(property_list)
    return x_data

def get_vector_y_data(material_list,property_name):
    '''Get y data for vector embedding'''
    y_data = np.zeros(len(material_list))
    for i in np.arange(len(material_list)):
        material = material_list[i]
        y_data[i] = material.get_property(property_name)
    return y_data


