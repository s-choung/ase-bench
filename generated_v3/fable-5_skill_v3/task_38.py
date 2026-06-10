import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
BFGS(FrechetCellFilter(atoms), logfile=None).run(fmax=0.01)

vib = Vibrations(atoms, name='cu_vib')
vib.run()
vib.summary()
energies = vib.get_energies()
vib.clean()

# 허수/0에 가까운 모드(병진) 제거 후 실수 양수 모드만 사용
real_energies = np.array([e.real for e in energies if e.imag == 0 and e.real > 1e-3])
print(f"사용된 진동 모드 수: {len(real_energies)}")
print("진동 주파수 (cm^-1):", vib.get_frequencies())

thermo = HarmonicThermo(vib_energies=real_energies)
F = thermo.get_helmholtz_energy(temperature=300)
print(f"Helmholtz free energy at 300 K: {F:.6f} eV")
