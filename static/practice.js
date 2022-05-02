/**
 * This function populates the text in the page. 
 */
let correct_answers = 0;

 function populateText(){

    //POPULATE TEXT
    $.each(ingredients_in_order, function(i, ingredient){
        let order;
        if(i == 0 || i == 3){
            if(i == 0){
                order = "First";
            }
            else{
                order = "Lastly";
            }
            
        }
        else{
            order = "Then";
        }

        let label = $("<label for='ingredient_"+i+"'>"+ order +", add <span id='ingredient_"+i+"_vol'></span></label>");
        $("#practice-questions").append(label);

        let input = $("<input type='text' id='ingredient_"+i+"' class='no-outline practice-input' name='ingredient_"+i+"' placeholder='ingredient name'>");
        $("#practice-questions").append(input);

        let check_button = $("<input id='ingredient_"+i+"_check' class='check' type='submit' value='Check'>");
        $("#practice-questions").append(check_button);

        let break_tag = $("<br><br>");
        $("#practice-questions").append(break_tag);

        $("#ingredient_"+i+"_check").click(function() {
          checkAnswer(i);
        });

        $("#ingredient_"+i).keyup(function(event) {
            if (event.keyCode === 13) {
                $("#ingredient_"+i+"_check").click();
            }
        });
    });

    // POPULATE RETURN BUTTON
    let not_ready = $("<h5 class='not-ready-text'>Not ready for the practice?</h5>");
    let return_to_learning_button = $("<a class='btn secondBtn' href='http://127.0.0.1:5000/learn/"+drink_info.link+"'>Return to Learning</a>");
    $("#practice-questions").append(not_ready);
    $("#practice-questions").append(return_to_learning_button);

    // POPULATE HINT HEADER
    let hint_header = $(" <div class='practiceHintText need-hint'>Need a hint?</div><button class='btn  btn-lg'  id='showHint' type='button' onclick='toggleHint()'>Show ingredients list</button>");

    $("#hintBox").append(hint_header);

    //POPULATE LIST OF INGREDIENT
    let hint_list = $("<div class='row invisible' id='hint_list'>");
    $("#hintBox").append(hint_list);

    $.each(all_ingredients_with_volume, function(i, ingredient){
        //Create card element
        let ing_card = $("<div class='card cardIngredientsHint'>");

        //Create row for image and info
        let info_row = $("<div class='row'>");

        //Append row for image and info to card
        $(ing_card).append(info_row);

        //Create image col + image
        let ing_card_img = $("<div class='col-md-4'><img class='imgOfIngredientsHint alcohol-img' src='"+ingredient.ingredient_image+"'alt=''/></div>");
        
        //Append card img to card
        $(info_row).append(ing_card_img);

        //Create card info
        let ing_card_info = $("<div class='col-md-8'><p class='alc-name-hint'>"+ingredient.name+"</p><p class='alc-info-hint'>Volume: "+ingredient.volume+" oz</p></div>");

        //Append card body to card
        $(info_row).append(ing_card_info);

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
    $(".empty-this").empty();
    $(".row.headers").empty();
    let congrats = $("<div class='quizBodyText'>Well done.</div>");
    let drinksReady = $("<div class = 'quizBodyText'>Your " + drink_info['name'] + " is ready. </div>");
    let drinkPic = $("<div class = 'quizBodyImg'><img class='practQuizImg'src='" +  drinksPics + "'  alt='drink image'></div>");
    let areYou = $("<div class = 'quizBodyText'>Are you ready for a </div>");
    let harder = $("<div class = 'quizBodyText'>harder Quiz? </div>");
    let quiz_button = $("<a class='btn btn-dark btn-lg-custom secondBtn'  href='http://127.0.0.1:5000/quiz/"+drink_info.link+"'>Take the Quiz</a>");
    let back_button = $("<a class='btn-lg-custom firstBtn whiteBtn' href='http://127.0.0.1:5000/'>Back to Home</a>");
    $(".row.headers").append(congrats);
    $(".drinksReady").append(drinksReady);
    $(".drinkPic").append(drinkPic);
    $(".areYou").append(areYou);
    $(".harder").append(harder);
    $(".button1").append(quiz_button);
    $(".button2").append(back_button);
}

$(document).ready(function(){
    populateText();
    populateVolumes();
})