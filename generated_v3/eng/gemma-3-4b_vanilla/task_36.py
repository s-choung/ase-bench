from ase.build import fcc111
from ase.calculators.eam import EamImplicitVasp
from ase.constraints import FixAtoms
from ase.io import write
from ase.optimize import Lbfgs
from ase.calculators.emt import EMT
from ase.gaussians import Gaussian
import numpy as np

def birch_murnaghan_eos(energies, pressures=None):
    a = np.linspace(0, 1.0, 100)
    E = np.poly1d(np.array(energies[::-1]))
    if pressures is None:
        pressures = np.array([E[i] - E[i-1] for i in range(1, len(E))])
    return a, E, pressures

def fit_eos(energies, pressures):
    a, E, pressures = birch_murnaghan_eos(energies, pressures)
    b = np.roots(E)[0]
    return a, b


def main():
    # Build Ag FCC lattice
    atoms = fcc111('Ag', size=(4, 4, 4), a=4.09)
    constraints = FixAtoms(indices=[range(len(atoms))])
    atoms.set_constraint(constraints)

    # Define lattice constant range
    a_min = 4.00
    a_max = 4.05
    a_values = np.linspace(a_min, a_max, 7)

    # Calculate energies for each lattice constant
    energies = []
    for a in a_values:
        atoms.cell *= a
        calculator = EamImplicitVasp(alloy=True, element_valence=1, prec='Accurate',
                                    kpts=(4, 4, 4), lreal='Auto')
        atoms.calc = calculator
        atoms.get_potential_energy()
        energies.append(atoms.get_potential_energy())

    # Fit EOS
    a, b = fit_eos(energies, np.array([energies[i+1] - energies[i] for i in range(len(energies)-1)]))

    # Calculate equilibrium lattice constant and bulk modulus
    equilibrium_a = a[np.argmin(np.abs(a - a_values[0]))]
    bulk_modulus = 2*np.pi**2 * (b**2 - b**2 / (equilibrium_a**2))
    bulk_modulus_GPa = bulk_modulus * 1e6

    # Print results
    print("Equilibrium lattice constant:", equilibrium_a, "Angstroms")
    print("Bulk modulus:", bulk_modulus_GPa, "GPa")

if __name__ == '__main__':
    main()
