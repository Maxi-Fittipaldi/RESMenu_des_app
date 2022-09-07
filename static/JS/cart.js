const cart = document.getElementsByClassName("products-in-cart")[0];
const productsContainer = document.getElementsByClassName("products-container")[0];
const confirmButton = document.querySelector("body > button")
const addToCartButton = document.querySelectorAll(".addToCart");
let ids = [];
console.log(addToCartButton);
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
for(let i = 0; i < addToCartButton.length; i++){
    addToCartButton[i].addEventListener("click",() =>{
        let productId = addToCartButton[i].name;
        const product = productsContainer.querySelector("[name='"+productId+"']");
        const quantity = product.getElementsByTagName("input")[0];
        const AddButton = product.getElementsByTagName("button")[0];
        ids.push({"product_id":productId, "quantity":quantity.value});
        quantity.remove()
        const clonedProd = product.cloneNode(true);
        addToCartButtonNew = clonedProd.getElementsByTagName("button")[0];
        addToCartButtonNew.remove();
        console.log(clonedProd)
        clonedProd.innerHTML += "<p>"+quantity.value+"</p>" 
        cart.appendChild(clonedProd);
        AddButton.remove()
    });
}

confirmButton.addEventListener("click", () => {
    data = JSON.stringify({"product_ids": ids});
    fetch('/menu/commit', {
    method: 'POST', // or 'PUT'
    headers: {
        'Content-Type': 'application/json',
    },
    body: data,
    })
    .then((response) => console.log(response))
    .then(() => {
        console.log('Success');
        window.location.reload();
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
