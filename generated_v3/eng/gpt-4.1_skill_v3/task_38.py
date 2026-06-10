from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Build and optimize primitive bulk cell
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

# Vibrational analysis (primitive cell)
vib = Vibrations(atoms, name='vib')
vib.run()
vib_energies = vib.get_energies()  # (eV)

# Helmholtz free energy (HarmonicThermo)
thermo = HarmonicThermo(vib_energies, atoms=atoms)
F = thermo.get_helmholtz_energy(temperature=300)

print(f'Helmholtz free energy at 300 K: {F:.6f} eV')

vib.clean()
