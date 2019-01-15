// a script to make change in US currency

// get input from user
let money_input = document.querySelector('#money_input')
let change_bt = document.querySelector('#change_bt')

let quarters_output = document.querySelector('#quarters')
let dimes_output = document.querySelector('#dimes')
let nickels_output = document.querySelector('#nickels')
let pennies_output = document.querySelector('#pennies')

// function to make change
change_bt.onclick = function() {
    let amt = parseFloat(money_input.value) * 100


    let quarters = Math.floor(amt / 25)
    amt = amt % 25
    let dimes = Math.floor(amt / 10)
    amt = amt % 10
    let nickels = Math.floor(amt / 5)
    let pennies = amt % 5

    // write the results to the page
    quarters_output.innerText = `${quarters} quarters`
    dimes_output.innerText = `${dimes} dimes`
    nickels_output.innerText = `${nickels} nickels`
    pennies_output.innerText = `${pennies} pennies` 
}