from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

opt = BFGS(atoms, trajectory='cu_bulk_opt.traj')
opt.run(fmax=0.001)

vib = Vibrations(atoms, name='cu_vib')
vib.run()
vib.summary()

vib_energies = vib.get_energies()
real_vib_energies = vib_energies[np.isreal(vib_energies) & (vib_energies.real > 0)].real

print(f"\nTotal modes: {len(vib_energies)}")
print(f"Real positive modes used for thermo: {len(real_vib_energies)}")

thermo = HarmonicThermo(vib_energies=real_vib_energies)

T = 300.0
F = thermo.get_helmholtz_energy(temperature=T, verbose=True)

print(f"\n=== Results at {T} K ===")
print(f"Helmholtz free energy F = {F:.6f} eV")

vib.clean()
