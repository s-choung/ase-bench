import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

volumes, energies = [], []
for s in np.linspace(0.94, 1.06, 9):
    a = atoms.copy()
    a.set_cell(a.get_cell() * s, scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()          # v0 in Å³, B in GPa
a0 = v0 ** (1/3)               # lattice constant Å

print(f"Equilibrium lattice constant a0 = {a0:.3f} Å")
print(f"Equilibrium volume V0 = {v0:.3f} Å³")
print(f"Bulk modulus B = {B:.1f} GPa")
