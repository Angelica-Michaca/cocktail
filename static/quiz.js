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
     $("#title").append( drink )
     $("#instruction").append("Drag and drop the necessary ingredients into the glass in the correct order to make a "+ drink + ".")
    $("#glassInstruction").append("In your glass:")
}

/**
 * This function adds images of the ingredients dynamically. 
 */
function addImages() {
    let new_post = $("<div class='col-lg-1 ingredients' id = 'Fresh Lime Juice'>  <img src='/static/images/fresh_lime_juice.png' alt='Fresh Lime Juice' draggable='true' width ='100' height = '100'>Fresh Lime Juice</div>")
    new_post.data("value", ingredients[0])
    $("#ingredientsRow").append(new_post)

    new_post = $("<div class='col-lg-1 ingredients' id = 'Pineapple Juice'>  <img src='/static/images/pineapple_juice.png' alt='Pineapple Juice' draggable='true' width ='100' height = '100'>Pineapple Juice</div>")
    new_post.data("value", ingredients[1])
    $("#ingredientsRow").append(new_post)

    new_post = $("<div class='col-lg-1 ingredients'  id = 'Ginger Syrup'>  <img src='/static/images/ginger_syrup.png' alt='Ginger Syrup' draggable='true' width ='100' height = '100'>Ginger Syrup</div>")
    new_post.data("value", ingredients[2])
    $("#ingredientsRow").append(new_post)
    
    new_post = $("<div class='col-lg-1 ingredients' id = 'Simple Syrup'>  <img src='/static/images/simple_syrup.png' alt='Simple Syrup' draggable='true' width ='100' height = '100'>Simple Syrup</div>")
    new_post.data("value", ingredients[3])
    $("#ingredientsRow").append(new_post)

    new_post = $("<div class='col-lg-1 ingredients' id = 'Orange Tequila'>  <img src='/static/images/orange_tequila.png' alt='Orange Tequila' draggable='true' width ='100' height = '100'>Orange Tequila</div>")
    new_post.data("value", ingredients[4])
    $("#ingredientsRow").append(new_post)

    new_post = $("<div class='col-lg-1 ingredients' id = 'Tequila'>  <img src='/static/images/tequila.png' alt='Tequila' draggable='true' width ='100' height = '100'>Tequila</div>")
    new_post.data("value", ingredients[5])
    $("#ingredientsRow").append(new_post)

    new_post = $("<div class='col-lg-1 ingredients' id = 'Vodka'>  <img src='/static/images/vodka.png' alt='Vodka' draggable='true' width ='100' height = '100'>Vodka</div>")
    new_post.data("value", ingredients[6])
    $("#ingredientsRow").append(new_post)

    new_post = $("<div class='col-lg-1 ingredients' id = 'Ginger Beer'>  <img src='/static/images/ginger_beer.png' alt='Giner Beer' draggable='true' width ='100' height = '100'>Giner Beer</div>")
    new_post.data("value", ingredients[7])
    $("#ingredientsRow").append(new_post)

    new_post = $("<div class='col-lg-1 ingredients' id = 'Cream of Coconut'>  <img src='/static/images/cream_of_coconut.png' alt='Cream of Coconut' draggable='true' width ='100' height = '100'>Cream of Coconut</div>")
    new_post.data("value", ingredients[8])
    $("#ingredientsRow").append(new_post)
}

/**
 * This function adds image of the glass dynamically. 
 */
function addGlass() {
    $("#glass-holder").append("<img src = 'https://dxf1.com/images/jdownloads/screenshots/wine-glass-01.png' alt='glass' draggable = 'false' id='glass'></img>")
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

    // if added more than 4, each additional element is -1 point
    if(glass.length >4){
        score = score - (glass.length -4);
    }
}

function reset() {
    score = 0;
    glass = [];
    for (i = 0; i < ingredients.length; i++) {
        ingredients[i] = initialIngredients[i] 
    }

}

function removeSpecificIngredientImage(ingredient){
    // let str = "#"+ingredient;
    // console.log("");
    document.getElementById((ingredient)).remove()
 
}

function undo(){
    if(glass.length>0){
       let lastItem = glass[glass.length-1];
        console.log(lastItem);
        removeSpecificIngredientImage(lastItem);

        //add ingredient back to the row
        lastItemJpeg = undo_dict[lastItem]

        

        new_post = $("<div class='col-lg-1 ingredients' id = " + lastItem + ">  <img src=" + lastItemJpeg + " draggable='true' width ='100' height = '100' alt= " + lastItem +">"+lastItem+"</div>")
        new_post.data("value", lastItem)
        $("#ingredientsRow").append(new_post)

        glass.splice(glass.length-1,1);
    }

}




$(document).ready(function () {
    copyArray()
    addInstruction()
    addImages()
    addGlass()
    updateLists()
    $(".ingredients").draggable({ revert: "false" })
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
            $(".ingredients").draggable({ revert: "false" })

            //for debugging purpose, console.log the arrays
            console.log("glass: " + glass)
            console.log("ingredients: " + ingredients)
            console.log("correct_ingredients:" + correct_ingredients)
        }
    })


    $("#submitButton").click(function () {
       if( confirm("Do you want to submit the ingredients in your glass?")){
            calculateScore()
            if(score != 4){
            alert("You submitted a wrong answer!\nYour score is: "+score + " out of 4")
            reset();
            removeLists();
            updateLists();
            location.reload(true); 
            window.location.reload();
            }else if(score==4){
                location.href = "/quizResult/"+ drink_link;
            }
            
       }
        
        
       
    })

    $("#resetButton").click(function () {
        reset();
        removeLists()
        updateLists()
        location.reload(true); 
        window.location.reload();
    })

    $("#undoButton").click(function () {
        undo();
        removeLists()
        updateLists()
    
        
        // need to add the image for  glass[length-1] back in the row.
    })
})
