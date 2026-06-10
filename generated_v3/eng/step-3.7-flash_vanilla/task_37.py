from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Build and optimize N2 geometry
atoms = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Calculate harmonic vibrational modes
vib = Vibrations(atoms)
vib.run()

# Compute thermodynamic properties
thermo = IdealGasThermo(
    vib.get_energies(),
    vib.get_frequencies(),
    'linear',
    symmetrynumber=2,
    atoms=atoms
)
gibbs = thermo.get_gibbs_energy(temperature=298.15, pressure=101325.)
print(f"Gibbs free energy: {gibbs:.3f} eV")
