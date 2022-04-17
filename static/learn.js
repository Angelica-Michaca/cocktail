function showLearnPage(cocktail) {
  let name = cocktail.["name"]
  let video = cocktail.video
  let fun_fact = cocktail.facts.fun_fact
  let taste_fact = cocktail.facts.taste
  let food_fact = cocktail.facts.goes_well_with
 

  $("#name-of-drink").append(name)

  let videoCode= "<iframe width='540' height='493.2' src=' "
  videoCode = videoCode + video
  videoCode = videoCode + "'></iframe>"
  $("#video-tutorial").append(videoCode)

  let ingredientsCode=
}