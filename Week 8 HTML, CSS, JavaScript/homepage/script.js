const indexPage = document.querySelector(".indexContent");

function fadeInOnLoad() {
  indexPage.classList.add('fadeIn');
}

window.addEventListener("load", fadeInOnLoad);