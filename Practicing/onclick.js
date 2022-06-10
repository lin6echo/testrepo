function calcAmount() {
    let price = 1000;
    let amountInput = document.querySelector("input[name='amount-input']");
    let amountNumber = parseInt(amountInput.value);
    amountNumber = (isNaN(amountNumber)) ? 0 : amountNumber;
    
    showSumPrice(price, amountNumber);
}

function showSumPrice(price, amountNumber) {
    let showAmount = document.querySelector("span.show-amount");
    if ( amountNumber > 10 ) {
        alert("Maximum 10 db rendelhető!"); 
    } else if ( amountNumber < 1 ) {
        alert("Minimum 1 db-ot kell rendelni!");
    } else {
        let amount = amountNumber * price;
        showAmount.innerHTML = amount;
    
    }
 
}
//Add helptext
let helpText = document.createElement("small");
helpText.className = "form-text text-muted";
helpText.innerHTML = "Adja meg a feltéteket!";

let parent = document.querySelector("div.form-group:nth-child(1)");
parent.appendChild(helpText);

//parent.removeChild(helpText)

//Window events.
/*let sendButton = document.querySelector("form .btn.btn-primary");

sendButton.onclick = function () {
    alert("Hello JS!");
}
*/

/*sendButton.addEventListener("click", function() {
    alert("Hello JS!");
});*/

/*window.addEventListener("resize", function(){
    console.log(this.innerHeight, this.innerWidth);
});*/

let orderForm = document.querySelector("#orderForm");
 orderForm.addEventListener("submit", function(ev){
    ev.preventDefault(); /*preventDefault - ha rákattintanak lefrissül az oldal*/
     
    let inputs = this.querySelectorAll("input");
    let values = {};
    for (let i = 0; i < inputs.length; i++) {
        values[inputs[i].name] = inputs[i].value;
    }
    console.log( values );
});

//Parent element kezelése.
let alertCloseButtons = document.querySelectorAll(".close[data-dismiss='alert']");
/*let alertCloseEventHandlerFunction = function(ev) {
    this.parentElement.style.display = "none";
}; */
for (let i = 0; i < alertCloseButtons.lenght; i++) {
alertCloseButtons[i].addEventListener("click", function(ev) {
    console.log( ev );
});
}

/*
//Select elem kitöltése.
let toppings = [
    "Szalonna",
    "Hagyma",
    "Tükörtojás",
    "Libamáj",
    "Extra Sonka"
];
let toppingSelect = document.querySelector("#topinput");
let index = 0;
while(index < toppings.length) {
    let option = document.createElement("option");
    option.value = index;
    option.innerHTML = toppings[index];
    toppingSelect.appendChild(option);
    index++;
}
*/