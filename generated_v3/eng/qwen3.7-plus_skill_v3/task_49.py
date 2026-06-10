import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.constraints import FixAtoms
from ase.eos import EquationOfState

# 1. EOS for Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(a.get_cell() * x, scale_atoms=True)
    a.calc = EMT()
    BFGS(FrechetCellFilter(a)).run(fmax=0.01)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = v0 ** (1. / 3.)

# 2. Create (111) 4-layer slab
slab = fcc111('Cu', size=(3, 3, 4), a=a_eq, vacuum=10.0)

# 3. Attach EMT
slab.calc = EMT()

# 4. Fix bottom 2 layers
z_coords = slab.positions[:, 2]
z_rounded = np.round(z_coords, 2)
unique_z = np.sort(np.unique(z_rounded))
mask = np.isin(z_rounded, unique_z[:2])
slab.set_constraint(FixAtoms(mask=mask))

# 5. Surface relaxation
BFGS(slab).run(fmax=0.05)

# 6. Print results
print(f"Final energy: {slab.get_potential_energy():.4f} eV")
for z in unique_z:
    layer_mask = np.abs(z_coords - z) < 1e-2
    avg_z = np.mean(slab.positions[layer_mask, 2])
    print(f"Layer (ref z={z:.2f} A): avg z = {avg_z:.4f} A")
