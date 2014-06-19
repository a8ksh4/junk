#include <Python.h>
#include <stdlib.h>
#include <stdio.h>

/*
 
On Ubuntu Linux 9.10, e.g., compile with:

gcc -c -I/usr/include/python2.6 tauntlibmodule.c
ld -shared -o tauntlib.so tauntlibmodule.o

*/

static char* taunts[] = {
    "Your mother was a hamster and your father smelt of elderberries.",
    "I *CENSORED* in your general direction",
    "I don't want to talk to you no more, you empty headed animal food trough whopper!",
    "You don't frighten us, English pig-dogs!",
    "Go and boil your bottoms, sons of a silly person.",
    "I blow my nose at you, so-called Arthur-king, you and all your silly English k-niggets.",
    "'Allo, daffy English k-niggets and Monsieur Arthur-King, who is afraid of a duck, you know!",
    " I one more time-a unclog my nose in your direction, sons of a window-dresser!",
    "I wave my *CENSORED* at your aunties, you heaving lot of second-hand electric donkey bottom biters.",
    "No chance, English bedwetting types.",
    "I burst my pimples at you and call your daughter an unrequested silly thing.",
    "You tiny-brained wipers of other people's bottoms!",
};

static PyObject *TauntError;

static int number_of_taunts() {
    return sizeof(taunts)/sizeof(char *);
}

static PyObject *
tauntlib_taunt(PyObject *self, PyObject *args) {
    const int taunt_index;
    /* parse args */
    if (!PyArg_ParseTuple(args, "i", &taunt_index))
        return NULL;

    /* check for index out of bounds */
    if( (taunt_index < 0) || (taunt_index >= number_of_taunts() ) ) {
        PyErr_SetString(TauntError,"Taunt index out of range");        
        return NULL;
    }

    /* return taunt */
    return Py_BuildValue("s",taunts[taunt_index]);
}

static PyObject *
tauntlib_randtaunt(PyObject *self, PyObject *args) {
    /* check for index out of bounds */

    int taunt_index = rand() % number_of_taunts();
    
    /* return taunt */
    return Py_BuildValue("s",taunts[taunt_index]);
}


static PyObject *
taunt_goaway(PyObject *self,PyObject *args) {
    puts("No, now go away or I shall taunt you a second time-a!\n");
    Py_INCREF(Py_None);
    return Py_None;
}

static PyObject *
tauntlib_tauntcount(PyObject *self,PyObject *args) {
    return Py_BuildValue("i",number_of_taunts());
}

static PyMethodDef tauntlibMethods[] = {
    {"taunt",  tauntlib_taunt, METH_VARARGS, "Return the requested taunt by index."},
    {"randtaunt",  tauntlib_randtaunt, METH_VARARGS,"Return a random taunt"},
    {"goaway",  taunt_goaway, METH_VARARGS,"Tell the silly English knights to go away"},
    {"tauntcount",  tauntlib_tauntcount, METH_VARARGS,"Return number of available taunts"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

PyMODINIT_FUNC
inittaunt(void) {
    PyObject *m;
    
    m = Py_InitModule("taunt", tauntlibMethods);
    if (m == NULL) {
        return;
    }
    
    TauntError = PyErr_NewException("tauntlib.taunterror", NULL, NULL);
    Py_INCREF(TauntError);
    PyModule_AddObject(m, "taunterror", TauntError);

}
