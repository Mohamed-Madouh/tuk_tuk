document.addEventListener("DOMContentLoaded", function () {
  const currentPage = window.location.pathname.split("/").pop();

  if (currentPage === "index.html") {
    const loginForm = document.getElementById("login-form");
    if (loginForm) {
      loginForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const email = loginForm
          .querySelector('input[name="email"]')
          .value.trim();
        const password = loginForm
          .querySelector('input[name="password"]')
          .value.trim();

        setTimeout(() => {
          if (email === "khaledabdo99@gmail.com" && password === "password") {
            alert("تم تسجيل الدخول بنجاح!");
            window.location.href = "home.html";
          } else {
            alert("البريد الإلكتروني أو كلمة المرور غير صحيحة");
          }
        }, 1000);
      });
    }
  }
});
