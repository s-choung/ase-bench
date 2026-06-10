from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
import numpy as np

# EOS for equilibrium lattice constant
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(atoms.cell * x, scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = (4 * v0)**(1/3)
print(f"Equilibrium lattice constant: {a0:.3f} Å")

# Create 4-layer (111) slab
slab = fcc111('Cu', size=(2, 2, 4), a=a0, vacuum=10.0)
slab.calc = EMT()

# Fix bottom 2 layers
mask = [a.tag >= 2 for a in slab]
slab.set_constraint(FixAtoms(mask=mask))

# Relax surface
BFGS(slab).run(fmax=0.01)

# Print results
print(f"Final energy: {slab.get_potential_energy():.3f} eV")
for tag in range(4):
    z = [a.z for a in slab if a.tag == tag]
    print(f"Layer {tag}: avg z = {np.mean(z):.3f} Å")
