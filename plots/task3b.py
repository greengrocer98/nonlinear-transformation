# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.backends.backend_pgf import FigureCanvasPgf
mpl.backend_bases.register_backend('pdf', FigureCanvasPgf)
pgf_with_latex = {
    "pgf.texsystem": "xelatex",         # use Xelatex which is TTF font aware
}

mpl.rcParams.update(pgf_with_latex)
plt.rc('text', usetex=True)
plt.rc('font', family='serif', serif = 'CMU Serif', size = 12)
plt.rcParams['text.latex.preamble'] = [
            r'\usepackage{amsmath}',
            r'\usepackage{amsfonts}',
            r'\usepackage{mathtext}',
            r'\usepackage{graphicx}',
            r'\usepackage[russian]{babel}',
            r'\usepackage[utf8]{inputenc}',
            r'\usepackage[T1]{fontenc}',
            ]

data = np.genfromtxt('experiment3.csv', delimiter=';')

fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111)
ax.plot(data[4,1:],data[3,1:],color='#FF7800',marker='o',lw=1,ms=2, label=r'$R_1C_1$')
ax.errorbar(data[4,1:],data[3,1:],yerr=4,fmt='.',color='#FF7800')
ax.plot(data[7,1:],data[6,1:],color='#133CAC',marker='o',lw=1,ms=2, label=r'$R_2C_2$')
ax.errorbar(data[7,1:],data[6,1:],yerr=4,fmt='.',color='#133CAC')
ax.set_ylabel(r'$V$, mv')
ax.set_xlabel(r'$f$, kHz')
ax.grid()
ax.legend(loc=5)
plt.savefig('exp3b.pdf')