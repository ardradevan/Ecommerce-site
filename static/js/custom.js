// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: true,
    margin: 0,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});



/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}


// $(document).ready(function (){
//     $('.decrement-btn').click(function (e){
//         e.preventDefault();
//     });

// $(document).ready(function (){
//     $('.increment-btn').click(function (e){
//         e.preventDefault();
//         var inc_value=$(this).closest('.product_data').find('.qty-input').val();
//         var value=parseInt(inc_value,10);
//         value=isNaN(value) ? 0 : value;
//         if(value < 10)
//         {
//             value++;
//             $(this).closest('.product_date').find('.qty-input').val(value);
//         }

//     });
// });