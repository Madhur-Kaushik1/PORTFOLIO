const btn = document.querySelector('#menu-icon')
const navi = document.querySelector('.navbar')

btn.onclick = () => {
  btn.classList.toggle('fa-circle-xmark');
  navi.classList.toggle('active');
};