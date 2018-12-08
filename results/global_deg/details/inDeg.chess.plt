#
# Distribution of in-degrees of nodes. G(6832, 36387). 953 (0.1395) nodes with in-deg > avg deg (10.7), 396 (0.0580) with >2*avg.deg (Thu Nov  8 20:26:35 2018)
#

set title "Distribution of in-degrees of nodes. G(6832, 36387). 953 (0.1395) nodes with in-deg > avg deg (10.7), 396 (0.0580) with >2*avg.deg"
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
set output 'inDeg.chess.png'
plot 	"inDeg.chess.tab" using 1:2 title "" with linespoints pt 6
