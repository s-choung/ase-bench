from ase.spacegroup import crystal

# NaCl 결정 구조 생성
# Na는 (0,0,0), Cl은 (0.5,0.5,0.5) 위치, spacegroup 225 (Fm-3m), 격자상수 5.64 Å
atoms = crystal(
    ('Na', 'Cl'),
    basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
    spacegroup=225,
    cellpar=5.64,
)

# 원자 수 출력
print(f"Number of atoms: {len(atoms)}")

# Chemical symbols 출력
print(f"Chemical symbols: {atoms.get_chemical_symbols()}")
