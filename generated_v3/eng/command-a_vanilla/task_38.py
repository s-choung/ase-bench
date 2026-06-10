from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Create Cu bulk structure
cu = Atoms('Cu', positions=[[0, 0, 0]], cell=[[3.6, 0, 0], [0, 3.6, 0], [0, 0, 3.6]], pbc=True)
cu *= (2, 2, 2)

# Attach EMT calculator
cu.calc = EMT()

# Relax the structure
cu.get_potential_energy()

# Calculate vibrational frequencies
vib = Vibrations(cu)
vib.run()
vib_energies = vib.get_energies()

# Compute Helmholtz free energy at 300K
thermo = HarmonicThermo(vib_energies, 300, calc=cu.calc)
helmholtz_free_energy = thermo.get_helmholtz_energy(temperature=300, pressure=0)

# Convert to eV and print
print(f"Helmholtz free energy at 300K: {helmholtz_free_energy / 96485.33212:.6f} eV")
