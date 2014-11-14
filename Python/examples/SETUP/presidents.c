
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LEN 132

static const char DATA_FILE[] = "../DATA/presidents.txt";

char *get_name(int target_term_number) {
    char *line;
    char *name;
    char *lname, *fname;
    int found = 0;

    int file_term_number = 0;

    line = malloc(MAX_LINE_LEN + 1);

    FILE *pres_file = fopen(DATA_FILE, "r");

    while ( fgets( line, MAX_LINE_LEN, pres_file ) != NULL ) {
        char *ptr = line;

        while (*ptr++ != ':') {
           ;
        }
        ptr--;
        *ptr = 0;

        int file_term_number = atoi(line);

        if (target_term_number == file_term_number) {
            // copy first and last names
            char *pos = ++ptr;
            while (*ptr++ != ':') {
               ;
            }
            ptr--;
            *ptr = 0;
            lname = strdup(pos);
            pos = ++ptr;
            while (*ptr++ != ':') {
               ;
            }

            ptr--;
            *ptr = 0;

            fname = strdup(pos);
            found = 1;

            break;
        }
    }

    fclose( pres_file );

    if (found) {
        name = malloc(strlen(fname) + strlen(lname) + 2);

        sprintf(name, "%s %s", fname, lname);
    }
    else {
        name = "NOT FOUND";
    }
    return name;
}