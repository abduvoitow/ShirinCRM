// Login Parol
const togglePassword = document.getElementById("togglePassword");
const password = document.getElementById("password");
const eyeIcon = document.getElementById("eyeIcon");

togglePassword.addEventListener("click", function () {
  const type = password.getAttribute("type") === "password" ? "text" : "password";
  password.setAttribute("type", type);

  if (type === "text") {
    eyeIcon.classList.remove("bi-eye");
    eyeIcon.classList.add("bi-eye-slash");
    eyeIcon.innerHTML = '<path d="M13.359 11.238A8.47 8.47 0 0 0 16 8s-3-5.5-8-5.5a7.94 7.94 0 0 0-3.146.641l.827.827A6.996 6.996 0 0 1 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.134 13.134 0 0 1 14.828 8c-.273.406-.593.825-.953 1.238l.832.832a14.065 14.065 0 0 0 .652-.832zM2.94 1.646 1.646 2.94l2.004 2.004C2.679 6.406 1.172 8 1.172 8s3 5.5 8 5.5c1.264 0 2.433-.306 3.475-.84l2.139 2.14 1.293-1.294L2.94 1.646zm3.036 4.33 1.337 1.337A3 3 0 0 0 8 11a3 3 0 0 0 1.996-5.24l1.385 1.385A1.993 1.993 0 0 1 10 9a2 2 0 0 1-2-2c0-.395.116-.761.31-1.064l1.39 1.39a1 1 0 0 1-1.406-1.406L5.975 5.975z"/>';
  } else {
    eyeIcon.classList.remove("bi-eye-slash");
    eyeIcon.classList.add("bi-eye");
    eyeIcon.innerHTML = '<path d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8a13.133 13.133 0 0 1-1.66 2.043C11.879 11.332 10.12 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.133 13.133 0 0 1 1.172 8z"/><path d="M8 5a3 3 0 1 0 0 6a3 3 0 0 0 0-6zM8 9a1 1 0 1 1 0-2a1 1 0 0 1 0 2z"/>';
  }
});



