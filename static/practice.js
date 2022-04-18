/**
 * This function populates the text in the page. 
 */
let correct_answers = 0;

 function populateText(){

    //POPULATE TEXT
    $.each(ingredients_in_order, function(i, ingredient){
        let label = $("<label for='ingredient_"+i+"'>First, add <span id='ingredient_"+i+"_vol'></span></label>");
        $("#practice-questions").append(label);

        let input = $("<input type='text' id='ingredient_"+i+"' class='no-outline' name='ingredient_"+i+"' placeholder='insert name of ingredient'>");
        $("#practice-questions").append(input);

        let check_button = $("<input id='ingredient_"+i+"_check' class='check' type='submit' value='Check'>");
        $("#practice-questions").append(check_button);

        let break_tag = $("<br><br>");
        $("#practice-questions").append(break_tag);

        $("#ingredient_"+i+"_check").click(function() {
          checkAnswer(i);
      });
    });

    // POPULATE HINT HEADER
    let hint_header = $("<div class='quizBodyText'>Need a hint?</div><button class='btn btn-light btn-lg'  id='showHint' type='button' onclick='toggleHint()'>Show ingredients list</button>");

    $("#hintBox").append(hint_header);

    //POPULATE LIST OF INGREDIENT
    let hint_list = $("<div class='row invisible' id='hint_list'>");
    $("#hintBox").append(hint_list);

    $.each(all_ingredients_with_volume, function(i, ingredient){
        //Create card element
        let ing_card = $("<div class='custom-white-card'>");

        //Create card img
        let ing_card_img = $("<img class='card-img-top' src='"+ ingredient.ingredient_image +"'>");
        
        //Append card img to card
        $(ing_card).append(ing_card_img);

        //Create card body
        let ing_card_body = $("<div class='card-body'>");

        //Append card body to card
        $(ing_card).append(ing_card_body);

        //Create artist name
        let ing_name = $("<h5>"+ ingredient.name +"</h5>");
        $(ing_card_body).append(ing_name);

        //Create ing volume
        let ing_volume = $("<p class='card-text'>"+ ingredient.volume +" oz</p>");
        $(ing_card_body).append(ing_volume);

        //Append finished card to row
        $(hint_list).append(ing_card);
    });
}

function populateVolumes() {
    $.each(ingredients_in_order, function(i, ingredient){
        let volume = all_ingredients_with_volume[ingredient]["volume"];
        if(volume == "N/A"){
            $("#ingredient_"+i+"_vol").html("some ");
        }
        else{
            $("#ingredient_"+i+"_vol").html(volume + " oz of ");
        }
    })
}

function checkAnswer(i){
    let user_input = $("#ingredient_"+i).val();
    if(user_input.toLowerCase() == ingredients_names_in_order[i].toLowerCase()){
        $("#ingredient_"+i+"_check").removeClass("wrong-background");
        $("#ingredient_"+i+"_check").addClass("right-background");
        correct_answers = correct_answers + 1
    }
    else{
        $("#ingredient_"+i).val("");
        $("#ingredient_"+i+"_check").removeClass("right-background");
        $("#ingredient_"+i+"_check").addClass("wrong-background");
        correct_answers = correct_answers - 1
    }

    if(correct_answers == 4){
        quizButton();
    }
}

function toggleHint(){
    if ($("#hint_list").hasClass("visible")){
        $("#hint_list").removeClass("visible")
        $("#hint_list").addClass("invisible")
        $("#showHint").html("Show ingredients list");
    }else{
        $("#hint_list").removeClass("invisible")
        $("#hint_list").addClass("visible")
        $("#showHint").html("Hide ingredients list");
    }
}

function quizButton(){
    $(".row.headers").empty();
    let congrats = $("<div class='quizBodyText'>Well done</div><div class='quizBodyText'>Your drink is ready.</div><div class='quizBodyText'>Are you ready for a harder quiz?</div>");
    let quiz_button = $("<a class='btn btn-light btn-lg' href='http://127.0.0.1:5000/quiz/"+drink_info.link+"'>Take the Quiz</a>");
    let back_button = $("<a class='btn btn-light btn-lg' href='http://127.0.0.1:5000/'>Back to Home</a>");
    $(".row.headers").append(congrats);
    $(".row.headers").append(quiz_button);
    $(".row.headers").append(back_button);
}

$(document).ready(function(){
    populateText();
    populateVolumes();
})