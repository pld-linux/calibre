#!/bin/sh

VERSION=$1

tar -xvJf calibre-$VERSION.tar.xz
rm -f calibre-$VERSION/resources/fonts/liberation/*
rm -f calibre-$VERSION/resources/fonts/prs500/*

tar -cvJf calibre-$VERSION-nofonts.tar.xz calibre-$VERSION
