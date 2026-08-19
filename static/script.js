document.addEventListener("DOMContentLoaded", function () {

    console.log("Student Management System Loaded");

    updateClock();
    setInterval(updateClock, 1000);

    const searchInput = document.getElementById("searchInput");

    if(searchInput){

        searchInput.addEventListener("keyup", function(){

            const filter = this.value.toLowerCase();

            const rows = document.querySelectorAll("tbody tr");

            rows.forEach(row => {

                const text = row.innerText.toLowerCase();

                if(text.includes(filter)){
                    row.style.display = "";
                }
                else{
                    row.style.display = "none";
                }

            });

        });

    }

});

function updateClock(){

    const now = new Date();

    const clock = document.getElementById("clock");

    if(clock){
        clock.innerHTML =
        now.toLocaleDateString() +
        " | " +
        now.toLocaleTimeString();
    }

}

function showWelcome(){

    alert("Welcome to Student Management System");

}

function confirmDelete(){

    return confirm("Are you sure you want to delete this record?");

}