
function showAlcoholName(){
  let alcname = $("<div id='title>" + drink["name"] + "</div>")
  $(".containerGray").append(alcname)
}    


$(document).ready(function () {
  showAlcoholName()

})
