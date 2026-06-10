from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.build import fcc111, molecule

# Create slab and adsorbate
slab = fcc111('Pt', (3, 3, 3), a=3.92, vacuum=10.0)
mol = molecule('CO', vacuum=5.0)
mol.positions += slab.positions[-1] + [0, 0, 2.0]
slab.extend(mol)

# Set calculator and constraints
slab.calc = EMT()
mask = [atom.tag == 1 for atom in slab]  # Bottom layer
constr = [FixAtoms(mask=mask), FixBondLength(len(slab)-2, len(slab)-1)]

# Run optimization
opt = BFGS(slab, constraints=constr)
opt.run(fmax=0.05)

# Output results
print("Energy: {:.3f} eV".format(slab.get_potential_energy()))
print("C-O distance: {:.3f} Å".format(slab.get_distance(-2, -1)))
