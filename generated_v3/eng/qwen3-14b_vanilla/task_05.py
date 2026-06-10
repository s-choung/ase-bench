import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import Murnaghan

volumes = []
energies = []

for a in np.arange(3.4, 4.1, 0.1):
    positions = [(0,0,0), (0.5,0.5,0), (0.5,0,0.5), (0,0.5,0.5)]
    cell = [[a,0,0], [0,a,0], [0,0,a]]
    atoms = Atoms('Cu4', positions=positions, cell=cell, pbc=True)
    atoms.set_calculator(EMT())
    volumes.append(a**3)
    energies.append(atoms.get_potential_energy())

eos = Murnaghan()
eos.fit(volumes, energies)

print(f"Equilibrium volume: {eos.get_volume():.3f} Å³")
print(f"Bulk modulus: {eos.get_bulk_modulus():.2f} eV/Å³")
