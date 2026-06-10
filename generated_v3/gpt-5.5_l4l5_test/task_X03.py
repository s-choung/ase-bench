import numpy as np
from ase.build import bulk, fcc111, fcc100, fcc110
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

conv = 16.021766208

alist = np.linspace(3.45, 3.75,  nine := 9)
vols, enes = [], []

for a in alist:
    atoms = bulk("Cu", "fcc", a=a)
    atoms.calc = EMT()
    vols.append(atoms.get_volume() / len(atoms))
    enes.append(atoms.get_potential_energy() / len(atoms))

eos = EquationOfState(vols, enes)
v0, e_bulk, _ = eos.fit()
a0 = (4 * v0) ** (1 / 3)

surfaces = {
    "(111)": fcc111,
    "(100)": fcc100,
    "(110)": fcc110,
}

results = []

for name, builder in surfaces.items():
    slab = builder("Cu", size=(1, 1, 4), a=a0, vacuum=10.0)
    slab.calc = EMT()
    e_slab = slab.get_potential_energy()
    n = len(slab)
    area = np.linalg.norm(np.cross(slab.cell[0], slab.cell[1]))
    gamma = (e_slab - n * e_bulk) / (2 * area) * conv
    results.append((name, gamma))

print(f"Cu EMT bulk: a0 = {a0:.4f} Å, E_bulk = {e_bulk:.6f} eV/atom\n")
print("Surface energy:")
for name, gamma in results:
    print(f"Cu {name}: {gamma:.4f} J/m^2")

print("\nComparison:")
for name, gamma in sorted(results, key=lambda x: x[1]):
    print(f"{name}: {gamma:.4f} J/m^2")
