from flask import Flask, render_template, request, jsonify
from solver import Sudoku

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    try:
        puzzle = Sudoku(request.data)
        puzzle.solve()
        solved_puzzle = {"puzzle": puzzle.board}
        
        return jsonify({'solution': solved_puzzle})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
