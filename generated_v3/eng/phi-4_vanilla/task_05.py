from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.optimize import ChainOfPrimitiveCell
from sklearn.linear_model import LinearRegression
import numpy as np

def find_equilibrium():
    # Define a range of lattice constants around known value for Cu (3.61 Å)
    lattice_constants = np.linspace(3.51, 3.71, 5)
    
    # Create Cu bulk structure for each lattice constant
    copper = bulk('Cu', 'fcc', 1)
    cu_fcc = copper.copy()
    energies = []
    volumes = []

    for a in lattice_constants:
        cu_fcc.set_cell([a, a, a])
        cu_fcc.set_pbc((True, True, True))
        lr = LinearRegression()
        
        regression_data_volume = []
        regression_data_energy = []

        # Use EMT calculator for each lattice constant
        molp = EMT(cu_fcc, label='locp')
        molp.get_potential_energy()
        energies.append(molp.results.total_energy)
        volumes.append(cu_fcc.get_volume())

    # Fit energies vs volumes using linear regression
    volumes = np.array(volumes).reshape(-1, 1)
    energies = np.array(energies).reshape(-1, 1)
    lr.fit(volumes, energies)
    slope_cache = -3 * lr.coef_[0, 0] / 2
    intercept_cache = energies[0][0] - lr.coef_[0, 0] * volumes[0][0]

    # Find equilibrium volume
    equilibrium_volume = -intercept_cache / slope_cache

    # Calculate corresponding equilibrium lattice constant
    for a in lattice_constants:
        if abs(cu_fcc.get_volume() - equilibrium_volume) < 1e-5:
            equilibrium_lattice_constant = a
            break

    # Calculate bulk modulus
    bulk_modulus = slope_cache / equilibrium_volume

    print(f'Equilibrium volume: {equilibrium_volume} Å^3')
    print(f'Equilibrium lattice constant: {equilibrium_lattice_constant} Å')
    print(f'Bulk modulus: {bulk_modulus} eV/Å^3')

find_equilibrium()
