# MolGen: Molecular Generator

## Description
MolGen is a GUI-based program designed to generate molecules based on user-defined criteria and visualize them using the RDKit library. It allows users to specify a base molecule (in SMILES format) and add functional groups at specific atom indices. The generated molecule's properties such as molecular weight, LogP, number of hydrogen bond donors, and acceptors are displayed alongside a visual representation of the molecule.

## Features
- **Input Fields:**
  - **Base SMILES:** Input field for entering the SMILES notation of the base molecule.
  - **Functional Groups:** Input field for specifying functional groups to add to the molecule. Each functional group is defined by its SMILES notation and the atom index where it should be attached.
  - **Desired Properties:** Fields to input desired LogP, sigma, pi, hydrogen bond acceptors (HBA), and hydrogen bond donors (HBD).

- **Output:**
  - **Generated Molecule:** SMILES representation of the generated molecule.
  - **Molecular Properties:** Display of molecular weight, LogP, number of hydrogen bond donors, and acceptors.
  - **Structure Visualization:** Visual representation of the generated molecule using RDKit and PIL libraries.

## Usage
1. **Base SMILES:** Enter the SMILES notation of the base molecule.
2. **Functional Groups:** Specify functional groups using SMILES notation followed by the atom index where each should be attached. Multiple groups are separated by commas.
3. **Desired Properties:** Optionally, specify desired LogP, sigma, pi, HBA, and HBD values to guide molecule generation.

## Functionality
- The program validates input SMILES and functional groups, displaying errors if invalid.
- It generates a molecule by sequentially adding specified functional groups to the base molecule.
- The resulting molecule's properties are calculated and displayed.
- The molecule's structure is visualized within the GUI for easy inspection.

## Dependencies
- Python libraries required: `tkinter`, `rdkit`, `PIL`.

## Installation
- Ensure Python is installed on your system.
- Install required libraries:
  ```bash
  pip install tkinter rdkit Pillow

## Execution
- Run the script `molgen.py` in your Python environment.
- The GUI window will open, allowing you to interactively generate and view molecules.

## Disclaimer
MolGen is a demonstration program and may not cover all edge cases or complex molecular structures. Use with appropriate understanding of chemistry and molecular modeling.

## Author
Created by Mihir Hurwanth
## Contact Information
- **LinkedIn:** [Mihir Hurwanth](https://www.linkedin.com/in/mihirhurwanth/)
- **Email:** mhurwanth@gmail.com


## License
This program is licensed under the MIT license. See LICENSE file for details.
