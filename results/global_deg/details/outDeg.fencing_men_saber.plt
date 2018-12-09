#
# Distribution of out-degrees of nodes. G(226, 527). 23 (0.1018) nodes with out-deg > avg deg (4.7), 0 (0.0000) with >2*avg.deg (Sat Dec  8 19:10:29 2018)
#

set title "Distribution of out-degrees of nodes. G(226, 527). 23 (0.1018) nodes with out-deg > avg deg (4.7), 0 (0.0000) with >2*avg.deg"
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
set output 'outDeg.fencing_men_saber.png'
plot 	"outDeg.fencing_men_saber.tab" using 1:2 title "" with linespoints pt 6
