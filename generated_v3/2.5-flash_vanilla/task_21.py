from ase.build import icosahedron
from ase.calculators.emt import EMT

# Au Icosahedron 나노입자 생성 (noshells=3)
atoms = icosahedron('Au', noshells=3)

# EMT calculator 할당 (내장 calculator 사용)
atoms.calc = EMT()

# 원자 수 출력
print(f"Number of atoms: {len(atoms)}")

# Center of mass 출력
print(f"Center of mass: {atoms.get_center_of_mass()}")
