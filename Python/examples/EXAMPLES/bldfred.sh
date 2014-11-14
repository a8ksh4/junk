#!/usr/bin/env sh


build_linux() {
    rm -f fredmodule.o libfred.so.1 libfred.so fred.so

    gcc -fPIC -c fred.c
    gcc -shared -Wl,-soname,fred.so.1.0 -o fred.so.1.0 fred.o
    ln -f -s fred.so.1.0 fred.so
}

build_osx() {
    gcc -c -I /System/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 fred.c
    gcc -arch x86_64 -dynamiclib -undefined suppress -flat_namespace fred.o -o fred.dylib -framework Python -Wl,-F.
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