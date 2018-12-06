#
# Distribution of out-degrees of nodes. G(1485, 52283). 245 (0.1650) nodes with out-deg > avg deg (70.4), 126 (0.0848) with >2*avg.deg (Thu Nov  8 20:27:23 2018)
#

set title "Distribution of out-degrees of nodes. G(1485, 52283). 245 (0.1650) nodes with out-deg > avg deg (70.4), 126 (0.0848) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Out-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'outDeg.tennismen.png'
plot 	"outDeg.tennismen.tab" using 1:2 title "" with linespoints pt 6
