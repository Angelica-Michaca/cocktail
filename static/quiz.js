/**
 * ingredients the array of ingredients to choose from
 * glass the array of ingredients that are added to the glass
 */


/**
 * This function adds instructions and title dynamically. 
 */

let score = 0;
let initialIngredients = []
 

function copyArray(){
    for (i = 0; i < ingredients.length; i++) {
        initialIngredients[i] = ingredients[i] 
    }
}

function addInstruction() { // for 3 drinks, make arrays of title / instructions in server.py and use that to create html dynamically
    $("#title").append("Margarita Quiz")
    $("#instruction").append("Drag and drop the necessary ingredients into the glass in the correct order to make a Margarita.")
    $("#glassInstruction").append("In your glass:")
}

/**
 * This function adds images of the ingredients dynamically. 
 */
function addImages() {
    let new_post = $("<div class='col-md ingredients'>  <img src='https://dtgxwmigmg3gc.cloudfront.net/imagery/assets/derivations/icon/256/256/true/eyJpZCI6IjVmNGIyODYyMzNkZTU4OThjZGNhMDEwMzkyODAzZWIzIiwic3RvcmFnZSI6InB1YmxpY19zdG9yZSJ9?signature=c07842b684848512ce6ef7cc21f9d4df6bdc535d08bc520aa570dd17bfa2de6f' alt='limeJuice' draggable='true' width ='100' height = '100'></div>")
    new_post.data("value", ingredients[0])
    $("#ingredientsRow").append(new_post)

    new_post = $("<div class='col-md ingredients'>  <img src='https://dtgxwmigmg3gc.cloudfront.net/imagery/assets/derivations/icon/256/256/true/eyJpZCI6IjVmNGIyODYyMzNkZTU4OThjZGNhMDEwMzkyODAzZWIzIiwic3RvcmFnZSI6InB1YmxpY19zdG9yZSJ9?signature=c07842b684848512ce6ef7cc21f9d4df6bdc535d08bc520aa570dd17bfa2de6f' alt='orangeJuice' draggable='true' width ='100' height = '100'></div>")
    new_post.data("value", ingredients[1])
    $("#ingredientsRow").append(new_post)

    new_post = $("<div class='col-md ingredients'>  <img src='https://dtgxwmigmg3gc.cloudfront.net/imagery/assets/derivations/icon/256/256/true/eyJpZCI6IjVmNGIyODYyMzNkZTU4OThjZGNhMDEwMzkyODAzZWIzIiwic3RvcmFnZSI6InB1YmxpY19zdG9yZSJ9?signature=c07842b684848512ce6ef7cc21f9d4df6bdc535d08bc520aa570dd17bfa2de6f' alt='ginegerSyrup' draggable='true' width ='100' height = '100'></div>")
    new_post.data("value", ingredients[2])
    $("#ingredientsRow").append(new_post)

    new_post = $("<div class='col-md ingredients'>  <img src='https://dtgxwmigmg3gc.cloudfront.net/imagery/assets/derivations/icon/256/256/true/eyJpZCI6IjVmNGIyODYyMzNkZTU4OThjZGNhMDEwMzkyODAzZWIzIiwic3RvcmFnZSI6InB1YmxpY19zdG9yZSJ9?signature=c07842b684848512ce6ef7cc21f9d4df6bdc535d08bc520aa570dd17bfa2de6f' alt='simpleSyrup' draggable='true' width ='100' height = '100'></div>")
    new_post.data("value", ingredients[3])
    $("#ingredientsRow").append(new_post)

    new_post = $("<div class='col-md ingredients'>  <img src='https://dtgxwmigmg3gc.cloudfront.net/imagery/assets/derivations/icon/256/256/true/eyJpZCI6IjVmNGIyODYyMzNkZTU4OThjZGNhMDEwMzkyODAzZWIzIiwic3RvcmFnZSI6InB1YmxpY19zdG9yZSJ9?signature=c07842b684848512ce6ef7cc21f9d4df6bdc535d08bc520aa570dd17bfa2de6f' alt='limeTequila' draggable='true' width ='100' height = '100'></div>")
    new_post.data("value", ingredients[4])
    $("#ingredientsRow").append(new_post)

    new_post = $("<div class='col-md ingredients'>  <img src='https://dtgxwmigmg3gc.cloudfront.net/imagery/assets/derivations/icon/256/256/true/eyJpZCI6IjVmNGIyODYyMzNkZTU4OThjZGNhMDEwMzkyODAzZWIzIiwic3RvcmFnZSI6InB1YmxpY19zdG9yZSJ9?signature=c07842b684848512ce6ef7cc21f9d4df6bdc535d08bc520aa570dd17bfa2de6f' alt='orangeTequila' draggable='true' width ='100' height = '100'></div>")
    new_post.data("value", ingredients[5])
    $("#ingredientsRow").append(new_post)

    new_post = $("<div class='col-md ingredients'>  <img src='https://dtgxwmigmg3gc.cloudfront.net/imagery/assets/derivations/icon/256/256/true/eyJpZCI6IjVmNGIyODYyMzNkZTU4OThjZGNhMDEwMzkyODAzZWIzIiwic3RvcmFnZSI6InB1YmxpY19zdG9yZSJ9?signature=c07842b684848512ce6ef7cc21f9d4df6bdc535d08bc520aa570dd17bfa2de6f' alt='lemonTequila' draggable='true' width ='100' height = '100'></div>")
    new_post.data("value", ingredients[6])
    $("#ingredientsRow").append(new_post)

    new_post = $("<div class='col-md ingredients'>  <img src='https://dtgxwmigmg3gc.cloudfront.net/imagery/assets/derivations/icon/256/256/true/eyJpZCI6IjVmNGIyODYyMzNkZTU4OThjZGNhMDEwMzkyODAzZWIzIiwic3RvcmFnZSI6InB1YmxpY19zdG9yZSJ9?signature=c07842b684848512ce6ef7cc21f9d4df6bdc535d08bc520aa570dd17bfa2de6f' alt='Tequila' draggable='true' width ='100' height = '100'></div>")
    new_post.data("value", ingredients[7])
    $("#ingredientsRow").append(new_post)


}

