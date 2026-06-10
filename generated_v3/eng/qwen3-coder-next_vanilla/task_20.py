from ase import Atoms
from ase.lattice import Nanotube

# Create (6,6) carbon nanotube with length=4 (in unit cells)
cnt = Nanotube(symbol='C', structure='armchair', 
               tuple=(6, 6), length=4, 
               unit='angstrom')

# Print number of atoms and cell information
print(f"Number of atoms: {len(cnt)}")
print("Cell info:")
print(f"  a={cnt.cell[0,0]:.3f} Å, b={cnt.cell[1,1]:.3f} Å, c={cnt.cell[2,2]:.3f} Å")
print(f"  Cell angles: alpha={cnt.cell[1,2]/cnt.cell[1,1]*90:.1f}°, beta={cnt.cell[0,2]/cnt.cell[0,0]*90:.1f}°, gamma={cnt.cell[0,1]/cnt.cell[0,0]*90:.1f}°")
print(f"  Volume: {cnt.cell.volume:.1f} Å³")
