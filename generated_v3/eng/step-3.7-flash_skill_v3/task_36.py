import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Ag', 'fcc', a=4.09)
scales = np.linspace(0.95, 1.05, 7)
volumes, energies = [], []
for s in scales:
    a = atoms.copy()
    a.set_cell(a.cell * s, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

v0, e0, B = EquationOfState(volumes, energies, eos='birchmurnaghan').fit()
print(f"Equilibrium lattice constant: {v0**(1/3):.3f} Å")
print(f"Bulk modulus: {B * 160.21766208:.2f} GPa")
