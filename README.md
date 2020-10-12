# K-map-Simplified
Python3 program to simplify and minimise a boolean expression using K-Maps.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project only needs python3 installed on the local machine.

### Installing

To start the program:

```
python3 KMapper.py
```

When prompted type the number of variables.

```
Enter number of variabes: 3
```
Type the cells containing '1's followed by the 'Don't Care' cells as follows:
`(1,2,3,6) d(0)`  
If there are no 'Don't Care's,
`(1,2,3,6) d-`  

```
Enter Minterms and Don’t Cares: (1,2,3,6) d(0)
```
The minimized results are printed.
```
SIMPLIFIED EXPRESSIONS: w'+xy'
```

## Running the tests

Some test have been included which can be run using:
```
python3 KMapper_testing.py
```
