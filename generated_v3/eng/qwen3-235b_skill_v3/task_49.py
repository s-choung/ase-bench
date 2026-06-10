from ase import units
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# Find equilibrium lattice constant using EOS
x_list = np.linspace(3.5, 4.0, 7)
vols, energies = [], []
for x in x_list:
    atoms = bulk('Cu', 'fcc', a=x)
    atoms.calc = EMT()
    vols.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(vols, energies)
v0, e0, B = eos.fit()
a_eq = (4 * v0)**(1/3)

# Create (111) slab with equilibrium lattice constant
slab = fcc111('Cu', size=(2, 2, 4), a=a_eq, vacuum=10.0)
slab.calc = EMT()

# Fix bottom 2 layers (tags 0 and 1)
mask = [atom.tag < 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

# Relax
BFGS(slab).run(fmax=0.01)

# Output final energy and average z per layer
print(f"Final energy: {slab.get_potential_energy():.6f} eV")
for layer in range(4):
    z_avg = np.mean([atom.position[2] for atom in slab if atom.tag == layer])
    print(f"Layer {layer} average z: {z_avg:.6f} Å")
