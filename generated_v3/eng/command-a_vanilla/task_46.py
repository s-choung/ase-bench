from ase import Atoms
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.emt import EMT

# Create Pt(111) 3-layer slab
slab = Atoms('Pt12',
             positions=[(0, 0, i*2.7) for i in range(3)]*4,
             cell=(4.0, 4.0, 8.1),
             pbc=(1, 1, 1))

# Add CO molecule above the slab
slab.extend(Atoms('CO', positions=[(2.0, 2.0, 8.5), (2.0, 2.0, 9.0)]))

# Apply constraints
mask = [atom.symbol != 'Pt' for atom in slab]
fix_bottom = FixAtoms(mask=mask)
fix_co = FixBondLength(slab.indices[-2], slab.indices[-1])
slab.set_constraint([fix_bottom, fix_co])

# Set calculator and optimize
slab.calc = EMT()
dyn = BFGS(slab, trajectory=None)
dyn.run(fmax=0.05)

# Print results
print(f'Final energy: {slab.get_potential_energy():.4f} eV')
print(f'Final C-O distance: {slab.get_distance(-2, -1):.4f} Å')
