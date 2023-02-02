# Formal Regression
A new method for regression on the polynomial function that makes up the data.

## 1. Introduce

From a minimum number of points (including coordinates and values) of a polynomial function. We can use them to regress to the original equation. 

<p align="center">
<img src="https://user-images.githubusercontent.com/96680644/216259217-ee335dc9-c6c8-4fb9-9f2c-a72536eec1f7.png" alt="drawing" width="800"/>
</p>


This algorithm works on the principle of the canonical equation of the [Hit Sum Function](https://github.com/Truongphi20/sumfor#introduction-to-the-hit-sum-function). When a canonical calculation is performed once, the degree of the function will decrease by one order. Continue execution until the result consists of only the same constants. Take the 'outermost' values and do the calculation with the Hit Sum function by [The polynomial function generating algorithm](https://github.com/Truongphi20/sumfor), the result is the initial function of the data.


## 2. Usage

### 2.1 Download and check up

To download the tool, select ``Code > Zip Download`` on Github page or type in Command Prompt on Windows or Terminal on other operating systems as follows:
    
    git clone https://github.com/Truongphi20/FormalRegression.git
    
For checking, move the terminal's working directory to the downloaded "FormalRegression" directory (`cd FormalRegression`).
    
    python  .\forre.py  -h
    
Output:

    usage: forre.py [-h] [-f INPUT] [-v] [-m MATRIX]

    optional arguments:
      -h, --help            show this help message and exit
      -f INPUT, --input INPUT
                            input file contain points
      -v, --version         show version
      -m MATRIX, --matrix MATRIX
                            Display the Minimalist Matrix, yes (y) or no (n)?

The syntax to run the algorithm is:

    forre.py -f <input file> [-m y]
    
The input file is a txt file containing the points $(x,y)$ of the function (an example of an input file is ex_input.txt). If you want to display the Minimalist Matrix, use the `-m y` tag.

### 2.2 Example

For example, we need to find a polynomial function that passes through points with coordinates $(x,y)$ as follows:

$$(0.1,-0.199), (0.7,-1.057), (1,-1), (1.1,-0.869), (0.8,-1.088)$$

First, create an input file containing points like  `ex_input.txt`. Next, run the algorithm with the following command:

    python  .\forre.py  -f .\ex_input.txt
    
Output:
    
    Formal Formula:
     -2.0*x^1+1.0*x^3

So the regression equation is: $f(x) = x^3-2x$ 

If you want to display [the Minimalist Matrix](#32-establish-the-minimalist-matrix):

    python  .\forre.py  -f .\ex_input.txt -m y
    
Output:

    Minimalist Matrix:
              0.7       0.8 0.9     1.0       1.1
    0  -143/1000  -31/1000      11/250  131/1000
    1                4/125        1/20    29/500
    2                            3/500     3/500



    Formal Formula:
     -2.0*x^1+1.0*x^3
     

## 3. Algorithm explanation
### 3.1 The canonical equation of Hit Sum Function

The Hit Sum function, $g(x)$, always has the following form:
    
$$\left. {{S_n}} \right|_a^bf(x) = g(x)$$

Once we know $f(x)$, we use the Hit Sum function to find $g(x)$. Conversely, when we know $g(x)$, we will use the canonical equation to find $f(x)$:

$$f(x) = g(x) - g(x-n)$$

For brevity, we can call $f(x)$ the inner function and $g(x)$ the outer function. The Hit Sum function and the above canonical equation are the relationships between $g(x)$ and $f(x)$. 

### 3.2 Establish the Minimalist Matrix

### 3.3 Use the Hit Sum Function to Regression
