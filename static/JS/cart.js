const cart = document.querySelector(".cart");
const productsContainer = document.getElementsByClassName("food-dropdown_content_cards")[0];
// const cart = document.getElementById("cart");
// const productsContainer = document.getElementById("products-container");
const confirmButton =document.querySelector("#text-button\\ confirmButton");
const addToCartButton = document.querySelectorAll(".addToCart");
let ids = [];
for(let i = 0; i < addToCartButton.length; i++){
    addToCartButton[i].addEventListener("click",() =>{
        console.log(addToCartButton[i])
        let productId = addToCartButton[i].name;
        console.log(productId)
        const product = productsContainer.querySelector(`[id='card ${productId}']`);
        console.log(product)
        const quantity = product.getElementsByTagName("input")[0];
        const addButton = product.getElementsByTagName("button")[0];
        quantity.remove()
        const clonedProd = product.cloneNode(true);
        addToCartButtonNew = clonedProd.getElementsByTagName("button")[0];
        addToCartButtonNew.remove();
        console.log(clonedProd)
        const proDescDiv = product.getElementsByClassName("ver-card_headline")[0];
        const proActDiv = product.getElementsByClassName("ver-card_actions")[0];
        const descDiv = clonedProd.getElementsByClassName("ver-card_headline")[0];
        descDiv.innerHTML += `<p class="medium-body price" id="${quantity.value}">Cantidad: ${quantity.value}</p>`
        descDiv.innerHTML +=
        `
         <button class="text-button removeFromCart hvr" name="${productId}" id="text-button">
           <p class="button">
            Remover del carro
           </p>
         </button>
        `
        const removeFromCartBtn = clonedProd.querySelector(`button[name= "${productId}"]`)
        removeFromCartBtn.addEventListener("click", () => {
            cart.removeChild(clonedProd);
            proDescDiv.appendChild(quantity);
            proActDiv.appendChild(addButton);
        });
        cart.appendChild(clonedProd);
        addButton.remove();
    });
}

confirmButton.addEventListener("click", () => {
    const products = document.querySelectorAll(".cart > .ver-card");
    console.log(products)
    for(let i = 0; i < products.length; i++){
        let product = products[i];
        let productId = product.querySelector(".product-id").id;
        console.log(product);
        console.log(productId);
        let quantity = product.querySelector(".price").id;
        ids.push({"product_id":productId, "quantity":quantity});
    }
    console.log(ids);
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
