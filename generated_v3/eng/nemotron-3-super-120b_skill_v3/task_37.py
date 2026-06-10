from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import IdealGasThermo

# N2 molecule
atoms = molecule('N2')
atoms.calc = EMT()

# Geometry optimization
BFGS(atoms).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(atoms)
vib.run()
vib_energies = vib.get_energies()   # in eV
vib.summary()
vib.clean()

# Thermochemistry
thermo = IdealGasThermo(vib_energies=vib_energies, atoms=atoms,
                        geometry='linear', symmetrynumber=2, spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(f'Gibbs free energy of N2 at 298.15 K, 1 atm: {G:.4f} eV')
