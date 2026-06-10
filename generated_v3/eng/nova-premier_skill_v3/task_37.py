from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import molecule
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Setup system
mol = molecule('N2'); mol.calc = EMT()
BFGS(mol).run(fmax=0.01)

# Vibration calculation
vib = Vibrations(mol)
vib.run()
freqs = vib.get_frequencies()
energies = vib.get_energies() * 96.485  # eV → kJ/mol

# Thermochemistry
thermo = IdealGasThermo(vib_energies=energies, atoms=mol,
                        geometry='linear', symmetrynumber=2, spin=0)
G = thermo.get_gibbs_energy(T=298.15, P=101325)
print(f"Gibbs free energy: {G:.3f} kJ/mol")
