## Recursive Sudoku Solver

This was just an exploration project where I was playing with recursion and backtracking. This works fairly well, it can handle an invalid board and should be able to solve anything else. It might be possible to give it a board with no solution though, which might produce an endless loop. I think giving the solving responsibility to a celery worker could make it safer by timing out any attempts that run too long.

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- Python as the API doing the solving
- JavaScript on the front-end doing the sending and displaying
- [Deployed on Fly.dev](https://sudoku-wispy-pond-6137.fly.dev/)

### Try It:
https://sudoku-wispy-pond-6137.fly.dev/

![Sudoku-Grid---Google-Chrome-2024-03-06-22-24-57](https://github.com/mcleeder/sudoku_python/assets/68357049/3fe86207-63fa-4356-8a2b-c8ab8a16a6da)



### Done:
- Can solve sudoku using recursion and backtracking
- front-end can send data to the back and get a solution returned & displayed
- enforcing good inputs with javascript

### To-Do:
- Setup celery to help prevent unsolvable boards from looping
    - run solver as celery worker with a timeout
    - redis
- Would be neat to feedback which cells board are invalid
