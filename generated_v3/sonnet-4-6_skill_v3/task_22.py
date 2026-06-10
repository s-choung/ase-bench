from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

n2 = molecule('N2')

add_adsorbate(slab, n2, height=2.0, position='bridge')

slab.calc = EMT()
opt = BFGS(slab, trajectory='al111_n2.traj')
opt.run(fmax=0.05)

print(f"총 원자 수: {len(slab)}")
symbols = slab.get_chemical_symbols()
unique = sorted(set(symbols))
for s in unique:
    print(f"  {s}: {symbols.count(s)}개")
