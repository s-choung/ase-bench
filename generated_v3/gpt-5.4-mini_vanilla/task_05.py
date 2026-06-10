from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

volumes = []
energies = []

for s in np.linspace(0.94, 1.06, 9):
    a = atoms.copy()
    a.set_cell(atoms.cell * s, scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = (4.0 * v0) ** (1.0 / 3.0)

print(f"Equilibrium volume: {v0:.6f} Å^3")
print(f"Bulk modulus: {B:.6f} eV/Å^3")
print(f"Equilibrium lattice constant: {a0:.6f} Å")
