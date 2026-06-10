from ase.spacegroup import crystal
atoms = crystal('Ti', basis=[(0,0,0), (1/3, 2/3, 1/2)], 
                spacegroup=194,  # P6_3/mmc for HCP
                cellpar=[a, a, c, 90, 90, 120])
