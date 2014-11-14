#include <stdio.h>
#include <stdbool.h>

#define board_size 10

bool step_board(int bs, bool **brd, bool **n_brd) {
    int count;
    for (int a=0; a<bs; a++) {
        for (int b=0; b<bs; b++) {
	    count = 0;
            for (int s=-1; s<2; s++)
		for (int t=-1; t<2; t++)
		    if (**brd[(a+s)%bs][(b+t)%bs] == true)
			count++;
            printf("at %d, %d: %d\n", a, b, count);
        }
    }
}

int main() {
    bool board[board_size][board_size];
    bool new_board[board_size][board_size];

    for (int a=0; a<board_size; a++) {
        for (int b=0; b<board_size; b++) {
            board[a][b] = false;
            new_board[a][b] = false;
        }
    }

    printf("Blah: %d\n", board_size);
    step_board(board_size, &board, &new_board);

    return 0; 
}

