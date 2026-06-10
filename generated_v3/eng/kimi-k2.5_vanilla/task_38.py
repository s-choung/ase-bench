from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
from ase import units

atoms = bulk('Cu', cubic=True)
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

potentialenergy = atoms.get_potential_energy()
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()

vib_energies = [f * units.invcm for f in freqs if f > 1e-4]
thermo = HarmonicThermo(potentialenergy, vib_energies)
F = thermo.get_helmholtz_energy(300)
print(f"{F:.6f} eV")
