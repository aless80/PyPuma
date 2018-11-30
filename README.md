## Description
Implementation of the Puma algorithm. Python code based on the Panda implementation pypanda from [https://github.com/QuackenbushLab/pypanda](https://github.com/QuackenbushLab/pypanda) and [https://github.com/davidvi/pypanda](https://github.com/davidvi/pypanda).  

<!--## TODO
Review formulas  
Review Results on the bottom of this README  
Figure
-->

## Table of Contents
* [Links to literature](#links-to-literature)
* [Puma algorithm](#puma-algorithm)  
* [Installation](#installation)  
* [Usage](#usage)  
  * [Run from terminal](#run-from-terminal)
  * [Run from python](#run-from-python)
* [Toy data](#toy-data)
* [Results](#results)


## Links to literature 

* **[PUMA](https://static-content.springer.com/esm/art%3A10.1186%2Fs13045-017-0465-4/MediaObjects/13045_2017_465_MOESM3_ESM.pdf)** (PANDA Using MicroRNA Associations)  
_Manuscript in preparation, used in [PUMA](https://static-content.springer.com/esm/art%3A10.1186%2Fs13045-017-0465-4/MediaObjects/13045_2017_465_MOESM3_ESM.pdf)._  
C and MATLAB code: [https://github.com/mararie/PUMA](https://github.com/mararie/PUMA)

* **[PANDA](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0064832)** Passing Attributes between Networks for Data Assimilation  
_Glass K, Huttenhower C, Quackenbush J, Yuan GC. Passing Messages Between Biological Networks to Refine Predicted Interactions, PLoS One, 2013 May 31;8(5):e64832_  
Original PANDA C++ code: [http://sourceforge.net/projects/panda-net/](http://sourceforge.net/projects/panda-net/).  

* **[LIONESS](https://arxiv.org/abs/1505.06440)** (Linear Interpolation to Obtain Network Estimates for Single Samples)   
_Marieke Lydia Kuijjer, Matthew Tung,GuoCheng Yuan,John Quackenbush, Kimberly Glass. Estimating sample-specific regulatory networks_  

LIONESS can be used to estimate single-sample networks using aggregate networks made with any network reconstruction algorithm (http://arxiv.org/pdf/1505.06440.pdf).

## Puma algorithm
<img src="img/puma.png" height="300">  

To find agreement between the three input networks first the responsibility (R) is calculated.  

<img src="img/responsibility.png" height="30">  

Thereafter availability (A) is calculated.  

<img src="img/availability.png" height="30">  

Availability and responsibility are combined with the following formula.  

<img src="img/combine.png" height="30">  

Protein cooperativity and gene co-regulatory networks are updated.  

<img src="img/cooperativity.png" height="30">  
<img src="/img/co-regulatory.png" height="30">  

P and C are updated to satisfy convergence.  

<img src="img/p.png" height="30">  
<img src="/img/c.png" height="30">  

Hamming distance is calculated every iteration.  

<img src="img/hamming.png" height="40">  


## Installation
PyPuma runs on Python 2.7. We recommend the following commands to install PyPuma on UNIX systems:
#### Using  a virtual environment
Using [python virtual environments](http://docs.python-guide.org/en/latest/dev/virtualenvs/) is the cleanest installation method. 

Cloning git and setting up a [python virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/):
```no-highlight
pip install --user pipenv   #Make sure you have pipenv
git clone https://github.com/aless80/PyPuma.git
cd PyPuma
```
Creating a virtual environment and installing pypanda:
```no-highlight
virtualenv pypumaenv #virtual environment created in a folder inside the git folder 
source pypumaenv/bin/activate
(pypumaenv)$ pip install -r requirements.txt
(pypumaenv)$ python setup.py install
```
Uninstall pypanda from virtual environment:
```no-highlight
cat files.txt | xargs rm -rf
```
Complete removal of virtual environment and pypanda:
```no-highlight
(pypuma)$ deactivate	#Quit virtual environment
rm -rf pypumaenv
```

#### Using pip 
Never use ~~sudo pip~~. Instead you can use pip on the user's install directory:
```no-highlight
git clone https://github.com/aless80/PyPuma.git
cd PyPuma
python setup.py install --user
#to run from the command line you will need to make PyPuma executable and add the bin directory to your PATH:
cd bin
chmod +x PyPuma
echo "$(pwd):PATH" >> ~/.bashrc
source ~/.bashrc
```
To run PyPuma from Windows (not fully tested) install Git (https://git-scm.com/downloads) and Anaconda Python2.7 (https://www.continuum.io/downloads) and from the Anaconda prompt run:
```no-highlight
git clone https://github.com/aless80/PyPuma.git
cd PyPuma
python setup.py install
```

## Usage
#### Run from terminal
PyPuma can be run directly from the terminal with the following options:
```
-h help
-e, --expression: expression values
-m, --motif: pair file of motif edges, or Pearson correlation matrix when not provided 
-p, --ppi: pair file of PPI edges
-o, --output: output file
-i, --mir: mir data miR file
-r, --rm_missing
-q, --lioness: output for Lioness single sample networks 
```
To run PyPuma on toy data:
```
python run_puma.py -e ./ToyData/ToyExpressionData.txt -m ./ToyData/ToyMotifData.txt -p ./ToyData/ToyPPIData.txt -o output_puma.txt -i ./ToyData/ToyMiRList.txt

TODO:
python run_puma.py -e ./ToyData/ToyExpressionData.txt -m ./ToyData/ToyMotifData.txt -p ./ToyData/ToyPPIData.txt -o output_puma.txt -i ./ToyData/ToyMiRList.txt -q output_lioness.txt
```
To reconstruct a single sample Lioness Pearson correlation network:
<!--```
pypuma -e ToyData/ToyExpressionData.txt -o output_puma_pearson.txt -q output_lioness_pearson.txt
```-->
```python
TODO:
python run_puma.py -e ./ToyData/ToyExpressionData.txt -m ./ToyData/ToyMotifData.txt -p ./ToyData/ToyPPIData.txt -o output_puma.txt -q output_lioness.txt
TODO:
python run_puma.py -e ./ToyData/ToyExpressionData.txt -m ./ToyData/ToyMotifData.txt -p ./ToyData/ToyPPIData.txt -i ToyData/ToyMiRList.txt -o test_puma.txt -q output_lioness.txt
```
#### Run from python
Fire up your python shell or ipython notebook. 
Import the classes in the PyPuma library:
```python
from pypuma.puma import Puma
from pypuma.lioness import Lioness
```
Run the Puma algorithm, leave out motif and PPI data to use Pearson correlation network:
```python
puma_obj = Puma('ToyData/ToyExpressionData.txt', 'ToyData/ToyMotifData.txt', 'ToyData/ToyPPIData.txt','ToyData/ToyMiRList.txt')
```
Save the results:
```python
puma_obj.save_puma_results('Toy_Puma.pairs.txt')
```
Return a network plot:

```python
puma_obj.top_network_plot(top=70, file='top_genes.png')
```
<!--
or
```python
from PyPuma.analyze_puma import AnalyzePuma
plot = AnalyzePuma(puma_obj)
plot.top_network_plot(top=100, file='top_100_genes.png')
```-->
Calculate indegrees for further analysis:
```python
indegree = puma_obj.return_puma_indegree()
```

Calculate outdegrees for further analysis:
```python
outdegree = puma_obj.return_puma_outdegree()
```
Run the Lioness algorithm for single sample networks:
```python
lioness_obj = Lioness(puma_obj)
```
Save Lioness results:
```python
lioness_obj.save_lioness_results('Toy_Lioness.txt')
```
Return a network plot for one of the Lioness single sample networks:
```python
plot = AnalyzeLioness(lioness_obj)
plot.top_network_plot(column= 0, top=100, file='top_100_genes.png')
```

## Toy data
The example gene expression data that we have available here contains gene expression profiles for different samples in the columns. Of note, this is just a small subset of a larger gene expression dataset. We provided these "toy" data so that the user can test the method. 

However, if you plan to model gene regulatory networks on your own dataset, you should use your own expression data as input.

## Results

TODO 
```
Example Puma output:
TF  Gene  Motif Force
---------------------
CEBPA	AACSL	0.0	-0.951416589143
CREB1	AACSL	0.0	-0.904241609324
DDIT3	AACSL	0.0	-0.956471642313
E2F1	AACSL	1.0	3.6853160511
EGR1	AACSL	0.0	-0.695698519643

Example lioness output:
Sample1 Sample2 Sample3 Sample4
-------------------------------
-0.667452814003	-1.70433776179	-0.158129613892	-0.655795512803
-0.843366539284	-0.733709815256	-0.84849895139	-0.915217389738
3.23445386464	2.68888472802	3.35809757371	3.05297381396
2.39500370135	1.84608635425	2.80179804094	2.67540878165
-0.117475863987	0.494923925853	0.0518448588965	-0.0584810456421

TF, Gene and Motif order is identical to the puma output file.
```
