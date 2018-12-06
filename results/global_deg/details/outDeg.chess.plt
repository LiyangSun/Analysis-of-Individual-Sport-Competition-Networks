#
# Distribution of out-degrees of nodes. G(6832, 36387). 998 (0.1461) nodes with out-deg > avg deg (10.7), 210 (0.0307) with >2*avg.deg (Thu Nov  8 20:26:03 2018)
#

set title "Distribution of out-degrees of nodes. G(6832, 36387). 998 (0.1461) nodes with out-deg > avg deg (10.7), 210 (0.0307) with >2*avg.deg"
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
set output 'outDeg.chess.png'
plot 	"outDeg.chess.tab" using 1:2 title "" with linespoints pt 6
