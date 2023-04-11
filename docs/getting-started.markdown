---
layout: page
title: Initial Setup
permalink: /docs/initial-setup/
parent: Docs
nav_order: 1
---

# Getting Started

Note: these instructions have been tested on Windows and MacOS but not on Linux. They should work however, some modifications may be necessary.

## Prerequisites Installation

1. Install anaconda from: https://www.anaconda.com/
2. Once installed, in your Anaconda Prompt on Windows or terminal on Mac, run the command `conda list` to test your installation. If it's installed correctly, a list of installed packages will appear. If you run into trouble visit: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation
3. Run the command `conda create --name quantum python=3.10` to create a new conda environment call "quantum" with a Python 3.10 installation.
4. Activate the environment with `conda activate quantum`.
5. Install JupyterLab, the JupyterLab git extension, pre-commit, and black with `conda install -c conda-forge jupyterlab jupyterlab-git pre-commit black`.
6. Install Qiskit with `pip install qiskit` for quantum computing development.
7. Install visualization support for Qiskit with `pip install qiskit[visualization]`. If this doesn't work it may be because use are using zsh, which is the default on newer MacOS systems. Use this command instead `pip install 'qiskit[visualization]'`. Note the extra quotes.
8. To deactivate your current conda environment use the command `conda deactivate`.

You are now ready to run the circuit. See the [instructions here for next steps](circuit).
