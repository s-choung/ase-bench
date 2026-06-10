from ase.build import bulk
from ase.io import write, read

nacl = bulk('NaCl', crystalstructure='rocksalt', a=5.64)
write('nacl.cif', nacl)

atoms = read('nacl.cif')
print(f"원자 수: {len(atoms)}")
print(f"원자 종류: {atoms.get_chemical_symbols()}")
print(f"화학식: {atoms.get_chemical_formula()}")
print(f"격자 상수 a: {atoms.cell.lengths()[0]:.4f} Å")

try:
    from ase.spacegroup import get_spacegroup
    sg = get_spacegroup(atoms)
    print(f"Space group: {sg.symbol} (No. {sg.no})")
except Exception as e:
    print(f"Spacegroup 분석 오류: {e}")
