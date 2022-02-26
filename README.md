# Degree Dynamics
Proof of time evolution of the Barabasi-Albert model.
## Works
Python implementation of the model was made. 

## Formulas
![](https://latex.codecogs.com/svg.image?\frac{\partial&space;k_i}{\partial&space;t}&space;\propto&space;\prod&space;(k_i)&space;=&space;A\frac{k_i}{\sum_j&space;k_j}) <br/>
![](https://latex.codecogs.com/svg.image?\sum_j&space;k_j&space;=&space;2mt) <br/>
![](https://latex.codecogs.com/svg.image?A&space;=&space;m)<br/>
![](https://latex.codecogs.com/svg.image?\frac{\partial&space;k_i}{\partial&space;t}&space;=&space;\frac{k_i&space;m}{2mt}&space;=&space;\frac{k_i}{2t})<br/>
![](https://latex.codecogs.com/svg.image?\frac{\partial&space;k_i}{k_i}&space;=&space;\frac{\partial&space;t}{2t})<br/>
![](https://latex.codecogs.com/svg.image?\int_{m}^{k}&space;\frac{\partial&space;k_i}{k_i}&space;=&space;\int_{t_i}^{t}&space;\frac{\partial&space;t}{2t}) <br/>
![](https://latex.codecogs.com/svg.image?ln(\frac{k}{m})&space;=&space;\frac{1}{2}&space;ln(\frac{t}{t_i})&space;=&space;ln((\frac{t}{t_i})^{\frac{1}{2}})) <br/>
![](https://latex.codecogs.com/svg.image?k_i(t)&space;=&space;m&space;(\frac{t}{t_i})^{\beta},&space;\beta&space;=&space;\frac{1}{2}) <br/>
Using the equation above, the degree of the node over time can be estimated.

## Usage
Simply run the code of "degree_dynamics.py". Before running, create a folder named "gif". To make "out.gif" file, uncomment the line start with "gif()" in the main in the code. 

## Output


