# MEASURE ON IMAGES

## Run and use

To run:
    
    python main.py


in V0 you have to edit the line 46, with path to your file:

    image_path = 'data/test.jpeg'

* Enter the scaling factor in terminal. 
* Draw first line (scaling line), then press enter.   
* Draw polygon around area of interest (currently there is a bug and area will not be visible until you press enter). Press enter
* Press enter again the results will be printed out in terminal (`Polygon area: 5051.5 pixels, 2061.499124607963 calibrated units`)

## Installation

Install conda -> https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html

Run

    conda install -c conda-forge opencv
    conda install numpy


## TODO

* [ ] Read file names from the input.
* [ ] If path is folder iterate over it.
* [ ] Fix green line for draw polygon not visible while drawing.
* [ ] Save measurements to file. 