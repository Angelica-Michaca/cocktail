function featureCocktails(cocktail){
  let link_learn = "http://127.0.0.1:5000/learn/" + cocktail.name
  let link_quiz = "http://127.0.0.1:5000/quiz/" + cocktail.name

  let featureCode = "<div class='card'><img class='card-img-top' src='/images/ginger_beer.png' "   
  
  featureCode = featureCode + "  alt='Card image cap'><div class='card-body'> "
  featureCode = featureCode + "<div class='btn-group'>"
  featureCode = featureCode + "<a href='"+ link_learn + "'><button>"+ cocktail.name + "</button></a>"
  featureCode = featureCode + "<a href='"+ link_quiz + "'><button> Take the Quiz</button></a></div></div></div>"
  
  
  return featureCode
}

$(document).ready(function(){
  let code=""

  code=featureCocktails(cocktails.margarita)
  $("#one").append(code)

  code=featureCocktails(cocktails.pina_colada)
  $("#two").append(code)

  code=featureCocktails(cocktails.moscow_mule)
  $("#three").append(code)

})


