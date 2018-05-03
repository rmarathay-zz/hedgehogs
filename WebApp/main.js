var app = new Vue({
	el: '#app',
	data: {
		brand: 'Vue Mastery',
		product: 'Socks',
		image: 'greensocks.jpg',
		inStock: true,
		// inventory: 8
		details: ["80% cotton", "20% polyester", "Gender-neutral"],
		variants: [
			{
				variantId: 2234,
				variantColor: "green",
				variantImage: "greensocks.jpg"
			},
			{
				variantId: 2235,
				variantColor: "blue",
				variantImage: "bluesocks.jpg"
			}
		],
		cart: 0
	},
	methods: {
		addToCart: function () {
			this.cart += 1
		},
		updateProduct: function (variantImage) {
			this.image = variantImage
		}
	},
	computed: {
		title() {
			return this.brand + ' ' + this.product
		}
	}
})