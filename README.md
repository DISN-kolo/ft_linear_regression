# ft_linear_regression
42's linear regression task

## Objective
Given a dataset of car mileages and their prices, estimate a function that preditcs the price by a given mileage.

## Installing
1. `python -m venv venv` for the first run
2. both then and in every subsequent run `source venv/bin/activate`
3. if this is the first run, `pip install -r requirements.txt`
4. done working? `deactivate`

## Usage
1. (Optional) Generate some data using the `./data_generator.py`.
2. Run the `./trainer.py <data.csv> [thetas]` to train the model. The results will be saved to the specified thetas file (if not specified, to `thetas`).
3. Run the `./estimator.py <data.csv> <thetas>` and enter your desired inputs in order to estimate the price.
4. (Optional) Visualize the results and data using `data_visualizer.py <data.csv> [thetas]`.

## Licensing

- [LICENSES/LICENSE-MIT](LICENSES/LICENSE-MIT) for the project
