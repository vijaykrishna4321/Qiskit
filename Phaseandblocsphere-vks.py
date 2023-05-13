#!/usr/bin/env python
# coding: utf-8

# In[2]:
#https://qiskit.org/documentation/getting_started.html 
#Create a minimal environment with only Python installed in it.python3 -m venv /path/to/virtual/environment
#Activate your new environment source /path/to/virtual/environment/bin/activate
# For Windows python3 -m venv c:\path\to\virtual\environment c:\path\to\virtual\environment\Scripts\Activate.ps1 
# Install Qiskit in a commmand/shell pip install qiskit
# pip install 'qiskit[Visualization]'
from qiskit import*
from qiskit.tools.visualization import plot_bloch_multivector
from qiskit.visualization import plot_histogram
get_ipython().run_line_magic('matplotlib', 'inline')
import math
# In[3]:
Aer.backends()
# qasm_simulator = Aer.get_backend('qasm_simulator')
# statevector_simulator = Aer.get_backend('statevector_simulator')
# In[5]:
qasm_simulator = Aer.get_backend('qasm_simulator') 
statevector_simulator = Aer.get_backend('statevector_simulator')
# In[6]:
def run_on_simulators(circuit):
    statevec_job = execute(circuit, backend=statevector_simulator)
    result = statevec_job.result()
    statevec = result.get_statevector()
    
    num_qubits = circuit.num_qubits
    
    circuit.measure([i for i in range(num_qubits)],[i for i in range(num_qubits)])
    qasm_job =execute(circuit, backend=qasm_simulator, shots=1024).result()
    counts = qasm_job.get_counts()
    return statevec, counts


# In[7]:


circuit = QuantumCircuit(2,2)
statevec, counts = run_on_simulators(circuit)


# In[8]:


plot_bloch_multivector(statevec)


# In[9]:


plot_histogram([counts])


# In[10]:


circuit.h(0)
statevec,counts = run_on_simulators(circuit)
plot_bloch_multivector(statevec)


# In[11]:


plot_histogram([counts])


# In[12]:


circuit = QuantumCircuit(2,2)
circuit.h(0)
circuit.cx(0,1)
statevec, counts = run_on_simulators(circuit)
plot_bloch_multivector(statevec)


# In[13]:


plot_histogram([counts])


# Phase is a property of a quantum state that determines the probability of finding the state in a particular measurement. In simpler terms, it's like the position of a needle on a compass that tells you which way you're facing.
# 
# Now, the Bloch sphere is a way to visualize the state of a qubit (quantum bit) in three dimensions. Think of it like a globe with a point on it. The point represents the state of the qubit, and the globe represents all possible states of the qubit.
# 
# For one qubit, the point can be anywhere on the surface of the sphere. But for two qubits, the point is located in a four-dimensional space that's difficult to visualize. However, we can still use the Bloch sphere to represent the two qubits by using two spheres and connecting them together.
# 
# One way to think about it is to imagine two people standing on opposite sides of the globe. Each person represents a qubit, and their position on the globe represents the state of their qubit. The connection between the two people represents the entanglement between the two qubits.
# 
# Now, let's bring it back to phase. On the Bloch sphere, phase is represented by rotating the point around the surface of the sphere. This is like turning the needle on a compass to face a different direction. By changing the phase of a qubit, we can change the probability of finding the qubit in a particular measurement.
# 
# So, for two qubits, we can use the Bloch sphere to represent the state of both qubits and how they're connected. And we can use phase to manipulate the probability of finding the qubits in a particular measurement.
# In[17]:
circuit = QuantumCircuit(2,2)
circuit.rx(math.pi/4,0)
circuit.rx(math.pi/2,1)
statevec, counts = run_on_simulators(circuit)
plot_bloch_multivector(statevec)
# In[18]:
plot_histogram([counts])
# In[20]:
circuit = QuantumCircuit(1,1)
circuit.h(0)
statevec, counts = run_on_simulators(circuit)
plot_bloch_multivector(statevec)
# In[21]:
circuit = QuantumCircuit(1,1)
circuit.h(0)
circuit.z(0)
statevec, counts = run_on_simulators(circuit)
plot_bloch_multivector(statevec)
# In[32]:
circuit = QuantumCircuit(3,3)
circuit.h(0)
circuit.z(0)
circuit.t(0)
circuit.h(1)
circuit.z(1)
circuit.h(2)
circuit.z(2)
circuit.cx(1,0)
circuit.cx(2,1)
statevec, counts = run_on_simulators(circuit)
plot_bloch_multivector(statevec)
# In[27]:
plot_histogram([counts])




