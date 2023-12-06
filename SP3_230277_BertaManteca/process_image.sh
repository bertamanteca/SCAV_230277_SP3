#!/bin/bash

ffmpeg -i messi.png -vf "scale=640:480" output.jpg

ffmpeg -i output.jpg -vf "format=gray" grayscale_output.jpg

ffmpeg -i grayscale_output.jpg -vf "transpose=1" rotated_output.jpg

ffmpeg -i rotated_output.jpg -i messi.png -filter_complex "overlay=W-w-10:H-h-10" final_output.jpg

echo "Image processing complete!"
