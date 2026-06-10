from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

def calculate_adsorption_energy(structure):
    calc = EMT()
    structure.calc = calc
    return structure.get_potential_energy()

def main():
    bulk_pt = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
    slab = bulk_pt.copy()
    
    sites = ['ontop', 'bridge', 'fcc']
    adsorption_energies = []

    for site in sites:
        structure = slab.copy()
        add_adsorbate(structure, 'OH', height=2.0, position='on', site=site)
        
        constraint = FixAtoms(mask=[atom.index for atom in structure if atom.tag == 1])
        structure.set_constraint(constraint)
        
        energy = calculate_adsorption_energy(structure)
        adsorption_energies.append(energy)

    min_energy = min(adsorption_energies)
    min_index = adsorption_energies.index(min_energy)

    print(f"Ontop energy: {adsorption_energies[0]} eV")
    print(f"Bridge energy: {adsorption_energies[1]} eV")
    print(f"Fcc hollow energy: {adsorption_energies[2]} eV")
    print(f"Lowest energy: {min_energy} eV at {sites[min_index]} site")

if __name__ == "__main__":
    main()
