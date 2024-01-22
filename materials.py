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
        for i in np.arange(len(sub_keys)):
            sub_key = sub_keys[i]
            if (isinstance(sub_key, list)):
                #this means that the sub_key is of a particular type, with sub_key[0] being the base key and sub_key[1] being an keyword for the keys
                key_handling_type = sub_key[1]
                if key_handling_type == "average_matches":
                    #this means that we want to average all values that match the base key
                    base_key = sub_key[0]
                    matching_keys = [key for key in self.properties.keys() if base_key in key]
                    matching_values = list(map(lambda a_key: key_handling(a_key,self.properties),matching_keys))
                    if not matching_values:
                        property_vector[i] = np.nan
                    else: property_vector[i] = np.mean(matching_values)
                else:
                    raise ValueError("Unrecognized key handling type {} ".format(key_handling_type))
            else:
                property_vector[i] = key_handling(sub_key,self.properties)
        return property_vector

def key_handling(sub_key,key_dict):
    if sub_key in key_dict:
        current_property = key_dict[sub_key]
        if isinstance(current_property, dict):
            if 'value' in current_property.keys():
                value_to_return = current_property['value']
            else:
                value_to_return = np.nan
        else:
            value_to_return = current_property
    else:
        value_to_return = np.nan
    return value_to_return
def get_vector_x_data(material_list, property_list=mcp.MC_PROPERTY_LIST_V1):
    '''Get x data for vector embedding'''
    x_data = np.zeros((len(material_list), len(property_list)))
    for i in np.arange(len(material_list)):
        material = material_list[i]
        x_data[i,:] = material.get_property_vector(property_list)
    return x_data

def get_vector_y_data(material_list,property_name,dtype= object):
    '''Get y data for vector embedding'''
    y_data = np.zeros(len(material_list),dtype= dtype)
    for i in np.arange(len(material_list)):
        material = material_list[i]
        y_data[i] = material.get_property(property_name)
    return y_data


