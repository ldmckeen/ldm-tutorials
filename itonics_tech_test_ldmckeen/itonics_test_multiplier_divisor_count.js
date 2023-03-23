// ITONICS Test Questions
// ====================================================

// Array Count of Multipliers and Divisors
// ~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o

function countMultiplesAndDivisors(arr) {
    // Set up  Result Set Array with default 0 integer values.
    let result_arr =  new Array(arr.length).fill(0);

    // Nested Loop through the arr, checking Multipliers and Divisors of each element
    // against the other elements.
    for (let i_index = 0; i_index < arr.length; ++i_index) {
        let count = 0;  // Set counter for each parent iteration
        console.log(count)
        for (let j_index = 0; j_index < arr.length; ++j_index) {
            // If current element is same as element were calculating for, move to next
            // nested loop iteration.
            if (j_index === i_index) {
                continue;
            }
            // Using Modulo operator check if outcomes of item divided by other elements
            // in the list have a zero remainder to confirm if multiplier/divisor and
            // increment counter if so.
            else if (arr[j_index] % arr[i_index] === 0 || arr[i_index] % arr[j_index] === 0) {
                count++;
            }
        }
        // Store count in result array for current i_index element.
        result_arr[i_index] = count;
    }
    console.log(result_arr);
    return result_arr;
}

// Test Inputs
// =========================================
let input = [6, 8, 9, 12, 24];

result = countMultiplesAndDivisors(input);


// Inventory List
// ~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o

function inventoryList() {
    return {
        // Inventory Items List Array
        inventory_items: [],

        // Function to add new item to Inventory List Array
        add: function (name) {
            // Cheque for uniqueness (i.e named item already exists in the Inventory List)
            if (this.inventory_items.includes(name)) {
                return;
            } else {
                this.inventory_items.push(name);
            }
        },
        // Function to remove item to Inventory List Array
        remove: function (name) {
            // Confirm named Item exists and retrieve it's index using splice array
            // function to delete named item/
            if (this.inventory_items.includes(name)) {
                let item_index = this.inventory_items.indexOf(name);
                this.inventory_items.splice(item_index, 1);
            }
        },
        // Simply return all current items
        getList: function () {
            return this.inventory_items;
        }
    }
}

const inventory_test = new inventoryList();
inventory_test.add("Shoes");
console.log(inventory_test.getList());
inventory_test.add("Trousers");
console.log(inventory_test.getList());
inventory_test.remove("Trousers");
console.log(inventory_test.getList());
inventory_test.add("Curtains");
console.log(inventory_test.getList());
inventory_test.remove("Shoes");
console.log(inventory_test.getList());
