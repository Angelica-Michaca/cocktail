function display_drinksCardRow(cocktail_name, imgLink){

  var drinksCardRow = "<div class = ' col-md-4'><div class = 'card text-center'><div class = 'card-body custom-card'> <div class = 'pic-of-drink'>"
  drinksCardRow = drinksCardRow + "<img src='" + imgLink + "'></img></div>"
  
  drinksCardRow = drinksCardRow + "<div class = 'drinkNameBtn'><a href='/learn/'" + cocktail_name +"'>"+ cocktail_name
  
  drinksCardRow = drinksCardRow + "</a></div>"
  drinksCardRow = drinksCardRow + "<div class = 'takeQuizBtn'><a href= '/quiz/' " + cocktail_name + "'>Take the Quiz"

  spotlight_row = spotlight_row + "</a></div>"

  $(".home-row").append(drinksCardRow);

}



$(document).ready(function(){

  let c1_name = cocktails[1].name
  let imgLink1 = cocktails[1].image

  let c2_name = cocktails[2].name
  let imgLink2 = cocktails[2].image

  let c3_name = cocktails[3].name
  let imgLink3 = cocktails[3].image
  
  display_cocktails(c1_name, imgLink1)
  display_cocktails(c2_name, imgLink2)
  display_cocktails(c3_name, imgLink3)

})
