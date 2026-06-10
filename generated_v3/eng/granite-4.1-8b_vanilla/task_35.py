from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS, LBFGS
from ase.neb import NEB

# Define initial and final states
initial = Atoms('Al2', positions=[[0, 0, 0], [1, 0, 0]])
final = Atoms('Al3', positions=[[0.5, 0, 0], [1, 0, 0], [1.5, 0, 0]])

# Fix the end points
constraint = FixAtoms(indices=[0, 1])
initial.set_constraint(constraint)
final.set_constraint(constraint)

# Attach EMT calculator
calc = EMT()
initial.calc = calc
final.calc = calc

# Create NEB with 3 images
images = NEB([initial, intermediate(initial, final), final])

# Helper function for linear interpolation
def intermediate(initial_atoms, final_atoms):
    positions_i = initial_atoms.get_positions()
    positions_f = final_atoms.get_positions()
    return Atoms('Al3', positions=(positions_i[0] + positions_f[0]) / 2,
                 cell=initial_atoms.cell, pbc=True)

# Optimize the images
images.calc = calc
opt = LBFGS(images, trajectory='neb.traj')
opt.run()

# Print energies of each image
for image in images:
    image.calc.results['energy'] = image.get_potential_energy()
    print(image.calc.results['energy'])
