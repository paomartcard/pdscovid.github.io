function openModal(identifier) {
  var toShow = document.getElementById(identifier);
  var back = document.getElementById("backgrounder");
  toShow.style.display = "block";
  back.style.display = "block";
}

function closeModal(identifier){
  var toHide = document.getElementById(identifier);
  var back = document.getElementById("backgrounder");
  toHide.style.display = "none";
  back.style.display = "none";
}

function w3_open() {
  document.getElementById("mySidebar").style.display = "block";
}

function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
}
