document.addEventListener("DOMContentLoaded", function () {
  const currentPage = window.location.pathname.split("/").pop();

  // (index.html)
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

        auth
          .signInWithEmailAndPassword(email, password)
          .then(() => {
            alert("تم تسجيل الدخول بنجاح!");
            window.location.href = "home.html";
          })
          .catch((error) => {
            alert("خطأ: " + error.message);
          });
      });
    }
  }

  //  (register.html)
  else if (currentPage === "register.html") {
    const registerForm = document.getElementById("register-form");
    if (registerForm) {
      registerForm.addEventListener("submit", function (event) {
        event.preventDefault();
        const email = registerForm
          .querySelector('input[name="email"]')
          .value.trim();
        const password = registerForm
          .querySelector('input[name="password"]')
          .value.trim();

        auth
          .createUserWithEmailAndPassword(email, password)
          .then(() => {
            alert("تم إنشاء الحساب بنجاح!");
            window.location.href = "index.html";
          })
          .catch((error) => {
            alert("خطأ: " + error.message);
          });
      });
    }
  }

  // (add-tuk-tuk.html)
  else if (currentPage === "add-tuk-tuk.html") {
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

        db.collection("drivers")
          .add({
            driverName,
            driverPhone,
            nationalId,
            tukTukNumber,
          })
          .then(() => {
            alert("تم إضافة بيانات التكتوك بنجاح!");
            window.location.href = "home.html";
          })
          .catch((error) => {
            alert("خطأ: " + error.message);
          });
      });
    }
  }

  //  (drivers-data.html)
  else if (currentPage === "drivers-data.html") {
    db.collection("drivers")
      .get()
      .then((snapshot) => {
        const driversList = document.getElementById("drivers-list");
        snapshot.forEach((doc) => {
          const driver = doc.data();
          const driverCard = `
              <div class="card">
                <p><strong>اسم السائق:</strong> ${driver.driverName}</p>
                <p><strong>الهاتف:</strong> ${driver.driverPhone}</p>
                <p><strong>الرقم القومي:</strong> ${driver.nationalId}</p>
                <p><strong>رقم التوكتوك:</strong> ${driver.tukTukNumber}</p>
              </div>
            `;
          driversList.innerHTML += driverCard;
        });
      })
      .catch((error) => {
        console.error("خطأ: ", error);
      });
  }

  //  (confirm-account.html)
  else if (currentPage === "confirm-account.html") {
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

  //  (verification-code.html)
  else if (currentPage === "verification-code.html") {
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

  // (reset-password.html)
  else if (currentPage === "reset-password.html") {
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

        if (newPassword && confirmPassword && newPassword === confirmPassword) {
          alert("تم تغيير كلمة المرور بنجاح!");
          window.location.href = "index.html";
        } else {
          alert("كلمة المرور غير متطابقة");
        }
      });
    }
  }

  //  (driver-location.html)
  else if (currentPage === "driver-location.html") {
    function initMap() {
      const location = { lat: 30.0444, lng: 31.2357 }; // إحداثيات القاهرة كمثال
      const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 12,
        center: location,
      });
      new google.maps.Marker({ position: location, map: map });
    }
    window.onload = initMap;
  }
});

gsap.from(".animated-text", {
  duration: 1.5,
  opacity: 0,
  y: -50,
  ease: "bounce.out",
});
const text = "!  Welcome ";
let i = 0;
function typeEffect() {
  if (i < text.length) {
    document.getElementById("typing-text").innerHTML += text.charAt(i);
    i++;
    setTimeout(typeEffect, 100);
  }
}
typeEffect();
