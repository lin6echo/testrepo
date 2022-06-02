function calcAmount() {
    let price = 1200;
    let amountInput = document.querySelector("input[name='amount-input']");
    let amountNumber = parseInt(amountInput.value);
    amountNumber = isNaN(amountNumber) ? 0 : amountNumber;
    
    showSumPrice(price, amountNumber)
}    


function showSumPrice(price, amountNumber)  {  
        let showAmount = document.querySelector("span.show-amount");
    if ( amountNumber > 10) {
        alert("Maximum 10 terméket vásárolhat!");
    } else if ( amountNumber < 1 ) {
        alert("Minimum 1 terméket kell vásárolnia!");
    } else {
        let amount = amountNumber * price;
        showAmount.innerHTML = amount;
    }
    }

let topInput = document.querySelector("input#topInput");

/*Add helptext.*/
let helpText = document.createElement("small");
helpText.className = "form-text text-muted"; 
helpText.innerHTML = "Adja meg a feltéteket!";


let parent = document.querySelector("div.form-group:nth-child(1)");
parent.appendChild(helpText);

let orderForm = document.querySelector("#orderForm");
orderForm.addEventListener("submit", function(ev) {
    ev.preventDefault();
    console.log( this );

let alertCloseButtons = document.querySelectorAll(".close[data-dismiss='alert']"); 
for (let i = 0; i < alertCloseButtons.length; i++) {
    alertCloseButtons[i].addEventListener("click", function(ev) {
        this.parentElement.style.display = "none";
    });
}

let toppings = [
    "Szalonna",
    "Hagyma",
    "Paradicsom",
    "Extra sajt",
    "Extra sonka"
];
let toppingSelect = document.querySelector("#topInput");
let index = 0;
while(index < toppings.length) {
    let option = document.createElement("option");
    option.value = index;
    option.innerHTML = toppings[index];
    toppingSelect.appendChild(option);
    index++;
}