function clearCalc() {
    $("p.calculator-current").text('');
    finished = false;
}
function oneCalc() {
    $('p.calculator-current').append('1');
}
function twoCalc() {
    $('p.calculator-current').append('2');
}
function twoCalc() {
    $('p.calculator-current').append('2');
}
function threeCalc() {
    $('p.calculator-current').append('3');
}
function fourCalc() {
    $('p.calculator-current').append('4');
}
function fiveCalc() {
    $('p.calculator-current').append('5');
}
function sixCalc() {
    $('p.calculator-current').append('6');
}
function sevenCalc() {
    $('p.calculator-current').append('7');
}
function eightCalc() {
    $('p.calculator-current').append('8');
}
function nineCalc() {
    $('p.calculator-current').append('9');
}
function zeroCalc() {
    $('p.calculator-current').append('0');
}
function decimalCalc() {
    if ($('p.calculator-current').text().includes('.')) {
        return
    }
    $('p.calculator-current').append('.');
}


var finished = false;
let globalSymbol = ''
function divideSymbol(symbol) {
    globalSymbol = symbol
}
function multiplySymbol(symbol) {
    globalSymbol = symbol
}
function minusSymbol(symbol) {
    globalSymbol = symbol
}
function addSymbol(symbol) {
    globalSymbol = symbol
}
let Temp = ''

function operatorCalc() {
    //$("p.calculator-previous").text($('p.calculator-current').text());
    //let Temp = $("p.calculator-current").text();
    //clearCalc();
    //console.log(Temp);

    if (finished == true) {
        let Second = $("p.calculator-current").text();
        console.log("Second variable: " + Second)

        switch (globalSymbol) {
            case '/':
                compute = Temp / Second
                console.log("Outputted: " + compute)
                $('p.calculator-current').text(compute)
                break;

            case '*':
                compute = Temp * Second
                console.log("Outputted: " + compute)
                $('p.calculator-current').text(compute)
                break;
            case '-':
                compute = Temp - Second
                $('p.calculator-current').text(compute)
                break;
            case '+':
                const first = parseFloat(Temp)
                const second = parseFloat(Second)
                compute = first + second
                $('p.calculator-current').text(compute)
                break;
            default:
                return;
        }
    } else {
        console.log("Pressed Operation: " + globalSymbol)
        Temp = $("p.calculator-current").text();
        clearCalc()
        console.log("First variable: " + Temp)
    }

}
function boolChange() {
    finished = !finished
    console.log(finished)

    operatorCalc()
}

//Demo Science and Engineering 2 - Thursday, October 14th, 2:30pm-4:30pm