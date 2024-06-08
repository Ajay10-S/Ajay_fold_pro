const buttons = document.querySelectorAll('.btn');
const boxes = document.querySelectorAll('.box');
const searchbox = document.getElementById("search");

// Searchbox event listener
searchbox.addEventListener('keyup', (e) => {
  const searchtext = e.target.value.toLowerCase().trim();
  filterBoxes(searchtext);
  resetActiveButton();
  buttons[0].classList.add('btn-clicked');
});

// Button event listeners
buttons.forEach((button) => {
  button.addEventListener('click', (e) => {
    e.preventDefault();
    setActiveBtn(e);
    const btnfilter = e.target.dataset.filter.toLowerCase();
    filterBoxesByButton(btnfilter);
  });
});

// Function to set active button
function setActiveBtn(e) {
  buttons.forEach((button) => {
    button.classList.remove('btn-clicked');
  });
  e.target.classList.add('btn-clicked');
}

// Function to filter boxes based on search text
function filterBoxes(searchtext) {
  boxes.forEach((box) => {
    const data = box.dataset.items.toLowerCase();
    if (data.includes(searchtext)) {
      box.style.display = 'block';
    } else {
      box.style.display = 'none';
    }
  });
}

// Function to filter boxes based on button filter
function filterBoxesByButton(btnfilter) {
  boxes.forEach((box) => {
    const boxfilter = box.dataset.items.toLowerCase();
    if (btnfilter === 'all') {
      box.style.display = 'block';
    } else {
      if (boxfilter === btnfilter) {
        box.style.display = 'block';
      } else {
        box.style.display = 'none';
      }
    }
  });
}

// Function to reset active button
function resetActiveButton() {
  buttons.forEach((button) => {
    button.classList.remove('btn-clicked');
  });
}
