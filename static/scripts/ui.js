const mobile_button_menu = document.getElementById('mobile-menu-button');
const side_nav = document.querySelector('.side-nav');

mobile_button_menu.addEventListener('mouseup', function(e) {
  side_nav.style.display = window.getComputedStyle(side_nav).display == 'none' ? 'block' : 'none';
  e.preventDefault();
});

window.addEventListener('resize', function(e) {
  if (window.getComputedStyle(mobile_button_menu).display == 'none') {
    side_nav.style.display = 'block';
  } else {
    side_nav.style.display = 'none';
  }
  e.preventDefault();
});
