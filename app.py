from flask import Flask, render_template, request, jsonify
from solver import solver

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        puzzle_str = request.form.get('sudokuPuzzle')
        
        # Validate the puzzle string (implement as needed)
        if not is_valid_sudoku(puzzle_str):
            return jsonify({'error': 'Invalid Sudoku puzzle format'})

        # Solve the Sudoku puzzle
        solved_puzzle = solver.solve(puzzle_str)
        solved_puzzle = {"puzzle":"solved"}
        
        return jsonify({'solvedPuzzle': solved_puzzle})

    except Exception as e:
        return jsonify({'error': str(e)})

def is_valid_sudoku(puzzle_str):
    # Implement Sudoku puzzle validation logic if needed
    # Return True if the puzzle is valid, False otherwise
    return True

if __name__ == '__main__':
    app.run(debug=True)
