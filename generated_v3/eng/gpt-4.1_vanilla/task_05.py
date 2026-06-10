from ase.build import bulk
from ase.calculators.emt import EMT
from ase.units import GPa
from ase.eos import EquationOfState
import numpy as np

a0 = 3.6
atoms = bulk('Cu', 'fcc', a=a0)
atoms.calc = EMT()

volumes = []
energies = []

scales = np.linspace(0.95, 1.05, 9)
for s in scales:
    ato = atoms.copy()
    ato.set_cell(atoms.cell * s, scale_atoms=True)
    volumes.append(ato.get_volume())
    energies.append(ato.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

print(f'Equilibrium volume: {v0:.2f} Å³')
print(f'Bulk modulus: {B / GPa:.2f} GPa')
