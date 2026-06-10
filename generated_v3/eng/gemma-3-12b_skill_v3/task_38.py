from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
import numpy as np

atoms = Atoms('Cu', pbc=True)
atoms.set_cell([[3.61, 0.0, 0.0], [0.0, 3.61, 0.0], [0.0, 0.0, 3.61]])
atoms.calc = EMT()

# Optimize the structure
from ase.optimize import BFGS
opt = BFGS(atoms, trajectory='opt.traj')
opt.run(fmax=0.01)
print(atoms.get_potential_energy())

# Calculate vibrational frequencies
vib = Vibrations(atoms)
vib.run()
frequencies = vib.get_frequencies()

# Compute vibrational energy
vib_energies = frequencies / 2.0  # Zero-point vibrational energy

# Calculate the Helmholtz free energy using HarmonicThermo
thermo = HarmonicThermo(vib_energies, atoms, geometry='cubic')
H = thermo.get_helmholtz_free_energy(temperature=300.0)

print(f"Helmholtz free energy at 300K: {H:.4f} eV")
