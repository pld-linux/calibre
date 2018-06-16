#!/bin/sh

VERSION=$1

wget https://download.calibre-ebook.com/$VERSION/calibre-$VERSION.tar.xz

tar -xvJf calibre-$VERSION.tar.xz
rm -f calibre-$VERSION/resources/fonts/liberation/*
rm -f calibre-$VERSION/resources/fonts/prs500/*

tar -cf - calibre-$VERSION | xz -9vv >calibre-$VERSION-nofonts.tar.xz

echo

md5sum calibre-$VERSION-nofonts.tar.xz
