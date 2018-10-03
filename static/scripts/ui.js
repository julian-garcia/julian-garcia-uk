const mobile_button_menu = document.getElementById('mobile-menu-button');
const side_nav = document.querySelector('.side-nav');
const page_title = document.title.replace('Julian Garcia - ','');

mobile_button_menu.addEventListener('mouseup', function(e) {
  side_nav.style.display = window.getComputedStyle(side_nav).display == 'none' ? 'block' : 'none';
  e.preventDefault();
});

side_nav.addEventListener('click', function(e) {
  Array.from(side_nav.children).forEach(function(nav_button) {
    console.log(nav_button);
    if (nav_button.textContent.trim() == page_title.trim()) {
      nav_button.classList.remove('inactive-border');
      nav_button.classList.add('active-border');
      console.log(nav_button);
    } else {
      nav_button.classList.remove('active-border');
      nav_button.classList.add('inactive-border');
    }
  });
});

/* Ensure that the menu is only hidden on mobile screen sizes, otherwise */
/* a browser window resize will hide the menu across all window widths   */
window.addEventListener('resize', function(e) {
  if (window.getComputedStyle(mobile_button_menu).display == 'none') {
    side_nav.style.display = 'block';
  } else {
    side_nav.style.display = 'none';
  }
  e.preventDefault();
});
