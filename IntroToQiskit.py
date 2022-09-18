# From: https://qiskit.org/documentation/intro_tutorial1.html


### Step 1 - Import packages
import numpy as np
from qiskit import transpile
import matplotlib.pyplot as plt

# Instructions of the quantum system
from qiskit import QuantumCircuit

# Aer high performance circuit simulator
from qiskit.providers.aer import QasmSimulator

# Creates histograms
from qiskit.visualization import plot_histogram

### Step 2 - Intialize variables
# Us Aer's qasm_simulator
simulator = QasmSimulator()

# Initialize a quantum circuit with 2 qubits in the zero state.
# The circuit acts on the q register.
circuit = QuantumCircuit(2, 2)

### Step 3 - Add gates
# Gates (operations) are added to manipulate the registers of the circuit
# The gates are added one by one to form the Bell state

# A Hadamard gate H on qubit 0.
# Puts it into a superposition state
circuit.h(0)

# A CX (CNOT) gate on control qubit 0 and target qubit 1
# CNOT is a controlled-Not operation
# Puts the qubits into an entagled state
circuit.cx(0, 1)

# Pass the entire quantum and classical registers to measure.
# The ith qubit's measurement result will be stored in the ith classical bit
# This maps the quantum measurements to the classical bits
circuit.measure([0, 1], [0, 1])

### Step 4 - Visualize the circuit
# Draw the circuit
print(circuit.draw())

# In this circuit, qubits are ordered with qubit 0 at the top and qubit 1 at the bottom
# Circuit is read left to right, so the gates that are applied earlier in the circuit show up farther to the left

### Step 5 - Simulate the experiment
# Compile the circuit down to low-level QASM instructions
# Supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(circuit, simulator)

# Execute the circuit on the qasm simulator.
job = simulator.run(compiled_circuit, shots=1000)

# Grab results from  the job
result = job.result()

# Returns counts
counts = result.get_counts(compiled_circuit)

# Each run of this circuit will yield either the bit string 00 or 11.
print("\nTotal count for 00 and 11 are:", counts)

### Step 6 - Visualize the results
# Draw a histogram
plot_histogram(counts)
