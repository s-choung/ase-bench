import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = {}

for metal in metals:
    # FCC bulk 생성
    atoms = bulk(metal, 'fcc', a=4.0)  # 초기 격자상수는 임의로 설정
    atoms.calc = EMT()

    # EOS 피팅을 위한 볼륨 및 에너지 계산
    cell = atoms.get_cell()
    volumes, energies = [], []
    for x in np.linspace(0.95, 1.05, 11):  # 평형 격자상수 주변 11개 포인트
        a = atoms.copy()
        a.set_cell(cell * x, scale_atoms=True)
        a.calc = EMT()  # 각 볼륨마다 계산기 재설정
        volumes.append(a.get_volume())
        energies.append(a.get_potential_energy())

    # EOS 피팅
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()

    # 결과 저장
    results[metal] = {'equilibrium_lattice_constant': v0**(1/3), 'bulk_modulus': B}

# 결과 테이블 출력
print("Metal | Equilibrium Lattice Constant (Å) | Bulk Modulus (GPa)")
print("------|---------------------------------|-------------------")
for metal, data in results.items():
    eq_a = data['equilibrium_lattice_constant']
    bulk_mod = data['bulk_modulus'] / units.GPa  # GPa 단위로 변환
    print(f"{metal:<5} | {eq_a:>30.4f} | {bulk_mod:>17.2f}")
