#include <stdio.h>
#include "fred.h"

static char*  skits[] = {
    "Parrot",
    "Spam",
    "Ministry of Silly Walks",
    "Cheese Shop"
};

static int num_skits = sizeof(skits)/sizeof(char *);

int
add(int x, int y) {
    int sum;
    sum = x + y;
    return sum;
}

void
hello() {
    printf("Hello, world\n");
}

char*
get_skit(int which) {
    which--;  // allow for starting at 1
    if ( (which < 0) || (which> num_skits) ) {
        return "Index out of range";
    }
    else {
        return skits[which];
    }
}