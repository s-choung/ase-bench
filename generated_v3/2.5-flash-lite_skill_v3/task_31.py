from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

# Al FCC 2x2x2 supercell 생성
atoms = bulk('Al', 'fcc', a=4.05, cubic=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

# NPT Berendsen MD 설정
temperature_K = 500
pressure_GPa = 10.0
pressure_eV_Ang3 = pressure_GPa * units.GPa / units.Bohr**3 * units.angstrom**3 # GPa -> eV/Ang^3 변환

md_steps = 100
timestep = 5 * units.fs

# 초기 cell volume 출력
initial_volume = atoms.get_volume()
print(f"Initial cell volume: {initial_volume:.2f} Å³")

# MD 실행
dyn = NPTBerendsen(atoms, timestep=timestep, temperature_K=temperature_K,
                   pressure_GPa=pressure_eV_Ang3,
                   ttime=0.5*units.fs, ptime=2.0*units.fs) # ttime, ptime는 예시 값

dyn.run(md_steps)

# 최종 cell volume 출력
final_volume = atoms.get_volume()
print(f"Final cell volume: {final_volume:.2f} Å³")
