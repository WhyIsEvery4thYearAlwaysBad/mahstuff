# My accel curve graphed in GNU Plot.

# Window stuff
set title "Amic's Linear Accel Curve"
set key box
set xlabel "Velocity (mickey)"
set ylabel "Output Sens"
set xrange [0:*] noreverse writeback
set yrange [0:*] noreverse writeback
# Vars
accel=1.9 # 19/10
# x = Distance.
plot [0:*] x title "Input Velocity", x*accel title "Output Sens"
NO_ANIMATION=1
