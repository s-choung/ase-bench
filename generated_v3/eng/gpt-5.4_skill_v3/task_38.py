from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

BFGS(FrechetCellFilter(atoms), logfile=None).run(fmax=0.01)

vib = Vibrations(atoms, name='cu_bulk_vib')
vib.run()
freqs = vib.get_frequencies()
energies = vib.get_energies()
vib.clean()

vib_energies = [e.real for e in energies if abs(e.imag) < 1e-8 and e.real > 1e-12]
thermo = HarmonicThermo(vib_energies=vib_energies, potentialenergy=atoms.get_potential_energy())
F = thermo.get_helmholtz_energy(temperature=300.0)

print("Vibrational frequencies (cm^-1):")
for f in freqs:
    print(f)
print(f"Helmholtz free energy at 300 K: {F:.6f} eV")
