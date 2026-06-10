from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

def main():
    # Initial structure
    atoms = bulk('Cu', 'fcc', a=3.5)
    atoms.calc = EMT()

    # Print initial state
    print(f'Initial cell: {atoms.get_cell_lengths_and_angles()}')
    print(f'Initial energy: {atoms.get_potential_energy()} eV')

    # Optimize
    opt = BFGS(FrechetCellFilter(atoms))
    opt.run(fmax=0.01)

    # Print final state
    print(f'Optimized cell: {atoms.get_cell_lengths_and_angles()}')
    print(f'Optimized energy: {atoms.get_potential_energy()} eV')

if __name__ == '__main__':
    main()
