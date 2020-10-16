document.addEventListener("DOMContentLoaded", delete_click());
function delete_click () {

        let buttons = document.querySelectorAll(".delete_wishlist_button");
        //console.log(forms.parentElement);
        for (let i = 0; i < buttons.length; i++) {
            let item = buttons[i].parentElement.parentElement;
            buttons[i].onclick = function() {
                console.log(item.id);
                const request = new Request("delete",
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
                    
                    //item.remove();
                    return false;
                })
                item.style.animationPlayState = "running";
                item.onanimationend = () => {
                    item.remove();
                }
            }
        }
}