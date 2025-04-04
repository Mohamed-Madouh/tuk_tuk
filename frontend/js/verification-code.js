document.addEventListener("DOMContentLoaded", function () {
  const currentPage = window.location.pathname.split("/").pop();

  if (currentPage === "verification-code.html") {
    const verificationCodeForm = document.getElementById(
      "verification-code-form"
    );
    if (verificationCodeForm) {
      verificationCodeForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const codeInputs = Array.from(
          verificationCodeForm.querySelectorAll(".code-inputs input")
        );
        const code = codeInputs.map((input) => input.value.trim()).join("");

        setTimeout(() => {
          if (code === "1234") {
            alert("رمز التأكيد صحيح!");
            window.location.href = "home.html";
          } else {
            alert("رمز التأكيد غير صحيح");
          }
        }, 1000);
      });
    }
  }
});
