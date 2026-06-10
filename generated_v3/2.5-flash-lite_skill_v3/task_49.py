from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# 1. Cu FCC bulk의 격자상수를 EOS로 구하기
a_initial = 3.6  # 초기 추정값
atoms_bulk = bulk('Cu', 'fcc', a=a_initial)
atoms_bulk.calc = EMT()

cell = atoms_bulk.get_cell()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    atoms_eos = atoms_bulk.copy()
    atoms_eos.set_cell(cell * x, scale_atoms=True)
    atoms_eos.calc = EMT()
    volumes.append(atoms_eos.get_volume())
    energies.append(atoms_eos.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
lattice_constant = v0**(1/3)

print(f"Calculated lattice constant: {lattice_constant:.4f} Å")

# 2. 구한 격자상수로 (111) slab 4층 만들기
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, a=lattice_constant)
slab.calc = EMT()

# 3. 하부 2층 고정
constraint = FixAtoms(mask=[atom.tag < 2 for atom in slab])
slab.set_constraint(constraint)

# 4. BFGS로 표면 relaxation
optimizer = BFGS(slab)
optimizer.run(fmax=0.05)

# 5. 최종 에너지와 각 layer의 z 좌표 평균 출력
final_energy = slab.get_potential_energy()

z_coords = slab.get_positions()[:, 2]
layer_heights = np.unique(z_coords)
layer_avg_z = {}
for height in layer_heights:
    layer_atoms = slab[[atom.tag for atom in slab if np.isclose(atom.position[2], height)]]
    layer_avg_z[height] = np.mean(layer_atoms.get_positions()[:, 2])

print(f"Final potential energy: {final_energy:.4f} eV")
print("Average z-coordinate for each layer:")
for height, avg_z in sorted(layer_avg_z.items()):
    print(f"  Layer at z={height:.4f}: {avg_z:.4f} Å")
