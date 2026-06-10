from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.units import GPa
import numpy as np

# Al FCC 2x2x2 supercell 생성
atoms = bulk('Al', 'fcc', a=4.05, cubic=True)
atoms = atoms.repeat((2, 2, 2))

# EMT calculator 설정
atoms.calc = EMT()

# 초기 cell volume
initial_volume = atoms.get_volume()
print(f"Initial cell volume: {initial_volume:.4f} Ang^3")

# 10 GPa를 eV/Ang^3로 변환
pressure_gpa = 10
pressure_ev_ang3 = pressure_gpa * GPa

# NPTBerendsen MD 설정 (500K, 10 GPa)
dyn = NPTBerendsen(atoms, 
                   timestep=1.0,
                   temperature_K=500,
                   externalstress=pressure_ev_ang3,
                   taut=0.1,
                   taup=1.0,
                   mask=[1, 1, 1, 0, 0, 0])

# 100 스텝 MD 실행
dyn.run(100)

# 최종 cell volume
final_volume = atoms.get_volume()
print(f"Final cell volume: {final_volume:.4f} Ang^3")
print(f"Volume change: {final_volume - initial_volume:.4f} Ang^3 ({(final_volume/initial_volume - 1)*100:.2f}%)")
