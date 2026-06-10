from ase.cluster import Octahedron
from ase.calculators.emt import EMT

# Create a Cu octahedron with 5 atoms along each edge
atoms = Octahedron('Cu', 5, latticeconstant=3.615)  # Cu fcc lattice constant ~3.615 Å

# Assign a simple built‑in calculator (optional, as no calculation is performed)
atoms.calc = EMT()

print("Number of atoms :", len(atoms))
print("Positions array shape :", atoms.get_positions().shape)
