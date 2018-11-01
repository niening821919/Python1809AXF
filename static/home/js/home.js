$(function () {
    $('.home').width(innerWidth)
    new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        paginationClickable: true,
        spaceBetween: 5,
        centeredSlides: true,
        autoplay: 2500,
        autoplayDisableOnInteraction: false,
        loop: true,
    });
    new Swiper('#mustbuySwiper', {
        slidesPerView: 3,
        paginationClickable: true,
        spaceBetween: 5,
        loop:true,
    });
})
