const productsContainer = document.getElementsByClassName("products-container")[0];
const productsInCart = document.getElementsByClassName("products-in-cart")[0];

const addToCart = (id) => {
    const product = productsContainer.querySelector("[name='"+ id +"']");
    const clonedProd = product.cloneNode(true);
    productsInCart.appendChild(clonedProd);
}
