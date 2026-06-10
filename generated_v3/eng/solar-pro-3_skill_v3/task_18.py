from ase.optimize import BFGS
from ase.build import molecule
from ase.calculators.emt import EMT

# 1. Build CH4 from the G2 database (ASE builds H2O, CO2, CH4, NH3, C60, etc.)
ch4 = molecule('CH4')                     # default geometry (see‑saw)

# 2. Attach a calculator for later optimization
ch4.calc = EMT()

# 3. Optimize the geometry (force convergence 0.05 eV/Å)
opt = BFGS(ch4, trajectory='ch4_opt.traj')
opt.run(fmax=0.05)

# 4. Print required information
print('Formula :', ch4.formula)
print('Coordinates (Å):')
for i, atom in enumerate(ch4):
    print(f'  {ch4.atomtypes[i][0]} ({i}): {atom.position}')
print('Bond lengths (Å):')
for i in range(len(ch4) - 1):
    bond = get_distances(ch4, i, i+1)
    print(f'  {ch4.atomtypes[i][0]}–{ch4.atomtypes[i+1][0]}: {bond[0][0]:.3f}')
