#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define SIZE 35
static const int maxval = 20;

typedef struct {
	unsigned bestscore, bestguess;
} winner;

unsigned compare(int correct[SIZE][SIZE], int guess[SIZE][SIZE]) {
	unsigned diff = 0, x, y;

	for(x = 0; x < SIZE; x++)
		for(y = 0; y < SIZE; y++)
			diff += abs(correct[x][y] - guess[x][y]);
	
	return diff;
}

winner findbest(int correct[SIZE][SIZE], int guesses[SIZE][SIZE][SIZE]) {
	unsigned bestscore = compare(correct, guesses[0]);
	unsigned bestguess = 0, c;
	winner w;

	for(c = 1; c < SIZE; c++) {
		unsigned newscore = compare(correct, guesses[c]);
		if(newscore < bestscore) {
			bestscore = newscore;
			bestguess = c;
		}
	}	

	w.bestscore = bestscore;
	w.bestguess = bestguess;
	return w;
}

void copyandmutate(int starter[SIZE][SIZE], int guesses[SIZE][SIZE][SIZE]) {
	unsigned i;

	memcpy(guesses[0], starter, sizeof(int) * SIZE * SIZE);

	for(i = 1; i < SIZE; i++) {
		unsigned x = rand() % SIZE;
		unsigned y = rand() % SIZE;
		int v;

		memcpy(guesses[i], guesses[0], sizeof(int) * SIZE * SIZE);
		v = guesses[i][x][y] + (rand() % 7) - 3;
		
		if(v < 0)
			v = 0;
		else if(v > maxval)
			v = maxval;

		guesses[i][x][y] = v;
	}
}

void randomguess(int guess[SIZE][SIZE]) {
	unsigned x, y;

	for(x = 0; x < SIZE; x++)
		for(y = 0; y < SIZE; y++)
			guess[x][y] = rand() % (maxval + 1);
}

void printguess(int guess[SIZE][SIZE]) {
	unsigned x, y;

	for(x = 0; x < SIZE; x++)
		for(y = 0; y < SIZE; y++)
			printf("%d ", guess[x][y]);
}

void printguesses(int correct[SIZE][SIZE], int guesses[SIZE][SIZE][SIZE]) {
	unsigned c;

	for(c = 0; c < SIZE; c++) {
		printf("guess%d: ", c);
		printguess(guesses[c]);
		printf("score: %d\n", compare(correct, guesses[c]));
	}
}

void go() {
	int guesses[SIZE][SIZE][SIZE];
	int correct[SIZE][SIZE];
	unsigned c;

	randomguess(correct);
	
	for(c = 0; c < SIZE; c++)
		randomguess(guesses[c]);
	
	for(;;) {
		winner best = findbest(correct, guesses);
		if(best.bestscore == 0)
			break;

		copyandmutate(guesses[best.bestguess], guesses);
	
	}	
}

int main() {
	go();
	return 0;
}
