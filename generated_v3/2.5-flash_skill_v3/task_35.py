```python
from ase import Atoms
from ase.calculators.emt import EMT
from ase.mep import NEB
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# 초기 상태 정의: Al 원자 두 개 사이에 세 번째 Al 원자가 위치
initial = Atoms('Al3',
                positions=[(0, 0, 0),
                           (1.0, 0, 0),
                           (5.0, 0, 0)],
                cell=(10, 10, 10),
                pbc=True)
initial.calc = EMT()
# 양 끝의 Al 원자 고정
initial.set_constraint(FixAtoms(indices=[0, 2]))

# 최종 상태 정의: 세 번째 Al 원자가 다른 위치로 이동
final = initial.copy()
final
