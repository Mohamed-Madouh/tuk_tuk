document.addEventListener("DOMContentLoaded", function () {
  const currentPage = window.location.pathname.split("/").pop();

  if (currentPage === "confirm-account.html") {
    const confirmAccountForm = document.getElementById("confirm-account-form");
    if (confirmAccountForm) {
      confirmAccountForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const phoneNumberOrEmail = confirmAccountForm
          .querySelector('input[name="phoneNumberOrEmail"]')
          .value.trim();

        setTimeout(() => {
          if (phoneNumberOrEmail) {
            alert("تم إرسال رمز التأكيد بنجاح!");
            window.location.href = "verification-code.html";
          } else {
            alert("يرجى إدخال رقم الهاتف أو البريد الإلكتروني");
          }
        }, 1000);
      });
    }
  }
});
const text = "ادخل رقم الهاتف أو البريد الإلكتروني";
let i = 0;
function typeEffect() {
  if (i < text.length) {
    document.getElementById("typing-text").innerHTML += text.charAt(i);
    i++;
    setTimeout(typeEffect, 60);
  }
}
typeEffect();
