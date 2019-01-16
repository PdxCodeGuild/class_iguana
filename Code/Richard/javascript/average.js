
let arr = []
for (i = 0; i < 10; ++i) {
    arr.push(Math.floor(Math.random)*100)
}

let array_output = document.querySelector("#array")
let arrMin_output = document.querySelector("#min")
let arrMax_output = document.querySelector("#max")
let arrSum_output = document.querySelector("#sum")
let arrAvg_output = document.querySelector("#average")

let arrMin = arr => Math.min(arr)
let arrMax = arr => Math.max(arr)
let arrSum = arr => arr.reduce((a,b) => a + b, 0)
let arrAvg = arr => arrSum / arr.length

array_output.innerText = `numbers: ${array.value}`
arrMin_output.innerText =`minimum: ${arrMin.value}`
arrMax_output.innerText = `maximum: ${arrMax.value}`
arrSum_output.innerText = `sum: ${arrSum.value}`
arrAvg_output.innerText = `average: ${arrAvg.value}`