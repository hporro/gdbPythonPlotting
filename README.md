gdbPythonPlotting is a repository to show how to make plotting commands for gdb debbugging C++ applications, using gdb's python API and Plotly shapes.

## Requirements 

This app requires requires gdb version > 8.0 (may be 7.something, it just requires gdb.Values load structure fields as dictionary entries). It also requires Python 3.X and Plotly installed.

## Usage

First thing, you have to compile the example programm a.cpp with the -g flag. There is a Makefile to make this step easier.

```bash
make
`````

Then you have to use gdb to debugg the compiled file. The .gdbinit file in the repository makes shure that the plottGraph.py file gets executed and that a breakpoint in a.cpp 16'th line is placed. To execute it just type in a console:

```bash
gdb a.out
`````

Then run the programm in gdb (r command), and when it reaches the breakpoint you can use the PlotTriangle command defined in plottGraph.py with the local variable t as argument (PlotTriangle t).


```bash
(gdb) r
(gdb) PlotTriangle t
`````

Your browser should display an image similar to the following:

![triangle](https://github.com/hporro/gdbPythonPlotting/blob/master/resources/triangle.png)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
````
````
