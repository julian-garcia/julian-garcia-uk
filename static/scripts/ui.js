const mobile_button_menu = document.getElementById('mobile-menu-button');
const side_nav = document.querySelector('.side-nav');
const my_name = 'Julian Garcia';
const page_title = document.title.replace(`${my_name} - `,'');
const meetups = document.querySelector('.meetups');

// On page load highlight the relevant navigation menu item based on the current page title
document.addEventListener('DOMContentLoaded', function(e) {
  Array.from(side_nav.children).forEach(function(nav_button) {
    if (nav_button.className.includes('button')) {
      if (nav_button.textContent.trim().startsWith(page_title.trim()) ||
          (page_title.trim() == my_name && nav_button.textContent.trim() == 'About Me')) {
        nav_button.classList.remove('inactive-border');
        nav_button.classList.add('active-border');
      } else {
        nav_button.classList.remove('active-border');
        nav_button.classList.add('inactive-border');
      }
    }
  });
});

mobile_button_menu.addEventListener('mouseup', function(e) {
  side_nav.style.display = window.getComputedStyle(side_nav).display == 'none' ? 'block' : 'none';
  e.preventDefault();
});

/* Ensure that the menu is only hidden on mobile screen sizes, otherwise
   a browser window resize will hide the menu across all window widths   */
window.addEventListener('resize', function(e) {
  if (window.getComputedStyle(mobile_button_menu).display == 'none') {
    side_nav.style.display = 'block';
  } else {
    side_nav.style.display = 'none';
  }
  e.preventDefault();
});

window.addEventListener('click', function(e) {
  const target_classes = e.target.className;

  // Close the curently displayed modal
  if (target_classes.includes('modal-close') || target_classes.includes('modal-background')) {
    e.target.parentElement.style.display = 'none';
  }

  // Show the relevant portfolio screenshot by passing the modal attribute of the modal trigger
  // link to retrieve and show the modal with an id that matches the attribute
  if ((target_classes.includes('portfolio-link') &&
       target_classes.includes('screenshot')) || target_classes.includes('portfolio-image')) {
    const modal_attribute = e.target.getAttribute('modal');
    document.getElementById(modal_attribute).style.display = 'block';
    e.preventDefault();
  }
});
