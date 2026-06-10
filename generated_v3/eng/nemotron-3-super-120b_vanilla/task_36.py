import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EOS

# reference lattice constant (approx.)
a_ref = 4.09  # Å
a_vals = np.linspace(a_ref * 0.95, a_ref * 1.05, 7)

volumes = []
energies = []
# get number of atoms in the cell (constant for all volumes)
natoms = len(bulk('Ag', 'fcc', a=a_ref))

for a in a_vals:
    atoms = bulk('Ag', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

volumes = np.array(volumes)
energies = np.array(energies)

eos = EOS(volumes, energies, eos='birchmurnaghan')
v0, e0, B, BP = eos.fit()

# volume per atom
V_atom = v0 / natoms
# equilibrium lattice constant for FCC: a = (4 * V_atom)^(1/3)
a0 = (4.0 * V_atom) ** (1.0 / 3.0)
# convert bulk modulus from eV/Å^3 to GPa (1 eV/Å^3 = 160.21766 GPa)
B_GPa = B * 160.21766

print(f'Equilibrium lattice constant: {a0:.3f} Å')
print(f'Bulk modulus: {B_GPa:.1f} GPa')
