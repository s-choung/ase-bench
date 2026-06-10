from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS
from ase.build import molecule  # Not directly needed but for potential expansion, here kept minimal

# Create initial and final states
initial = Atoms('Al3', positions=[[0, 0, 0], [1, 0, 0], [2, 0, 0]], cell=[10, 10, 10], pbc=False)
final = Atoms('Al3', positions=[[0, 0, 0], [2, 0, 0], [1, 0, 0]], cell=[10, 10, 10], pbc=False)  # Swapped third atom

# Fix first and third atoms in both states (they remain stationary)
for atoms in [initial, final]:
    atoms.set_constraint(FixAtoms(indices=[0, 2] if len(atoms) > 2 else [0]))  # Simplified for 3 atoms, fix first and last
    # Actually for 3 atoms, index 0 and 2 are fixed, index 1 moves

# Alternatively, more precisely for 3-atom system:
initial.set_constraint(FixAtoms(indices=[0, 2]))
final.set_constraint(FixAtoms(indices=[0, 2]))

# Create images
images = [initial] + [initial.copy() for _ in range(3)] + [final]  # 3 images between initial and final

# Set calculator
for atoms in images:
    atoms.calc = EMT()

# Setup and run NEB
neb = NEB(images)
neb.interpolate()  # Linear interpolation

# Optimize with BFGS
opt = BFGS(neb, trajectory='neb_trajectory.traj')
opt.run(fmax=0.01)

# Print energies of each image
for i, atoms in enumerate(images):
    print(f"Image {i}: Energy = {atoms.get_potential_energy():.6f} eV")
