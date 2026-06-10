from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# Build N2 molecule
atoms = molecule('N2')
atoms.calc = EMT()

# Optimize geometry
BFGS(atoms).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms, name='vib')
vib.run()
freqs = vib.get_frequencies()
vib_energies = vib.get_energies()
vib.summary()

# Thermochemistry
thermo = IdealGasThermo(
    vib_energies=vib_energies,
    atoms=atoms,
    geometry='linear',
    symmetrynumber=2,
    spin=0,
)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(f"Gibbs free energy at 298.15 K, 1 atm: {G:.4f} eV")

vib.clean()
