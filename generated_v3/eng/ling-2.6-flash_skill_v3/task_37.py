from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo
import numpy as np

# Build N2 molecule and relax
atoms = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]], calculator=EMT())
BFGS(atoms).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
vib.clean()

# Filter imaginary frequencies and convert to eV
eigvals = vib.get_frequencies().flatten()  # in eV (vib returns eV by default)
imag_mask = eigvals < 0
vib_energies = np.abs(eigvals)  # IdealGasThermo expects positive energies

# Gibbs free energy
thermo = IdealGasThermo(vib_energies=vib_energies, atoms=atoms,
                        geometry='linear', symmetrynumber=2, spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(f'Gibbs free energy: {G:.3f} eV')
