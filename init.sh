#!/bin/bash
src_dir="`dirname \"$0\"`"              # relative path
src_dir="`( cd \"$src_dir\" && pwd )`"  # absolutized and normalized path

ln -snf $src_dir/i3 ~/.i3
ln -snf $src_dir/dunstrc ~/.config/dunstrc
ln -snf $src_dir/Xresources ~/.Xresources
