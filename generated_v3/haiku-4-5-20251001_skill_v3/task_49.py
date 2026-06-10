import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.eos import EquationOfState

# Step 1: EOS로 Cu FCC 격자상수 구하기
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    atoms = bulk('Cu', 'fcc', a=3.6)
    atoms.set_cell(atoms.get_cell() * x, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_opt = (4 * v0) ** (1/3)
print(f"Optimized lattice constant: {a_opt:.4f} Å")

# Step 2: (111) slab 4층 생성
slab = fcc111('Cu', size=(3, 3, 4), a=a_opt, vacuum=10.0)
print(f"Slab atoms: {len(slab)}")

# Step 3: 하부 2층 고정 (tag 기반)
z_coords = slab.get_positions()[:, 2]
z_min = z_coords.min()
z_max = z_coords.max()
z_threshold = z_min + 0.4 * (z_max - z_min)
mask = z_coords < z_threshold
slab.set_constraint(FixAtoms(mask=mask))
print(f"Fixed atoms: {mask.sum()}")

# Step 4: EMT calculator 설정 및 BFGS relaxation
slab.calc = EMT()
opt = BFGS(slab, trajectory='slab_relax.traj')
opt.run(fmax=0.05)

# Step 5: 최종 에너지 및 layer별 z 좌표 평균 출력
final_energy = slab.get_potential_energy()
print(f"\nFinal energy: {final_energy:.6f} eV")

positions = slab.get_positions()
z_coords = positions[:, 2]
z_sorted = np.sort(np.unique(np.round(z_coords, 2)))

print("\nLayer-wise z-coordinate averages:")
for i, z_layer in enumerate(z_sorted, 1):
    mask_layer = np.abs(z_coords - z_layer) < 0.1
    z_avg = z_coords[mask_layer].mean()
    print(f"Layer {i}: {z_avg:.4f} Å")
