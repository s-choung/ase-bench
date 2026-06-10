import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

volumes, energies = [], []
scale_factors = np.linspace(0.95, 1.05, 7)

for s in scale_factors:
    a = atoms.copy()
    a.set_cell(a.get_cell() * s, scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {B:.1f} GPa")
