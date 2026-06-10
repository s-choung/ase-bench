import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

volumes, energies = [], []
for scale in np.linspace(0.95, 1.05, 11):
    atoms.set_cell(atoms.cell * scale, scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

print(f"Equilibrium volume: {v0:.3f} A^3")
print(f"Bulk modulus: {B:.3f} GPa")
