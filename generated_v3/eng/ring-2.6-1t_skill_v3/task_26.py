from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

# create Ni fcc bulk (experimental lattice constant ~3.52 Å)
atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT()

# optimize with PreconLBFGS and automatic preconditioner
opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

# output
print('Steps:', opt.nsteps)
print('Final energy (eV):', atoms.get_potential_energy())
a, b, c, alpha, beta, gamma = atoms.get_cell_lengths_and_angles()
print(f'Cell parameters: a={a:.4f} b={b:.4f} c={c:.4f} '
      f'α={alpha:.2f} β={beta:.2f} γ={gamma:.2f}')
