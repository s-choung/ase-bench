from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# --- EOS for Cu FCC bulk ---
a_guess = 3.6
scales = np.linspace(0.95, 1.05, 7)
volumes, energies = [], []
for s in scales:
    atoms = bulk('Cu', 'fcc', a=a_guess * s)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = (v0 * 4) ** (1/3)  # FCC: 4 atoms per conventional cell
print(f'Equilibrium lattice constant a0 = {a0:.3f} Å')

# --- Build (111) slab ---
slab = fcc111('Cu', size=(2,2,4), vacuum=10.0, a=a0)
slab.calc = EMT()

# Fix bottom two layers (tags 0 and 1)
mask = [atom.tag < 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

# Relax
BFGS(slab).run(fmax=0.05)

# Final energy
E = slab.get_potential_energy()
print(f'Final slab energy = {E:.4f} eV')

# Average z per layer
tags = slab.get_tags()
zs = slab.get_positions()[:, 2]
for t in np.unique(tags):
    avg_z = zs[tags == t].mean()
    print(f'Layer tag {t}: <z> = {avg_z:.3f} Å')
