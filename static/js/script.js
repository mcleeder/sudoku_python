function clearInputs() {
    const inputElements = document.querySelectorAll('#sudokuForm input');

    inputElements.forEach((input) => {
        input.value = "";
    });
}

function prepareData() {
    const inputElements = document.querySelectorAll('#sudokuForm input');
    const sudokuArray = [];
    inputElements.forEach((input) => {
        sudokuArray.push(parseInt(input.value) || 0);
    });
    return sudokuArray;
}

function submitForm() {
    const formData = prepareData()

    fetch('/solve', {
        method: 'POST',
        body: formData
    })
        .then(response => response.text())
        .then(data => {
            updateInputs(JSON.parse(data)["solution"]["puzzle"])
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function updateInputs(array) {
    const inputs = document.querySelectorAll('#sudokuForm input');

    inputs.forEach((input, index) => {
        const rowIndex = Math.floor(index / 9);
        const colIndex = index % 9;

        input.value = array[rowIndex][colIndex] || '';
    });
}

allInputs = document.querySelectorAll('#sudokuForm input')

allInputs.forEach((input) => {
    input.addEventListener("input", function (event) {
        if (!/^[1-9]$/.test(event.target.value)) {
            event.target.value = event.target.value.slice(-1)
        }
        // my favorite edge case
        if (event.target.value == 0) {
            event.target.value = ""
        }
    })
})