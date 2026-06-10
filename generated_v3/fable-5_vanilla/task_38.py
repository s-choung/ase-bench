from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()
BFGS(atoms, logfile=None).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
vib.summary()

# 허수/0에 가까운 모드(병진 모드 등) 제거
vib_energies = [e.real for e in vib.get_energies() if e.imag == 0 and e.real > 1e-3]

thermo = HarmonicThermo(vib_energies=vib_energies,
                        potentialenergy=atoms.get_potential_energy())
F = thermo.get_helmholtz_energy(temperature=300.0)
print(f"Helmholtz free energy at 300 K: {F:.6f} eV")
