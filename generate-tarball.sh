#!/bin/sh

VERSION=$1

tar -xvJf calibre-$VERSION.tar.xz
rm -f calibre-$VERSION/resources/fonts/liberation/*
rm -f calibre-$VERSION/resources/fonts/prs500/*

tar -cf - calibre-$VERSION | xz -9vv >calibre-$VERSION-nofonts.tar.xz

echo

md5sum calibre-$VERSION-nofonts.tar.xz
