from ase.build import bulk
from ase.lattice.cubic import FaceCenteredCubic

# NaCl has the Fm-3m space group (FCC lattice)
# Na is at (0,0,0), Cl is at (0.5, 0.5, 0.5) relative to the FCC basis
a = 5.64
atoms = FaceCenteredCubic(directions=[[a, 0, 0], [0, a, 0], [0, 0, a]],
                          symbol='Na',
                          basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
                          ratio=[1, 1])

# Add Cl atoms to the basis positions
# Since it's FCC, the basis (0,0,0) and (0.5,0.5,0.5) defines the salt structure
# The 'bulk' function is more direct for NaCl
atoms = bulk('NaCl', 'rocksalt', a=5.64)

print(f"Number of atoms: {len(atoms)}")
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")
