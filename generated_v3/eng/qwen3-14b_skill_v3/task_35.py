from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.optimize.neb import NEB
from ase.constraints import FixAtoms

# Create initial and final states
symbols = ['Al', 'Al', 'Al']
initial = Atoms(symbols=symbols, positions=[[0, 0, 0], [2, 0, 0], [0, 1, 0]])
final = Atoms(symbols=symbols, positions=[[0, 0, 0], [2, 0, 0], [2, 1, 0]])
middle = Atoms(symbols=symbols, positions=[[0, 0, 0], [2, 0, 0], [1, 1, 0]])

# Set cell with vacuum and scale atoms
cell = [[4.0, 0.0, 0.0], [0.0, 4.0, 0.0], [0.0, 0.0, 4.0]]
for atoms in [initial, middle, final]:
    atoms.set_cell(cell, scale_atoms=True)
    atoms.set_constraint(FixAtoms(indices=[0, 1]))
    atoms.calc = EMT()

# Set up NEB and optimize
images = [initial, middle, final]
neb = NEB(images)
opt = BFGS(neb)
opt.run(fmax=0.05)

# Print energies
for i, img in enumerate(images):
    print(f"Image {i} energy: {img.get_potential_energy()} eV")
