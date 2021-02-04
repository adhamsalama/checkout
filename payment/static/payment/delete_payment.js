document.addEventListener("DOMContentLoaded", () => {
    let buttons = document.querySelectorAll(".payment_delete_button");
    for(let i = 0; i < buttons.length; i++) {
        buttons[i].onclick = function() {
            let item_div = buttons[i].parentElement.parentElement;
            let request = new Request("delete_payment", {
                headers: {'X-CSRFToken': getCookie("csrftoken")}
            }
            );
            fetch(request, {
                method: "POST",
                body: JSON.stringify({
                    payment_id: item_div.id
                })
            })
            .then(response => response.json())
            .then (result => {
                console.log(result);
            })
            item_div.style.animationPlayState = "running";
            item_div.onanimationend = () => {
                item_div.remove();
            }
            return false;
        }
    }
});