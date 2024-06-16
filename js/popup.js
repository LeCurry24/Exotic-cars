'use strict';

document.getElementById('carPopupBtn').addEventListener("click", function(){
        document.getElementById('backPop').style.display = 'flex';
    });

document.getElementById('popupYourselfBtn').addEventListener("click", function(){
    document.getElementById('secondPop').style.display = 'flex';
});

document.getElementById('close').addEventListener('click', function(){
    document.querySelector('#backPop').style.display = 'none';
});

document.getElementById('closeBtn').addEventListener('click', function(){
    document.querySelector('#secondPop').style.display = 'none';
});