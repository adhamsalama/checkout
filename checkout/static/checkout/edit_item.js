document.addEventListener("DOMContentLoaded", edit_click());

function edit_click () {
    {
        let buttons = document.querySelectorAll(".edit_button");
        //console.log(forms.parentElement);
        for (let i = 0; i < buttons.length; i++) {
            let item = buttons[i].parentElement.parentElement;
            //console.log(item.id);
            let props = item.querySelectorAll(".item");
            //console.log(props);
            //console.log("-----------------------");
            buttons[i].onclick = function() {
                const request = new Request("/edit_item/" + item.id,
                    {headers: {'X-CSRFToken': getCookie("csrftoken")}}
                );
                fetch(request)
                .then(response => response.text())
                .then(result => {
                    // Print result
                    let item_copy = item.cloneNode(true);
                    console.log(item_copy);
                    item.innerHTML = result;
                    let save_button = item.querySelector(".btn");
                    save_button.onclick = function() {
                        let data = new URLSearchParams()
                        data.append("item_id", item.id);
                        //let props = [{"name": "", "price": "", "quantity": "", "seller": "", "date": "", "category": "", "comment": ""}];
                        let props = ["name", "price", "quantity", "seller", "date", "category", "comment"];
                        for(let j = 0; j < props.length; j++) {
                            let a = item.querySelector("#id_" + props[j]);
                            data.append(props[j], a.value);
                            item_copy.querySelector(".item_" + props[j]).innerHTML = a.value;
                        }
                        console.log(data);
                        
                      const request2 = new Request("/edit_item/" + item.id,
                          {headers: {'X-CSRFToken': getCookie("csrftoken")}}
                      );
                      fetch(request2, {
                          method: "POST",
                          body: data
                      })
                      .then(response => response.json())
                      .then(result => {
                          console.log(result);
                          item.innerHTML = item_copy.innerHTML;
                          item.querySelector(".edit_button").onclick = edit_click;
                          return false;
                      })
                      
                    }
                });
            }
        }
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}