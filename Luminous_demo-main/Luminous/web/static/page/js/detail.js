function calculate(){

    var price = document.getElementById("price").value;
    var Quantity = document.getElementById("Quantity").value;
    var shipping;
    var sum;
    shipping=3;
    sum = parseInt(price)*parseInt(Quantity)+parseInt(shipping);

    if(isNaN(price)==true||isNaN(Quantity)==true){
      alert("Please enter a number ! ");
      return false;
    }

    alert("Price : $"+price+"\nQuantity : "+Quantity+ "\n"+ "Shipping : $"+shipping+"\nYour final Price : $"+sum+"\n");
  }