/**
 * This function adds image of the glass dynamically. 
 */
function addGlass() {
    $("#glass-holder").append("<img src = 'https://proofmart.com/wp-content/uploads/2021/06/glass-4-web.png' alt='glass' draggable = 'false' id='glass'></img>")
}


/**
 * This function updates "in your glass" section, by appending what's in the glass array. 
 */
function updateLists() {
    let glassLength = glass.length;
    for (i = 0; i < glassLength; i++) {
        let new_post = $("<div class = glassContents>" + glass[i] + "</div>")
        new_post.data("value", glass[i])
        $("#glassInput").append(new_post)  // first in first out 
    }
}


/**
 * this function removes the ingredients in "in your glass" section.
 */
function removeLists() {
    document.querySelectorAll(".glassContents").forEach(function (a) {
        a.remove()
    })
}

function calculateScore() {
    for (i = 0; i < glass.length; i++) {
        if (glass[i] === correct_ingredients[i]) {
            score++;
        }
    }
}

function reset() {
    score = 0;
    glass = [];
    for (i = 0; i < ingredients.length; i++) {
        ingredients[i] = initialIngredients[i] 
    }

}

function undo(){
    
    if(glass.length>0){
        glass.splice(glass.length-1,1);
    }

}




$(document).ready(function () {
    copyArray()
    addInstruction()
    addImages()
    addGlass()
    updateLists()
    $(".ingredients").draggable({ revert: "valid" })
    $("#glass").droppable({  // dropping to glass
        accept: ".ingredients",


        classes: {
            "ui-droppable-hover": "highlightHover",
            "ui-droppable-active": "highlightActive"
        },

        drop: function (event, ui) {

            let name = $(ui.draggable[0]).data("value")   // when dynamically creating this, do sth like                                             
            glass.push(name)
            //remove the elem from ingredients  splice(index,1)
            let index = ingredients.indexOf(name)
            ingredients.splice(index, 1)
            //delete exising "what's in your glass"
            removeLists()
            //update new "what's in your glass"
            updateLists()
            $(".ingredients").draggable({ revert: "valid" })

            //for debugging purpose, console.log the arrays
            console.log("glass: " + glass)
            console.log("ingredients: " + ingredients)
            console.log("correct_ingredients:" + correct_ingredients)
        }
    })


    $("#submitButton").click(function () {
        calculateScore()
        console.log(score)
    })

    $("#resetButton").click(function () {
        reset();
        removeLists()
        updateLists()
    })

    $("#undoButton").click(function () {
        undo();
        removeLists()
        updateLists()
    })
})
