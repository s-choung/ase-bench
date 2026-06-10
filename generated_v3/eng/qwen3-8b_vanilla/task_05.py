import ase
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import fit

lattice_params = [3.5, 3.55, 3.6, 3.65, 3.7]
volumes = []
energies = []

for a in lattice_params:
    atoms = bulk('Cu', 'fcc', a=a, cubic=True)
    atoms.calc = EMT()
    atoms.get_potential_energy()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_energy())

v0, b = fit(volumes, energies)
print(f"Equilibrium volume: {v0:.4f} Å³")
print(f"Bulk modulus: {b:.4f} eV/Å³")
