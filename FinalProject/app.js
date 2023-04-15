//Where to look for when grabbing information
const calculator = document.getElementById("calculator");
const display = document.getElementById("display");

//Add event listeners for when the user taps number 1-9
const numberButtons = document.querySelectorAll(".number");
numberButtons.forEach(button => {button.addEventListener("click", ()=>{
    display.textContent += button.textContent;
})});

//Add event listeners for when the user taps any operations 
const operationButtons = document.querySelectorAll(".operation");
operationButtons.forEach(button => {button.addEventListener("click", ()=>{
    display.textContent += "" + button.textContent+ "";
})});

//Add event listeners 
const clearButton=Document.getElementById("clear");
clearButton.addEventListener("click", ()=>{
    display.textContent="";
});

//Add event listeners
const equalsButton = Document.getElementById("equals");
equalsButton.addEventListener("click", ()=>{
    const expression = display.textContent;
    try{
        const result=eval(expression);
        display.textContent=result;
    }catch(error){
        display.textContent = "error try again";
    }
});
