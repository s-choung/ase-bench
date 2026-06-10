from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.io import write
import numpy as np

# Cu FCC bulk 생성
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)

# EMT calculator 설정
atoms.calc = EMT()

# 초기 에너지 계산
E_initial = atoms.get_total_energy()
print(f"Initial total energy: {E_initial:.6f} eV")

# 초기 온도 300K로 velocity 설정
T_init = 300
kb = 8.617333262e-5  # eV/K
v_rms = np.sqrt(3 * kb * T_init / atoms.get_masses().mean())
atoms.set_velocities(np.random.randn(len(atoms), 3) * v_rms)

# NVE MD (VelocityVerlet) 50스텝
md = VelocityVerlet(atoms, dt=1.0, trajectory='md_nve.traj')
md.run(50)

# 최종 에너지 계산
E_final = atoms.get_total_energy()
print(f"Final total energy: {E_final:.6f} eV")
print(f"Energy difference: {E_final - E_initial:.6f} eV")
print(f"Energy conservation error: {abs(E_final - E_initial) / abs(E_initial) * 100:.4f} %")
