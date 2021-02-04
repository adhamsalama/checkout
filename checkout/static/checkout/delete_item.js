document.addEventListener("DOMContentLoaded", () => {
    let buttons = document.querySelectorAll(".delete_button");
    for(let i = 0; i < buttons.length; i++) {
        buttons[i].onclick = delete_click;
    }
});

function delete_click () {

        
        //console.log(forms.parentElement);
            let item = this.parentElement.parentElement;

                const request = new Request("/delete_item",
                          {headers: {'X-CSRFToken': getCookie("csrftoken")}}
                      );
                fetch(request, {
                  method: "POST",
                  body: JSON.stringify({
                    item_id: item.id
                })
                })
                .then(response => response.json())
                .then(result => {
                    console.log(result);
                    // edited this to work on darshboard where balance isn't shown
                    let balance = document.querySelector("#balance");
                    
                    if (balance) {
                        let pr = item.querySelector(".item_price").innerHTML;
                        let new_balance = parseFloat(balance.innerHTML.slice(10, )) + parseFloat(pr);
                        console.log(new_balance, new_balance.toFixed(1));
                        balance.innerHTML = "Balance: $" + new_balance.toFixed(1); 
                    }
                    //item.remove();
                    return false;
                })
                item.style.animationPlayState = "running";
                item.onanimationend = () => {
                    item.remove();
                }
            
        
}