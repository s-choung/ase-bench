from ase import Atoms
from ase.calculator.emt import EMT
from ase.io import write, read

# Setup Cu FCC bulk
 "\"\"\"
Cu FCC bulk structure.
单元格: 5.2 Angstrom
原子: Cu, FCC结构, 单元格原子坐标:
"""
a = 5.2
bulk = Atoms('Cu', positions=[
    [0, 0, 0],
    [0.5, 0.5, 0],
    [0.5, 0, 0.5],
    [0, 0.5, 0.5]
], cell=[[a, 0, 0], [0, a, 0], [0, 0, a]], pbc=True)

# Initialize EMT calculator
calc = EMT(bulk)

# Assign calculator
bulk.calc = calc

# Run MD for 10 steps
bulk.run('md', steps=10, trajectory='cu_md.traj')

# Read trajectory back
traj = read('cu_md.traj', index=':")
print(len(traj), 'frames')
print(traj[-1].get_total_energy())
