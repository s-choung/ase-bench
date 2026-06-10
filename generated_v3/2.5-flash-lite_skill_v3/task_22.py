from ase.build import bulk, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# Al(111) slab 생성
al_slab = bulk('Al', 'fcc', a=4.05, cubic=True)
al_slab = al_slab.repeat((2, 2, 1)) # 더 큰 slab 생성
al_slab = al_slab.edit(cell=[[al_slab.cell[0,0], 0, 0], [0, al_slab.cell[1,1], 0], [0, 0, al_slab.cell[2,2]]]) # cell을 직교로 변경
al_slab = al_slab.repeat((1, 1, 3)) # 3층으로 쌓기
al_slab.center(vacuum=10.0, axis=2) # z축으로 vacuum 추가

# N2 분자 생성
n2 = molecule('N2')

# N2 분자를 bridge 사이트에 흡착
# Al(111) 표면에서 bridge 사이트의 대략적인 위치를 찾기 위해 slab의 첫 번째 층 원자들을 이용
surface_atoms = al_slab[[atom.index for atom in al_slab if atom.tag == 0]]
# bridge 사이트의 대략적인 위치를 계산 (두 원자 사이의 중간점)
# 여기서는 간단하게 첫 번째 층의 두 원자를 선택하여 그 중간점을 기준으로 함
# 실제로는 더 정교한 방법이 필요할 수 있음
bridge_pos = (surface_atoms[0].position + surface_atoms[1].position) / 2.0

# 흡착 위치를 slab의 z=0 평면 위로 조정
# bridge 사이트의 z 좌표를 slab의 첫 번째 층 원자들의 평균 z 좌표로 설정하고 height만큼 위로 올림
avg_z_surface = sum([atom.position[2] for atom in surface_atoms]) / len(surface_atoms)
ads_pos = [bridge_pos[0], bridge_pos[1], avg_z_surface + 2.0]

add_adsorbate(al_slab, n2, height=2.0, position=ads_pos)

# 고정할 원자 설정 (아래 2층 고정)
constraint = FixAtoms(indices=[atom.index for atom in al_slab if atom.tag < 2])
al_slab.set_constraint(constraint)

# 계산기 설정
al_slab.calc = EMT()

# 구조 최적화
opt = BFGS(al_slab)
opt.run(fmax=0.05)

# 최종 구조의 원자 수와 종류 출력
print(f"Number of atoms: {len(al_slab)}")
print(f"Atom types: {al_slab.get_chemical_symbols()}")
