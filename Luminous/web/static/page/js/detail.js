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

  function unlikealert() {
    alert("The product has been removed in the list of likes.");
    document.getElementById("Like").style.color = "white";
    document.getElementById("Like").style.backgroundColor = "#FFA2AD"
    document.getElementById("border").style.border = "5px solid #FFA2AD";
  }
  function likealert() {
    alert("The product has been reflected in the list of likes.");
    document.getElementById("Like").style.color = "white";
    document.getElementById("Like").style.backgroundColor = "#FFA2AD"
    document.getElementById("border").style.border = "5px solid #FFA2AD";
  }
  function cartalert() {
    alert("The product is in the cart.");
    document.getElementById("Cart").style.color = "white";
    document.getElementById("Cart").style.backgroundColor = "#61F3EB";
  }
  function buynowalert() {
    alert("Your order has been completed.");
  }
