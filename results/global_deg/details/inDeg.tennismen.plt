#
# Distribution of in-degrees of nodes. G(1485, 52283). 201 (0.1354) nodes with in-deg > avg deg (70.4), 119 (0.0801) with >2*avg.deg (Thu Nov  8 20:27:23 2018)
#

set title "Distribution of in-degrees of nodes. G(1485, 52283). 201 (0.1354) nodes with in-deg > avg deg (70.4), 119 (0.0801) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'inDeg.tennismen.png'
plot 	"inDeg.tennismen.tab" using 1:2 title "" with linespoints pt 6
