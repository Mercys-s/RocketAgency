$(document).ready(function(){
  $('.slider-for').slick({
  });
});

$('.slider-for').slick({
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  fade: true,
  asNavFor: '.slider-nav'
});
$('.slider-nav').slick({
  arrows: true,
  slidesToShow: 3,
  slidesToScroll: 1,
  asNavFor: '.slider-for',
  dots: false,
  centerMode: true,
  focusOnSelect: true,
  adaptiveHeight: true,
  centerMode: true,
  variableWidth: true,
  variableHeight: true,
  centerPadding: false,
});