from ase.build import bulk
from ase.io import read, write
from ase.calculators.emt import EMT

# ---------- Build bulk Cu ----------
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)   # EMT calculator가 자동 연결됨

# ---------- Save to VASP POSCAR (format='vasp' 옵션) ----------
write('Cu.bulk', atoms, format='vasp')        # 문자열 관례: Cu.bulk.vasp

# ---------- Read back ----------
read_atoms = read('Cu.bulk', format='vasp')

# ---------- Print info ----------
print(f'Number of atoms: {read_atoms.get_number_of_atoms()}')
a, b, c, alpha, beta, gamma = read_atoms.get_cell_lengths_and_angles()
print(f'Cell (Å): a={a:.3f}, b={b:.3f}, c={c:.3f}, α={alpha:.3f}°')
