from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
import math

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT()
opt = PreconLBFGS(atoms, precon='auto')
nsteps = opt.run(fmax=0.01)
energy = atoms.get_potential_energy()
cell = atoms.cell
a, b, c = (sum(cell[i, j]**2 for j in range(3))**0.5 for i in range(3))
dot01, dot02, dot12 = (sum(cell[i, j] * cell[k, j] for j in range(3)) for i, k in [(0, 1), (0, 2), (1, 2)])
alpha = math.degrees(math.acos(dot12 / (b * c)))
beta = math.degrees(math.acos(dot02 / (a * c)))
gamma = math.degrees(math.acos(dot01 / (a * b)))

print(f"Steps: {nsteps}")
print(f"Final energy: {energy:.4f} eV")
print(f"Cell parameters: a={a:.4f} Å, b={b:.4f} Å, c={c:.4f} Å")
print(f"Cell angles: α={alpha:.2f}°, β={beta:.2f}°, γ={gamma:.2f}°")
