//This function dynamically creates the three cocktail cards on the home page
function featureCocktails(){
  let new_card = $("<div class = 'col-md-4 '><div class='card custom-card customHomeCard center-text'> <div class = 'ratio-images'> <img class='card-img-top' src='" + cocktails[drink]['image'] + "' alt='card image cap' /> </div> <div class='card-body'> <div class='btn-container'> <a href=" + cocktails[drink]['learnUrl'] + "><button class='btn-in-home-cards learn-drink-btn'>" + cocktails[drink]['name']+ "</button></a> <a  href=" + cocktails[drink]['quizUrl'] + "><button class='take-quiz-btn btn-in-home-cards'>Take the Quiz</button></a></div></div></div></div>") 
  $(".homeDynamicCardsRow").append(new_card)
}

function addTitle(){
  let new_title = $("<div class='col-md-12 welcomeLine1 center-text'>LionBar</div>");
  $(".homeTitle").append(new_title)
}

function addInstruction1(){
  let new_instruction = $("<div class='col-md-12 welcomeLine2 center-text'> Learn about drinks and how to mix them</div>");
  $(".homeInstruction1").append(new_instruction);
}

function addInstruction2(){
  let new_instruction = $("<div class='col-md-12 welcomeLine3 center-text'>Choose a drink to learn or a quiz to test your knowledge about each drink</div>");
  $(".homeInstruction2").append(new_instruction);
}


$(document).ready(function(){
  addTitle();
  addInstruction1();
  addInstruction2();
  for (drink in cocktails){
    featureCocktails();

  }
  

})


