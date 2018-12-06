#
# Distribution of out-degrees of nodes. G(963, 29581). 172 (0.1786) nodes with out-deg > avg deg (61.4), 75 (0.0779) with >2*avg.deg (Thu Nov  8 20:27:46 2018)
#

set title "Distribution of out-degrees of nodes. G(963, 29581). 172 (0.1786) nodes with out-deg > avg deg (61.4), 75 (0.0779) with >2*avg.deg"
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
set output 'outDeg.tenniswomen.png'
plot 	"outDeg.tenniswomen.tab" using 1:2 title "" with linespoints pt 6
