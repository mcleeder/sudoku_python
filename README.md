## Recursive Sudoku Solver

Learning project. I was playing with recursion and backtracking. I want to continue exploring and try to use redis/celery to do the solving.

### Try It:
https://sudoku-wispy-pond-6137.fly.dev/

### Done:
- Can solve sudoku using recursion and backtracking
- front-end can send data to the back and get a solution returned & displayed
- enforcing good inputs with javascript

### To-Do:
- Setup celery to help prevent unsolvable boards from looping
    - run solver as celery worker with a timeout
    - redis
- Would be neat to feedback which cells board are invalid