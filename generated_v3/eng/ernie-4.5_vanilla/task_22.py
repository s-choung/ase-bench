from ase import Atoms
from ase.build import fcc111, molecule
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

# Create Al(111) slab (3 layers)
slab = fcc111('Al', size=(1, 1, 3), vacuum=10.0)

# Constrain bottom two layers
constraint = FixAtoms(mask=[a.index < 2 * 1 * 1 for a in slab])  # Adjusting for 1x1 surface cells
slab.set_constraint(constraint)

# Create N2 molecule
n2 = molecule('N2')

# Position N2 at bridge site, 2.0 angstroms above slab
n2.positions[:, 2] += 2.0  # Set initial height

# Center N2 over bridge site
slab_center = slab.cell[:2, :].sum(axis=0) / 2
n2.positions[:, :2] += slab_center - (n2.positions[:, :2].max(axis=0) + n2.positions[:, :2].min(axis=0)) / 2

# Combine slab and N2
system = slab + n2

# Print number of atoms and atom types
print("Number of atoms:", len(system))
print("Atom types:", {site.symbol for site in system})

# Optional: Perform calculation
system.set_calculator(EMT())
print("Energy of the system:", system.get_potential_energy())
