from ase.build import bulk
from ase.eos import EquationOfState
from ase.calculators.emt import EMT
import numpy as np

atoms = bulk('Ag', 'fcc', a=4.09)
scale_factors = np.linspace(0.95, 1.05, 7)
volumes, energies = [], []

for x in scale_factors:
    a = atoms.copy()
    a.set_cell(a.get_cell() * x, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

a0 = v0 ** (1/3)
B_GPa = B * 160.2176634  # eV/Å³ → GPa

print(f"Equilibrium lattice constant: {a0:.3f} Å")
print(f"Bulk modulus: {B_GPa:.3f} GPa")
