var myInput = document.getElementsByName("customer[email]")[0];
myInput.oninvalid = function() {
  myInput.setCustomValidity("Hey! the email isn't right")
};