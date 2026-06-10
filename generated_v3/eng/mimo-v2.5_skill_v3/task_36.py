from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Ag', 'fcc', a=4.09, cubic=True)

volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    trial = atoms.copy()
    trial.set_cell(atoms.cell * x, scale_atoms=True)
    trial.calc = EMT()
    volumes.append(trial.get_volume())
    energies.append(trial.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

B_GPa = B * 160.21766208
a0 = v0 ** (1.0 / 3.0)

print(f'Equilibrium lattice constant: {a0:.4f} Å')
print(f'Bulk modulus: {B_GPa:.2f} GPa')
