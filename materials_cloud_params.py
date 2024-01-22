
'''Parameter lists for parsing Materials Cloud databases'''


#full properties for 2D MC database
MC_PROPERTY_LIST_FULL = ['abundance',  # float, in percentage
                         'all_3D_parents',  #string
                         "band_gap",  # float, eV
                         'bands_2D',  #string,directs to file of bandstructure
                         'bands_2D_y_max_lim',  #float (eV)
                         'bands_2D_y_min_lim',  #float (eV)
                         'bands_2D_y_origin',  #float (eV)
                         "binding_energy_per_substructure_per_unit_area_df2",  # float (meV/A^2)
                         "binding_energy_per_substructure_per_unit_area_rvv10",  #float (meV/A^2)
                         'cite', #string
                         "delta_df2",  #float interlayer distance percentage (100 %)
                         "delta_rvv10", #float interlayer distance percentage (100 %)
                         "fermi_energy",  #float (eV)
                         "formula", #string
                         "initial_3D_bulk_structure",
                         "initial_3D_db_id",
                         "initial_3D_formula",
                         "initial_3D_source_db",
                         "initial_3D_spg",
                         "magnetic_state",
                         "magnetic_state_long",
                         "n_atoms",
                         "n_bands",
                         "n_electrons",
                         "n_species",
                         "phonons_2D",
                         "point_group",
                         "prototype",
                         "relaxed_3D_bulk_structure_df2",
                         "relaxed_3D_bulk_structure_revpbe",
                         "relaxed_3D_bulk_structure_rvv10",
                         "space_group",
                         "species",
                         "structure_2D",
                         "suffix"]


#selected properties (rvv100)
MC_PROPERTY_LIST_V1 =   ["band_gap",  # float, eV
                         ["binding_energy_per_substructure_per_unit_area","average_matches"],  #float (meV/A^2), True means to average all values that match
                         ["delta","average_matches"], #float interlayer distance percentage (100 %), True means to average all values that match
                         "fermi_energy",  #float (eV)
                         "n_atoms",
                         "n_electrons",
                         "n_species"]
