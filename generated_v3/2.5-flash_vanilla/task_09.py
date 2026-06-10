import os
from ase.build import bulk
from ase.io import write, read
from ase.calculators.emt import EMT

a_cu = 3.61
cu_bulk = bulk('Cu', 'fcc', a=a_cu)
cu_bulk.calc = EMT()

poscar_filename = 'POSCAR'
write(poscar_filename, cu_bulk, format='vasp')
print(f"'{poscar_filename}' 파일이 성공적으로 저장되었습니다.")

read_cu_bulk = read(poscar_filename, format='vasp')
print(f"'{poscar_filename}' 파일이 성공적으로 읽혔습니다.")

print(f"\n읽어온 구조의 원자 수: {len(read_cu_bulk)}")

cell_lengths_angles = read_cu_bulk.get_cell_lengths_and_angles()
print(f"읽어온 구조의 Cell parameters (a, b, c, alpha, beta, gamma):")
print(f"  a = {cell_lengths_angles[0]:.3f} Å")
print(f"  b = {cell_lengths_angles[1]:.3f} Å")
print(f"  c = {cell_lengths_angles[2]:.3f} Å")
print(f"  alpha = {cell_lengths_angles[3]:.2f} degrees")
print(f"  beta  = {cell_lengths_angles[4]:.2f} degrees")
print(f"  gamma = {cell_lengths_angles[5]:.2f} degrees")
