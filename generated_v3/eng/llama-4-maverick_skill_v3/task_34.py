from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS

# Create Cu(111) slab and adatom
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
adatom = Atoms('Cu', positions=[(1.5, 0.75, 8.0)], cell=slab.get_cell())
slab += adatom

# Define initial and final states
initial = slab.copy()
final = slab.copy()
final.positions[-1, 1] += 1.36  # Move adatom to hcp site

# Create NEB images
images = [initial] + [initial.copy() for _ in range(5)] + [final]
neb = NEB(images)
neb.interpolate(method='idpp')

# Set constraints and calculators
constraint = FixAtoms(mask=[atom.tag >= 3 for atom in slab])
for img in images:
    img.set_constraint(constraint)
    img.calc = EMT()

# Optimize NEB path
opt = BFGS(neb)
opt.run(fmax=0.05)

# Calculate energy barrier
energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(f'Energy barrier: {barrier:.3f} eV')
