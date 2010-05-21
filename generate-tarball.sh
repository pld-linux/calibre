#!/bin/sh

VERSION=$1

rm -rf calibre
tar -xvzf calibre-$VERSION.tar.gz
rm -f calibre/resources/fonts/liberation/*
rm -f calibre/resources/fonts/prs500/*

tar -cvjf calibre-$VERSION-nofonts.tar.bz2 calibre
