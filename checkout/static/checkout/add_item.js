let button = document.querySelector("#new_item_button");
if (button){
    button.onclick = function() {
        form = document.querySelector("#new_item_form");
        form.style.display = "block";
        form.onsubmit = function () {
            let name = form.querySelector("#id_name");
            let price = form.querySelector("#id_price");
            let quantity = form.querySelector("#id_quantity");
            let seller = form.querySelector("#id_seller");
            let date = form.querySelector("#id_date");
            let category = form.querySelector("#id_category");
            let comment = form.querySelector("#id_comment");
            const request = new Request("/create_item",
                      {headers: {'X-CSRFToken': getCookie("csrftoken")}}
            );
            fetch(request, {
                method: "POST",
                body: JSON.stringify({
                    name: name.value,
                    price: price.value,
                    quantity: quantity.value,
                    seller: seller.value,
                    date: date.value,
                    category: category.value,
                    comment: comment.value
                })
            })
            .then(response => response.json())
            .then(result => {
                console.log(result);
                console.log(name);
                console.log(name.value);
                
            })
            let new_item = document.createElement("div");
                new_item.className = "card mt-4 mb-4 item_div";
                let html = `
                              <div class="card-body">
                                <h2 class="card-title"><span class="item item_name">${name.value}</span></h2>
                                <p class="card-text p-4">
                                Price: $<span class="item item_price">${price.value}</span>
                                <br>
                                Quantity: <span class="item item_quantity">${quantity.value}</span>
                                <br>
                                Seller: <span class="item item_seller">${seller.value}</span>
                                <br>
                                Date: <span class="item item_date">${date.value}</span>
                                <br>
                                Category: <span class="item item_category">${category.value}</span>
                                <br>
                                Comment: 
                                <span class="item item_comment">${comment.value}</span>
                                </p>
                              </div>
                            `
                new_item.innerHTML = html;
                let list = document.querySelector("#items_list");
                list.insertBefore(new_item, list.firstChild);
            let balance = document.querySelector("#balance");
            let new_balance = parseFloat(balance.innerHTML.slice(10, )) - parseFloat(price.value);
            balance.innerHTML = "Balance: $" + new_balance.toFixed(1);
            form.style.display = "none";
            name.value = "";
            price.value = "";
            quantity.value = "";
            seller.value = "";
            date.value = "";
            category = "";
            comment.value = "";
             
            return false;
        }
    }
}
