from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Create Cu bulk supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)
atoms.calc = EMT()

# Reference potential energy
pot_energy = atoms.get_potential_energy()

# Vibrational analysis
vib = Vibrations(atoms)
vib.run()
vib_energies = vib.get_energies()  # in eV
vib.clean()

# Remove translational near-zero modes
vib_energies = [e for e in vib_energies if e > 1e-4]

# Helmholtz free energy at 300 K
thermo = HarmonicThermo(vib_energies=vib_energies, potentialenergy=pot_energy)
F = thermo.get_helmholtz_energy(300)

print(f"Helmholtz free energy at 300 K: {F:.4f} eV")
