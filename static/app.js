let menu_toggle = document.querySelector(".menu-toggle")
let sidebar = document.querySelector(".navigation")

menu_toggle.addEventListener('click', () => {
    menu_toggle.classList.toggle('is-active');
    sidebar.classList.toggle('is-active');
})