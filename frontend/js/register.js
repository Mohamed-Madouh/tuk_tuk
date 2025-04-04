document.addEventListener("DOMContentLoaded", function () {
  const currentPage = window.location.pathname.split("/").pop();

  if (currentPage === "register.html") {
    const registerForm = document.getElementById("register-form");
    if (registerForm) {
      registerForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const firstName = registerForm
          .querySelector('input[name="firstName"]')
          .value.trim();
        const lastName = registerForm
          .querySelector('input[name="lastName"]')
          .value.trim();
        const phone = registerForm
          .querySelector('input[name="phone"]')
          .value.trim();
        const email = registerForm
          .querySelector('input[name="email"]')
          .value.trim();
        const password = registerForm
          .querySelector('input[name="password"]')
          .value.trim();

        setTimeout(() => {
          if (firstName && lastName && phone && email && password) {
            alert("تم إنشاء الحساب بنجاح!");
            window.location.href = "index.html";
          } else {
            alert("يرجى ملء جميع الحقول");
          }
        }, 1000);
      });
    }
  }
});
