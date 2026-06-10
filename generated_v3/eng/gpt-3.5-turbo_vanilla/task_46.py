from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS

# Create CO molecule
CO = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.2)])

# Create Pt slab with 3 layers
slab = Atoms('Pt4',
             scaled_positions=[(0.0, 0.0, 0.0),
                               (0.5, 0.5, 0.0),
                               (0.5, 0.0, 1 / 3),
                               (0.0, 0.5, 1 / 3)],
             cell=[(0, 2.75, 2.75),
                   (2.75, 0, 2.75),
                   (2.75, 2.75, 0)],
             pbc=True)

slab.set_calculator(EMT())

# Apply constraints
constraints = [FixAtoms(indices=[atom.index for atom in slab if atom.position[2] < slab.cell[2, 2] / 3]),
               FixBondLength(0, 1, 1.1)]

slab.set_constraint(constraints)

# Optimize slab
dyn = BFGS(slab, logfile=None)
dyn.run(fmax=0.05)

# Print final energy and CO distance
energy = slab.get_potential_energy()
distance = slab.get_distance(0, 1)
print("Final energy:", energy)
print("C-O distance:", distance)
