from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

a0 = 3.6
atoms0 = bulk('Cu', 'fcc', a=a0)
atoms0.calc = EMT()

scales = np.linspace(0.94, 1.06, 9)
volumes, energies = [], []

for s in scales:
    atoms = atoms0.copy()
    atoms.set_cell(atoms0.cell * s, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

a_eq = (4 * v0) ** (1 / 3)
B_GPa = B / 1e9 / 1.602176634e-19 * 1e-30  # Pa from eV/Å^3, then GPa
B_GPa = B * 160.21766208

print(f"Equilibrium lattice constant a0 = {a_eq:.6f} Å")
print(f"Equilibrium volume V0 = {v0:.6f} Å^3")
print(f"Bulk modulus B = {B_GPa:.3f} GPa")
