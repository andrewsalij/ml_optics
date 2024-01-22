from mp_api.client import MPRester
import requests
import materials
'''Helper functions for interfacing with the Materials Project API (https://next-gen.materialsproject.org/api
and with the Materials Cloud databases (https://doi.org/10.1038/s41597-020-00637-5)'''


URL_MC2D = "https://www.materialscloud.org/mcloud/api/v2/discover/mc2d/compounds"

def get_mc2D_data():
    '''Get data from Materials Cloud 2D database'''
    json_mc2D = requests.get(URL_MC2D).json()
    data= json_mc2D["data"]
    compounds_dict = data["compounds"]
    return compounds_dict

def compounds_dict_to_materials_list(compounds_dict):
    '''Converts a dict of compounds to a list of materials'''
    compound_keys = list(compounds_dict.keys())
    materials_list = []
    for compound_key in compound_keys:
        cur_compound =  compounds_dict[compound_key]
        cur_name = cur_compound[0]['formula']
        material = materials.Crystal_Material(cur_name, cur_compound[0])
        materials_list.append(material)
    return materials_list



