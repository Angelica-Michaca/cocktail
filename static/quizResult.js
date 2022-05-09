function addInstruction() { // for 3 drinks, make arrays of title / instructions in server.py and use that to create html dynamically
    $("#title").append(drink_list[0]+ " Quiz Result")
    $("#feedback").append("You scored 4/4!<br>You Mastered the " + drink_list[0]+"!");
    $("#drinkImage").append("<img src="+drink_image +" alt='+drink+' width ='470' height = '400'>")
    $("#instruction").append("Congratulations on learning how to make this cocktail.<br> Are you ready to learn how to make other cocktails?")
}

function addButtons(){
   $("#otherDrinkToLearn1").append("<button class='btn ' id='quizResultButton1' type='button'>"+drink_list[1]+"</button>")
   $("#otherDrinkToLearn2").append("<button class='btn ' id='quizResultButton2' type='button'>"+drink_list[2]+"</button>")
}


$(document).ready(function () {
  
    addInstruction()
    addButtons()

    $("#otherDrinkToLearn1").click(function () {
        location.href = "/learn/"+drink_link[0];

    })

    $("#otherDrinkToLearn2").click(function () {
        location.href = "/learn/"+drink_link[1];
    })

    $("#backToHomePageButton").click(function () {
        location.href = "/home";
    })
})
