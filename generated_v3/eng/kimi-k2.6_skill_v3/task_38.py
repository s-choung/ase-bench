from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)

e_pot = atoms.get_potential_energy()
vib = Vibrations(atoms)
vib.run()
vib_energies = [e for e in vib.get_energies() if e > 1e-3]

thermo = HarmonicThermo(vib_energies, electronicenergy=e_pot)
F = thermo.get_free_energy(temperature=300)

print(f'Helmholtz free energy at 300 K: {F:.4f} eV')
