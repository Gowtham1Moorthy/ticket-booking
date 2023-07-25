function addTags() {

    var n = document.getElementById("no").value;
    if(n > 10){
        n = 10;
    }else if(n < 3){
        n = 3
    }
    for(var i = 0; i < n; i++){

        var container = document.getElementById("teamsName");
    
        var newElement = document.createElement("div");
    
        newElement.setAttribute("class", "team"+i);
        newElement.innerHTML = '<fieldset><legend>ENTER TEAM '+(i+1)+ '</legend><input type="text" placeholder="TEAM NAME" name="team'+(i)+'" id="team'+(i)+'" required><br><input type="password" name="teampass'+(i)+'" placeholder="PASSWORD" required></fieldset>';
        
        container.appendChild(newElement);
    }
    var newId = document.getElementById("newid");

    var newElement = document.createElement("div");
    newElement.setAttribute("class","newClass");
    newId.appendChild(newElement);

    //remove button
    var btn = document.getElementById('btns');
    // var no = document.getElementById('no');
    // no.remove();
    btn.remove();

    var container = document.getElementById('n');
    var newElement = document.createElement("div");
    newElement.innerHTML = '<button onclick="app()" id="btn">Sign up</button>';
    container.appendChild(newElement);

}

function app() {

    var gamepassword = document.getElementById('GamePassword');
    var gameconform = document.getElementById('conformGamePassword');
    var manager = document.getElementById('managerPassword');
    var managerconform = document.getElementById('conformManagerPassword');
    var budget = document.getElementById('budget');
    if(gamepassword.value !== gameconform.value){
        alert('GAME PASSWORD AND CONFORM PASSWORD IS NOT MATCHING');
    }
    if(manager.value !== managerconform.value){
        alert('MANAGER PASSWORD AND CONFORM PASSWORD IS NOT MATCHING');
    }
    if(budget.value > 100){
        alert("YOUR BUDGET IS GREATER THEN 100C")
    }


    var teamNames = [];

    for (var i = 0; i < document.getElementById("no").value; i++) {
        var teamInput = document.getElementById("team" + i);
        var teamName = teamInput.value;

        if (teamNames.includes(teamName)) {
            alert("This name is already used");
            return;
        }

        teamNames.push(teamName);
    }
}


//ithu manager uadiya code

function sold() {
    var text = document.getElementsByClassName('addtext')
    text.innerHTML  =  '<p>{{ row[0][1]}} is sold to {{ team[0]}}</p>'
}

// script.js
document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("nave");
    const navigationBar = document.getElementById("navigationBar");

    toggleButton.addEventListener("click", function () {
        if (navigationBar.style.display === "none") {
            navigationBar.style.display = "block";
        } else {
            navigationBar.style.display = "none";
        }
    });
});