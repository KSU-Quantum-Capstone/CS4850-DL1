---
layout: page
title: Getting Started
permalink: /getting-started/
---

# Getting Started

### Prerequisites Installation

1. Install anaconda from: https://www.anaconda.com/
2. Once installed, in your Anaconda Prompt on Windows or terminal on Mac, run the command `conda list` to test your installation. If it's installed correctly, a list of installed packages will appear. If you run into trouble visit: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation
3. Run the command `conda create --name quantum python=3.10` to create a new conda environment call "quantum" with a Python 3.10 installation.
4. Activate the environment with `conda activate quantum`.
5. Install JupyterLab, the JupyterLab git extension, pre-commit, and black with `conda install -c conda-forge jupyterlab jupyterlab-git pre-commit black`.
6. Install Qiskit with `pip install qiskit` for quantum computing development.
7. Install visualization support for Qiskit with `pip install qiskit[visualization]`. If this doesn't work it may be because use are using zsh, which is the default on newer MacOS systems. Use this command instead `pip install 'qiskit[visualization]'`. Note the extra quotes.
8. To deactivate your current conda environment use the command `conda deactivate`.

### Setting Up Pre-Commit Hooks

1. Open your terminal/command prompt and activate your conda environment with `conda activate quantum`.
2. Clone the repository with `git clone https://github.com/KSU-Quantum-Capstone/CS4850-DL1.git`.
3. Navigate into the git repository on your local computer with the `cd` command.
4. Once you are in `.../CS4850-DL1/`, use the command `pre-commit install`. This will set up the pre-commit hooks (which are used for formatting code).
5. Lastly, run the command `pre-commit run --all-files` which will run the hooks on all of the files. If it says FAILED, see the note in the Git Workflow section below. If you get the error `ImportError: DLL load failed while importing _ctypes`, try removing your conda environment and restarting from getting started step 3.

### Git Workflow

TODO

Note: if your code doesn't conform to [https://pypi.org/project/black/](black's) code guidelines, then each time you try to commit, it will fail. The code will then be automatically reformatted for you. Afterwards, stage your changes, commit them, and then push. If you want to prevent this from happening, format your code (assuming you are in the project's root directory) beforehand with `black ..`

### Using GitHub Pages

1. Create a new anaconda environment used specifically for the gh-pages branch `conda create --name gh-pages`
2. Activate the new environment with `conda activate gh-pages`
3. Install the necessary anaconda packages `conda install -c conda-forge c-compiler compilers cxx-compiler ruby`
4. Install jekyll and bundler `gem install jekyll bundler`
5. Clone the repository with `git clone https://github.com/KSU-Quantum-Capstone/CS4850-DL1.git`.
6. Navigate into the git repository on your local computer with the `cd` command. 4. Once you are in `.../CS4850-DL1/`,
7. Switch to the gh-pages branch `git checkout gh-pages`
8. Install the bundle's prerequisites `bundle install`
9. Start the jekyll server `bundle exec jekyll serve`
10. End the server with `ctrl+c`
