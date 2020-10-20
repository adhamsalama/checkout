document.addEventListener("DOMContentLoaded", function () {
    let form = document.querySelector("#payment_form");
    form.onsubmit = function () {
        let value = document.querySelector("#id_value");
        let source = document.querySelector("#id_source");
        let date = document.querySelector("#id_date");
        let request = new Request("add_payment", {
            headers: {'X-CSRFToken': getCookie("csrftoken")}
        }
        );
        fetch(request, {
            method: "POST",
            body: JSON.stringify({
                value: value.value,
                source: source.value,
                date: date.value
            })
        })
        .then(response => response.json())
        .then (result => {
            console.log(result);
        })
        let new_payment = document.createElement("div");
        new_payment.className = "card mb-2";
        let html = `<div class="card-body">
                      <h2 class="card-title">$${value.value}</h2>
                      <p class="card-text">
                      Source: ${source.value}
                      <br>
                      Date: ${date.value}
                      </p>
                    </div>`
        new_payment.innerHTML = html;
        let list = document.querySelector("#payments_list");
        list.insertBefore(new_payment, list.firstChild);
        value.value = "";
        source.value = "";
        date.value = "";
        return false;        
    }
})