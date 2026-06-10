```python
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.units import invcm

# CH4 분자 구조 생성 및 계산기 설정
atoms = molecule('CH4')
atoms.calc = EMT()

# 구조 최적화 수행
optimizer = BFGS(atoms)
optimizer.run(fmax=0.01)
