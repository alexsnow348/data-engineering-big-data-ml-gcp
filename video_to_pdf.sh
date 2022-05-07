#!/bin/bash
read -p 'video_path: ' video_path

find $video_path  -type f -name '*.webm' -exec sh -c '
  for file do
    # transfrom to image
    ffmpeg -i ${file}  -vf  fps=0.3 out%d.png
    # transfrom to pdf
    convert `find -type f -name "*.png" | sort -V` ${file}.pdf
    # detele all images files
    rm -f *.png
    # delete the video file
    rm -f ${file}
  done
' exec-sh {} +

# combine all pdf files
pdfunite *.pdf all.pdf