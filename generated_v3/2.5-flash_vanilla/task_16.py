from ase.build import surface
from ase.calculators.emt import EMT

# Fe BCC lattice constant
a_fe_bcc = 2.87  # Angstroms

# Fe BCC(110) 표면 생성
# size=(2,2,4)는 2x2x4 표면 단위 셀을 의미하며, 4는 층의 개수입니다.
atoms = surface(
    name='Fe',
    miller=(1, 1, 0),
    size=(2, 2, 4),
    vacuum=10.0,
    a=a_fe_bcc,
    crystalstructure='bcc'
)

# EMT 계산기 설정 (계산은 수행하지 않음)
atoms.set_calculator(EMT())

# 원자 수 출력
print(f"원자 수: {len(atoms)}")

# Cell 크기 출력
print("Cell 크기 (옹스트롬):")
print(atoms.get_cell())
