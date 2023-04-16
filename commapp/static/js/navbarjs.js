const myDiv = document.getElementById('drop');
const dropdown = document.getElementById('dropdown');
 const element = document.querySelector('.dropdown');
myDiv.addEventListener('mouseover', () => {
  
if (element.classList.contains('dropdown')) {
  console.log('my-class exists');
  element.classList.add('hidedropdown');
  element.classList.remove('dropdown');
  element.classList.remove('hidenow');
   element.classList.remove("see");
} else if (element.classList.contains('hidedropdown')){
  console.log('my-class does not exist');
element.classList.add('hidenow');
  element.classList.add('dropdown');
  element.classList.add("see");
}
});
