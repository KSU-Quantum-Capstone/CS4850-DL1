# CS4850-DL1
Quantum Computing Research Capstone project for CS4850

## Getting Started
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
Via JupyterLab:
  1. Open JupyterLab and navigate to the Git tab on the left hand side.
  2. If you haven't already cloned the repository, hit "Clone a Repository" and input this URL: https://github.com/KSU-Quantum-Capstone/CS4850-DL1.git
      a. If you have already cloned the repo, hit "Open the FileBrowser" and navigate to the file location you cloned the repo to.
  3. After the local repository has been set up, select the current branch to modify and push your changes to.
  NOTE: there should already be a branch with your name on it. If not, ask Ethan or Ben to create one for you.
  4. To commit changes you have made locally, hit the "+" symbol next to the file under the "Changed" dropdown menu.
  5. To push commited changes to the remote repository:
      a. First, hit the cloud symbol with the down arrow inside of it to make sure your repository is up-to-date.
        I. If there were changes pulled down, you will have to do a file compare to make sure your changes will still function properly.
      b. Once you are ready to push the changes, hit the up cloud symbol with the up arrow inside of it.
  6. Finally, when you have sufficiently completed a task, it is time to merge your changes to the Staging branch by:
      a. Go to https://github.com/KSU-Quantum-Capstone/CS4850-DL1/pulls and hit the "New Pull Request"
      b. Set the base branch to "Staging" and the compare branch to your branch
      c. Review the detected changes
      d. If everything looks good, hit "Create Pull Request", fill out the subject and comment if need be, and hit "Create Pull Request" (again).
  7. At this point you're all done. The pull request will be reviewed by Ben and/or Ethan who will reach out to you with any comments.

Note: if your code doesn't conform to [https://pypi.org/project/black/](black's) code guidelines, then each time you try to commit, it will fail. The code will then be automatically reformatted for you. Afterwards, stage your changes, commit them, and then push. If you want to prevent this from happening, format your code (assuming you are in the project's root directory) beforehand with `black ..`
