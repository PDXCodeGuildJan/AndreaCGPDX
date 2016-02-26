// Establish the event listener for when they click an item 
//add the click event handler to the "add-item" button

var button = document.getElementById("add-item");  
var addItemButton = document.getElementById("add-item");
addItemButton.onclick = addItem;
var addStockButton = document.getElementById("add-stock");
addStockButton.onclick = addStock;
var removeStockButton = document.getElementById("remove-stock");
removeStockButton.onclick = removeStock;

function addStock(){
	//not allowed to use querySelectorAll()
	var inputs = document.getElementsByTagName("input");
	console.log(inputs)
	var checked = [];
	for (i = 0; i < inputs.length; i++){
		if (inputs[i].type === "checkbox" && inputs[i].id != "in_stock") {
			console.log(inputs[i])
			if (inputs[i].checked){
				checked.push(inputs[i]);
			}
		}

	}
  
	console.log(checked)

	}
	//find all the selected things 

	//Change the inStock value of the selected things 


	//Update the display? (Depends on previous step.)
	

function removeStock(){
	//use querySelectorAll()

	var selected = document.querySelectorAll("tbody > tr > td > input:checked");
	for (var i = 0; i < selected.length; i++) {
		var status = selected[i].parentNode.parentNode.children[3];
		status.textContent = "no";
		status.className = "false";
		};

//td> input.selector[typr= checkbox].checked"
//".selected:checked"
//"input[type='checkbox']:checked"
//"tbody> tr > td > input:checked"


	
/*Add the item in the text field to the inventory 
 *list, which is in the table body (id="inventory")
 */
}
	

	 
function addItem() {
	var materialName = document.getElementById("name").value;
	var price= document.getElementById("price").value;
	var inStock = document.getElementById("in_stock").checked;
	


	var inventory =document.getElementById("inventory");
	var newRow = "<tr><td><input type='checkbox' type='checkbox' /></td>" +
	"<td>" + materialName + "</td>" +
	"<td>" + price + " </td>" +
	"<td class ='" + inStock + "'>";

	if (inStock) {
		newRow += "yes";
	} 
	else{
		newRow += "no";
	}
	newRow += "</td></tr>";
	
	inventory.innerHTML += newRow;
	}
