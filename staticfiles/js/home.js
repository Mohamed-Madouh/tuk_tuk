function initializeEventListeners() {
  document.getElementById("drivers-btn").addEventListener("click", function () {
    const baseUrl = window.location.origin;
    window.location.href = `${baseUrl}/tuk_tuk/templates/driver_detail.html`;
  });

  // Uncomment and modify the following block if needed
  // document.getElementById("tuktuk-btn").addEventListener("click", function () {
  //   window.location.href = "tuk_tuk/templates/add_driver.html";
  // });
}

document.addEventListener("DOMContentLoaded", initializeEventListeners);
//   });
// });
