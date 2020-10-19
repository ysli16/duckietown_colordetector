# duckietown_colordetector

## Execution:

build container:

`docker -H luna.local build -t colordetector .  `

run container:

`docker -H luna.local run -e N_SPLITS=10 -it --privileged colordetector`

N_SPLITS is the environment veriable indicating the number of horizontal splits of the image


## Input:

image stream captured by duckiebot

## Output:

an N_SPLITS*4 matrix, each column represents the number of the pixels in white/yellow/red/other color respectively.
