import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import ExpCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk("Cu", "fcc", cubic=True)
atoms.calc = EMT()

BFGS(ExpCellFilter(atoms), logfile=None).run(fmax=1e-4)

vib = Vibrations(atoms, name="cu_bulk_vib")
vib.run()

vib_energies = vib.get_energies()
vib.clean()

vib_energies = np.array([e.real for e in vib_energies if abs(e.imag) < 1e-8 and e.real > 1e-5])

thermo = HarmonicThermo(
    vib_energies=vib_energies,
    potentialenergy=atoms.get_potential_energy()
)
F = thermo.get_helmholtz_energy(temperature=300.0, verbose=False)

print("Vibrational energies (eV):")
for e in vib_energies:
    print(f"{e:.8f}")

print(f"Helmholtz free energy at 300 K (eV): {F:.8f}")
