from ase import bulk
from ase.calculators.emt import EMT
from ase.constraints import StrainFilter
from ase.optimize import BFGS

atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()

a0 = atoms.get_volume()**(1/3)
e0 = atoms.get_potential_energy()
print(f"Initial lattice constant: {a0:.6f} Å")
print(f"Initial energy: {e0:.6f} eV")

sf = StrainFilter(atoms)
opt = BFGS(sf)
opt.run(fmax=0.01)

a = atoms.get_volume()**(1/3)
e = atoms.get_potential_energy()
print(f"Optimized lattice constant: {a:.6f} Å")
print(f"Final energy: {e:.6f} eV")
