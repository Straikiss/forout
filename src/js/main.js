let myLink = document.getElementById('header-menu-show');
let myLink2 = document.getElementById('hidden-menu-hide');
let myElement = document.getElementById('aside-hide');
myLink.onclick = function(){myElement.style.transform = "translateX(0)";};
myLink2.onclick = function(){myElement.style.transform = "translateX(-100%)";};