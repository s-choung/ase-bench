```python
import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# 1. Find the optimal lattice constant for bulk Cu using EOS
cu_bulk = bulk('Cu', 'fcc', a=3.6)
cu_bulk.calc = EMT()
cell = cu_bulk.get_cell()
volumes = []
energies = []

for strain in np.linspace(0.95, 1.05, 11):
    atoms = cu_bulk.copy()
    atoms.set_cell(cell * strain, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
# For a primitive FCC cell with 1 atom, V = a^3 / 4
a0 = (v0 * 4)**(1/3)

print(f"Optimal lattice constant from EOS: {a0:.4f} Å")

# 2. Create a (111) slab with the optimized lattice constant
slab = fcc111('Cu', a=a0, size=(2, 2, 4), vacuum=10.0)

# 3. Set up calculator and constraints for surface relaxation
slab.calc = EMT()
# Fix the bottom two layers (tags 1 and 2)
constraint = FixAtoms(mask=[atom.tag <= 2 for atom in slab])
slab.set_constraint(constraint)

# 4. Run the relaxation
optimizer = BFGS(slab)
optimizer.run(fmax=0.05)

# 5. Print final energy and average z-coordinates of each layer
final_energy = slab.get_potential_energy()
print(f"\nFinal energy of the relaxed
