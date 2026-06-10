from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT()

opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

print(f"Steps: {opt.nsteps}")
print(f"Energy: {atoms.get_potential_energy():.4f} eV")
print(f"Cell:\n{atoms.cell}")
