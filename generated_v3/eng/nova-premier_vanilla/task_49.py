from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

# Bulk Cu properties
bulk = Atoms('Cu', crystalstructure='fcc', pbc=True)
eos = []

# Calculate EOS
for x in np.linspace(0.9, 1.1, 5):
    bulk.set_cell(bulk.cell * x, scale_atoms=True)
    bulk.calc = EMT()
    eos.append(bulk.get_potential_energy())

# Fit EOS and find equilibrium lattice
eos = EquationOfState(bulk.cell.lengths()[0]*np.linspace(0.9,1.1,5), eos)
a_eq = eos.fit()
bulk.set_cell([a_eq, a_eq, a_eq], scale_atoms=True)

# Build (111) slab
slab = bulk*(2, 2, 4)
slab = slab[slab.positions[:, 2] < 6]

# EMT & constraints
slab.calc = EMT()
mask = [a.z < 2.5 for a in slab]
slab.set_constraint(FixAtoms(mask=mask))

# Optimize
dyn = BFGS(slab)
dyn.run(fmax=0.01)

# Analysis
layers = [atom.z for atom in slab]
z_avg = [np.mean(np.array(layers)[np.isclose(layers, z, atol=0.5)]) for z in sorted(set(np.round(layers)))]
print("Energy:", slab.get_potential_energy())
print("Layer z-avg:", z_avg)
