import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# 1. Find equilibrium lattice constant using EOS
bulk_cu = bulk('Cu', 'fcc', a=3.6)
cell0 = bulk_cu.get_cell()
volumes, energies = [], []

for x in np.linspace(0.95, 1.05, 7):
    a = bulk_cu.copy()
    a.set_cell(cell0 * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = (4 * v0) ** (1.0 / 3.0)  # V = a^3 / 4 for FCC primitive cell

# 2. Create (111) 4-layer slab with equilibrium lattice constant
slab = fcc111('Cu', size=(2, 2, 4), a=a0, vacuum=10.0)
slab.set_constraint(FixAtoms(mask=[atom.tag <= 2 for atom in slab]))
slab.calc = EMT()

# 3. Surface relaxation
BFGS(slab).run(fmax=0.05)

# 4. Print results
print(f"Equilibrium lattice constant: {a0:.4f} Å")
print(f"Final Energy: {slab.get_potential_energy():.4f} eV")
for i in range(1, 5):
    layer_z = [atom.z for atom in slab if atom.tag == i]
    print(f"Layer {i}: Average z = {np.mean(layer_z):.4f} Å")
