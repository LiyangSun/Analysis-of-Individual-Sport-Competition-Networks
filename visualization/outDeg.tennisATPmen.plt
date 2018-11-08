#
# Distribution of out-degrees of nodes. G(1485, 52283). 245 (0.1650) nodes with out-deg > avg deg (70.4), 126 (0.0848) with >2*avg.deg (Wed Nov  7 15:01:25 2018)
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
set output 'outDeg.tennisATPmen.png'
plot 	"outDeg.tennisATPmen.tab" using 1:2 title "" with linespoints pt 6
