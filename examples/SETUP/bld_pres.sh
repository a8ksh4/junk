#!/usr/bin/env sh


build_linux() {
    rm -f presidents.o libpresidents.so.1 libpresidents.so presidents.so

    gcc -fPIC -c presidents.c
    gcc -shared -Wl,-soname,presidents.so.1.0 -o ../DATA/presidents.so.1.0 presidents.o
    ln -f -s ../DATA/presidents.so.1.0 ../DATA/presidents.so
}

build_osx() {
    gcc -c -I /System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 presidents.c
    gcc -arch x86_64 -dynamiclib -undefined suppress -flat_namespace presidents.o -o ../DATA/presidents.dylib -framework Python -Wl,-F.
}

PLATFORM=$(uname -s)

if [ "$PLATFORM" = "Darwin" ]
then
    build_osx
else
    if [ "$PLATFORM" = "Linux" ]
    then
        build_linux
    fi
fi