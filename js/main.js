'use strict';


const carInfo = async () => {
    const user = document.getElementById("nameOfCar").value;

    await fetch("http://localhost:8000/cars",{
        method: "post",
        header: {"content-type": "application/json"},
        body: user,
    })

}

 

function showInfo(Car) {
    const carName = document.getElementById('nameOfCar');
    carName.innerText = Car.name;

   
};

showInfo();