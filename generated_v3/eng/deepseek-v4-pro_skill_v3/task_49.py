from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
from ase.optimize import BFGS
import numpy as np

# 1. EOS for equilibrium lattice constant
initial_a = 3.6
atoms_bulk = bulk('Cu', 'fcc', a=initial_a, cubic=True)
atoms_bulk.calc = EMT()

# vary lattice constant by scaling cell
scales = np.linspace(0.97, 1.03, 9)
volumes, energies = [], []
for s in scales:
    a = atoms_bulk.copy()
    a.set_cell(initial_a * s * np.eye(3), scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = (4 * v0) ** (1/3)  # cubic cell: volume = a**3 for conventional cell, but we used cubic=True with 4 atoms; V = a**3

# 2. Create (111) 4-layer slab with the lattice constant a0
slab = fcc111('Cu', a=a0, size=(1,1,4), vacuum=10.0)
slab.calc = EMT()

# 3. Fix bottom 2 layers (tags 0 and 1)
mask = [atom.tag < 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

# 4. BFGS relaxation
opt = BFGS(slab, trajectory='opt.traj')
opt.run(fmax=0.01)

# 5. Results
final_energy = slab.get_potential_energy()
print(f'Final energy: {final_energy:.6f} eV')

# Average z per layer
layers = sorted(set(slab.get_tags()))
for tag in layers:
    indices = [a.index for a in slab if a.tag == tag]
    z = slab.positions[indices, 2].mean()
    print(f'Layer {tag}, average z: {z:.4f} Å')
