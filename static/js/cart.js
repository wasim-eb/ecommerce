var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:', productId, 'Action:', action)

		console.log('USER:', user)
		if (user == 'AnonymousUser'){
			addCookieItem(productId, action)
			
		}else{
			updateUserOrder(productId, action)
		}

	})
}

//Add to cookie item function
function addCookieItem(productId, action){
	console.log('User is not logged in')

	if (action == 'add'){
		//Adds item if item is not already in the cart
		//If the item is already in the cart, it adds
		//to the quantity instead
		if (cart[productId] == undefined){
			cart[productId] = {'quantity':1}
		}else{
			cart[productId]['quantity'] += 1
		}
	}
	//Decreases the quantity of the item by 1 if
	//the item already exists in the cart.
	//If the item quantity is 1, the item
	//is removed completely from the cart
	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Remove Item')
			delete cart[productId]
		}
	}

	console.log('Cart:', cart)
	document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
	location.reload()
}


function updateUserOrder(productId, action){
	console.log('User is logged in, sending data...')

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productId': productId, 'action': action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) =>{
		    console.log('data:', data)
			location.reload()
		})
}