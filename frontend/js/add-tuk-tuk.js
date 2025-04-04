document.addEventListener("DOMContentLoaded", function () {
  const currentPage = window.location.pathname.split("/").pop();

  if (currentPage === "add-tuk-tuk.html") {
    const addTukTukForm = document.getElementById("add-tuk-tuk-form");
    if (addTukTukForm) {
      addTukTukForm.addEventListener("submit", function (event) {
        event.preventDefault();

        const driverName = addTukTukForm
          .querySelector('input[name="driverName"]')
          .value.trim();
        const driverPhone = addTukTukForm
          .querySelector('input[name="driverPhone"]')
          .value.trim();
        const nationalId = addTukTukForm
          .querySelector('input[name="nationalId"]')
          .value.trim();
        const tukTukNumber = addTukTukForm
          .querySelector('input[name="tukTukNumber"]')
          .value.trim();

        setTimeout(() => {
          if (driverName && driverPhone && nationalId && tukTukNumber) {
            alert("تم إضافة بيانات التكتوك بنجاح!");
            window.location.href = "home.html";
          } else {
            alert("يرجى ملء جميع الحقول");
          }
        }, 1000);
      });
    }
  }
});

// const text = "Register for TukTuk here ";
// let i = 0;
// function typeEffect() {
//   if (i < text.length) {
//     document.getElementById("typing-text").innerHTML += text.charAt(i);
//     i++;
//     setTimeout(typeEffect, 70);
//   }
// }
// typeEffect();