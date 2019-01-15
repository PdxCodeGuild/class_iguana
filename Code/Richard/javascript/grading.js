let grade_input = document.querySelector('#grade_input')
let grade_bt = document.querySelector('#grade_bt')
let grade_output = document.querySelector('#grade_output')

grade_bt.onclick = function() {
    let x = parseInt(grade_input.value)
    let output = ''
    if (x >= 90) {
        output = 'A'
    }
    else if (x >= 80) {
        output = 'B'
    }
    else if (x >= 70) {
        output = 'C'
    }
    else if (x > 60) {
        output = 'D'
    }
    else {
        output = 'F'
    }
    grade_output.innerText = output
}