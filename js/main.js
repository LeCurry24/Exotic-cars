'use strict';


const carInfo = async () => {

    const response = await fetch("http://localhost:8000/cars",{
        method: "get",
        headers: {"content-type": "application/json"},
        
    })
    const data = await response.json();
    showInfo(data[0])
}

 

function showInfo(nameOfCar) {
    const carName = document.getElementById('nameOfCar');
    carName.innerText = nameOfCar.name;

   
};

carInfo();