const productsInCart = document.getElementsByClassName("products-in-cart")[0];
const productsContainer = document.getElementsByClassName("products-container")[0];
const onClick = (event) => {
    const productId = event.srcElement.id;
    const product = productsContainer.querySelector("[name='"+productId+"']");
    const clonedProd = product.cloneNode(true);
    productsInCart.appendChild(clonedProd);
}
window.addEventListener("click",onClick);