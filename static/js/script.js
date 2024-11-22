 window.addEventListener("DOMContentLoaded", () => {
    const swiper = new Swiper(".mySwiper", {
      loop: true,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    });

    // Verify Swiper is initialized
    console.log(swiper);
  });

