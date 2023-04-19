// // category js
const dropdiv = document.getElementById('drop');
const dropdown = document.getElementById('dropdown');
 const element = document.querySelector('.dropdown');
dropdiv.addEventListener("mouseover", () => {
  if (element.classList.contains("dropdown")) {
    console.log("my-class exists");
    element.classList.add("hidedropdown");
    element.classList.remove("dropdown");
    element.classList.remove("hidenow");
    element.classList.remove("showdrop");
  } else if (element.classList.contains("hidedropdown")) {
    console.log("my-class does not exist");
    element.classList.add("hidenow");
    element.classList.add("dropdown");
    element.classList.add("showdrop");
  }
});

// cart dropdown
function cartdrop() {
    
  var hidecart = document.getElementById("cartdropdownhide");
    if (hidecart.style.display === "none") {
      hidecart.style.display = "block";
    } else {
      hidecart.style.display = "none";
    }
  }




