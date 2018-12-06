#
# Distribution of in-degrees of nodes. G(270, 630). 54 (0.2000) nodes with in-deg > avg deg (4.7), 12 (0.0444) with >2*avg.deg (Thu Nov  8 21:06:46 2018)
#

set title "Distribution of in-degrees of nodes. G(270, 630). 54 (0.2000) nodes with in-deg > avg deg (4.7), 12 (0.0444) with >2*avg.deg"
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
set output 'inDeg.fencing.png'
plot 	"inDeg.fencing.tab" using 1:2 title "" with linespoints pt 6
