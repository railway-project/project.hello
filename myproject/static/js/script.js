function disableKeys() {
  // Disable right-click
  document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
  });

  // Disable Control + U
  document.addEventListener('keydown', function(e) {
    if (e.ctrlKey && e.keyCode === 85) {
      e.preventDefault();
    }
  });

  // Disable Control + Shift + U
  document.addEventListener('keydown', function(e) {
    if (e.ctrlKey && e.shiftKey && e.keyCode === 85) {
      e.preventDefault();
    }
  });

  // Disable Control + Shift + I
  document.addEventListener('keydown', function(e) {
    if (e.ctrlKey && e.shiftKey && e.keyCode === 73) {
      e.preventDefault();
    }
  });

  // Disable Alt key
  document.addEventListener('keydown', function(e) {
    if (e.altKey) {
      e.preventDefault();
    }
  });

  // Disable mouse right-click
  document.addEventListener('mousedown', function(e) {
    if (e.button === 2) {
      e.preventDefault();
    }
  });
}

// Call the function to disable the keys and right-click
disableKeys();


document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("contact-form");
    const submitButton = document.getElementById("submit-button");

    form.addEventListener("submit", function (event) {
        if (!form.checkValidity()) {
            event.preventDefault();
            const errorMessage = document.getElementById("error-message");
            errorMessage.textContent = "Please fill all required fields.";
            errorMessage.style.color = "red";
            errorMessage.style.marginTop = "10px";
        }
    });

    // Optional: Clear error message when user starts typing again
    const formElements = form.elements;
    for (let i = 0; i < formElements.length; i++) {
        formElements[i].addEventListener("input", function () {
            const errorMessage = document.getElementById("error-message");
            errorMessage.textContent = "";
        });
    }
});
