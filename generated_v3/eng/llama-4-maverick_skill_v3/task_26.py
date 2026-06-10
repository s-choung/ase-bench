from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()

opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

print(f"Steps: {opt.get_number_of_steps()}")
print(f"Energy: {atoms.get_potential_energy():.4f} eV")
a, b, c, alpha, beta, gamma = atoms.get_cell_lengths_and_angles()
print(f"Cell: a={a:.4f}, b={b:.4f}, c={c:.4f}, α={alpha:.2f}, β={beta:.2f}, γ={gamma:.2f}")
