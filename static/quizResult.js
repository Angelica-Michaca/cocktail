


 


function addInstruction() { // for 3 drinks, make arrays of title / instructions in server.py and use that to create html dynamically
    $("#title").append("Margarita Quiz Result")
    $("#instruction").append("You Mastered the Margarita! Congratulations on learning how to make this cocktail. Are you ready to learn how to make other cocktails?")
}


$(document).ready(function () {
  
    addInstruction()

    $("#pinaColadaButton").click(function () {
      console.log("send me to pinacolada learning page")

    })

    $("#moscowMuleButton").click(function () {
        console.log("send me to moscowmule learning page")
    })

    $("#backToHomePageButton").click(function () {
        location.href = "/home";
    })
})
