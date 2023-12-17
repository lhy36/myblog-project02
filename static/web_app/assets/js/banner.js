// script.js
const bannerContainer = document.querySelector('.banner');
const bannerSlides = document.querySelectorAll('.banner-slide');
let currentIndex = 0;

function showSlide(index) {
    if (index < 0) {
        currentIndex = bannerSlides.length - 1;
    } else if (index >= bannerSlides.length) {
        currentIndex = 0;
    }

    const translateX = currentIndex * -100;
    bannerContainer.style.transform = `translateX(${translateX}%)`;
}

function prevSlide() {
    currentIndex--;
    showSlide(currentIndex);
}

function nextSlide() {
    currentIndex++;
    showSlide(currentIndex);
}

const prevButton = document.querySelector('.prev-button');
const nextButton = document.querySelector('.next-button');

prevButton.addEventListener('click', prevSlide);
nextButton.addEventListener('click', nextSlide);

// 초기 배너 표시
showSlide(currentIndex);
