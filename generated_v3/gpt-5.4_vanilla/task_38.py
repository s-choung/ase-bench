import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms.calc = EMT()

BFGS(atoms, logfile=None).run(fmax=0.01)

vib = Vibrations(atoms, name='cu_bulk_vib')
vib.run()

energies = vib.get_energies()
freqs = vib.get_frequencies()

print('Vibrational frequencies (eV):')
for e in energies:
    if np.isfinite(e):
        print(float(np.real(e)))

thermo = HarmonicThermo(vib_energies=[float(np.real(e)) for e in energies if np.isfinite(e)])
F = thermo.get_helmholtz_energy(temperature=300.0, verbose=False)

print('Helmholtz free energy at 300 K (eV):')
print(float(F))

vib.clean()
