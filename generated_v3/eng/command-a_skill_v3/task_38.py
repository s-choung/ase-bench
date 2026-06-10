from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Create Cu bulk structure
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Optimize structure (optional but recommended)
from ase.optimize import BFGS
BFGS(atoms).run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms)
vib.run()
frequencies = vib.get_frequencies()  # cm⁻¹

# Convert frequencies to energies (eV)
vib_energies = [units.invcm2eV * freq for freq in frequencies]

# Compute Helmholtz free energy using HarmonicThermo
thermo = HarmonicThermo(vib_energies=vib_energies, 
                        atoms=atoms,
                        temperature=300)

# Get Helmholtz free energy in eV
F = thermo.get_helmholtz_energy(temperature=300) / units.eV
print(f"Helmholtz free energy at 300K: {F:.4f} eV")
