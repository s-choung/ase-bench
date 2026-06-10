from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

a0 = 3.6
volumes = []
energies = []

for scale in np.linspace(0.90, 1.10, 20):
    scaled = atoms.copy()
    scaled.set_cell(atoms.cell * scale, scale_atoms=True)
    scaled.calc = EMT()
    volumes.append(scaled.get_volume())
    energies.append(scaled.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

print(f"평형 부피 V0 = {v0:.4f} Å³")
print(f"체적탄성계수 B  = {B / 1.60218e-19 * 1e30 * 1e-9:.2f} GPa")
