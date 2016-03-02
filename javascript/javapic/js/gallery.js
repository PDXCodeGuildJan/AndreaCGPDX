//This is the js for my javapic I am going to work on backwards from gallery to join
//alert("OMyGERD Look what i can do!");
//this sets and event listener to initalize the images popping up 
window.onload = image
//this is the function that 
function image(){
	

	var poo = document.getElementById("gallery");
	//this function initalizes a var that links the js to
	//the element id in the html
	

	var allImages = "<ul>"
	//this is the var that set the string to an unordered list
	//and we do it this way bc if we added it in the forloop 
	//it would have a begining and ending tag with every image
	
	for (i = 1; i <= 60; i++){
		if (i < 10){
		i = "0" + i 
		}
		//this is a for loop that sets i to 1, then loops thru
		//the numbers to the end and incriments to the next number.  
		//the if statement inserts a 0 infront of #'s with one didget 
		//and then incerts it back into the variable i 
		
		var image="<li><img src=images/pdxcg_" + i + ".jpg></li>"
		//we defined a list item and stuck it in a variable 
		//then we broke it into strings and concotinate it 
		//by adding in the variable i which refers to the looping
		//through of numbers in the for loop  
		
		console.log(image);
		//displays to console
		
		allImages = allImages + image
		//here we set the image var to a ul of strings
		//and concotinate it to allow
		//adding the image to the string of images 
		
}
		allImages = allImages + "</ul>"
		//this sets a closing tag to the end of the string 

 
	poo.innerHTML=allImages
	//this sets all the images to the gallery 
	
	
} 
document.getElementById("gallery").addEventListener("click",lightBox)
document.getElementById("image_show").addEventListener("click", unLightBox)

function lightBox(event){
	//if click = pic
	//do shitbox
	if  (event.target.nodeName === "IMG"){
		var shitBox = document.getElementById("image_show")
		shitBox.className = "display_img";
		shitBox.firstChild.src = event.target.src;

	}
  
}
function unLightBox(){
	//if click not = pic
	// so unshitbox
	if (event.target.nodeName != "IMG"){
		var unShitBox = document.getElementById("image_show")
		unShitBox.className = "display_none";

	}			

}



	


	










 


	