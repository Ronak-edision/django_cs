// Select all elements with the class 'add-cart'
let carts6 = document.querySelectorAll('.add-cart');//

// Define an array of product objects
let products = [
    {
        name: 'canon/eos r6',
        price: '800',
        incart: 0,
        tag: 'console',

    },
    {
        name: 'lX bag',
        price: '1000',
        incart: 0,
        tag: 'bag1',

    },
    {
        name: 'nikon D 850',
        price: '900',
        incart: 0,
        tag: 'camera1',

    },
    {
        name: 'ZV -E1L',
        price: '1500',
        incart: 0,
        tag: 'camera2',

    }
]

// Attach click event listeners to the 'add-cart' elements
for (let i = 0; i < carts6.length; i++) {
    carts6[i].addEventListener('click', () => {
        cartNumbers(products[i]);
        totalCost(products[i]);
    })

}

// Function to load the cart numbers from local storage
function onLoadCartNumbers() {

    let productNumbers = localStorage.getItem('cartNumbers');
    if (productNumbers) {
        document.querySelector('.carts .cart5 span').textContent = productNumbers;
    }
}

// Function to update the cart numbers in local storage
function cartNumbers(product) {

    let productNumbers = localStorage.getItem('cartNumbers');
    productNumbers = parseInt(productNumbers);

    if (productNumbers) {
        localStorage.setItem('cartNumbers', productNumbers + 1);
        document.querySelector('.carts .cart5 span').textContent = productNumbers + 1;
    } else {
        localStorage.setItem('cartNumbers', 1);
        document.querySelector('.carts .cart5 span').textContent = 1;
    }
    setItems(product);

}

function setItems(product) {


    let cartItems = localStorage.getItem('productsInCart');
    cartItems = JSON.parse(cartItems)

    if (cartItems != null) {
        if (cartItems[product.tag] == undefined) {
            cartItems = {
                ...cartItems,
                [product.tag]: product
            }
        }
        cartItems[product.tag].inCart += 1;
    } else {
        product.inCart = 1;
        cartItems = {
            [product.tag]: product
        }
    }


    localStorage.setItem("productsInCart", JSON.stringify
        (cartItems));
}

function totalCost(product) {

    let cartCost = localStorage.getItem('totalCost');


    console.log("my cartCost is", product.price);


    console.log(typeof product.price);

    if (cartCost != null) {
        cartCost = parseInt(cartCost);
        product.price = parseInt(product.price);
        localStorage.setItem("totalCost", product.price + cartCost);
    }
    else {
        localStorage.setItem("totalCost", product.price);
    }

}

function displayCart() {
    let cartItems = localStorage.getItem("productsInCart");
    cartItems = JSON.parse(cartItems);
    let productContainer = document.querySelector(".products");

    console.log(cartItems);
    if (cartItems && productContainer) {
        productContainer.innerHTML = '';
        Object.values(cartItems).map(item => {
            productContainer.innerHTML +=
                `
  <div class="product-title1">
 
  <img src="../images/${item.tag}.jcarts .cart5 span>${item.carts.cart5 span >
  </div >
                <div class="quantcarts .cart5 span> ${item.inCcarts .cart5 span> </div>
 <div class="price1">${item.price}</div>



                < div class="total1" > ${ item.inCart * item.price } </ >
                    `
        });


    }
}

onLoadCartNumbers()/*to have the number of itam in cart preserved after refresh */

displayCart();
