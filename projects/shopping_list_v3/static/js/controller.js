var stores = ['Fareway', 'Ace Hardware', 'Caseys', 'The Hatchery', 'Amundsens']
var sections = ['Produce', 'Meats', 'Cereal', 'Canned Goods', 'Frozen Foods', 'Dairy', 'Liquor', 'Tools', 'Clothing']

var shoppingModel = new ShoppingList()
var myView = new ShoppingView(shoppingModel)

function clickedon() {
    let rowcolids = ['itemname', 'qty', 'store', 'category', 'price', 'priority']
    let vals = {}
    for (let cid of rowcolids) {
        vals[cid] = document.getElementById(cid).value;
    }
    let it = new Item(vals.itemname, vals.qty, vals.priority, vals.store, vals.category, vals.price)
    shoppingModel.addItem(it)
    
}

function populateSelect(selectId, sList) {
    let sel = document.getElementById(selectId, sList)
    for (let s of sList) {
        let opt = document.createElement("option")
        opt.value = s
        opt.innerHTML = s
        sel.appendChild(opt)
    }
}

function saveList() {
 
    localStorage.setItem('row', (JSON.stringify(shoppingModel.newItems)));
     
    var xhr = new XMLHttpRequest();
    var url = "http://localhost:5000/save";
    xhr.open("POST", url, true);
    xhr.setRequestHeader("Content-Type", "application/json");   
    var data = (JSON.stringify(shoppingModel.newItems));
    xhr.send(data);
}

function loadList() {

    //var xhr = new XMLHttpRequest();
    //var url = "http://localhost:5000/get";
    //xhr.open("GET", url, true);
    //xhr.setRequestHeader("Content-Type", "application/json");
    //xhr.send();

    var url = "http://localhost:5000/get";

    $.get(url, function (data) {
        var x = JSON.parse(data);
        for (let i of x) {
            let j = new Item(i.name, i.quantity, i.priority, i.store, i.section, i.price);
            shoppingModel.addItem(j);
        }
    });


}

function deleteRow(rowclass) {

    var rows = document.getElementsByClassName(rowclass);
    for (let row of rows) {
        row.parentNode.removeChild(row);

        //this line already works
        //document.getElementsByClassName(table).deleteRow(row);

        document.getElementsByClassName('table').deleteRow(row);
    }

}

function removePurchased() {

    deleteRow('checked');
    shoppingModel.update();

}

function removeAll() {

    shoppingModel.emptyList();
    shoppingModel.update();
    localStorage.setItem('row', '');

}

$(document).ready(function () {

    populateSelect('store', stores)
    populateSelect('category', sections)
    loadList();
    
})

