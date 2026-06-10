from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

# EOS for Cu FCC equilibrium lattice constant
bulk_cu = bulk('Cu', 'fcc', a=3.6)
bulk_cu.calc = EMT()
cell = bulk_cu.get_cell()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    scaled = bulk_cu.copy()
    scaled.set_cell(cell * x, scale_atoms=True)
    volumes.append(scaled.get_volume())
    energies.append(scaled.get_potential_energy())
eos = EquationOfState(volumes, energies, 'birchmurnaghan')
v0, _, _ = eos.fit()
a_eq = v0 ** (1/3)

# 4-layer (111) slab setup
slab = fcc111('Cu', size=(2,2,4), a=a_eq, vacuum=10.0)
slab.calc = EMT()
slab.set_constraint(FixAtoms(mask=[a.tag >= 2 for a in slab]))

# Surface relaxation
BFGS(slab).run(fmax=0.05)

# Result output
print(f'Final energy: {slab.get_potential_energy():.6f} eV')
layer_zs = {}
for atom in slab:
    layer_zs.setdefault(atom.tag, []).append(atom.position[2])
for tag in sorted(layer_zs):
    print(f'Layer {tag} avg z: {np.mean(layer_zs[tag]):.6f} Å')
