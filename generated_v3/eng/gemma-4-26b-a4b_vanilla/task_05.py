import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Note: EMT is for metals like Cu, but it's an empirical model for transition metals.
# For true Cu, one would use a more accurate potential, but EMT is the ASE built-in.
lat_constants = np.linspace(3.4, 4.0, 10)
volumes = []
energies = []

for a in lat_constants:
    atoms = bulk('Cu', 'fcc', a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
    volumes.append(atoms.get_volume())

volumes = np.array(volumes)
energies = np.array(energies)

eos = EquationOfState(volumes, energies)
v0, b0 = eos.fit()

print(f"Equilibrium Volume: {v0:.4f} Å^3")
print(f"Bulk Modulus: {b0:.4f} eV/Å^3")

# Convert eV/A^3 to GPa (1 eV/A^3 approx 160.218 GPa)
print(f"Bulk Modulus: {b0 * 160.218:.2f} GPa")
