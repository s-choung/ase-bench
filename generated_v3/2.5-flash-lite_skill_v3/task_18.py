from ase.build import molecule
from ase.data import atomic_numbers
from ase.neighborlist import NeighborList

# G2 데이터베이스에서 CH4 분자 가져오기
ch4 = molecule('CH4')

# 원자 좌표 출력
print("Atom positions:")
for atom in ch4:
    print(f"  {atom.symbol}: {atom.position}")

# Bond lengths 계산 및 출력
nl = NeighborList(
    natural_cutoffs(ch4.get_cell(), ch4.get_atomic_numbers()),
    self_interaction=False,
    bothways=True,
)
nl.update(ch4)

print("\nBond lengths (C-H):")
for i, atom in enumerate(ch4):
    if atom.symbol == 'C':
        for j in atom.index:
            if ch4[j].symbol == 'H':
                dist = ch4.get_distance(i, j)
                print(f"  C-{j} (H): {dist:.4f} Å")

# Chemical formula 출력
print(f"\nChemical formula: {ch4.get_chemical_formula()}")
