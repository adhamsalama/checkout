document.addEventListener("DOMContentLoaded", get_form);


function get_form() {
    document.querySelector("#add_wishlist").onclick = function() {
        fetch("/wishlist/get_wishlist_form")
        .then(response => response.text())
        .then(result =>  {
            //console.log(result);
            let form_div = document.querySelector("#form");
            form_div.className = "container p-4 mt-4 border";
            form_div.innerHTML = result;
            form_div.querySelector("form").onsubmit = function() {
                let name = form_div.querySelector("#id_name").value;
                let price = form_div.querySelector("#id_price").value;
                let link = form_div.querySelector("#id_link").value;
                let token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
                let request = new Request("add", {
                    headers: {'X-CSRFToken': getCookie("csrftoken")}
                }
                );
                fetch(request, {
                    method: "POST",
                    body: JSON.stringify({
                        name: name,
                        price: price,
                        link: link
                    })
                })
                .then(response => response.json())
                .then (result => {
                    console.log(result);
                })
                //return false;
                console.log("-----", name, price, link);
                let items_div = document.querySelector("#items");
                let html = `
                              <div class="card-body">
                                Name: ${name}
                                <br>
                                Price: ${price}
                                <br>
                                <a href="${link}">Link</a>
                              </div>
                            `
                let new_item = document.createElement("div");
                new_item.className = "card mt-2 mb-2";
                new_item.innerHTML = html;
                items_div.insertBefore(new_item, items_div.firstChild);
                console.log("success");
                form_div.innerHTML = "";
                form_div.className = "";
                return false;
                
            }
            
        })
    }
}

