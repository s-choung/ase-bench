from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.visualize import view

# Calculator
atoms.calc = EMT()

# Initial state: Al atom at left, a third atom near left
initial = Atoms([
    ['Al', (-2.5, 0, 0)],   # fixed
    ['Al', ( 2.5, 0, 0)],   # fixed
    ['Al', (-2.0, 0, 0)]    # movable
])

# Final state: Al atoms as before, third atom at right
final = Atoms([
    ['Al', (-2.5, 0, 0)],
    ['Al', ( 2.5, 0, 0)],
    ['Al', ( 2.0, 0, 0)]
])

# Images (0 initial, 1‑2 middle, 3 final) – need independent Energies; they are computed by NEB
images = [initial] + [
    initial.copy() for _ in range(2)
] + [final]

# Linear interpolation
ne = NEB(images)
ne.interpolate()

# Run optimization; fmax stops when force change < 0.05 eV/Å
opt = BFGS(ne)
opt.run(fmax=0.05)

# Energy of each image
energies = [img.get_potential_energy() for img in images]
print('Image energies (eV):', energies)

# Quick view (optional)
view(images, viewer='x3d')  # 또는 'ngl', 'pyplot' 등
