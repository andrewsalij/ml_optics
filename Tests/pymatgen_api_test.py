from mp_api.client import MPRester

'''
Test to see how pymatgen API works. See https://docs.materialsproject.org/downloading-data/using-the-api/querying-data
'''

API_KEY = "jHAkWM1tUZUKWNlZddRizz44AJYrUrw7"
mpr = MPRester(API_KEY)

fields=  mpr.materials.available_fields

sample_structure=  mpr.get_structure_by_material_id("mp-738") #Sb2Au (selected randomly)

print("Density:"+str(sample_structure.density))
print("Volume:"+str(sample_structure.volume))



