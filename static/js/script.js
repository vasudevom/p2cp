// // Timer Function
// (function() {
//     const second = 1000,
//         minute = second * 60,
//         hour = minute * 60,
//         day = hour * 24;

//     let birthday = "Jul 3, 2021 00:00:00",
//         countDown = new Date(birthday).getTime(),
//         x = setInterval(function() {

//             let now = new Date().getTime(),
//                 distance = countDown - now;

//             document.getElementById("days").innerText = Math.floor(distance / (day)),
//                 document.getElementById("hours").innerText = Math.floor((distance % (day)) / (hour)),
//                 document.getElementById("minutes").innerText = Math.floor((distance % (hour)) / (minute)),
//                 document.getElementById("seconds").innerText = Math.floor((distance % (minute)) / second);

//             //do something later when date is reached
//             if (distance < 0) {
//                 let headline = document.getElementById("headline"),
//                     countdown = document.getElementById("countdown"),
//                     content = document.getElementById("content");
//             }
//         }, 0)
// }())

//javascript for navigation bar effect on scroll
window.addEventListener("scroll", function() {
    var header = document.querySelector("header");
    header.classList.toggle('sticky', window.scrollY > 0);
});

//javascript for responsive navigation sidebar menu
var menu = document.querySelector('.menu');
var menuBtn = document.querySelector('.menu-btn');
var closeBtn = document.querySelector('.close-btn');

menuBtn.addEventListener("click", () => {
    menu.classList.add('active');
});

closeBtn.addEventListener("click", () => {
    menu.classList.remove('active');
});


$(function() {
    $("#customer-testimonial").owlCarousel({
        items: 1,
        autoplay: true,
        smartSpeed: 700,
        look: true,
        autoPlayHoverPause: true
    });
});
$(document).ready(function() {
    $("#registration-div1-contentholder").hover(function() {
        $("#x").css("color", "#F79521");
    }, function() {
        $("#x").css("color", "#FFFFFF");
    });
    $("#registration-div1-contentholder").hover(function() {
        $("register1").css("color", "#FFFFFF");
    }, function() {
        $("register1").css("color", "#C4C4C4");
    });
    $("#registration-div1-contentholder").hover(function() {
        $("#btn1").css({
            "color": "#f79521",
            "backgroundColor": "white"
        });
    }, function() {
        $("#btn1").css({
            "color": "black",
            "backgroundColor": "#F79521"
        });
    });

});

