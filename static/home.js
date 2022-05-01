//This function dynamically creates the three cocktail cards on the home page
function featureCocktails(){
  let new_card = $("<div class = 'col-md-4 '><div class='card custom-card customHomeCard text-center '> <div class = 'ratio-images'> <img class='card-img-top' src='" + cocktails[drink]['image'] + "' alt='card image cap' /> </div> <div class='card-body'> <div class='btn-container'> <a href=" + cocktails[drink]['learnUrl'] + "><button class='btn-in-home-cards learn-drink-btn'>" + cocktails[drink]['name']+ "</button></a> <a  href=" + cocktails[drink]['quizUrl'] + "><button class='take-quiz-btn btn-in-home-cards'>Take the Quiz</button></a></div></div></div></div>") 
  $(".homeDynamicCardsRow").append(new_card)
}


$(document).ready(function(){
  for (drink in cocktails){
    featureCocktails()

  }
  

})


