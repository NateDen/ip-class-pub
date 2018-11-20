//from investigation i must conclude that there's a problem. 


$(document).ready(function () {

});


var table = document.getElementById('output_table');
var t_body = $('#all_output_rows');


function addToList() {

    //there is another way to do this, see here:
    //https://stackoverflow.com/questions/16722752/javascript-function-call-in-conditional-not-being-called-if-first-returns-false

    if (validateInput() != false) {
        newRow();
    }
}

function validateInput() {
    var item_name_field_input = document.forms["shopping_list_input"]["item_name_field"].value;
    if (item_name_field_input == "") {
        alert("Item name must be filled out");
        return false;
    }
}

function newRow() {


    //newoutput still exists in case for some reason i need it
    var newoutput = '<div class="container-fluid row" id="output_rows"><div class="col-lg-2 border"><input type="checkbox"></div><div class="col-lg-2 border"><p id="output_rows_item"></p></div><div class="col-lg-2 border"><p id="output_rows_quantity"></p></div><div class="col-lg-2 border"><p id="output_rows_store"></p></div><div class="col-lg-2 border"><p id="output_rows_section"></p></div><div class="col-lg-2 border"><p id="output_rows_price"></p></div></div>';

    var cell_Index = 0;
    var row = table.insertRow(-1);
    for (i = 0; i < 6; i++) {
        var cell = row.insertCell(cell_Index);
        cell_Index++;
    }

    row.setAttribute('class', 'output_rows');


    var last_row = (table.rows.length - 1);
    var first_cell = 0;

    populateRows();

    var set_row_id = $('#item_name_field').val();
    row.setAttribute('id', set_row_id);
    var row_id = row.getAttribute('id');
    document.getElementById('output_table').rows[last_row].cells[first_cell].innerHTML = "<input type='checkbox' onchange=boughtItem(" + row_id + ")>";

}

function populateRows() {


    //this is the last row, not 2nd to last :/
    var second_to_last_row = [table.rows.length - 1];

    //get priority and color based on priority
    var priority = $('#priority_field').val();
    if (priority == 'low') {
        document.getElementById('output_table').rows[second_to_last_row].setAttribute("style", "background-color: #adebad;");
    }
    if (priority == 'med') {
        document.getElementById('output_table').rows[second_to_last_row].setAttribute("style", "background-color: #ffffb3;");
    }
    if (priority == 'high') {
        document.getElementById('output_table').rows[second_to_last_row].setAttribute("style", "background-color: #ffcccc;");
    }

    var item_name = $('#item_name_field').val();
    document.getElementById('output_table').rows[second_to_last_row].cells[1].innerHTML = item_name;

    var quantity = $('#quantity_field').val();
    document.getElementById('output_table').rows[second_to_last_row].cells[2].innerHTML = quantity;

    var store = $('#store_name_field').val();
    document.getElementById('output_table').rows[second_to_last_row].cells[3].innerHTML = store;

    var section = $('#store_section_field').val();
    document.getElementById('output_table').rows[second_to_last_row].cells[4].innerHTML = section;

    var price = $('#price_field').val();
    document.getElementById('output_table').rows[second_to_last_row].cells[5].innerHTML = price;

}

function boughtItem(x) {

    x.classList.add('strike_through');

}

function removePurchased() {

}

//var row_Index = 2;

function saveList() {
    for (let row_Index = 1; row_Index < (document.getElementById('output_table').rows.length); row_Index++) {
        ark = [];
        //the output rows start at row[2]
        ark.push(document.getElementById('output_table').rows[row_Index].classList);
        ark.push(document.getElementById('output_table').rows[row_Index].cells[1].innerText);
        ark.push(document.getElementById('output_table').rows[row_Index].cells[2].innerText);
        ark.push(document.getElementById('output_table').rows[row_Index].cells[3].innerText);
        ark.push(document.getElementById('output_table').rows[row_Index].cells[4].innerText);
        ark.push(document.getElementById('output_table').rows[row_Index].cells[5].innerText);
        localStorage.setItem('row' + row_Index, JSON.stringify(ark));

        arch = [];

    }

    localStorage.setItem('broker', 'test');

}

function loadList() {
  
    //localStorage.getItem('row' + row_Index, JSON.parse(ark));
    //console.log(localStorage.getItem('row' + row_Index, JSON.parse(ark)));

    key_array = [];

    for (var i = 0; i < localStorage.length; i++) {
        console.log(localStorage.key(i));
        key_array.push(localStorage.key(i));
        //push into array
        //search in array to get all the rows
        //use them as keys to iterate through local storage and fetch values
    }

    for (key in key_array) {
        if (row in key) {
            console.log(key);
        };
    } 

    //get items from array
    //for loop to create the amount of rows in table based on how many items with row name in local storage

    //for (let local_storage_rows = 0; local_storage_rows)

    //then populate it
    //then write to cells using populate row code ie cell[1] = row1[1]
    //then add class
    
    /*
    if have class: strike through:
        apply strike through
    */
}

function removeAll() {

}

