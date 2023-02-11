function submitForm() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  if (username === "admin" && password === "password") {
    alert("Login Successful!");
  } else {
    alert("Incorrect username or password");
  }
}
