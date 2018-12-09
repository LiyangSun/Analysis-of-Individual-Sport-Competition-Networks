#
# Distribution of in-degrees of nodes. G(350, 595). 48 (0.1371) nodes with in-deg > avg deg (3.4), 18 (0.0514) with >2*avg.deg (Sat Dec  8 19:10:33 2018)
#

set title "Distribution of in-degrees of nodes. G(350, 595). 48 (0.1371) nodes with in-deg > avg deg (3.4), 18 (0.0514) with >2*avg.deg"
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
set output 'inDeg.fencing_men_foil.png'
plot 	"inDeg.fencing_men_foil.tab" using 1:2 title "" with linespoints pt 6
