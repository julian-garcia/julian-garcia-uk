const notes_filter_div = document.querySelector('.category-filter');
const notes = document.querySelector('.notes-content');

notes_filter_div.addEventListener('click', function(e) {
  Array.from(notes_filter_div.children).forEach(function(filter) {
    filter.classList.remove('active-border');
    filter.classList.add('inactive-border');
  });

  // Show/hide note cards by matching the data-category attibute value of
  // the selected filter button against the same attribute of each card
  Array.from(notes.children).forEach(function(note) {
    if (note.className.includes('card') && e.target.getAttribute('data-category') != null) {
      if (e.target.getAttribute('data-category') == note.getAttribute('data-category')) {
        note.classList.add('is-block');
        note.classList.remove('is-hidden');
        e.target.classList.add('active-border');
        e.target.classList.remove('inactive-border');
      } else {
        if (e.target.getAttribute('data-category') == 'all') {
          note.classList.remove('is-hidden');
          note.classList.remove('is-block');
          e.target.classList.add('active-border');
          e.target.classList.remove('inactive-border');
        } else {
          note.classList.add('is-hidden');
          note.classList.remove('is-block');
        }
      }
    }
  });

  e.preventDefault();
});
