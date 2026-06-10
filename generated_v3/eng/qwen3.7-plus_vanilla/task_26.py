from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

print(f"Steps: {len(opt)}")
print(f"Final Energy: {atoms.get_potential_energy():.6f} eV")
print("Cell Parameters:\n", atoms.get_cell())
