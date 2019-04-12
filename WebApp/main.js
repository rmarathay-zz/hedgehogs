// // import Tabs from 'vue-tabs-component'
// // import Tab from 'vue-tabs-component'
// Vue.component('tabs', Tabs);
// // Vue.component('Tab', Tab);
    
// // new Vue({
// // 	el:'#vue-tabs-component'
// // })

// new Vue({
//     el: '#app', 
//     data: {
// 		message: 'Hedgehogs'
// 	},

// })
new Vue({
    el: '#app',
    data: {
        choice: 'homeActive',
        image: 'charticon.png'
    },
    methods: {
        makeActive: function(val) {
            this.choice = val;
        },
        isActiveTab: function(val) {
          return this.choice === val;
        }
    }
});