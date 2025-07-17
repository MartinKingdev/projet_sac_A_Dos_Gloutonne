# Greedy Knapsack Problem Solver

This project implements several greedy approaches to solve the Knapsack Problem using data from Excel or CSV files.

## Features

- Reads knapsack data from Excel (`.xlsx`) or CSV (`.csv`) files
- Three greedy strategies:
  - Selection by highest value
  - Selection by lowest weight
  - Selection by highest value-to-weight ratio
- Displays selected items, total value, and total weight for each approach
- Automatically determines the best greedy solution

## Main Files

- [`knapsack_Problem.py`](knapsack_Problem.py): Main script and class implementation
- `donnees_sac_a_dos1.xlsx`, `donnees_sac_a_dos2.xlsx`, `donnees_sac_a_dos3.csv`: Data files

## Usage

1. Install dependencies:

```sh
pip install pandas
```

2. Place your data files in the project folder.

3. Run the main script:

```sh
python knapsack_Problem.py
```

4. Results for each approach and each file will be displayed in the console.

## Example

The main class is [`sac_Dos_approche_gloutonne`](knapsack_Problem.py):

```python
from knapsack_Problem import sac_Dos_approche_gloutonne

knapsack = sac_Dos_approche_gloutonne(typeDeFichier='csv', fichier='donnees_sac_a_dos3.csv', max_Weight=900)
knapsack.SolutionOptimal()
```

## Author

Project by Bonaventure DANFI.
