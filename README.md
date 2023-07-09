# Qiskit
Qiskit practice codes
Create a minimal environment with only Python installed in it.
python3 -m venv /path/to/virtual/environment
Activate your new environment.
source /path/to/virtual/environment/bin/activate
Note: if you are using Windows, use the following commands in PowerShell.
python3 -m venv c:\path\to\virtual\environment
c:\path\to\virtual\environment\Scripts\Activate.ps1
Next, install the Qiskit package.
pip install qiskit
If the packages were installed correctly, you can run pip list to see the active packages in your virtual environment.
If you intend to use visualization functionality or Jupyter notebooks it is recommended to install Qiskit with the extra visualization support:
pip install qiskit[visualization]
It is worth pointing out that if you’re a zsh user (which is the default shell on newer versions of macOS), you’ll need to put qiskit[visualization] in quotes:
pip install 'qiskit[visualization]'
Sign up in https://quantum-computing.ibm.com/ for analyzing through circuits and understanding Quantum gates. 
conda install -c anaconda git
pip install git+https://github.com/qiskit-community/qiskit-textbook.git#subdirectory=qiskit-textbook-src
https://quantumcomputing.stackexchange.com/questions/14096/using-the-qiskit-textbook-package
