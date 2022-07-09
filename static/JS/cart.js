const cart = document.getElementsByClassName("products-in-cart")[0];
const productsContainer = document.getElementsByClassName("products-container")[0];
const confirmButton = document.querySelector("body > form.cart > button");
const addToCartButton = document.querySelectorAll(".addToCart");
let ids = [];
console.log(addToCartButton);
for(let i = 0; i < addToCartButton.length; i++){
    addToCartButton[i].addEventListener("click",() =>{
        let productId = addToCartButton[i].name;
        ids.push(productId);
        console.log(productId);
        const product = productsContainer.querySelector("[name='"+productId+"']");
        const clonedProd = product.cloneNode(true);
        addToCartButtonNew = clonedProd.getElementsByTagName("button")[0];
        addToCartButtonNew.remove();
        console.log(clonedProd)
        cart.appendChild(clonedProd);
    });
}

confirmButton.addEventListener("click", () => {
    data.append("product", ids);
    console.log(ids);
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/menu/commit');
    xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
    xhr.send(JSON.stringify({product_ids: ids}));
});
//ver esto
// https://code-maven.com/slides/python/flask-and-ajax-plain-javascript
