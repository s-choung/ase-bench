from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.visualize import view

# Cu 정팔면체 나노입자 생성 (fcc111 표면을 이용)
# length=5는 표면의 크기를 결정합니다.
atoms = fcc111('Cu', size=(5, 5, 1), vacuum=10.0)

# 정팔면체 모양으로 만들기 위해 추가적인 원자들을 배치합니다.
# 이 부분은 정팔면체 모양을 만들기 위한 일반적인 방법이며,
# 정확한 정팔면체 모양을 위해서는 추가적인 조정이 필요할 수 있습니다.
# 여기서는 간단하게 층을 쌓는 방식으로 근사합니다.
for i in range(1, 5):
    layer = fcc111('Cu', size=(5-i, 5-i, 1), vacuum=10.0)
    layer.translate([i*0.5, i*0.5, i*0.866]) # fcc 구조에 맞는 간격으로 이동
    atoms.extend(layer)

# EMT 계산기 설정
atoms.calc = EMT()

# 원자 수와 positions shape 출력
print(f"Number of atoms: {len(atoms)}")
print(f"Positions shape: {atoms.get_positions().shape}")

# GUI 없이 시각화 (선택 사항, 주석 처리)
# view(atoms)
