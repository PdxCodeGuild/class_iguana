let madlib_bt = document.querySelector('#madlib_bt')
// create arrays for inclusion in madlib, to be chosen at random
let jobs = ['laborer', 'physician', 'grocer', 'astronaut']
let tasks = ['dig', 'market', 'disassemble', 'reproduce']
let teams = ['team', 'collection', 'mob', 'corps']
let objects = ['products', 'miracles', 'irrelevancies', 'constructs']

// implement a random.choice style function
function randomChoice(arr) {
    i = Math.floor(Math.random() * arr.length)
    return arr[i]
}

function firstUpper(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}


// get input from user
let ant = document.querySelector('#ant')
let handed = document.querySelector('#handed')
let adj = document.querySelector('#adj')
let others = document.querySelector('#others')
let bldg = document.querySelector('#bldg')
let buzz = document.querySelector('#buzz')
let tech = document.querySelector('#tech')
let comp = document.querySelector('#comp')

madlib_bt.onclick = function() {

    document.querySelector('#output_div').style.display = ''

    let job = randomChoice(jobs)
    let task = randomChoice(tasks)
    let team = randomChoice(teams)
    let object = randomChoice(objects)
    job_desc.innerText = `${firstUpper(ant.value)} Expert Job Description`
    key_resp.innerText = `Seeking ${adj.value} ${job}, able to ${task} ${buzz.value} ${object} with a ${team} of ${others.value}. Must be ${handed.value}.`
    resp_1.innerText = `Engage in profound study of all things ${ant.value}`
    resp_2.innerText = `Reconfigure ${bldg.value}`
    resp_3.innerText = `Explore application of ${tech.value} to ${comp.value}s`
}
