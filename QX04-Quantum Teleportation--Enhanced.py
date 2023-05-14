#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import*
from qiskit.tools.visualization import plot_bloch_multivector
from qiskit.visualization import plot_histogram
get_ipython().run_line_magic('matplotlib', 'inline')
import math


# In[2]:


Aer.backends()


# In[3]:


qasm_simulator = Aer.get_backend('qasm_simulator')
statevector_simulator = Aer.get_backend('statevector_simulator')


# In[4]:


def run_on_simulators(circuit):
    statevec_job = execute(circuit, backend=statevector_simulator)
    result = statevec_job.result()
    statevec = result.get_statevector()
    
    num_qubits = circuit.num_qubits
    
    circuit.measure([i for i in range(num_qubits)],[i for i in range(num_qubits)])
    qasm_job =execute(circuit, backend=qasm_simulator, shots=1024).result()
    counts = qasm_job.get_counts()
    return statevec, counts


# In[5]:


circuit = QuantumCircuit(3,3)
circuit.x(0)
circuit.barrier()
circuit.h(1)
circuit.cx(1,2)
circuit.barrier()
circuit.draw(output ='mpl')


# In[6]:


statevec, counts = run_on_simulators(circuit)


# In[7]:


plot_bloch_multivector(statevec)


# In[11]:


circuit.cx(0,1)
circuit.h(0)
circuit.barrier()
circuit.draw(output='mpl')


# In[8]:


statevec, counts = run_on_simulators(circuit)
plot_bloch_multivector(statevec)


# In[9]:


plot_histogram([counts])


# In[10]:


circuit.measure([0,1],[0,1])
circuit.barrier()
circuit.draw(output='mpl')


# In[11]:


circuit.cx(1,2)
circuit.cz(0,2)
circuit.measure([2],[2])
circuit.draw(output = 'mpl')


# In[15]:


plot_histogram([counts])


# In[16]:


statevec, counts = run_on_simulators(circuit)
plot_bloch_multivector(statevec)


# In[ ]:




