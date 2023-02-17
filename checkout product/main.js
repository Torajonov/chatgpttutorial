// Load product data from JSON file
fetch('products.json')
	.then(response => response.json())
	.then(products => {
		// Initialize cart
		let cart = [];

		// Render product list
		const productList = document.getElementById('product-list');
		products.forEach(product => {
			const tr = document.createElement('tr');
			tr.innerHTML = `
				<td>${product.name}</td>
				<td>$${product.price.toFixed(2)}</td>
				<td><input type="number" value="0" min="0"></td>
				<td><button onclick="addToCart(${product.id})">Add to Cart</button></td>
			`;
			productList.appendChild(tr);
		});

		// Update cart and display on page
		function addToCart(productId) {
			const quantity = parseInt(document.querySelector(`#product-list tr:nth-child(${productId}) input`).value);
			if (quantity > 0) {
				const product = products.find(p => p.id === productId);
				const item = cart.find(i => i.id === productId);
				if (item) {
					item.quantity += quantity;
				} else {
					cart.push({
						id: product.id,
						name: product.name,
						price: product.price,
						quantity: quantity
					});
				}
				displayCart();
			}
		}

		// Display cart on page
		function displayCart() {
			const cartList = document.getElementById('cart-list');
			cartList.innerHTML = '';
			let total =
