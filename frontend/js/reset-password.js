document.addEventListener("DOMContentLoaded", function () {
  const currentPage = window.location.pathname.split("/").pop();

  if (currentPage === "reset-password.html") {
    const resetPasswordForm = document.getElementById("reset-password-form");
    if (resetPasswordForm) {
      resetPasswordForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const newPassword = resetPasswordForm
          .querySelector('input[name="newPassword"]')
          .value.trim();
        const confirmPassword = resetPasswordForm
          .querySelector('input[name="confirmPassword"]')
          .value.trim();

        setTimeout(() => {
          if (
            newPassword &&
            confirmPassword &&
            newPassword === confirmPassword
          ) {
            alert("تم تغيير كلمة المرور بنجاح!");
            window.location.href = "index.html";
          } else {
            alert("كلمة المرور غير متطابقة");
          }
        }, 1000);
      });
    }
  }
});
const text = " الرجاء ادخال كلمة المرور الجديده";
let i = 0;
function typeEffect() {
  if (i < text.length) {
    document.getElementById("typing-text").innerHTML += text.charAt(i);
    i++;
    setTimeout(typeEffect, 70);
  }
}
typeEffect();
