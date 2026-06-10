from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

# Build Ni fcc bulk
atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()

# Preconditioned LBFGS optimizer (auto preconditioner)
opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

# Results
steps = opt.nsteps
energy = atoms.get_potential_energy()
cell = atoms.get_cell()

print(f'Steps: {steps}')
print(f'Final energy (eV): {energy:.6f}')
print('Cell vectors (Å):')
for vec in cell:
    print('  ', ' '.join(f'{x: .6f}' for x in vec))
