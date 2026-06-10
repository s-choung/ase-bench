import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.eos import EquationOfState

# EOS로 격자상수 결정
atoms = bulk('Cu', 'fcc', a=3.6)
cell0 = atoms.get_cell()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 9):
    a = atoms.copy()
    a.set_cell(cell0 * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_opt = (4 * v0) ** (1 / 3)
print(f'Optimized lattice constant a = {a_opt:.4f} A')

# (111) slab 4층, 하부 2층 고정
slab = fcc111('Cu', size=(2, 2, 4), a=a_opt, vacuum=10.0)
slab.set_constraint(FixAtoms(mask=[atom.tag >= 3 for atom in slab]))
slab.calc = EMT()
BFGS(slab, logfile=None).run(fmax=0.02)

print(f'Final energy = {slab.get_potential_energy():.4f} eV')
for layer in sorted(set(slab.get_tags())):
    z_mean = np.mean([atom.position[2] for atom in slab if atom.tag == layer])
    print(f'Layer {layer} (1=top): mean z = {z_mean:.4f} A')
