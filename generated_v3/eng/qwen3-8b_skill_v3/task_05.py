import numpy as np
from ase import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()

scaling = np.linspace(0.95, 1.05, 7)
vols = []
energies = []

for s in scaling:
    a = atoms.copy()
    a.set_cell(atoms.get_cell() * s, scale_atoms=True)
    a.calc = EMT()
    e = a.get_potential_energy()
    vols.append(a.get_volume())
    energies.append(e)

eos = EquationOfState(vols, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

print(f"Equilibrium volume: {v0} Å³")
print(f"Bulk modulus: {B} eV/Å³")
