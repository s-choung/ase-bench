from ase.lattice.cubic import FaceCenteredCubic
from ase import Atoms

# NaCl structure (spacegroup 225)
NaCl = FaceCenteredCubic(size=(1,1,1), symbol='Na', latticeconstant=5.64)
NaCl += FaceCenteredCubic(size=(1,1,1), symbol='Cl', latticeconstant=5.64)
NaCl.positions[1,:] = [2.82, 2.82, 2.82]  # Cl at (0.5,0.5,0.5)

print(len(NaCl), NaCl.get_chemical_symbols())
