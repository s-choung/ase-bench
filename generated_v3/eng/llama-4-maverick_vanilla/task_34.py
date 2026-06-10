from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import FIRE
from ase.mep import NEB, IDPPInterpolation

# Define the Cu(111) surface with an adatom
slab = Atoms('Cu6',
             [(0, 0, 0), (1, 0, 0), (0.5, 0.866, 0), (1.5, 0.866, 0),
              (0, 0, -1.1), (1, 0, -1.1)],
             cell=[(2.74, 0, 0), (1.37, 2.373, 0), (0, 0, 6.0)],
             pbc=(1, 1, 0))
slab.set_calculator(EMT())

# Define initial and final states
initial = slab.copy()
final = slab.copy()
final.positions[-1, 1] += 1.732 / 3

# Fix the slab atoms
mask = [atom.symbol != 'Cu' or atom.position[2] < -0.5 for atom in slab]
constraint = FixAtoms(mask=mask)
initial.set_constraint(constraint)
final.set_constraint(constraint)

# NEB setup
images = [initial]
images += [initial.copy() for _ in range(3)]
images.append(final)
neb = NEB(images, climb=True, parallel=False, remove_rotation_and_translation=True)
idpp = IDPPInterpolation(images,mic=True)
neb.interpolate(idpp)

# Optimize NEB images
for image in images[1:-1]:
    image.set_calculator(EMT())
    FIRE(image).run(fmax=0.05)

# Print the energy barrier
energies = [image.get_potential_energy() for image in images]
barrier = max(energies) - energies[0]
print(barrier)
