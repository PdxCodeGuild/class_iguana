
let arr = []
for (let i = 0; i <= 10; ++i) {
    arr.push(Math.floor(Math.random()*100))
}

let array_output = document.querySelector("#array")
let arrMin_output = document.querySelector("#min")
let arrMax_output = document.querySelector("#max")
let arrSum_output = document.querySelector("#sum")
let arrAvg_output = document.querySelector("#average")
let arrMed_output = document.querySelector("#median")
let arrMode_output = document.querySelector("#mode")
let arrFreq_output = document.querySelector("#freqs")

let array_output_interactive = document.querySelector("#array_interactive")
let arrMin_output_interactive = document.querySelector("#min_interactive")
let arrMax_output_interactive = document.querySelector("#max_interactive")
let arrSum_output_interactive = document.querySelector("#sum_interactive")
let arrAvg_output_interactive = document.querySelector("#average_interactive")
let arrMed_output_interactive = document.querySelector("#median_interactive")
let arrMode_output_interactive = document.querySelector("#mode_interactive")
let arrFreq_output_interactive = document.querySelector("#freqs_interactive")

let calc_bt = document.querySelector("#calc_bt")

let fieldList = document.querySelector("#fieldList")

let arrMin = x => Math.min(... x)
let arrMax = x => Math.max(... x)
let arrSum = x => x.reduce((a,b) => a + b, 0)
let arrAvg = x => arrSum(x) / x.length
let arrMed = x => x.length % 2===0? [x[x.sort((a, b) => a - b).length / 2], x[x.sort((a, b) => a - b).length / 2 - 1]]: x[Math.floor(x.sort((a, b) => a - b).length / 2)]
let freqs = {}
let arrFreqs = function(a) {
    for (i=0; i < a.length; ++i) {
        if (a[i] in freqs) {freqs[a[i]] += 1}
        else freqs[a[i]] == 1
    }
    return freqs
}
let arrMode = x => arrMax(Object.keys(arrFreqs(x)))

array_output.innerText = `numbers: ${arr}`
arrMin_output.innerText =`minimum: ${arrMin(arr)}`
arrMax_output.innerText = `maximum: ${arrMax(arr)}`
arrSum_output.innerText = `sum: ${arrSum(arr)}`
arrAvg_output.innerText = `average: ${arrAvg(arr).toFixed(2)}`
arrMed_output.innerText = `median: ${arrMed(arr)}`
arrMode_output.innerText = `mode: ${arrMode(arr)}`
arrFreq_output.innerText = `frequencies: ${arrFreqs(arr)}`


let inputs = []
for (let i=1; i<=10; ++i) {
    let input = document.createElement('input')
    fieldList.appendChild(input)
    inputs.push(input)
}
calc_bt.onclick = function() {
    nums = []
    for (let i=0; i<inputs.length; ++i) {
        nums.push(parseFloat(inputs[i].value))
    }
    array_output_interactive.innerText = `numbers: ${nums}`
    arrMin_output_interactive.innerText =`minimum: ${arrMin(nums)}`
    arrMax_output_interactive.innerText = `maximum: ${arrMax(nums)}`
    arrSum_output_interactive.innerText = `sum: ${arrSum(nums)}`
    arrAvg_output_interactive.innerText = `average: ${arrAvg(nums).toFixed(2)}`
    arrMed_output_interactive.innerText = `median: ${arrMed(nums)}`
    arrMode_output_interactive.innerText = `mode: ${arrMode(nums)}`
    arrFreq_output_interactive.innerText = `frequencies: ${arrFreqs(nums)}`
}