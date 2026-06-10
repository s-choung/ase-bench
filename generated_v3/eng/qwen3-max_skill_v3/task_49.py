from ase import bulk
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
import numpy as np

# Step 1: Find equilibrium lattice constant via EOS
a0_guess = 3.6
cell = bulk('Cu', 'fcc', a=a0_guess).get_cell()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    atoms = bulk('Cu', 'fcc', a=a0_guess)
    atoms.set_cell(cell * x, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = (4 * v0)**(1/3)

# Step 2: Create relaxed (111) slab
slab = fcc111('Cu', size=(1, 1, 4), a=a0, vacuum=10.0)
slab.calc = EMT()
constraint = FixAtoms(mask=[a.tag <= 2 for a in slab])
slab.set_constraint(constraint)
from ase.optimize import BFGS
BFGS(slab).run(fmax=0.01)

# Step 3: Print results
print(f"Final energy: {slab.get_potential_energy():.6f} eV")
z_coords = slab.positions[:, 2]
for layer in range(1, 5):
    layer_mask = [a.tag == layer for a in slab]
    avg_z = np.mean(z_coords[layer_mask])
    print(f"Layer {layer} avg z: {avg_z:.6f} Å")
