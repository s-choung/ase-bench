from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.geometry import get_distances
from scipy.optimize import curve_fit
import numpy as np

def eos_fit(volumes, energies, guess_bulk_modulus):
    def murnaghan(V, E0, B0, BP, V0):
        return E0 + B0*V/BP*((V0/V)**BP/((BP-1)*V0/V + 1) - 1) + B0*V0/(BP-1)
        
    params, _ = curve_fit(murnaghan, volumes, energies, p0=[energies.min(), guess_bulk_modulus, 4.0, volumes[np.argmin(energies)]])
    return params[1], params[2]

def calculate_properties(material, metals):
    results = {}
    for metal in metals:
        print(f"Processing {metal}...")
        a = 4.05 if metal == 'Cu' else 4.17 if metal == 'Ag' else 4.08
        fcc = bulk(metal, 'fcc', a=a)
        pressures = []
        total_energies = []
        for i, cell in enumerate(np.linspace(0.8, 1.2, 21)):
            cell = atom.cell.copy()
            cell *= cell.diag() * cell.diag() * cell.diag()  # Cubic cell
            cell[0][0] = cell[1][1] = cell[2][2] = cell.diagonal()[0] * cell[i]
            fcc.set_cell(cell, scale_atoms=True)
            fcc.calc = EMT()
            fcc.get_potential_energy()
            pressures.append(-1 * fcc.get_stress(as_dict=True)['xx'] * len(fcc) / 6)
            total_energies.append(fcc.get_potential_energy())
        
        energies = np.array(total_energies)
        vol = fcc.get_volume()
        volumes = vol / (cell.diagonal()[0] ** 3) * np.array([cell.diagonal()[0] ** 3 for cell in cell])
        
        bulk_modulus, equilibrium_volume = eos_fit(volumes, energies, 100.0)
        lattice_constant = vol ** (1. / 3.) / nsites
        results[metal] = {"Lattice Constant (Å)": lattice_constant, "B0 (GPa)": bulk_modulus * 0.1}
    
    print("{:<10} {:<20} {:<10}".format("Metal", "Lattice Constant (Å)", "B0 (GPa)"))
    for material, properties in results.items():
        print("{:<10} {:<20} {:<10}".format(material, round(properties["Lattice Constant (Å)"], 4),
                                             round(properties["B0 (GPa)"], 2)))

metals = ['Cu', 'Ag', 'Au']
calculate_properties(None, metals)
