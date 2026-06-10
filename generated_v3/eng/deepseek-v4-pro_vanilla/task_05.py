from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

volumes = []
energies = []
for a in np.linspace(3.4, 3.8, 21):
    atoms.set_cell([a, a, a], scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
e0, v0, B, Bp = eos.fit()
a0 = v0**(1/3)

print(f"Equilibrium lattice constant: {a0:.3f} Å")
print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {B * 160.21766:.2f} GPa")
