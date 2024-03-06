## Recursive Sudoku Solver

In-progress

Done:
- Can solve sudoku using recursion and backtracking
- front-end can send data to the back and get a solution returned
- enforcing good inputs with javascript

To-Do:
- Setup celery to help prevent unsolvable boards from looping
    - run solver as celery worker with a timeout
    - redis
- Error handling
    - handle errors on front-end
    - return errors from back-end
    - display back-end errors