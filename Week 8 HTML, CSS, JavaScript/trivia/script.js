const button = document.querySelectorAll(".answerButton");
const input = document.querySelector(".input");
const buttonSubmit = document.querySelector(".submitButton");
const text = document.createElement('p');
const correctAnswer = '1 person per 6 sheep';
const correctAnswerTheSecond = 'Switzerland';

//change button color and add text depending on which button is clicked
function changeColorOnCorrectAnswer(e) {
  if (e.target.textContent === correctAnswer) {
    e.target.classList.add('correctAnswerColor');
    text.textContent = 'Correct!';
    text.style.position = 'absolute';
    e.target.appendChild(text);
  } else {
    e.target.classList.add('incorrectAnswerColor');
    text.textContent = 'Incorrect!';
    text.style.position = 'absolute';
    e.target.appendChild(text);
  }
}

// change input color depending if the answer is correct or not
function changeColorOnCorrectInput(e) {
  e.preventDefault();
  if (input.value === correctAnswerTheSecond) {
    input.classList.add('correctAnswerColor');
    input.classList.remove('incorrectAnswerColor');
  }
  if (input.value !== correctAnswerTheSecond) {
    input.classList.add('incorrectAnswerColor');
    input.classList.remove('correctAnswerColor');
  }
}

button.forEach(button => button.addEventListener('click', changeColorOnCorrectAnswer));
buttonSubmit.addEventListener('click', changeColorOnCorrectInput);