import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
cell = atoms.get_cell()

volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 9):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a0 = (4 * v0) ** (1 / 3)  # FCC primitive cell: V = a^3 / 4

print(f"평형 부피: {v0:.4f} Å³/atom")
print(f"평형 격자상수: {a0:.4f} Å")
print(f"체적탄성계수: {B / units.kJ * 1.0e24:.2f} GPa")
print(f"최소 에너지: {e0:.4f} eV")
