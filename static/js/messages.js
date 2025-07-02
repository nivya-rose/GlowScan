document.addEventListener("DOMContentLoaded", () => {
  const msgBox = document.querySelector('.message-box');
  if (msgBox) {
    setTimeout(() => {
      msgBox.style.display = 'none';
    }, 4000);
  }
});
