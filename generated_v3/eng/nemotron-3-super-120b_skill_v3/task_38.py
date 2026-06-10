from ase import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Build Cu bulk (fcc) and attach EMT calculator
atoms = bulk('Cu', 'fcc', a=3.61)
atoms.calc = EMT()

# Relax both positions and cell
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)

# Vibrational analysis (finite differences)
vib = Vibrations(atoms)
vib.run()
vib_energies = vib.get_energies()   # eV, shape (3N,)

# Reference potential energy of the relaxed structure
potential_energy = atoms.get_potential_energy()

# Harmonic thermodynamics
thermo = HarmonicThermo(vib_energies=vib_energies,
                        atoms=atoms,
                        potentialenergy=potential_energy)
F = thermo.get_helmholtz_energy(temperature=300.0)

print(f'Helmholtz free energy at 300 K: {F:.6f} eV')
