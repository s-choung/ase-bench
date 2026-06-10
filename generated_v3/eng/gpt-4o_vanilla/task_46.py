from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms, FixBondLengths
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create Pt slab
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
slab.set_calculator(EMT())

# Add CO molecule
co = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.2)])
add_adsorbate(slab, co, height=1.8, position=(2, 2))

# Fix bottom layer and CO bond distance
slab.constraints = [FixAtoms(indices=[atom.index for atom in slab if atom.position[2] < slab.positions[:, 2].min() + 1.0]),
                    FixBondLengths(bonds=[(-1, -2)])]

# Optimize structure
optimizer = BFGS(slab)
optimizer.run(fmax=0.05)

# Output final energy and C-O distance
print('Final energy:', slab.get_potential_energy())
print('C-O distance:', co.get_distance(-1, -2))
