from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
import numpy as np

# Build and relax bulk Cu
atoms = bulk('Cu', 'fcc', a=3.615)
atoms.calc = EMT()
atoms.get_potential_energy()
atoms.get_forces()

# Vibrations (single atom cell)
vib = Vibrations(atoms)
vib.run()
frequencies = vib.get_frequencies()

# Remove imaginary/zero acoustic modes (<1 cm^-1)
freqs = np.array([f for f in frequencies if f > 1.0])

thermo = HarmonicThermo(vib_energies=freqs * 1e-2 * 1.23981e-4,  # cm^-1 to eV
                        potentialenergy=atoms.get_potential_energy(),
                        electronicenergy=0.0,
                        geometry='monatomic')

F = thermo.get_helmholtz_energy(temperature=300)
print(f"Helmholtz free energy at 300K: {F:.6f} eV")

vib.clean()
