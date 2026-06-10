import numpy as np
from ase import bulk
from ase.calculators.emt import EMT
from ase.eos import BirchMurnaghan

a0 = 4.09
atoms = bulk('Ag', 'fcc', a=a0)
calc = EMT()
atoms.calc = calc

a_values = np.linspace(0.95*a0, 1.05*a0, 7)

volumes = []
energies = []

for a in a_values:
    new_atoms = bulk('Ag', 'fcc', a=a)
    new_atoms.calc = calc
    energy = new_atoms.get_potential_energy()
    volumes.append(a**3)
    energies.append(energy)

eos = BirchMurnaghan()
eos.fit(volumes, energies)

equilibrium_volume = eos.v0
equilibrium_a = equilibrium_volume ** (1/3)
bulk_modulus_GPa = eos.K0 * 160.2176634

print(f"Equilibrium lattice constant: {equilibrium_a:.3f} Å")
print(f"Bulk modulus: {bulk_modulus_GPa:.2f} GPa")
