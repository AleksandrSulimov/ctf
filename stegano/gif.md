https://ctf-wiki.mahaloz.re/misc/picture/gif/

split each frame of the GIF file
`ffmpeg -i cake.gif cake-%d.png`

print the time interval of each frame
`identify -format "%s %T \n" 100.gif`
