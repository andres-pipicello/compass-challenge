# compass-challenge

## Quickstart

```bash
# create a virtualenv
python -m venv .venv

# activate it (unix-like system)
source .venv/bin/activate

# activate it (Windows)
.venv\Scripts\activate

# install requirements
pip install -r requirements.txt

  # run the script
python main.py


```

## Using poetry

The project is configured using [`poetry`](https://python-poetry.org/). This requires to install an extra tool if not installed already. 
To avoid having to install it if not necessary/preferred, a requirements.txt file is included.

If you decide to use it, use the following commands
```bash
poetry install

poetry run pytest
```

## Design decisions

The solution is very loosely based on the [Fellegi-Sunter](https://courses.cs.washington.edu/courses/cse590q/04au/papers/Felligi69.pdf) model for Record Linkage, that I happened to implement some years ago. 
In this model, set of difference functions is chosen for the learning algorithm to learn their outputs probabilities. Of course, in this implementation, no learning was done, and all difference functions have the same image.

Part of the process for model construction would be to learn the hyperparameters related to the decision logic. I decided to choose a set of arbitrary but intuitive values.

While the scores computed from the difference functions seem to be probabilities, how they are used go against all rules and laws of probability theory (e.g. they are added and averaged). The original Fellegi-Sunter model computes correct probabilities.