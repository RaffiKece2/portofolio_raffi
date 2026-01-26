import matplotlib.pyplot as plt
from qiskit import  QuantumCircuit

qc = QuantumCircuit(5,5)


for superposisi in range(10):
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    qc.h(4)

qc.cx(2,4)
qc.cx(3,4)
qc.cx(1,4)
qc.cx(0,4)
qc.measure([0,1,2,3,4],[0,1,2,3,4])
qc.draw('mpl')
plt.show()

