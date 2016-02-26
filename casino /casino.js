//number of times we are going to loop 
var number = 5;

var inputField = document.getElementById("num-loops");
var counter = document.getElementById("counter");




function dice(){
	roll = Math.ceil(Math.random()*6);
	return roll;
	}


function loopClick(){
	number = inputField.value;
	counter.innerHTML = "";

for (var i=0; i < number; i++){
	//Print something to the browser's console
	counter.innerHTML += "<img src='dice/" + dice() + ".png' alt='A die.'/><br/>";
	//called function in dice in the for loop to add to page 
	};
};

//add click listener
document.getElementById("loop-btn").onclick = loopClick;





