import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'xtick.labelsize': 14,
                     'ytick.labelsize': 14,
                     'font.size': 14})

plt.rc("axes", linewidth=1.5)
plt.rc("lines", markeredgewidth=1.5)

data = np.loadtxt("single_level.txt")

nodes = data[:,0]
MPI = data[:,1]
OMP = data[:,2]
time = data[:,3]

num_threads = MPI*OMP

plt.scatter(nodes, time, label="coarse level only")
plt.plot(nodes, nodes[0]/nodes*time[0], ls=":")


data = np.loadtxt("one_amr.txt")

nodes = data[:,0]
MPI = data[:,1]
OMP = data[:,2]
time = data[:,3]

num_threads = MPI*OMP

plt.scatter(nodes, time, label="coarse + 1 AMR level")
plt.plot(nodes, nodes[0]/nodes*time[0], ls=":")

plt.xlim(10, 256)

plt.xlabel("# of nodes", fontsize="medium")
plt.ylabel(r"avg time to update step", fontsize="medium")

plt.legend(frameon=False, loc=3)

ax = plt.gca()
ax.set_xscale("log")
ax.set_yscale("log")

threads_per_node = 68*4
ax2 = ax.twiny()
ax2.set_xlim(10*threads_per_node, 256*threads_per_node)
ax2.set_xlabel("# of threads")

ax = plt.gca()
plt.text(0.95, 0.95, "Castro KNL scaling (wdmerger)", 
         fontsize="small", horizontalalignment="right", transform = ax.transAxes)


f = plt.gcf()
f.set_size_inches(8, 6)

plt.tight_layout()
plt.savefig("cori_scaling.pdf", dpi=150, bbox_inches="tight")
