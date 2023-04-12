---
layout: page
title: Running the Circuit
permalink: /docs/running-circuit/
parent: Docs
nav_order: 2
---

# Running the Circuit

Note: these instructions have been tested on Windows and MacOS but not on Linux. They should work however, some modifications may be necessary.

You will have needed to install the dependencies. See the [instructions here if not done already](getting-started).

1. In your Anaconda prompt on Windows or terminal on Mac/Linux activate the anaconda environment with `conda activate quantum`
2. Navigate to the location on your computer where you would like the code to be. Use the `cd` command. For example, if you want to store it in a documents directory use the command `cd ~/documents`.
3. Clone the repository with the command `git clone https://github.com/KSU-Quantum-Capstone/CS4850-DL1.git`
4. Go into the repository with the command `cd CS4850-DL1`
5. Start the Jupyter server with `jupyter lab`. This should open the repository in your browser.
6. Create a new file inside of the folder called `ibmqID.py`
7. Inside of this file, paste `token = INSERT IBM API TOKEN HERE`
8. Retrieve your API token from [https://quantum-computing.ibm.com/account](https://quantum-computing.ibm.com/account). An IBM Quantum account is required. Replace "INSERT IBM API TOKEN HERE" with your actual IBM API token.
9. Open ALU.py inside of the Jupyter server.
10. You are then able to run code by hitting the run button or selecting Run->Run All Cells.
11. Alternatively, you are able to run the code in your favorite IDE as one file, instead of running it in a Jupyter server.
12. To close the server, press `Ctrl+C` inside of your /Anaconda prompt/terminal. Then press `y` to confirm.
