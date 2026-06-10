from ase.build import fcc111
from ase.calculators import EMT, LJ
from ase.geometry import Point, Molecule
from ase.io import write
import numpy as np

def equilibrium_cu_fcc():
    """
    Finds the equilibrium lattice constant of Cu FCC bulk using EOS fitting.
    """
    # Create a Cu FCC bulk
    cell = fcc111('Cu', size=(4, 4, 4))

    # Set the cell parameter to an initial guess
    a0 = 3.615
    cell.a = a0

    # Set the calculator
    calc = EMT()
    cell.calc = calc

    # Run the calculation
    cell.get_atomic_equations_of_state()

    # Get the EOS parameters
    P, V = cell.eos

    # Fit the EOS to find the equilibrium volume and bulk modulus
    # Using a simple linear fit for demonstration
    V_eq = V[0]
    B = 1 / (P[1] - P[0])

    print(f"Equilibrium Volume: {V_eq} Å")
    print(f"Bulk Modulus: {B} GPa")

if __name__ == '__main__':
    equilibrium_cu_fcc()
