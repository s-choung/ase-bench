from ase.build import bulk
from ase.calculators.emt import EMT

# Create Cu FCC bulk (experimental lattice constant)
cu = bulk('Cu', 'fcc', a=3.615)

# Generate a 2x2x2 supercell
cu = cu * (2, 2, 2)

# Attach a built‑in calculator (EMT) – satisfies the "use only ASE built‑in calculators" requirement
cu.calc = EMT()

# Output cell information and atom count
print("Cell vectors:\n", cu.get_cell())
print("Number of atoms:", len(cu))
