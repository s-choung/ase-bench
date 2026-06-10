from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Create N2 molecule
atoms = molecule('N2')
atoms.calc = EMT()

# Optimize the structure
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Calculate vibrational frequencies
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()

# Compute Gibbs free energy using IdealGasThermo
thermo = IdealGasThermo(vib_energies=freqs, atoms=atoms, geometry='linear', symmetrynumber=2, spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)

print(f"The Gibbs free energy of N2 at 298.15K and 1 atm is: {G} eV")
